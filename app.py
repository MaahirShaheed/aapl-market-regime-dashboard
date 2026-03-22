import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AAPL Market Regime Dashboard")

df = pd.read_csv("data/aapl_with_rsi.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.subheader("Dataset Preview")
st.dataframe(df.tail(10))

st.subheader("Closing Price with Moving Averages")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df["Date"], df["Close"], label="Close")
ax1.plot(df["Date"], df["MA20"], label="20-day MA")
ax1.plot(df["Date"], df["MA50"], label="50-day MA")
ax1.legend()
st.pyplot(fig1)

st.subheader("RSI (14-day)")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df["Date"], df["RSI14"], label="RSI14")
ax2.axhline(70, linestyle="--", label="Overbought")
ax2.axhline(30, linestyle="--", label="Oversold")
ax2.legend()
st.pyplot(fig2)