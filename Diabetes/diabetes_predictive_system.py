import numpy as np
import pickle
import pandas as pd

loaded_model = pickle.load(
    open(
        "S:/Skill_WORK/CODE/Multiple_Disease_prediction/Diabetes/diabetes_trained_model.sav",
        "rb",
    )
)

input_data = (10, 168, 74, 0, 0, 38, 0.537, 34)
input_df = pd.DataFrame([input_data])

prediction = loaded_model.predict(input_df)

if prediction[0] == 0:
    print("The person is not Diabetic")

else:
    print("The person is Diabetic")
