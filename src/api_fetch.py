import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def fetch_stock_data(symbol="AAPL", start="2015-01-01", end=None):
    end = end or datetime.today().strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start, end=end)
    data.to_csv(f"../data/{symbol}_data.csv")
    print(f"Data for {symbol} saved to ../data/{symbol}_data.csv")

if __name__ == "__main__":
    fetch_stock_data()