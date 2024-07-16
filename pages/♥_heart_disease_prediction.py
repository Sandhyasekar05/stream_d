import streamlit as st
import joblib
import numpy as np
model = joblib.load('hmodel.sav')
st.title('Heart Disease Prediction')
st.write("input features")

col1,col2,col3 = st.columns(3)
with col1:
    Age=st.number_input('Age',min_value=1, max_value=120, value=50)
    sex = st.selectbox('Sex', ['Male', 'Female']) 
    chest_pain=st.selectbox('chest pain type',[1,2,3,4])
    bp=st.number_input('Bp',min_value=80,max_value=200,value=120)
    chol=st.number_input('cholesterol',min_value=100,max_value=600,value=200)
with col2:   
    FBS=st.selectbox('FBS over 120',[0,1])
    EKG_results = st.selectbox('Resting Electrocardiographic Results', [0, 1 , 2])
    Max_HR= st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
    Exercise_angina= st.selectbox('Exercise Induced Angina', [0, 1])
with col3:
    ST_depression=st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=6.0, value=1.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2,3])
    ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=10, value=0)
    thal = st.selectbox('Thalassemia (thal)', [0, 1, 2, 3,4,5,6,7,8])
sex_value = 0 if sex == 'Male' else 1
if st.button('predict'):
        
        input_features = np.array([[Age, sex_value, chest_pain, bp, chol, FBS,EKG_results,Max_HR,Exercise_angina,ST_depression, slope, ca, thal]])
        prediction = model.predict(input_features)[0]
        # print(prediction)
    
       # Display the prediction
        if prediction == 'Presence':
          st.write('The model predicts that the person has heart disease.')
        else:
          st.write('The model predicts that the person does not have heart disease.')
    
    