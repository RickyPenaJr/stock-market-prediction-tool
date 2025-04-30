# Stock Market Prediction Tool
![stock-market-banner-1](https://github.com/user-attachments/assets/ccf5614a-5865-48d1-a43a-df788bd6f951)
<br>
<br>


## Project Description
A simple, user-friendly Python tool for predicting stock market prices by utilizing historical data, machine learning models, and clear visualizations to help predict how investments might perform in the future.

This project aims to provide investors, students, and financial analysts with a lightweight analytics pipeline that fetches real-time and historical stock data, cleans and stores it, runs predictive models, and visualizes trends through interactive graphs and dashboards.
<br>
<br>


## What This Project Does
✔ Fetches live and historical stock data using APIs (Yahoo Finance / Alpha Vantage)  
✔ Stores and organizes the data in a SQL database for long-term tracking  
✔ Trains machine learning models on historical price data to predict future closing prices  
✔ Displays clean visualizations of price trends and model predictions  
✔ Links to Power BI dashboards for high-level business intelligence reporting  
<br>
<br>


## Features
- 📡 Real-time stock data via APIs and web scraping
- 🧠 Predictive machine learning models (Linear Regression, Random Forest)
- 🗃️ SQL database storage and ETL pipeline
- 📊 Visualizations with Power BI and Matplotlib
- ⚙️ Automated data sync and preprocessing
<br>

## 📁 Project Structure

<pre>
stock-market-tool/
├── data/                   # Raw CSVs or SQL database backups
├── notebooks/              # Jupyter notebooks for exploration and modeling
│   └── stock_prediction.ipynb
├── src/                    # Python scripts for automation
│   ├── api_fetch.py        # Get stock data from APIs
│   ├── db_utils.py         # Create, insert, and query SQL database
│   ├── model_train.py      # Train and evaluate prediction models
│   └── visualize.py        # Generate plots for price trends and predictions
├── powerbi/                # Power BI dashboards and exports
├── requirements.txt        # Python dependency list
└── README.md               # Project documentation
</pre>

<br>

## ⚙️ How to Use It

1. **Clone the Repository**  
       git clone https://github.com/rickypenajr/stock-market-tool.git  
       cd stock-market-tool  

2. **Install Dependencies**  
       pip install -r requirements.txt  

3. **Set Up API Key**  
   - Create a `.env` file in the root directory with:  
         ALPHA_VANTAGE_API_KEY=your_api_key_here  

4. **Fetch and Store Stock Data**  
       python src/api_fetch.py  
   This pulls data from the API and saves it into a local SQL database (SQLite by default).

5. **Train the Prediction Model**  
       python src/model_train.py  
   Loads historical data, trains a machine learning model, and saves predictions.

6. **Visualize the Results**  
       python src/visualize.py  
   Generates visual charts comparing predicted vs. actual prices.

7. **Use the Jupyter Notebook (Optional)**  
       jupyter notebook notebooks/stock_prediction.ipynb  
   Explore, tweak models, and test predictions interactively.

8. **View Power BI Dashboard (Optional)**  
   Open the `.pbix` files in the `powerbi/` folder to explore interactive dashboards.

<br>

## 📊 Sample Visuals (Coming Soon)

- Predicted vs Actual Closing Price Comparison  
- Technical Indicators (SMA, RSI, EMA)  
- Power BI Overview Dashboard  

---

## 🧠 Technologies Used

- **Languages**: Python, SQL  
- **Libraries**: pandas, NumPy, matplotlib, scikit-learn, yfinance, requests, python-dotenv  
- **Database**: SQLite (default), MySQL (optional)  
- **APIs**: Alpha Vantage, Yahoo Finance  
- **Visualization**: Power BI, Plotly, Matplotlib  

---

## 🛠️ Future Enhancements

- Add LSTM or Prophet for advanced forecasting  
- Deploy a web interface with Flask or Streamlit  
- Real-time dashboard updates using cloud services  
- User-defined stock ticker and date-range input  

---

## 👤 Author

**Ricky Peña Jr.**  
📍 Houston, TX  
🌐 [rickypenajr.github.io](https://rickypenajr.github.io)  
🔗 [GitHub](https://github.com/rickypenajr) • [LinkedIn](https://linkedin.com/in/rickypenajr)
