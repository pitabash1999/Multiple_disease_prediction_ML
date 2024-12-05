# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 



diabetes_model=pickle.load(open('Diabetes_model.sav','rb'))

heart_model=pickle.load(open('Heart_disease.sav','rb'))

parkinson_model=pickle.load(open('parkinsons_prediction.sav','rb'))

breast_cancer_model=pickle.load(open('breast_cancer.sav','rb'))



     
def diabetes_prediction(input_data):
    input_data_as_nparray=np.asarray(input_data)
    reshaped_data=input_data_as_nparray.reshape(1,-1)
    prediction=diabetes_model.predict(reshaped_data)
    
    if(prediction[0]==0):
        return "Person is not diabetic."
    else:
        return "Person is diabatic"


        
def diabetes():
    #Setting title of the webpage
    st.title("Female diabetes prediction")
    
    #declaring required variables
    #pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_predigree,age
    
    
    #taking input from textareas and assigning them to their respective variables
    pregnancies=st.text_input("Pregnancies")
    glucose=st.text_input("Glucose")
    blood_pressure=st.text_input("Blood Pressure")
    skin_thickness=st.text_input("Skin thickness")
    insulin=st.text_input("Insulin")
    bmi=st.text_input("BMI")
    diabetes_predigree=st.text_input("Diabates pedigree")
    age=st.text_input("Age")
    
    diabetes_input=(pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_predigree,age)
    
    #declaring output res as a null string
    
    prediction='';
    
    if(st.button("PREDICT")):
        try:
            prediction=diabetes_prediction(diabetes_input)
            st.success(prediction)
        except Exception:
            st.error("Give inputs properly.")
            
            
#*******************************************************************

def heart_predict(heart_input):
    heart_input_data_as_nparray=np.asarray(heart_input)
    heart_reshaped_data=heart_input_data_as_nparray.reshape(1,-1)
    prediction=heart_model.predict(heart_reshaped_data)
    
    if(prediction[0]==0):
        return "Person is not suffering from heart disease"
    else:
        return "Person is suffering from heart disease"
    
