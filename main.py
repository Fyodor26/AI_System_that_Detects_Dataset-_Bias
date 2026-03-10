import pandas as pd
import os

from src.pipeline import run_bias_pipeline

data_path = "data/uploaded_dataset.csv"

# check if dataset exists
if not os.path.exists(data_path):

    print("No dataset found in /data folder.")
    print("Please upload a dataset using the Streamlit dashboard first.")
    exit()

print("Dataset found. Loading...")

df = pd.read_csv(data_path)

print("\nColumns in dataset:")
print(df.columns)

target = input("\nEnter target column: ")
sensitive = input("Enter sensitive column: ")

results = run_bias_pipeline(df, target, sensitive)

print("\nModel Accuracy:", results["accuracy"])
print("Bias Before:", results["bias_before"])
print("Bias After:", results["bias_after"])
print("Bias Reduction:", results["bias_reduction"])