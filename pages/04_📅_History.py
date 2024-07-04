import streamlit as st
import os 
import pandas as pd

# function to set up page configuration
st.set_page_config(
        page_title="History",
        page_icon="🕰️",
        layout="wide",
    )

def display_history():
    csv_path = "Data_History/history.csv"
    csv_exists = os.path.exists(csv_path)
    
    if csv_exists:
        history = pd.read_csv(csv_path)
        st.dataframe(history)
        
        
if __name__ == "__main__":
    st.title("Prediction History")
    display_history()
        