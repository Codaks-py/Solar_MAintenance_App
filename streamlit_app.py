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



DC_POWER = st.sidebar.number_input("DC Power (W)")
AC_POWER = st.sidebar.number_input("AC_Power (W)")
HOUR = st.sidebar.number_input("Hour of the Day", max_value=23)
AMBIENT_TEMPERATURE = st.sidebar.number_input("Ambient Temperature (C)")
MODULE_TEMPERATURE = st.sidebar.number_input("Module Temperature (C)")
IRRADIATION = st.sidebar.number_input("Irradiation (W/m)")





normal_threshold = 0
fault_threshold =  0.4


def final_status(prob, drop):
    
        if prob > normal_threshold and drop < fault_threshold:
            return 'Normal'
        elif drop > fault_threshold:
            return 'Fault'
        else:
            return 'Warning'


if st.button("Make Prediction"):

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

    irr = IRRADIATION + 0.000001

    PERFORMANCE_RATIO = abs(AC_POWER / irr)
    PERFORMANCE_DROP = abs((PERFORMANCE_RATIO - reg_pred) / (reg_pred + 0.0000001))
    status = final_status(PERFORMANCE_DROP, cls_pred)
    




    st.subheader("Output")

    col1, col2, col4, col3  = st.columns(4)

    col1.metric('Performance Ratio Drop', round(PERFORMANCE_DROP, 3))
    col2.metric('Abnormality Probability', round(cls_pred, 3))
    col3.metric("Predicted PR", round(reg_pred, 2))
    col4.metric('Actual PR', round(PERFORMANCE_RATIO, 2))



    st.subheader("🚦 System Status")

    if status == "Normal":
        st.success("🟢 Normal Operation")
    elif status == "Warning":
        st.warning("🟡 Warning: Performance Dropping")
    else:
        st.error("🔴 Fault Detected")




  