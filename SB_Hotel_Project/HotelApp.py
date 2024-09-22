import streamlit as st
import pandas as pd
import joblib
from DataCleaning import data_cleaning  # Import your data cleaning function

model = joblib.load("saved_model.pkl")

def main(): 
    st.title("SB Hotel Predictions/Suggestions")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">SB Hotel Suggestions App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    hotel_price = st.number_input("Desire Hotel Prices", min_value = 0, max_value = None)
    Number_review = st.number_input("Number of Reviews", min_value = 0, max_value = 2400)
    