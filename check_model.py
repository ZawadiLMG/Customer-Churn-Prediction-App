import joblib

# Load the model
model = joblib.load('modelpipelines/Logistic_Regression.joblib')

# Print the model
print(model)

# Optionally, if it's a scikit-learn model, print more details
if hasattr(model, 'get_params'):
    print(model.get_params())
