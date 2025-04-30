import sqlite3
import pandas as pd
import os

def create_db(db_path="../data/stock_data.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            Date TEXT,
            Open REAL,
            High REAL,
            Low REAL,
            Close REAL,
            Adj_Close REAL,
            Volume INTEGER,
            Symbol TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data_from_csv(csv_path, db_path="../data/stock_data.db", symbol="AAPL"):
    df = pd.read_csv(csv_path)
    df['Symbol'] = symbol
    conn = sqlite3.connect(db_path)
    df.to_sql("stocks", conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    insert_data_from_csv("../data/AAPL_data.csv")