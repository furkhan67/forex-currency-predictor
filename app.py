from autots import AutoTS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
sns.set()
plt.style.use('seaborn-v0_8-whitegrid')


import streamlit as st
st.title(("Future Forex Currency Price Prediction Model"))

options = {
    'AUSTRALIAN DOLLAR': 'AUSTRALIA - AUSTRALIAN DOLLAR/US$',
    'EURO': 'EURO AREA - EURO/US$',
    'NEW ZEALAND DOLLAR': 'NEW ZEALAND - NEW ZEALAND DOLLAR/US$',
    'GREAT BRITAIN POUNDS': 'UNITED KINGDOM - UNITED KINGDOM POUND/US$',
    'BRAZILIAN REAL': 'BRAZIL - REAL/US$',
    'CANADIAN DOLLAR': 'CANADA - CANADIAN DOLLAR/US$',
    'CHINESE YUAN$': 'CHINA - YUAN/US$',
    'HONG KONG DOLLAR': 'HONG KONG - HONG KONG DOLLAR/US$',
    'INDIAN RUPEE': 'INDIA - INDIAN RUPEE/US$',
    'KOREAN WON$': 'KOREA - WON/US$',
    'MEXICAN PESO': 'MEXICO - MEXICAN PESO/US$',
    'SOUTH AFRICAN RAND$': 'SOUTH AFRICA - RAND/US$',
    'SINGAPORE DOLLAR': 'SINGAPORE - SINGAPORE DOLLAR/US$',
    'DANISH KRONE': 'DENMARK - DANISH KRONE/US$',
    'JAPANESE YEN$': 'JAPAN - YEN/US$',
    'MALAYSIAN RINGGIT': 'MALAYSIA - RINGGIT/US$',
    'NORWEGIAN KRONE': 'NORWAY - NORWEGIAN KRONE/US$',
    'SWEDEN KRONA': 'SWEDEN - KRONA/US$',
    'SRILANKAN RUPEE': 'SRI LANKA - SRI LANKAN RUPEE/US$',
    'SWISS FRANC': 'SWITZERLAND - FRANC/US$',
    'NEW TAIWAN DOLLAR': 'TAIWAN - NEW TAIWAN DOLLAR/US$',
    'THAI BAHT': 'THAILAND - BAHT/US$'
}

#function to make predictions, we'll use the code from analysis.ipynb file and make a function which would return forecasts
def make_forecast(selected_option,forecast):
    data = pd.read_csv("data/Foreign_Exchange_Rates.xls")
    print(data.head())
    data.dropna()
    data['Time Serie'] = pd.to_datetime(data['Time Serie'], format='%d-%m-%Y')
    model = AutoTS(forecast_length=int(forecast), frequency='infer', ensemble='simple', drop_data_older_than_periods=200)
    model = model.fit(data, date_col = 'Time Serie', value_col=options[selected_option], id_col=None)
    prediction = model.predict()
    forecast = prediction.forecast
    return forecast

    #currently the model is trained on every submit action from streamlit, find a solution to this problem so that on every submit action, a pretrained model for each currecncy is loaded and inferenced.



with st.form(key='user_form'):
    # Add input widgets to the form
    # Create the selectbox
    selected_option = st.selectbox('Choose a currency:', options)
    forecast = st.number_input(
    "Enter an integer",  # Label displayed to the user
    min_value=1,         # Minimum value allowed
    max_value=100,      # Maximum value allowed
    value=1,            # Default value
    step=1              # Increment step
)
    submit_button = st.form_submit_button(label='Generate Predictions')

if submit_button:
    
    forecast = make_forecast(selected_option,forecast)
        
    st.write(forecast)
    st.line_chart(forecast)
    st.dataframe(forecast)
