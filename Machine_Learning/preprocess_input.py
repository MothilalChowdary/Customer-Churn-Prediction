import pandas as pd
import numpy as np
import joblib

SERVICE_MAP = {
    'Yes': 1,
    'No': 0,
    'No internet service': 0,
    'No phone service': 0
}

INTERNET_MAP = {
    'DSL': 1,
    'Fiber optic': 1,
    'No': 0
}

BINARY_MAP = {
    'Yes': 1,
    'No': 0,
    'Male': 1,
    'Female': 0
}

def safe_map(value, mapping):
    if isinstance(value, (int, float, np.integer)):
        return int(value)
    return mapping.get(value, 0)

def preprocess_input(raw_input, model_name):
    df = pd.DataFrame([raw_input])

    df['tenure'] = df['tenure'].astype(float)
    df['MonthlyCharges'] = df['MonthlyCharges'].astype(float)
    df['avg_charge_per_month'] = (df['MonthlyCharges'] * df['tenure']) / (df['tenure'] + 1)



    services = [
        'PhoneService','MultipleLines','OnlineSecurity',
        'OnlineBackup','DeviceProtection','TechSupport',
        'StreamingTV','StreamingMovies'
    ]

    for col in services:
        df[col] = df[col].apply(lambda x: safe_map(x, SERVICE_MAP))

    df['InternetService'] = df['InternetService'].apply(lambda x: safe_map(x, INTERNET_MAP))

    binary_cols = ['gender', 'Partner', 'Dependents', 'PaperlessBilling']
    for col in binary_cols:
        df[col] = df[col].apply(lambda x: safe_map(x, BINARY_MAP))

    categorical_cols = ['Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    if model_name.lower() == 'rf':
        feature_columns = joblib.load("Machine_Learning/feature_columns_rf.pkl")
    elif model_name.lower() == 'xgb':
        feature_columns = joblib.load("Machine_Learning/feature_columns_xgb.pkl")
    else:
        raise ValueError("Unknown model_name. Choose 'rf' or 'xgb'.")

    df = df.reindex(columns=feature_columns, fill_value=0)
    return df
