import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(page_title="Solar Predictive Maintenance", layout="wide")

st.title("☀️ Solar Predictive Maintenance")


#This allows the models to be reused witjout having to be rerun
@st.cache_resource
def load_models():
    class_ = joblib.load("classifier.pkl")
    reg_ = joblib.load("Regressor.pkl")
    return class_, reg_

class_model, reg_model = load_models()




st.sidebar.header("Sensor Inputs")


#The user input
DC_POWER = st.sidebar.number_input("DC Power (W)")
AC_POWER = st.sidebar.number_input("AC_Power (W)")
HOUR = st.sidebar.number_input("Hour of the Day", max_value=23)
AMBIENT_TEMPERATURE = st.sidebar.number_input("Ambient Temperature (C)")
MODULE_TEMPERATURE = st.sidebar.number_input("Module Temperature (C)")
IRRADIATION = st.sidebar.number_input("Irradiation (W/m)")




#setting threshold for the rule-based classification
normal_threshold = 0
fault_threshold =  0.4

#based on the model, the predict_proba will be used to get the probability that an abnormality will occur
#Once the probability that an abnormality will occur, the final status function checkes if the less than the 
#the threshold aand also if the performance drop is zero or greater to give a normal signal and 
# for fault if the probability is higher than the fault threshold and for the rest for warning

def final_status(drop, prob):
    
        if drop >= normal_threshold and prob < fault_threshold:
            return 'Normal'
        elif prob > fault_threshold:
            return 'Fault'
        else:
            return 'Warning'

#this defines the the passing of the vallues into the the model to make prediction once the button is clicked
if st.button("Make Prediction"):
    #passes the user input into the model
    data = pd.DataFrame([{
        'DC_POWER' : DC_POWER,
        'AC_POWER' : AC_POWER,
        'HOUR' : HOUR,
        'AMBIENT_TEMPERATURE' : AMBIENT_TEMPERATURE,
        'MODULE_TEMPERATURE' : MODULE_TEMPERATURE,
        'IRRADIATION' : IRRADIATION
    }])


    reg_pred = reg_model.predict(data)[0]
    cls_pred = class_model.predict_proba(data)[0][0]

    #irr = IRRADIATION + 0.000001

    PERFORMANCE_RATIO = (AC_POWER / (IRRADIATION + 0.000001))
    PERFORMANCE_DROP = abs((PERFORMANCE_RATIO - reg_pred) / (reg_pred + 0.0000001))
    status = final_status(PERFORMANCE_DROP, cls_pred)
    
    #The formalu behinh the performace drop is calculated as shown above, and the reason is been that the performance ratio can be claculated manually without the need of a predictor
    #  and it was calculated and a predicted perfomance was gotten too. 
    # A comparison needs to be done to check how well is it to perform then. If the predicted value is greater than actual then there's an issue
    # this means that the system overperformed it actual performance meaning a surge in the intake of current, voltage or maybe the controller in the inverter malfunctioned
    # all of this cases are said to be true if the predicted value exceed the actual values.
    # The Performance drop has to be positive to have a good system.


    #this outputs the calculated values
    st.subheader("Output")

    col1, col2, col4, col3  = st.columns(4)
    #they are arranged in the order of presentation
    col1.metric('Performance Ratio Drop', round(PERFORMANCE_DROP, 3))
    col2.metric('Abnormality Probability', round(cls_pred, 3))
    col3.metric("Predicted PR", round(reg_pred, 2))
    col4.metric('Actual PR', round(PERFORMANCE_RATIO, 2))


    #using streamlit success function to give the signals, 
    #just like red means serious alert, green means all is fine and yellow gives a warning signal
    st.subheader("🚦 System Status")

    if status == "Normal":
        st.success("🟢 Normal Operation")
    elif status == "Warning":
        st.warning("🟡 Warning: Performance Dropping")
    else:
        st.error("🔴 Fault Detected")


#EnD

  