def Heart():
    #Setting title of the webpage
    st.title("Heart disease prediction.")
    st.markdown("(*)means all fields are mandatory")
    
   
    
    #taking input from textareas and assigning them to their respective variables
    age=st.text_input("Age*")
    sex=st.text_input("Gender 1(MALE) 0(FEMALE)*")
    cp=st.text_input("Chest pain type(0,1,2)*")
    trestbps=st.text_input("resting blood pressure*")
    chol=st.text_input("Serum cholestoral*")
    fbs=st.text_input("Fasting blood sugar")
    restecg=st.text_input("Resting electrocardiographic results(0,1,2)*")
    thalach=st.text_input("Exercise induced angina*")
    exang=st.text_input("Maximum heart rate achieved*")
    oldpeak=st.text_input("Oldpick*")
    slope=st.text_input("Slope*")
    ca=st.text_input("CA*")
    thal=st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect*")
    
    
    heart_input=(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    
    #declaring output res as a null string
    
    heart_prediction='';
    
    if(st.button("PREDICT")):
        try:
            heart_prediction=heart_predict(heart_input)
            st.success(heart_prediction)
        except Exception:
            st.error("Give inputs properly.")
            
                
        
#*************************************************************************

def parkinson_predict(parkinson_input):
    parkinson_input_data_as_nparray=np.asarray(parkinson_input)
    parkinson_reshaped_data=parkinson_input_data_as_nparray.reshape(1,-1)
    prediction=parkinson_model.predict(parkinson_reshaped_data)
    
    if(prediction[0]==0):
        return "Person is not suffering from  parkinson"
    else:
        return "Person is suffering from  parkinson"

def parkinson():
    #Setting title of the webpage
    st.title("Parkinsons disease prediction.")
    st.markdown("(*)means all fields are mandatory")
    
   
    
    #taking input from textareas and assigning them to their respective variables
    mdvp=st.text_input("Average vocal fundamental frequency*")
    max_mdvp=st.text_input("Maximum vocal fundamental frequency*")
    low_mdvp=st.text_input("Minimum vocal fundamental frequency*")
    per_mdvp=st.text_input("MDVP:Jitter(%)*")
    abs_mdvp=st.text_input("MDVP:Jitter(Abs)*")
    mdvp_rap=st.text_input("MDVP:RAP*")
    mdvp_prq=st.text_input("MDVP:PPQ*")
    jitter_ddp=st.text_input("Jitter:DDP*")
    mdvp_shim=st.text_input("MDVP:Shimmer*")
    mdvp_shim_db=st.text_input("MDVP:Shimmer(dB)*")
    shim_aq3=st.text_input("Shimmer:APQ3*")
    shim_aq5=st.text_input("Shimmer:APQ5*")
    mdvp_apq=st.text_input("MDVP:APQ*")
    shim_dda=st.text_input("Shimmer:DDA*")
    nhr=st.text_input("NHR*")
    hnr=st.text_input("HNR*")
    rpde=st.text_input("RDPE*")
    dfa=st.text_input("DFA*")
    spread1=st.text_input("Spread1*")
    spread2=st.text_input("Spread2*")
    d2=st.text_input("D2*")
    ppe=st.text_input("PPE*")
    
    parkinson_input=(mdvp, max_mdvp,low_mdvp,per_mdvp,abs_mdvp,mdvp_rap,mdvp_prq,jitter_ddp,mdvp_shim,mdvp_shim_db,shim_aq3,shim_aq5,
                     mdvp_apq,shim_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe)
    
    #declaring output res as a null string
    
    parkinson_prediction='';
    
    if(st.button("PREDICT")):
        try:
            parkinson_prediction=parkinson_predict(parkinson_input)
            st.success(parkinson_prediction)
        except Exception:
            st.error("Give inputs properly(Make sure all fields are filled)")
       
        
#***********************************************************************************

def bc_predict(bc_input):
    bc_input_data_as_nparray=np.asarray(bc_input)
    bc_reshaped_data=bc_input_data_as_nparray.reshape(1,-1)
    prediction=breast_cancer_model.predict(bc_reshaped_data)
    
    if(prediction[0]==0):
        return "The breast cancer is Benign"
    else:
        return "The breast cancer is Malignant"
    
def breast_cancer():
    #Setting title of the webpage
    st.title("Breast cancer classification(Benign,Malignant)")
    st.markdown("(*)means all fields are mandatory")
    
   
    
    #taking input from textareas and assigning them to their respective variables
    mean_radius=st.number_input("Radius_mean*")
    mean_texture=st.number_input("Texture_mean*")
    perimeter_mean=st.number_input("Perimeter mean*")
    area_mean=st.number_input("Area mean*")
    smoothness_mean=st.number_input("Smoothness mean*")
    compactness_mean=st.number_input("Compactness mean*")
    concavity_mean=st.number_input("Concavity mean*")
    concave_points_mean=st.number_input("concave points mean*")
    symmetry_mean=st.number_input("Symmetry mean*")
    fractal_dimension_mean=st.number_input("Fractal dimension mean*")
    radius_se=st.number_input("Radius_se*")
    texture_se=st.number_input("Texture_se*")
    perimeter_se=st.number_input("Perimeter_se*")
    area_se=st.number_input("Area_se*")
    smoothness_se=st.number_input("Smoothness_se*")
    compactness_se=st.number_input("Compactness_se*")
    concavity_se=st.number_input("Concavity_se*")
    concave_points_se=st.number_input("Concave points_se*")
    symmetry_se=st.number_input("Symmetry_se*")
    fractal_dimension_se=st.number_input("Fractal_dimension_se*")
    radius_worst=st.number_input("Radius_worst*")
    texture_worst=st.number_input("Texture_worst*")
    perimeter_worst=st.number_input("Perimeter_worst*")
    area_worst=st.number_input("Area_worst*")
    smoothness_worst=st.number_input("smoothness_worst*")
    compactness_worst=st.number_input("Compactness_worst*")
    concavity_worst=st.number_input("Concavity_worst*")
    concave_points_worst=st.number_input("concave points_worst*")
    symmetry_worst=st.number_input("Symmetry_worst*")
    fractal_dimension_worst=st.number_input("Fractal_dimension_worst*")
    
    
    bc_input=(mean_radius,mean_texture,perimeter_mean,area_mean,
                     smoothness_mean,compactness_mean,concavity_mean,
                     concave_points_mean,symmetry_mean,fractal_dimension_mean,
                     radius_se,texture_se,perimeter_se,area_se,smoothness_se,
                     compactness_se,concavity_se,concave_points_se,symmetry_se,
                     fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,
                     area_worst,smoothness_worst,compactness_worst,concavity_worst,
                     concave_points_worst,symmetry_worst,fractal_dimension_worst)
    
    #declaring output res as a null string
    
    bc_prediction='';
    
    if(st.button("PREDICT")): 
        try:
            bc_prediction=bc_predict(bc_input)
            st.success(bc_prediction)
        except Exception:
            st.error("Give inputs properly(Make sure all fields are filled)")
        
            
                

with st.sidebar:
     selected=option_menu("Disease_prediction using ML",
                          ["Breast cancer",
                           "Parkinsons",
                           "Diabetes",
                           "Heart"],
                          default_index=0)
         
    
def main():
    
    if(selected=="Diabetes"):
        diabetes()
    if(selected=="Heart"):
        Heart()
    if(selected=='Parkinsons'):
        parkinson()
    if(selected=='Breast cancer'):
        breast_cancer()
    

   


if(__name__=='__main__'):
    main()    