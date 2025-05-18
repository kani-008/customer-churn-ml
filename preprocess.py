import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()
    
    # Safely drop customerID only if it exists
    if 'customerID' in df.columns:
        df.drop(['customerID'], axis=1, inplace=True)


    # Handle TotalCharges as numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill missing numeric values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Encode categorical features
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = LabelEncoder().fit_transform(df[column].astype(str))

    return df
