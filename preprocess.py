import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()
    df.drop(['customerID'], axis=1, inplace=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.fillna(df.mean(numeric_only=True), inplace=True)

    for column in df.select_dtypes(include=['object']).columns:
        df[column] = LabelEncoder().fit_transform(df[column])
    
    return df
