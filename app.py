import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Loading trained model
model_path = "drug_prediction_pipeline.pkl"  
with open(model_path, "rb") as file:
    model = pickle.load(file)

# LabelEncoders for consistent encoding
labelled_encoder_sex = LabelEncoder()
labelled_encoder_blood_pressure = LabelEncoder()
labelled_encoder_cholesterol = LabelEncoder()

# Dummy fit for LabelEncoders to match training
labelled_encoder_sex.classes_ = np.array(['Female', 'Male'])
labelled_encoder_blood_pressure.classes_ = np.array(['High', 'Low', 'Normal'])
labelled_encoder_cholesterol.classes_ = np.array(['High', 'Normal'])

# Streamlit App
st.title("Personalized Drug Recommendation System")
st.write("Discover the best-suited medication for patients based on key health parameters, ensuring effective and personalized treatment.")

# Input fields
age = st.slider("Age", 0, 100, 25)  
sex = st.selectbox("Sex", ['Female', 'Male'])
blood_pressure = st.selectbox("Blood Pressure", ['Low', 'Normal', 'High'])
cholesterol = st.selectbox("Cholesterol", ['Normal', 'High'])
sodium_to_potassium = st.slider("Sodium-to-Potassium Ratio", 0, 50, 10)

# Predict Button
if st.button("Predict"):
    # Encode inputs
    sex_encoded = labelled_encoder_sex.transform([sex])[0]
    bp_encoded = labelled_encoder_blood_pressure.transform([blood_pressure])[0]
    chol_encoded = labelled_encoder_cholesterol.transform([cholesterol])[0]

    # input array including age
    input_data = np.array([[age, sex_encoded, bp_encoded, chol_encoded, sodium_to_potassium]])
    
    # Prediction
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted drug is: {prediction}")
