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

# def load_encoder():
#     encoder = joblib.load('./models/encoder.joblib')
#     return encoder

# # Initialize the session state for the selected model if it doesn't exist
# if 'selected_model' not in st.session_state:
#     st.session_state['selected_model'] = 'Logistic Regression'

# # Select box to choose the model
# col1, _ = st.columns(2)
# with col1:
#     st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')

# # Load the appropriate model pipeline and encoder
# if st.session_state['selected_model'] == 'Logistic Regression':
#     pipeline = load_logistic_regression_model_pipeline()
# else:
#     pipeline = load_random_forest_model_pipeline()

# encoder = load_encoder()


# def make_prediction(pipeline, encoder):
#     gender = st.session_state['gender']
#     partner = st.session_state['partner']
#     dependents = st.session_state['dependents']
#     paymentmethod = st.session_state['paymentmethod']
#     tenure = st.session_state['tenure']
#     phoneservice = st.session_state['phoneservice']
#     internetservice = st.session_state['internetservice']

#     # Create DataFrame
#     data = [[gender, partner, dependents, paymentmethod, tenure, phoneservice, internetservice]]
#     columns = ['gender', 'partner', 'dependents', 'paymentmethod', 'tenure', 'phoneservice', 'internetservice']
#     df = pd.DataFrame(data, columns=columns)

#     # Prediction
#     pred = pipeline.predict(df)
#     st.write("Prediction:", pred)


# def display_form():
        
#     with st.form('Input_Features'):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.write('### Personal Information 👨')
#             st.selectbox('Gender', options=['Male', 'Female'], key='gender')
#             st.selectbox('Do you have a partner?', options=['Yes', 'No'], key='partner')
#             st.selectbox('Do you have dependents?', options=['Yes', 'No'], key='dependents')
#             st.selectbox('What is your main Payment Method?', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='paymentmethod')
            
#         with col2:
#             st.write(' ### Customer Information 💸')
#             st.number_input('How long have you been a customer at Telco? (Enter in Months)', key='tenure', min_value=1, step=1)
#             st.number_input('Enter your Monthly Charges', key='monthlycharges', min_value=15, max_value=120, step=1)
#             st.selectbox('Do you have phone service?', options=['Yes', 'No'], key='phoneservice')
#             st.selectbox('What type of internet service do you use?', options=['DSL', 'Fiber optic', 'No'], key='internetservice')
                        
#         submitted = st.form_submit_button('Submit', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))
        
#         if submitted:
#             st.write("Form submitted successfully!")
#             # st.write(f"Gender: {st.session_state.gender}")
#             # st.write(f"Tenure (Months): {st.session_state.tenure}")

# if __name__ == '__main__':
#     display_form()

# st.write(st.session_state)



import streamlit as st
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
    return joblib.load('./models/Logistic_Regression.joblib')

@st.cache_resource()
def load_random_forest_model_pipeline():
    return joblib.load('./models/Random_Forest.joblib')

@st.cache_resource()
def load_encoder():
    return joblib.load('./models/encoder.joblib')


def select_model():
    if 'selected_model' not in st.session_state:
        st.session_state['selected_model'] = 'Logistic Regression'
    
    col1, _ = st.columns(2)
    with col1:
        st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')
        
    if st.session_state['selected_model'] == 'Logistic Regression':
        pipeline = load_logistic_regression_model_pipeline()
    else:
        pipeline = load_random_forest_model_pipeline()
        
    encoder = load_encoder()
    
    return pipeline, encoder

def make_prediction(pipeline, encoder):
    gender = st.session_state['gender']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    paymentmethod = st.session_state['paymentmethod']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    internetservice = st.session_state['internetservice']

    # Create DataFrame
    data = [[gender, partner, dependents, paymentmethod, tenure, phoneservice, internetservice]]
    columns = ['gender', 'partner', 'dependents', 'paymentmethod', 'tenure', 'phoneservice', 'internetservice']
    df = pd.DataFrame(data, columns=columns)

    # Prediction
    pred = pipeline.predict(df)
    st.write("Prediction:", pred)

def display_form(pipeline, encoder):
    with st.form('Input_Features'):
        col1, col2 = st.columns(2)

        with col1:
            st.write('### Personal Information 👨')
            st.selectbox('Gender', options=['Male', 'Female'], key='gender')
            st.selectbox('Do you have a partner?', options=['Yes', 'No'], key='partner')
            st.selectbox('Do you have dependents?', options=['Yes', 'No'], key='dependents')
            st.selectbox('What is your main Payment Method?', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='paymentmethod')

        with col2:
            st.write('### Customer Information 💸')
            st.number_input('How long have you been a customer at Telco? (Enter in Months)', key='tenure', min_value=1, step=1)
            st.number_input('Enter your Monthly Charges', key='monthlycharges', min_value=15, max_value=120, step=1)
            st.selectbox('Do you have phone service?', options=['Yes', 'No'], key='phoneservice')
            st.selectbox('What type of internet service do you use?', options=['DSL', 'Fiber optic', 'No'], key='internetservice')

        submitted = st.form_submit_button('Submit', on_click=make_prediction, kwargs={'pipeline': pipeline, 'encoder': encoder})
        
        if submitted:
            st.write("Form submitted successfully!")
            
if __name__ == '__main__':
    pipeline, encoder = select_model()
    display_form(pipeline, encoder)

st.write(st.session_state)
