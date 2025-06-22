import streamlit as st
import numpy as np
import pandas as pd



st.title("Student Score Prediction")

st.header("Enter Student Details")

gender = st.selectbox("Gender", ['Male', 'Female'])

ethnicity = st.selectbox(
    "Race/Ethnicity", 
    ["Group A", "Group B", "Group C", "Group D","Group E" ]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education", 
    ["some High School", "High School", "Some College", 
    "Associate's Degree", "Bachelor's Degree", 
    "Master's Degree"]
)

lunch = st.selectbox(
    "Lunch",
    [
        "Standard",
        "Free/Reduced"
    ]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["None", "Completes"]
)

reading_score = st.number_input(
    "Reading", min_value= 0.0, max_value=100.0, steps=1.0
)

writing_score = st.number_input(
    "Writing Score", min_value=0.0, max_value=100.0, steps=1.0
)


#if st.button("Predict Math Score"):
    