import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.pipeline import run_bias_pipeline

st.title("⚖️ Dataset Bias Audit System")

# ensure data folder exists
os.makedirs("data", exist_ok=True)

uploaded_file = st.file_uploader("Upload CSV Dataset")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # save uploaded dataset
    save_path = "data/uploaded_dataset.csv"
    df.to_csv(save_path, index=False)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    columns = df.columns.tolist()

    target = st.selectbox("Select Target Column", columns)
    sensitive = st.selectbox("Select Sensitive Attribute", columns)

    if st.button("Run Bias Analysis"):

        with st.spinner("Running ML pipeline..."):

            results = run_bias_pipeline(df, target, sensitive)

        st.success("Analysis Complete")

        st.subheader("Model Accuracy")
        st.write(results["accuracy"])

        st.subheader("Bias Score")
        st.write(results["bias_score"])

        st.subheader("Bias Status")
        st.write(results["bias_status"])