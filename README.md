# Stock Market Prediction Project
![stock-market-banner-1](https://github.com/user-attachments/assets/ccf5614a-5865-48d1-a43a-df788bd6f951)
<br>
<br>


## 📘 Project Description
A simple, Python project for predicting stock market prices by utilizing historical data, machine learning models, and clear visualizations to help forecast how investments might perform in the future.

This project provides investors, students, and financial analysts with a lightweight analytics pipeline that:
- Fetches historical stock data via `yfinance`
- Cleans and stores it in a local SQL database
- Trains predictive models on past price movements
- Generates interactive trend and prediction charts
<br>
<br>


## ✅ What This Project Does
- ✔ Fetches historical stock data using `yfinance`  
- ✔ Stores and organizes data in a local SQL database  
- ✔ Trains machine learning models (Linear Regression, Random Forest) on historical prices  
- ✔ Plots actual vs. predicted closing prices  
- ✔ Prepares exports for Power BI dashboarding  
<br>
<br>


## 🚀 Features
- 📈 Historical data retrieval with `yfinance`  
- 🤖 Predictive modeling using scikit-learn  
- 🗃️ SQLite database for time-series storage  
- 📊 Visualizations with Power BI & Matplotlib (Plotly optional)  
- 🔄 Fully automated end-to-end pipeline  
<br>

## 📁 Project Structure

<pre>
stock-market-tool/
├── data/                   # Raw CSVs or SQL database backups
│   └── .gitkeep            # Keeps empty folder in repo
├── notebooks/              # Jupyter notebooks for exploration and modeling
│   └── stock_prediction.ipynb
├── src/                    # Python scripts for automation & dashboard
│   ├── api_fetch.py        # Get historical stock data via yfinance
│   ├── db_utils.py         # Create, insert, and query SQLite database
│   ├── model_train.py      # Train and evaluate regression models
│   ├── visualize.py        # Generate plots for price trends and predictions
│   └── dashboard.py        # Streamlit app for interactive dashboard
├── powerbi/                # Power BI dashboards and exports
│   └── .gitkeep            # Keeps empty folder in repo
├── requirements.txt        # Python dependency list
├── .gitignore              # Excludes cache, envs, models, and sensitive files from Git
├── LICENSE                 # MIT License for open-source usage
└── README.md               # Project documentation
</pre>

<br>
<br>


## ⚙️ How to Use It

1. **Clone the repo**  
       git clone https://github.com/rickypenajr/stock-market-tool.git  
       cd stock-market-tool  

2. **Install dependencies**  
       pip install -r requirements.txt  

3. **Fetch & store historical data**  
       python src/api_fetch.py  
   - By default downloads **AAPL** from 2015-01-01 to today  
   - To specify another symbol or date range, edit the `fetch_stock_data()` defaults or add arguments  

4. **Populate the database**  
       python src/db_utils.py  
   - Creates `data/stock_data.db` and imports the CSV  

5. **Train the prediction model**  
       python src/model_train.py  
   - Reads from the DB, trains a Linear Regression, saves `data/stock_model.pkl`  

6. **Generate visualizations**  
       python src/visualize.py  
   - Produces a plot of actual vs. predicted close price and saves `data/stock_prediction_plot.png`  

7. **Explore interactively (optional)**  
       jupyter notebook notebooks/stock_prediction.ipynb  

8. **View Power BI dashboards (optional)**  
   Open the `.pbix` files in `/powerbi/` 

<br>

## 📊 Sample Visuals (Coming Soon)

- Predicted vs Actual Closing Price Comparison  
- Technical Indicators (SMA, RSI, EMA)  
- Power BI Overview Dashboard  


## 🧠 Technologies Used

- **Languages**: Python, SQL  
- **Libraries**: `yfinance`, `pandas`, `NumPy`, `scikit-learn`, `matplotlib`, `joblib`  
- **Database**: SQLite  
- **Visualization**: Matplotlib, Plotly (optional), Power BI  



## 📌 License
MIT License



## 🏷️ GitHub Topics
`#python` `#stock-market` `#machine-learning` `#data-visualization` `#financial-analysis` `#yfinance` `#sql` `#pandas` `#matplotlib` `#time-series` `#regression-model` `#jupyter-notebook` `#powerbi` `#predictive-modeling`



## 👤 Author

**Ricky Peña Jr.**  
🌐 [rickypenajr.github.io](https://rickypenajr.github.io)  
🔗 [GitHub](https://github.com/rickypenajr) • [LinkedIn](https://linkedin.com/in/rickypenajr)
