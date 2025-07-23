import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(
    open("diabetes_trained_model.sav", "rb")
)

heart_model = pickle.load(
    open("heart_trained_model.sav", "rb")
)

parkinson_model = pickle.load(
    open("parkinson_trained_model.sav", "rb")
)

# sidebar
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson Prediction"],
        icons=["activity", "heart", "person"],  # from bootstrap
        default_index=0,
    )


# Diabetes Prediction Page

if (selected) == "Diabetes Prediction":
    # page title
    st.title("Diabetes Prediction using ML")

    # getting the input data from the users
    # columns for the input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        Glucose = st.text_input("Glucose level")
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value")

    with col2:
        BloodPressure = st.text_input("BloodPressure value")
        SkinThickness = st.text_input("SkinThickness value")
        Age = st.text_input("Age of the person")

    with col3:
        Insulin = st.text_input("Insulin level")
        BMI = st.text_input("BMI value")

    # code for prediction

    diab_diagnosis = ""

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict(
            [
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
            ]
        )

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is Diabetic"

        else:
            diab_diagnosis = "The person is not Diabetic"

        st.success(diab_diagnosis)


# Heart Prediction Page

elif (selected) == "Heart Disease Prediction":
    # page title
    st.title("Heart Disease Prediction using ML")

    # getting the input data from the users
    # columns for the input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Person Age")
        sex = st.text_input("Sex")
        cp = st.text_input("Chest Pain Type(Type of Angina)")
        trestbps = st.text_input("Resting Blood Pressure")
        thalach = st.text_input("Maximum heart rate achieved")

    with col2:
        chol = st.text_input("Serum Cholesterol level")
        fbs = st.text_input("Fasting Blood Pressure")
        restecg = st.text_input("Resting ECG Result")
        thal = st.text_input("Thalassemia Test Result")

    with col3:
        exang = st.text_input("Exercise Induced Angina")
        oldpeak = st.text_input("ST Depression Induced by Exercise")
        slope = st.text_input("Slope of the peak exercise ST segment")
        ca = st.text_input("Fluoroscopy Vessels Colored")

    # code for prediction

    heart_diagnosis = ""

    if st.button("Heart Test Result"):
        try:
            input_data = [
                [
                    int(age),
                    int(sex),
                    int(cp),
                    int(trestbps),
                    int(chol),
                    int(fbs),
                    int(restecg),
                    int(thalach),
                    int(exang),
                    float(oldpeak),
                    int(slope),
                    int(ca),
                    int(thal),
                ]
            ]

            heart_prediction = heart_model.predict(input_data)

            if heart_prediction[0] == 1:
                heart_diagnosis = "Defective Heart"

            else:
                heart_diagnosis = "Healthy Heart"

            st.success(heart_diagnosis)

        except ValueError:
            st.error("Please enter VALID values")


# Parkinsons Prediction Page

elif (selected) == "Parkinson Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    st.markdown(
        "Please enter the following measurements obtained from voice recordings."
    )
    st.divider()

    # Fundamental Frequency Section
    st.markdown("##### Fundamental Frequency")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)")
    with col4:
        pass # Empty column for spacing
    st.divider()

    # Jitter Section
    st.markdown("##### Jitter")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        MDVP_RAP = st.text_input("MDVP:RAP")
    with col4:
        MDVP_PPQ = st.text_input("MDVP:PPQ")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col2:
        pass # Fill remaining columns
    with col3:
        pass
    with col4:
        pass
    st.divider()

    # Shimmer Section
    st.markdown("##### Shimmer")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    with col2:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col3:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col4:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col2:
        Shimmer_DDA = st.text_input("Shimmer:DDA")
    with col3:
        pass
    with col4:
        pass
    st.divider()

    # Harmonics & Noise Section
    st.markdown("##### Harmonics & Noise")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        NHR = st.text_input("NHR")
    with col2:
        HNR = st.text_input("HNR")
    with col3:
        pass
    with col4:
        pass
    st.divider()

    # Nonlinear & Complexity Measures Section
    st.markdown("##### Nonlinear & Complexity Measures")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        RPDE = st.text_input("RPDE")
    with col2:
        DFA = st.text_input("DFA")
    with col3:
        D2 = st.text_input("D2")
    with col4:
        PPE = st.text_input("PPE")
    st.divider()

    # Spectral Spread Section
    st.markdown("##### Spectral Spread")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        pass
    with col4:
        pass
    st.divider()

    # code for prediction

    parkinson_diagnosis = ""

    if st.button("Parkinson's Test Result", help="Click to see the prediction"):
        try:
            input_data = [
                [
                    float(MDVP_Fo_Hz),
                    float(MDVP_Fhi_Hz),
                    float(MDVP_Flo_Hz),
                    float(MDVP_Jitter),
                    float(MDVP_Jitter_Abs),
                    float(MDVP_RAP),
                    float(MDVP_PPQ),
                    float(Jitter_DDP),
                    float(MDVP_Shimmer),
                    float(MDVP_Shimmer_dB),
                    float(Shimmer_APQ3),
                    float(Shimmer_APQ5),
                    float(MDVP_APQ),
                    float(Shimmer_DDA),
                    float(NHR),
                    float(HNR),
                    float(RPDE),
                    float(DFA),
                    float(spread1),
                    float(spread2),
                    float(D2),
                    float(PPE),
                ]
            ]

            parkinson_prediction = parkinson_model.predict(input_data)

            if parkinson_prediction[0] == 1:
                parkinson_diagnosis = "The person has Parkinson's disease"
                st.warning(parkinson_diagnosis)
            else:
                parkinson_diagnosis = "The person does not have Parkinson's disease"
                st.success(parkinson_diagnosis)

        except ValueError:
            st.error("⚠️ Please enter **all values** as valid numbers.")
        except Exception as e:
            st.error(f"An error occurred: {e}")