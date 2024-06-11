import streamlit as st
import streamlit as st
import os
import joblib
from pathlib import Path
import streamlit_authenticator as stauth


st.set_page_config(
    page_title='Home Page',
    page_icon='🏡',
    layout='wide',
)

st.title('Churn Prediction App')

name = st.text_input('What is your name?')

st.write(f'Hello {name}')


