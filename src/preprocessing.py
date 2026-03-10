import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    df = df.dropna()

    encoders = {}

    for col in df.columns:
        if df[col].dtype == object:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le

    return df