import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

st.title("AAPL Market Regime Dashboard")

df = pd.read_csv("data/aapl_with_rsi.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Return"] = df["Close"].pct_change()
df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["Volatility_5"] = df["Return"].rolling(5).std()
df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

feature_cols = ["RSI14", "Volume", "MA20", "MA50", "Return", "Volatility_5"]
model_df = df[feature_cols + ["Target"]].dropna()


X = model_df[feature_cols]
y = model_df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

latest_features = model_df[feature_cols].iloc[[-1]]
latest_pred = model.predict(latest_features)[0]
latest_prob = model.predict_proba(latest_features)[0][1]

st.subheader("Dataset Preview")
st.dataframe(df.tail(10))

st.subheader("AI Prediction")
prediction_label = "Up" if latest_pred == 1 else "Down"
st.write(f"**Next-Day Prediction:** {prediction_label}")
st.write(f"**Probability of Up Move:** {latest_prob:.2%}")
st.write(f"**Model Accuracy:** {accuracy:.2%}")

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