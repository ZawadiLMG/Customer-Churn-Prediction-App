import streamlit as st
import pandas as pd 
import joblib

st.set_page_config(
    page_title = "Dashboard Page",
    page_icon = "🚀",
    layout = 'wide'
)
st.title('Dashboard 📈')
st.sidebar.success("Select a page")