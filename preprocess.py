import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()

    # Safely drop customerID if present
    df.drop(['customerID'], axis=1, inplace=True, errors='ignore')

    # Convert TotalCharges to numeric, force errors to NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill numeric NaNs with column means
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Encode categorical columns
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        try:
            df[column] = le.fit_transform(df[column])
        except:
            df[column] = le.fit_transform(df[column].astype(str))  # handle unexpected types

    return df
