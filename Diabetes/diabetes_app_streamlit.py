import numpy as np
import pandas as pd
import streamlit as st
import pickle


loaded_model = pickle.load(
    open(
        "S:/Skill_WORK/CODE/Multiple_Disease_prediction/Diabetes/diabetes_trained_model.sav",
        "rb",
    )
)

feature_names = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]


def diabetes_prediction(input_data):
    input_df = pd.DataFrame([input_data], columns=feature_names)

    prediction = loaded_model.predict(input_df)

    if prediction[0] == 0:
        return "The person is not Diabetic"
    else:
        return "The person is Diabetic"


def main():
    # giving the titile
    st.title("Diabetes Prediction Web App")

    # getting the input data from the user

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("BloodPressure value")
    SkinThickness = st.text_input("SkinThickness value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value")
    Age = st.text_input("Age of the person")

    diagnosis = ""

    if st.button("Diabetes test result"):
        diagnosis = diabetes_prediction(
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]
        )

    st.success(diagnosis)


if __name__ == "__main__":
    main()
