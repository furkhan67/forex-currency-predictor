# 🚀 Build an End-to-End Machine Learning Project: Forex Currency Prediction

Welcome to this hands-on, industry-style machine learning project! In this tutorial, you’ll go from raw data to a deployed application that forecasts foreign exchange rates for multiple currencies.

You’ll use:
- 📊 Jupyter Notebook for exploration and modeling  
- 🧠 Multiple ML algorithms for comparison  
- 💻 Streamlit for web app development  
- 🐳 Docker for production-ready packaging  

---

## 📁 Project Structure

| File/Folder      | Description                                                  |
|------------------|--------------------------------------------------------------|
| `analysis.ipynb` | 🔬 Your sandbox for EDA and predictive modeling              |
| `app.py`         | 🎯 Streamlit app UI and logic                                 |
| `data/`          | 📂 Folder containing the Excel dataset                        |
| `models/`        | 📦 Directory (you'll create this) to store saved models       |
| `Dockerfile`        | This file (you'll create this) to dockerise your python application so that it is ready for deployment     |
| `requirements.txt`        | This file contains all the dependencies of the project (make sure to update it after you install additional libraries)     |

---

## 🧪 Step 1: Data Analysis & Preprocessing (`analysis.ipynb`)

Start your journey in the Jupyter Notebook.

### ✅ Tasks:
1. **Load the dataset**
`df = pd.read_excel("data/Foreign_Exchange_Rates.xls")`
2. **Convert dates and clean the data using appropriate pre-processing techniques**
3. **Explore the time-series data** using visualizations and correlation plots

---

## 🔍 Step 2: Predictive Modeling – Try Different Models

Your goal is to **compare several time-series forecasting models** and pick the best one for each currency.

### 🔁 Model Suggestions:
- **ARIMA / SARIMA** – statistical modeling  
- **Prophet** – handles trends and seasonality well  
- **AutoTS** – automates model selection  
- **XGBoost / LightGBM** – can work with time features  
- **LSTM** – deep learning approach for sequential data  

For each model:
- Split your data into train and test (e.g., last 60 days as test)
- Train and evaluate each model
- Compare metrics: **MAE**, **RMSE**, **MAPE**

> 🧠 **Important:** Train a **separate model for each currency**. Different currencies may require different modeling approaches due to their unique patterns.

---

## 💾 Step 3: Save the Best Model for Each Currency

Once you’ve selected the best model for a currency, save it for use in the web app.

### Suggested libraries for saving models:
- `joblib` – efficient for saving scikit-learn and Prophet models  
- `pickle` – Python’s built-in way to serialize objects  
- `tensorflow` / `keras.models.save_model()` – if using LSTM or deep learning  

> 📦 Store each model in a separate file under a `models/` folder.  
> Example: `models/USD_model.pkl`, `models/EUR_model.pkl`, etc.

---

## 💻 Step 4: Build the Streamlit App (`app.py`)

The Streamlit app serves as your frontend for interactive predictions.

### Key features:
- Dropdown to select currency  
- Forecast horizon input (e.g., next 30 days)  
- Uses your saved model to generate predictions  
- Displays forecast table and chart  

> ✅ Make sure `make_forecast()` dynamically loads the correct model based on user selection.

Run the streamlit app using `streamlit run app.py` (make sure to install dependencies from requirements.txt first.)
---

## 🌐 Step 5: Make It Production Ready with Docker

Now that your app works locally, package it with Docker so that it is ready for deployment  !

Follow the official Docker guide to install it on your system:  
👉 [Installing Docker](https://docs.docker.com/get-started/get-docker/) 
👉 [Dockerizing Streamlit Applications]([https://docs.docker.com/language/python/build-images/](https://docs.streamlit.io/deploy/tutorials/docker))

### Steps:
- Write a `Dockerfile` to define the app environment. For example:  

`FROM python:3.9`  
`WORKDIR /app`  
`COPY . /app`  
`RUN pip install -r requirements.txt`  
`EXPOSE 8501`  
`CMD ["streamlit", "run", "app.py"]`
- Make sure you have a `requirements.txt` listing all libraries  
- Use `docker build` and `docker run` to run the app in a container. For example:
`sudo docker build -t forex-predictor .`
`docker run -p 8501:8501 forex-predictor`  

---

## 🧾 Final Checklist

✅ Explore and clean the data in `analysis.ipynb`  
✅ Try multiple models, evaluate performance  
✅ Choose and save the best model for each currency  
✅ Build a Streamlit app in `app.py` that loads saved models  
✅ Dockerize your project for easy deployment  

## Optional

Use this [link](https://github.com/oanda/py-api-streaming) to fetch live data from OANDA api. You can create your own dataset using this api.

