# AAPL Market Regime Dashboard with AI Forecasting

This project analyzes Apple (AAPL) stock behavior using Python, pandas, matplotlib, Jupyter Notebook, and Streamlit, then adds a machine learning layer to predict next-day price direction. The dashboard combines technical indicators, volatility analysis, and interactive visualization to showcase financial analytics and AI-driven forecasting.

## Features

- Downloads and prepares historical daily price data for AAPL
- Calculates 20-day and 50-day moving averages
- Computes RSI(14) to identify overbought and oversold conditions
- Measures daily returns and short-term volatility
- Detects bullish and bearish regime shifts using moving-average crossovers
- Engineers financial features for machine learning
- Trains a logistic regression model to predict next-day price direction
- Displays AI prediction, probability of upward movement, and model accuracy
- Presents results in an interactive Streamlit dashboard

## Tools Used

- Python
- pandas
- matplotlib
- scikit-learn
- yfinance
- Jupyter Notebook
- Streamlit

## Project Files

- `app.py` — Streamlit dashboard with AI prediction
- `data/aapl_data.csv` — raw downloaded AAPL data
- `data/aapl_data_clean.csv` — cleaned AAPL dataset
- `data/aapl_regime_signals.csv` — regime signal dataset
- `data/aapl_with_rsi.csv` — dataset with RSI indicator
- `notebooks/aapl_regime_analysis.ipynb` — notebook analysis
- `requirements.txt` — project dependencies

## Key Findings

- AAPL showed meaningful short-term momentum and volatility changes over the sample period
- Moving-average crossover signals identified bullish and bearish regime changes
- RSI captured overbought and oversold conditions
- Engineered features such as RSI, moving averages, returns, volatility, and volume supported next-day direction prediction
- The logistic regression model added an interpretable AI layer to the dashboard by generating directional forecasts and probability estimates

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt

