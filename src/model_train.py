import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def load_data(db_path="../data/stock_data.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM stocks WHERE Symbol = 'AAPL'", conn)
    conn.close()
    return df

def train_model(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date")
    df['Target'] = df['Close'].shift(-1)
    df.dropna(inplace=True)

    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "../data/stock_model.pkl")
    print("Model trained and saved to ../data/stock_model.pkl")

if __name__ == "__main__":
    df = load_data()
    train_model(df)