import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from matplotlib.gridspec import GridSpec

# Set the style for Seaborn plots
sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("day_data.csv")

# Set page configuration for Streamlit
st.set_page_config(page_title="BIKERS",
                   page_icon="🚴‍♂️",
                   layout="wide")
st.markdown("---")

# Title and Subheaders for the Dashboard
st.title("Bike Sharing Analysis")
st.markdown("---")
st.subheader("DataFrame Jumlah Penyewa Sepeda")

# Display DataFrame in Streamlit
st.dataframe(day_df.head())

# Section for Data Overview
st.subheader("Overview")
st.write("Data ini menunjukkan jumlah penyewa sepeda per hari, berikut faktor cuaca, suhu, kelembaban, dan informasi lain.")

# Visualize total bike rentals by working day (Workingday: 1 = Hari Kerja, 0 = Hari Libur)
st.subheader("Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=day_df, estimator=sum, palette='Set2', ax=ax)
ax.set_title('Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur', fontsize=16)
ax.set_xlabel('Hari Libur vs Hari Kerja', fontsize=12)
ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
st.pyplot(fig)

# Section for Weather Effects on Bike Rentals
st.subheader("Pengaruh Cuaca Terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=day_df, estimator=sum, palette='Set1', ax=ax)
ax.set_title('Pengaruh Cuaca Terhadap Penggunaan Sepeda', fontsize=16)
ax.set_xlabel('Situasi Cuaca', fontsize=12)
ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
st.pyplot(fig)

# Section for Temperature Effects on Bike Rentals
st.subheader("Pengaruh Suhu Terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df, palette='coolwarm', ax=ax)
ax.set_title('Pengaruh Suhu Terhadap Penggunaan Sepeda', fontsize=16)
ax.set_xlabel('Suhu Normalisasi', fontsize=12)
ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
st.pyplot(fig)

# Sidebar Filters
st.sidebar.title("Filter Data")
working_day_filter = st.sidebar.selectbox("Pilih Hari", ('Hari Kerja', 'Hari Libur'))
if working_day_filter == 'Hari Kerja':
    filtered_df = day_df[day_df['workingday'] == 1]
else:
    filtered_df = day_df[day_df['workingday'] == 0]

# Display filtered data
st.sidebar.subheader("Data Penyewaan Berdasarkan Hari")
st.sidebar.write(filtered_df[['dteday', 'cnt']])

st.sidebar.subheader("Total Penyewaan Sepeda")
total_rentals = filtered_df['cnt'].sum()
st.sidebar.write(f"Total Penyewaan: {total_rentals}")

st.caption('Copyright (c), created by Febrisa Eka Nur Patricia')
