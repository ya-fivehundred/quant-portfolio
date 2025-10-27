-- Example of scheduled query running on bigquery.
-- Purpose: extract the 10 largest daily stock price increases on XNAS, the same scheduled query exists for top 10 decreases
-- ... and for each exchange I work with.
-- Frequency: once per day (BigQuery scheduled query). 
-- Destination: xnas_dataset.xnas_daily_top_10.

WITH daily_prices AS (
  SELECT
    symbol,
    DATE(start_timestamp) AS day,
    MIN(open) AS open_price_day,
    MAX(close) AS close_price_day
  FROM `projectid.xnas_dataset.xnas_live_data`
  WHERE DATE(start_timestamp) = CURRENT_DATE()
  GROUP BY symbol, day
),

daily_variation AS (
  SELECT
    day,
    symbol,
    open_price_day,
    close_price_day,
    SAFE_DIVIDE(close_price_day - open_price_day, open_price_day) * 100 AS variation_pct
  FROM daily_prices
)

SELECT *
FROM daily_variation
QUALIFY ROW_NUMBER() OVER(PARTITION BY day ORDER BY variation_pct DESC) <= 10;

