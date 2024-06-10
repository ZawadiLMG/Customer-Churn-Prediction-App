# import streamlit as st
# import pyodbc
# import pandas as pd
# import joblib

# st.set_page_config(
#     page_title='Prediction Page',
#     page_icon='🏬',
#     layout='wide',
# )

# st.title('Predict Customer Churn⭐')

# st.cache_resource()
# def load_logistic_regression_model_pipeline():
#     pipeline = joblib.load('./models/Logistic_Regression.joblib')
#     return pipeline


# def load_random_forest_model_pipeline():
#     pipeline = joblib.load('./models/Random_Forest.joblib')
#     return pipeline

# st.cache_resource(show_spinner='Models loading... ')
# # define a function to select the model
# def select_model():
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')
#     with col2:
#         pass
    
#     if st.session_state['selected_model'] == 'Logistic Regression':
#         pipeline = load_logistic_regression_model_pipeline()
#     else:
#         pipeline = load_random_forest_model_pipeline()
        
#     encoder = joblib.load('models/encoder.joblib')
        
#     return pipeline, encoder

# pipeline, encoder = select_model()

# st.write(st.session_state)    








# import streamlit as st
# import pyodbc
# import pandas as pd
# import joblib

# st.set_page_config(
#     page_title='Prediction Page',
#     page_icon='🏬',
#     layout='wide',
# )

# st.title('Predict Customer Churn⭐')

# @st.cache_resource()
# def load_logistic_regression_model_pipeline():
#     pipeline = joblib.load('./models/Logistic_Regression.joblib')
#     return pipeline

# @st.cache_resource()
# def load_random_forest_model_pipeline():
#     pipeline = joblib.load('./models/Random_Forest.joblib')
#     return pipeline

# # Define a function to select the model
# def select_model():
#     col1, _ = st.columns(2)
    
#     with col1:
#         # Initialize the session state for the selected model if it doesn't exist
#         if 'selected_model' not in st.session_state:
#             st.session_state['selected_model'] = 'Logistic Regression'
        
#         # Select box to choose the model
#         st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')
    
#     # Load the appropriate model pipeline
#     if st.session_state['selected_model'] == 'Logistic Regression':
#         pipeline = load_logistic_regression_model_pipeline()
#     else:
#         pipeline = load_random_forest_model_pipeline()
        
#     # Load the encoder
#     encoder = joblib.load('./models/encoder.joblib')
        
#     return pipeline, encoder

# # Get the selected model pipeline and encoder
# pipeline, encoder = select_model()


# # display a form
# def display_form():
    
#     with st.form('Input_Features'):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.text_input('gender', key='gender')
#         with col2:
#             st.number_input('How long have you been a customer at Telco? (Enter in Months)', key='tenure', min_value=1, step=1)
        
#         submitted = st.form_submit_button('Submit')
        
#         if submitted:
#             st.write("Form submitted successfully!")
#             st.write(f"Gender: {st.session_state.gender}")
#             st.write(f"Tenure: {st.session_state.tenure}")

# if __name__ == '__main__':
        
#     select_model()
#     display_form()
    
# st.write(st.session_state)


import streamlit as st
import pyodbc
import pandas as pd
import joblib

st.set_page_config(
    page_title='Prediction Page',
    page_icon='🏬',
    layout='wide',
)

st.title('Predict Customer Churn⭐')

@st.cache_resource()
def load_logistic_regression_model_pipeline():
    pipeline = joblib.load('./models/Logistic_Regression.joblib')
    return pipeline

@st.cache_resource()
def load_random_forest_model_pipeline():
    pipeline = joblib.load('./models/Random_Forest.joblib')
    return pipeline

def load_encoder():
    encoder = joblib.load('./models/encoder.joblib')
    return encoder

# Initialize the session state for the selected model if it doesn't exist
if 'selected_model' not in st.session_state:
    st.session_state['selected_model'] = 'Logistic Regression'

# Select box to choose the model
col1, _ = st.columns(2)
with col1:
    st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')

# Load the appropriate model pipeline and encoder
if st.session_state['selected_model'] == 'Logistic Regression':
    pipeline = load_logistic_regression_model_pipeline()
else:
    pipeline = load_random_forest_model_pipeline()

encoder = load_encoder()

def display_form():
    with st.form('Input_Features'):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write('### Personal Information 👨')
            st.text_input('Gender', key='gender')
        with col2:
            st.write(' ### Customer Information 💸')
            st.number_input('How long have you been a customer at Telco? (Enter in Months)', key='tenure', min_value=1, step=1)
        
        submitted = st.form_submit_button('Submit')
        
        if submitted:
            st.write("Form submitted successfully!")
            st.write(f"Gender: {st.session_state.gender}")
            st.write(f"Tenure (Months): {st.session_state.tenure}")

if __name__ == '__main__':
    display_form()

st.write(st.session_state)
