import joblib
import os
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pandas as pd
import numpy as np
import tensorflow as tf

def pred_wrangle(data):
    data = data.copy()  # avoid SettingWithCopyWarning
    scaler = MinMaxScaler()
    
    data['Dependents'] = int(data['Dependents'].squeeze())
    
    # Optional: Reset index if needed before dropping columns (to avoid PerformanceWarning)
    if isinstance(data.index, pd.MultiIndex):
        data = data.reset_index()

    # data.drop(columns=['CoapplicantIncome'], inplace=True)
    
    # Data Scaling
    SCALER_DIR = 'scalers'
    # columns_to_scale = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Total_Income']
    
    applic = joblib.load(os.path.join(SCALER_DIR, 'ApplicantIncome_scaler.pkl'))
    data['ApplicantIncome'] = applic.transform(data[['ApplicantIncome']])

    loan = joblib.load(os.path.join(SCALER_DIR, 'LoanAmount_scaler.pkl'))
    data['LoanAmount'] = loan.transform(data[['LoanAmount']])

    loan_term = joblib.load(os.path.join(SCALER_DIR, 'Loan_Amount_Term_scaler.pkl'))
    data['Loan_Amount_Term'] = loan_term.transform(data[['Loan_Amount_Term']])

    total_income = joblib.load(os.path.join(SCALER_DIR, 'Total_Income_scaler.pkl'))
    data['Total_Income'] = total_income.transform(data[['Total_Income']])
    
    # Feature Engineering
    data['IncomePerDependent'] = data['Total_Income'] / (data['Dependents'].squeeze() + 1)
    data['Loan_to_IncomeRatio'] = data['LoanAmount'].squeeze() / data['Total_Income'].squeeze()
    data['Income_Stability_Factor'] = data['ApplicantIncome'].squeeze() * data['Credit_History'].squeeze()
    data['Employment_Income_Interaction'] = data['ApplicantIncome'].squeeze() * data['Self_Employed'].squeeze()
    data['Loan_Amount_Interaction'] = data['LoanAmount'].squeeze() / data['Loan_Amount_Term'].squeeze()
    data['Income_per_Term'] = data['Total_Income'].squeeze() / data['Loan_Amount_Term'].squeeze()
    data['Property_Adjusted_Income'] = data['Total_Income'].squeeze() * data['Property_Area'].squeeze()
    
    # Data Encoding
    # data = pd.get_dummies(data, columns=['Dependents'])
    
    # dropping unsed columns
    # data.drop(columns=['ID', 'Loan_ID'], inplace=True)
    data = data.drop(columns=['ID', 'Loan_ID', 'CoapplicantIncome'])
 
    max_float32 = np.finfo(np.float32).max
    data[np.isinf(data)] = max_float32 
# -----------------------------------------
    
    data.ffill(inplace=True)
    
    return data

def predict(data, model_path):
    # data = data.values 
    # print(data)
    data = pred_wrangle(pd.DataFrame(data))
    data = data.values.reshape(1, -1)
    data = tf.convert_to_tensor(data)
    
    

    # load the model
    model = tf.keras.models.load_model(model_path)

    confidence = model.predict(data)
    if confidence > 0.5:
        prediction = 1
    else:
        prediction = 0
    return {'confidence':confidence[0][0], 
            'prediction': prediction}

# Variable parser
# columns
col = ['ID',
 'Loan_ID',
 'Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'ApplicantIncome',
 'CoapplicantIncome',
 'LoanAmount',
 'Loan_Amount_Term',
 'Credit_History',
 'Property_Area',
 'Total_Income']

# Values
val = [70607, 'LP002560', 1, 1, 0, 1, 0, 15890, 89071.0759519, 188, 371, 1, 1, 600]

# Convert to dataframe
data = pd.DataFrame([val], columns=[col])
# make prediction
prediction = predict(data, 'model.h5')
print(prediction)