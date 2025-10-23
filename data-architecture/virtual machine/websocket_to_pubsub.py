import os
import json
import time
import logging
import threading
from typing import List
from google.cloud import bigquery, pubsub_v1
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Feed, Market

POLYGON_API_KEY = "x"
PROJECT_ID = "x"

# Datasets ET tables distincts
TABLES = {
    "XNAS": {"dataset": "xnas_dataset", "table": "xnas_top150tickers_marketcap"},
    "XNYS": {"dataset": "xnys_dataset", "table": "xnys_top150tickers_marketcap"},
    "XASE": {"dataset": "xase_dataset", "table": "xase_top150tickers_marketcap"},
}

# Topics Pub/Sub distincts
PUBSUB_TOPICS = {
    "XNAS": "xnas-websocket",
    "XNYS": "xnys-websocket",
    "XASE": "xase-websocket"
}

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

bq_client = bigquery.Client(project=PROJECT_ID)
pub_client = pubsub_v1.PublisherClient()


def get_tickers_from_bigquery(exchange: str):
    dataset = TABLES[exchange]["dataset"]
    table = TABLES[exchange]["table"]
    query = f"""
        SELECT DISTINCT ticker
        FROM `{PROJECT_ID}.{dataset}.{table}`
        WHERE ticker IS NOT NULL
    """
    df = bq_client.query(query).to_dataframe()
    tickers = set(df["ticker"].dropna().astype(str))
    logging.info(f"{exchange}: {len(tickers)} tickers récupérés depuis {dataset}.{table}")
    return tickers


def init_pubsub_topic(exchange: str):
    topic_name = PUBSUB_TOPICS[exchange]
    return pub_client.topic_path(PROJECT_ID, topic_name)

def handle_msg(msgs: List[WebSocketMessage]):
    global all_tickers_by_exchange

    for m in msgs:
        try:
            symbol = getattr(m, "symbol", None)
            if not symbol:
                continue

            # Recherche du bon exchange
            for exchange, tickers in all_tickers_by_exchange.items():
                if symbol in tickers:
                    topic_path = init_pubsub_topic(exchange)

                    payload = {
                        "exchange": exchange,
                        "symbol": symbol,
                        "price": getattr(m, "close", None),
                        "volume": getattr(m, "volume", None),
                        "timestamp": getattr(m, "start_timestamp", None),
                        "raw": m.__dict__,
                    }

                    data = json.dumps(payload).encode("utf-8")
                    pub_client.publish(topic_path, data=data)
                    logging.info(f"✅ Publié: {symbol} → {exchange}")
                    break

        except Exception as e:
            logging.error(f"Erreur dans handle_msg: {e}")


def refresh_tickers_every(hours: float = 12):
    global all_tickers_by_exchange
    last_refresh = 0

    while True:
        now = time.time()
        if now - last_refresh > hours * 3600:
            logging.info("♻️ Rafraîchissement des tickers depuis BigQuery...")
            all_tickers_by_exchange = {ex: get_tickers_from_bigquery(ex) for ex in TABLES}
            last_refresh = now
        time.sleep(300)


if __name__ == "__main__":
    logging.info("🚀 Initialisation du flux WebSocket Polygon + Pub/Sub")

    all_tickers_by_exchange = {ex: get_tickers_from_bigquery(ex) for ex in TABLES}

    refresh_thread = threading.Thread(target=refresh_tickers_every, args=(12,), daemon=True)
    refresh_thread.start()

    client = WebSocketClient(
        api_key=POLYGON_API_KEY,
        feed=Feed.Delayed,  # ou Feed.RealTime
        market=Market.Stocks,
    )

    client.subscribe("AM.*")
    client.run(handle_msg)
