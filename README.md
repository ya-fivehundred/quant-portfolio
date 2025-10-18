# Quant Portfolio — Finance, Data and Cloud

## Objective

This portfolio presents a set of quantitative finance projects designed to demonstrate three key abilities:

1. Financial data manipulation (tickers, prices, volatility, correlations)
2. Implementation of classical quantitative methods (backtesting, portfolio optimization, option pricing, risk modeling)
3. Industrialization of solutions (data pipelines, cloud architecture, CI/CD, APIs, dashboards)

The goal is not to upload dozens of exploratory notebooks, but to showcase three to five solid, well-documented projects that combine rigor and clarity.

## Portfolio Structure

Each project is an independent repository focusing on a specific skill area within quantitative finance.

| # | Project | Main Topic | Key Message |
|:-:|:--------|:------------|:-------------|
| 1 | [quant-data-pipeline](https://github.com/<username>/quant-data-pipeline) | Data and Infrastructure | Ability to build and scale a financial market database |
| 2 | [quant-backtesting](https://github.com/<username>/quant-backtesting) | Strategy and Performance | Understanding and implementation of trading logic |
| 3 | [quant-portfolio-optimization](https://github.com/<username>/quant-portfolio-optimization) | Portfolio Optimization | Application of classical quantitative finance theory |
| 4 | [quant-risk-modelling](https://github.com/<username>/quant-risk-modelling) | Volatility and Risk | Modeling and quantification of financial risk |
| 5 | [quant-ml-finance (optional)](https://github.com/<username>/quant-ml-finance) | Machine Learning | Application of ML in finance with methodological rigor |

## Project Overview

### 1. Financial Data Pipeline
Goal: Build a cloud-based infrastructure to collect and store market data such as S&P 500 or CAC 40.  
Technologies: Python, Pub/Sub, BigQuery, Cloud Run, VM Instances. 
Includes scripts, an automated pipeline, and dashboard integration.  
Message: Ability to design scalable market data infrastructure.

### 2. Backtesting and Simple Strategies
Goal: Develop a lightweight backtesting framework and test several classical strategies:  
- Momentum (Moving Average Crossover)  
- Mean Reversion (Bollinger Bands)  
- Portfolio Rebalancing (60/40 Equity/Bond)  
Includes benchmark comparison with Buy & Hold.  
Message: Understanding and coding of quantitative strategies.

### 3. Portfolio Optimization
Goal: Implement and visualize the efficient frontier for a multi-asset portfolio.  
Constraints: weight limits, no short-selling, limited leverage  
Extensions: shrinkage covariance, Black-Litterman, risk-parity  
Visualization in 2D/3D.  
Message: Application of quantitative finance in a realistic setting.

### 4. Volatility and Risk Modelling
Goal: Model and quantify portfolio risk using time-series techniques.  
Includes GARCH, EGARCH, Heston simulations, comparison of realized vs implied volatility, and Monte Carlo estimation of Value-at-Risk.  
Message: Mastery of quantitative risk modeling tools.

### 5. Machine Learning for Finance (Optional)
Goal: Explore ML methods for predicting returns or volatility.  
Models: LSTM, Random Forest  
Methodology: time-based train/test split, overfitting analysis, and model limitations.  
Message: Application of ML to financial data with methodological rigor.

## Technical Organization

Each project follows a consistent structure:

project-name/
├── README.md
├── notebooks/
├── src/
├── tests/
├── requirements.txt
├── .gitignore
└── LICENSE

vbnet
Copier le code

## Portfolio Presentation

This main repository serves as an index for all projects, with:
- An overview of the portfolio
- Visual slides and architecture diagrams
- References to each project repository

Example structure:
quant-portfolio/
├── README.md
├── projects/
│ ├── data-pipeline.md
│ ├── backtesting.md
│ ├── portfolio-optimization.md
│ └── risk-modelling.md
└── slides/
└── quant_portfolio_presentation.pdf

markdown
Copier le code

## Global Tech Stack

- Python (Pandas, NumPy, Scikit-learn, Statsmodels, Plotly)
- Google Cloud Platform (Pub/Sub, BigQuery, Cloud Run, Scheduler)
- Docker, GitHub Actions (CI/CD)
- Jupyter, Streamlit, Looker Studio
- Quantitative Finance: Markowitz, GARCH, VaR, Machine Learning for time-series

## Author

Youri  


## License

This portfolio is released under the MIT License.  
All notebooks and scripts are open-source for educational and demonstration purposes.
