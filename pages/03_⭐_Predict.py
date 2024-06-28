import streamlit as st
import uuid
import os
import joblib
from sklearn.compose import ColumnTransformer
import pandas as pd
import datetime

# function to set up page configuration
st.set_page_config(
        page_title="Churn Prediction",
        page_icon="🤖",
        layout="wide",
        )

st.title("Churn Prediction⭐")


@st.cache_resource(show_spinner= 'Models loading...')
def load_logistic_regression_pipeline():
                pipeline = joblib.load('./models/Logistic_Regression.joblib')
                return pipeline


@st.cache_resource(show_spinner= 'models loading...')
def load_random_forest_pipeline():
                pipeline = joblib.load('./models/Random_Forest.joblib')
                return pipeline


def select_model():
                col1, col2 = st.columns(2)
                
                with col1:
                        st.selectbox('Select a model', options=[
                                'Logistic_Regression', 'Random Forest'], key='selected_model')
                with col2:
                        pass

        
                if st.session_state['selected_model'] == 'Logistic_Regression':
                        pipeline = load_logistic_regression_pipeline()
                else:
                        pipeline = load_random_forest_pipeline()

                encoder = joblib.load('models/encoder.joblib')

                return pipeline, encoder


if 'prediction' not in st.session_state:
                st.session_state['prediction'] = None
if 'probability' not in st.session_state:
                st.session_state['probability'] = None
                
st.cache_resource(show_spinner= 'models loading...')
def make_predictions(pipeline, encoder):
                gender = st.session_state['gender']
                partner = st.session_state['partner']
                dependents = st.session_state['dependents']
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
                seniorcitizen = st.session_state['seniorcitizen']
                tenure = st.session_state['tenure']
                monthlycharges = st.session_state['monthlycharges']
                totalcharges = st.session_state['totalcharges']


                # Convert tenure to integer
                tenure = int(tenure)

                # Create columns for the dataframe
                columns = ['gender', 'partner', 'dependents', 'phoneservice',
                        'multiplelines', 'internetservice', 'onlinesecurity', 'onlinebackup',
                        'deviceprotection', 'techsupport', 'streamingtv', 'streamingmovies',
                        'contract', 'paperlessbilling', 'paymentmethod', 'seniorcitizen',
                        'tenure','monthlycharges','totalcharges', 'customerid']
        

                # Create rows for the dataframe
                data = [['gender', 'partner', 'dependents', 'phoneservice',
                        'multiplelines', 'internetservice', 'onlinesecurity', 'onlinebackup',
                        'deviceprotection', 'techsupport', 'streamingtv', 'streamingmovies',
                        'contract', 'paperlessbilling', 'paymentmethod', 'seniorcitizen',
                        'tenure', 'monthlycharges', 'totalcharges','customerid']]
        
                # Create a dataframe
                df= pd.DataFrame(data, columns=columns)

                # Save dataframe to csv file as history data
                df.to_csv('./Data/history.csv' ,mode='a',header=not os.path.exists('./Data/history.csv'), index=False)


                # Change the data types to numerical 
                df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
                df['monthlycharges'] = pd.to_numeric(df['monthlycharges'], errors='coerce')
                df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')



                # Make a prediction and probability
                pred = pipeline.predict(df)
                pred_int = int(pred[0])
                prediction = encoder.inverse_transform([pred_int])


                # Get probabilities
                probability = pipeline.predict_proba(df)

                # Updating/Save in session state
                st.session_state['prediction'] = prediction
                st.session_state['probability'] = probability

                # This makes prediction for History
                df['prediction']= prediction
                df['Predictions Time'] = datetime.date.today()
                df['Model Used'] = st.session_state['selected_model']

                return prediction, probability
        

def display_form():
                pipeline, encoder = select_model()
                col1, col2, col3, col4 = st.columns(4)
        
                with col1:
                        st.write('### Personal Info👨')
                        st.selectbox('What is your gender?', ['Male', 'Female'], key='gender')
                        st.selectbox('Do you have a partner?', ['Yes', 'No'], key='partner')
                        st.selectbox('Do you have people that depend on you?', ['Yes', 'No'], key='dependents')
                        st.selectbox('Are you a senior citizen?', ['Yes', 'No'], key='seniorcitizen')
        
                with col2:
                        st.write('#### Customer Info👪')
                        st.selectbox('Do you use paperless billing?', ['Yes', 'No'], key='paperlessbilling')
                        st.selectbox('What type of payment do you use?', ['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'], key='paymentmethod')
                        st.selectbox('Do you have access to phone services?', ['Yes', 'No'], key='phoneservice')
                        st.selectbox('Do you have multiple lines?', ['Yes', 'No'], key='multiplelines')
                        st.selectbox('Do you have access to tech support?', ['Yes', 'No'], key='techsupport')
                
                with col3:
                        st.write('#### Services🔮')
                        st.selectbox('What type of internet connection do you use?', ['DSL', 'Fiber Optic', 'No'], key='internetservice')
                        st.selectbox('Do you have online security?', ['Yes', 'No'], key='onlinesecurity')
                        st.selectbox('Do you have online backup storage?', ['Yes', 'No'], key='onlinebackup')
                        st.selectbox('Do you have device protection?', ['Yes', 'No'], key='deviceprotection')
                        st.selectbox('Do you stream TV channels smoothly?', ['Yes', 'No'], key='streamingtv')
                with col4:
                        st.write('#### Payment Info💰')
                        st.selectbox('Are you able to stream your movies perfectly?', ['Yes', 'No'], key='streamingmovies')
                        st.selectbox('What type of contract have you subscribed to?', ['Month-to-Month', 'One Year', 'Two Year'], key='contract')

                        
                        if 'tenure' not in st.session_state:
                                st.session_state.tenure = 12
                        st.number_input('How long have you been our customer?', min_value=0, max_value=72, value=st.session_state.tenure)
                
                        if 'monthlycharges' not in st.session_state:
                                st.session_state.monthlycharges = 100
                        st.number_input('How much is your monthly charges?', min_value=0, max_value=1000, value=st.session_state.monthlycharges)

                        if 'totalcharges' not in st.session_state:
                                st.session_state.totalcharges = 1000
                        st.number_input('How much is your total annual charges?', min_value=0, max_value=10000, value=st.session_state.totalcharges)
                

                # Prediction button
                with st.form(key='prediction_form'):
                        st.form_submit_button('Make prediction', on_click=make_predictions, kwargs=dict(pipeline=pipeline, encoder=encoder))
        
if __name__ == "__main__":
                st.markdown("### Make a Prediction")
                display_form()

                prediction = st.session_state['prediction']
                probability = st.session_state['probability']

                if not prediction:
                        st.markdown("### Prediction shows here!")
                        st.divider()
                elif prediction == "Yes":
                        probability_of_yes = probability[0][1] * 100
                        st.markdown(f"### The customer is highly likely to churn | Probability = {round(probability_of_yes,2)}%")
                else:
                        probability_of_no = probability[0][0]*100
                        st.markdown(f"### The customer will not churn | Probability = {round(probability_of_no,2)}%")
        
st.write(st.session_state)
        
                