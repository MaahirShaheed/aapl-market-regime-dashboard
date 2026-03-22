\# AAPL Market Regime Dashboard



This project analyzes Apple (AAPL) stock behavior over the last 6 months using Python, pandas, yfinance, matplotlib, Jupyter Notebook, and Streamlit.



\## Features

\- Downloads historical daily price data for AAPL and SPY

\- Cleans and structures stock market data

\- Calculates 20-day and 50-day moving averages

\- Detects bullish and bearish regime shifts using moving-average crossovers

\- Computes RSI(14) to identify overbought and oversold conditions

\- Compares AAPL performance against SPY

\- Measures daily return volatility

\- Displays results in an interactive Streamlit dashboard



\## Tools Used

\- Python

\- pandas

\- yfinance

\- matplotlib

\- Jupyter Notebook

\- Streamlit



\## Project Files

\- `app.py` — Streamlit dashboard

\- `data/aapl\_data.csv` — raw downloaded AAPL data

\- `data/aapl\_data\_clean.csv` — cleaned AAPL dataset

\- `data/aapl\_regime\_signals.csv` — regime signal dataset

\- `data/aapl\_with\_rsi.csv` — dataset with RSI indicator

\- `notebooks/aapl\_regime\_analysis.ipynb` — notebook analysis

\- `requirements.txt` — project dependencies



\## Key Findings

\- AAPL was more volatile than SPY over the sample period.

\- AAPL daily return volatility was about 1.33%, compared with 0.77% for SPY.

\- Both AAPL and SPY had slightly negative average daily returns over this window.

\- Moving-average crossover signals identified bullish and bearish regime changes in AAPL.

\- RSI showed that AAPL moved through both overbought and oversold conditions.



\## How to Run

1\. Install dependencies:

&#x20;  `pip install -r requirements.txt`



2\. Run the dashboard:

&#x20;  `python -m streamlit run app.py`



\## Author

Maahir Shaheed

