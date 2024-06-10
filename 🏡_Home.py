import streamlit as st

st.set_page_config(
    page_title='Home Page',
    page_icon='🏡',
    layout='wide',
)

st.title('Churn Prediction App')

name = st.text_input('What is your name?')

st.write(f'Hello {name}')


