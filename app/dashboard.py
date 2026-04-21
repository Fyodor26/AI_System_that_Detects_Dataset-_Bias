import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.pipeline import run_bias_pipeline, run_bias_scan   # ✅ added import

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

    # -------------------------------
    # Single Bias Analysis
    # -------------------------------
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

    # -------------------------------
    # Full Bias Scan (NEW FEATURE)
    # -------------------------------
    # -------------------------------
# Full Bias Scan
# -------------------------------
if st.button("Run Full Bias Scan"):

    with st.spinner("Scanning all columns for bias..."):

        acc, ranking = run_bias_scan(df, target)

    st.success("Scan Complete")

    # Accuracy
    st.subheader("Model Accuracy")
    st.write(acc)

    # Ranking
    st.subheader("Bias Ranking")

    for i, (col, score) in enumerate(ranking, 1):
        st.write(f"{i}. {col} → {score:.3f}")

    # Visualization
    import matplotlib.pyplot as plt

    cols = [col for col, score in ranking]
    scores = [score for col, score in ranking]

    fig, ax = plt.subplots()
    ax.barh(cols[::-1], scores[::-1])
    ax.set_xlabel("Bias Score")
    ax.set_title("Bias Ranking (All Features)")

    st.pyplot(fig)