# import streamlit as st
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
#     return joblib.load('./models/Logistic_Regression.joblib')

# @st.cache_resource()
# def load_random_forest_model_pipeline():
#     return joblib.load('./models/Random_Forest.joblib')

# @st.cache_resource()
# def load_encoder():
#     return joblib.load('./models/encoder.joblib')


# def select_model():
#     if 'selected_model' not in st.session_state:
#         st.session_state['selected_model'] = 'Logistic Regression'
    
#     col1, _ = st.columns(2)
#     with col1:
#         st.selectbox('Select A Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')
        
#     if st.session_state['selected_model'] == 'Logistic Regression':
#         pipeline = load_logistic_regression_model_pipeline()
#     else:
#         pipeline = load_random_forest_model_pipeline()
        
#     encoder = load_encoder()
    
#     return pipeline, encoder

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

# def display_form(pipeline, encoder):
#     with st.form('Input_Features'):
#         col1, col2 = st.columns(2)

#         with col1:
#             st.write('### Personal Information 👨')
#             st.selectbox('Gender', options=['Male', 'Female'], key='gender')
#             st.selectbox('Do you have a partner?', options=['Yes', 'No'], key='partner')
#             st.selectbox('Do you have dependents?', options=['Yes', 'No'], key='dependents')
#             st.selectbox('What is your main Payment Method?', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='paymentmethod')

#         with col2:
#             st.write('### Customer Information 💸')
#             st.number_input('How long have you been a customer at Telco? (Enter in Months)', key='tenure', min_value=1, step=1)
#             st.number_input('Enter your Monthly Charges', key='monthlycharges', min_value=15, max_value=120, step=1)
#             st.selectbox('Do you have phone service?', options=['Yes', 'No'], key='phoneservice')
#             st.selectbox('What type of internet service do you use?', options=['DSL', 'Fiber optic', 'No'], key='internetservice')

#         submitted = st.form_submit_button('Submit', on_click=make_prediction, kwargs={'pipeline': pipeline, 'encoder': encoder})
        
#         if submitted:
#             st.write("Form submitted successfully!")
            
# if __name__ == '__main__':
#     pipeline, encoder = select_model()
#     display_form(pipeline, encoder)

# st.write(st.session_state)

import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title = "Prediction Page",
    page_icon = "🚀",
    layout = 'wide'
)
st.title('CUSTOMER CHURN PREDICTION 🚀')
st.sidebar.success("select a page above")

# function to load the models
st.cache_resource(show_spinner='models loading ...')
def select_model():
    col1,col2 = st.columns(2) # to reduce the size of the select box
    with col1:
        st.selectbox('select a model', options=['Random_Forest','Logistic_Regression'], key='selected_model') # a selectbox with the option of two models
    with col2:
        pass
    if st.session_state['selected_model']=='Random_Forest':
        pipeline = joblib.load('./models/Random_Forest.joblib')
    else:
        pipeline = joblib.load('./models/Logistic_Regression.joblib')
    encoder = joblib.load('./models/encoder.joblib')
    return pipeline,encoder  
     
#columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       #'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       #'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       #'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       #'MonthlyCharges', 'TotalCharges']      
       
