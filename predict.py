import pickle
import numpy as np
from preprocess import preprocess_data
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_single(input_dict):
    df = pd.DataFrame([input_dict])
    df = preprocess_data(df)
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0].max()
    return "Yes" if prediction == 1 else "No", round(probability, 2)
