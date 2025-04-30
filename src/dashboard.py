import streamlit as st
import pandas as pd
import sqlite3
import joblib
import matplotlib.pyplot as plt

# ——— Helpers ———
@st.cache
def load_data(symbol: str, db_path="data/stock_data.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM stocks WHERE Symbol='{symbol}'", conn, parse_dates=["Date"])
    conn.close()
    return df.sort_values("Date")

@st.cache
def load_model(model_path="data/stock_model.pkl"):
    return joblib.load(model_path)

# ——— App Layout ———
st.title("📊 Stock Market Dashboard")
st.sidebar.header("Settings")

# Sidebar inputs
symbol = st.sidebar.text_input("Ticker Symbol", value="AAPL").upper()
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Load data & model
df = load_data(symbol)
model = load_model()

# Filter by date
df = df[(df.Date >= pd.to_datetime(start_date)) & (df.Date <= pd.to_datetime(end_date))]

# Prepare features & predictions
df["Target"] = df["Close"].shift(-1)
X = df[["Open","High","Low","Volume"]].dropna()
df = df.loc[X.index]
df["Prediction"] = model.predict(X)

# ——— Main Chart ———
st.subheader(f"{symbol}: Actual vs. Predicted Close Price")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Close"], label="Actual")
ax.plot(df["Date"], df["Prediction"], label="Predicted")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# ——— Summary Stats ———
st.subheader("Model Performance")
mse = ((df["Prediction"] - df["Close"])**2).mean()
st.markdown(f"- **MSE:** {mse:.2f}")
st.markdown(f"- **Data points:** {len(df)}")

# ——— Data Table ———
if st.checkbox("Show raw data"):
    st.dataframe(df[["Date","Open","High","Low","Close","Prediction"]])
