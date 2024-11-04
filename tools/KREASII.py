import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and description
st.title("Data Analysis App")
st.write("This app allows you to perform data analysis tasks based on Kelompok08's project.")
# Load data
data = pd.read_csv("https://github.com/NobelNizam/buku_kating_bayessian/tree/main/tools/Pendataan Peserta Magang CEO HMSD 2024 (Responses) - Form Responses 1.csv")
# Display dataset
if st.checkbox("Show Data"):
    st.write(data.head())
# Data Analysis Section
st.subheader("Data Analysis")
# Example: Correlation Heatmap
if st.checkbox("Show Correlation Heatmap"):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)
# Filter data based on a selected column
column = st.selectbox("Select column to analyze", data.columns)
st.write(f"Data in selected column {column}:")
st.write(data[column].describe())
