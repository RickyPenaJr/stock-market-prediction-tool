import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import joblib

def load_data(db_path="../data/stock_data.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM stocks WHERE Symbol = 'AAPL'", conn)
    conn.close()
    return df

def plot_predictions():
    df = load_data()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date")
    df['Target'] = df['Close'].shift(-1)
    df.dropna(inplace=True)

    X = df[['Open', 'High', 'Low', 'Volume']]
    model = joblib.load("../data/stock_model.pkl")
    df['Prediction'] = model.predict(X)

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Actual Close')
    plt.plot(df['Date'], df['Prediction'], label='Predicted Close')
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title("Actual vs Predicted Close Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig("../data/stock_prediction_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_predictions()