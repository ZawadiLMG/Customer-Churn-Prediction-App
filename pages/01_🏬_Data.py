import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title='Data Page',
    page_icon='🏬',
    layout='wide',
)

st.title('Telcom Customer Churn Database 🏬')
st.sidebar.success("select a page above")
 
# Load data
df = pd.read_csv('.data/training_data.csv')
 
# Identify categorical and numerical columns
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
 
# Create select box at the top
option = st.selectbox(
    "Select data to display",
    ("All Data", "Categorical Columns", "Numerical Columns")
)
 
# Display data based on selection
if option == "All Data":
    st.write(df)
elif option == "Categorical Columns":
    st.write(df[categorical_columns])
elif option == "Numerical Columns":
    st.write(df[numerical_columns])
    