# function to make predictions
def make_prediction(pipeline,encoder):
    gender = st.session_state['gender']
    seniorcitizen = st.session_state['seniorcitizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = int(st.session_state['tenure'])
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling = st.session_state['paperlessbilling']
    paymentmethod = st.session_state['paymentmethod']
    monthlycharges = float(st.session_state['monthlycharges'])
    totalcharges = float(st.session_state['totalcharges'])
    
#    data = {'gender': [gender], 'SeniorCitizen': [seniorcitizen], 'Partner': [partner], 'Dependents': [dependents],
 #       'tenure': [tenure], 'PaperlessBilling': [paperlessbilling],'PaymentMethod': [paymentmethod], 'MonthlyCharges': [monthlycharges],
  #      'TotalCharges': [totalcharges], 'PhoneService': [phoneservice], 'MultipleLines': [multiplelines], 'InternetService': [internetservice],
   #    'OnlineSecurity': [onlinesecurity], 'OnlineBackup': [onlinebackup], 'DeviceProtection': [deviceprotection], 'TechSupport': [techsupport],
    #   'StreamingTV': [streamingtv], 'StreamingMovies': [streamingmovies], 'Contract': [contract] }

    data = [[gender, partner, dependents, paymentmethod, tenure, phoneservice, internetservice, seniorcitizen, multiplelines, 
             onlinesecurity,  onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, 
             contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]      
       ]
    columns = [gender, partner, dependents, paymentmethod, tenure, phoneservice, internetservice, seniorcitizen, multiplelines, 
             onlinesecurity,  onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, 
             contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]      
    
    df = pd.DataFrame(data, columns=columns)

    # Make predictions
    pred = pipeline.predict(df)
    pred_int =int(pred[0])
    # The encoder.inverse_transform expects a 1D array
    prediction = encoder.inverse_transform([pred_int])
    probability = pipeline.predict_proba(df)
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability[0]
    return prediction, probability[0]
    
if 'prediction' not in st.session_state:
    st.session_state['prediction']=None
    
if 'probability' not in st.session_state:
    st.session_state['probability']=None   
    
def display_form():
    pipeline,encoder = select_model()
    with st.form('input-features'):
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.write('### Personal Info 👨‍⚖️')
            st.selectbox('select your Gender', key='gender', options=['Female', 'Male'])
            st.selectbox('Are you a SeniorCitizen?',key='seniorcitizen',options=['Yes','No'])
            st.selectbox('Do you have a partner?',key='partner',options=['Yes','No'])
            st.selectbox('Do you have dependents?',key='dependents',options=['Yes','No'])
        with col2:
            st.write('### Work info 👨‍🎨')
            st.number_input('Enter your tenure',key='tenure',max_value=72,min_value=0,step=1)
            st.selectbox('Choose your Contract',key='contract',options=['Month-to-month', 'One year', 'Two year'])
            st.selectbox('Do you do paperlessBilling',key='paperlessbilling',options=['Yes','No'])
            st.selectbox('Choose your payment method',key='paymentmethod',options=['Electronic check', 'Bank transfer (automatic)', 'Mailed check',
       'Credit card (automatic)'])
            st.number_input('Enter your Monthly Charges',key='monthlycharges',max_value=118 ,min_value=18 ,step=1)
            st.number_input('Enter your Total Charges',key='totalcharges',min_value=118 ,max_value=8670,step=1)    
        with col3:
            st.write('### Internet Services 🌐')    
            st.selectbox('Do you have a phoneservice?',key='phoneservice',options=['Yes','No'])
            st.selectbox('Do you have multiplelines?',key='multiplelines',options=['Yes','No'])
            st.selectbox('Choose your internetservice',key='internetservice',options=['Fiber optic', 'No', 'DSL'])
            st.selectbox('Do you stream TV?',key='streamingtv',options=['Yes','No'])
            st.selectbox('Do you stream movies?',key='streamingmovies',options=['Yes','No'])
        with col4:
            st.write('### Security 🚨')    
            st.selectbox('Do you have onlinesecurity?',key='onlinesecurity',options=['Yes','No']) 
            st.selectbox('Do you have onlinebackup?',key='onlinebackup',options=['Yes','No'])
            st.selectbox('Do you have deviceprotection?',key='deviceprotection',options=['Yes','No'])
            st.selectbox('Do you have techsupport?',key='techsupport',options=['Yes','No'])
            
        st.form_submit_button('submit',on_click=make_prediction,kwargs=dict(pipeline=pipeline,encoder=encoder))
             
if __name__ == '__main__':
    display_form()
    
    final_prediction = st.session_state['prediction']
    if not final_prediction:
        st.write('### PREDICTIONS!!')
        st.divider()
    else:
        st.write(f'WILL THE CUSTOMER CHURN ? {final_prediction}')
    st.write(st.session_state)
