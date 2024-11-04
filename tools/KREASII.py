import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Data Kesibukan Peserta Kaderisasi saat magang CEO HMSD 2024")

# Penjelasan Umum
st.write("""
Selamat datang di artikel analisis data peserta magang CEO HMSD 2024 oleh Kelompok 1 Jordan. 
Pada analisis ini, kita akan melihat dan menjelaskan data peserta magang yang berasal dari berbagai daerah dan melakukan analisis statistik 
deskriptif serta visualisasi data untuk memberikan gambaran mengenai peserta magang ini.
""")

# 1. Membaca Dataset
st.header("1. Membaca Dataset")
st.write("Dataset diambil dari file CSV yang berisi data peserta magang CEO HMSD 2024.")
# Link CSV dari GitHub
data_magang = pd.read_csv('https://raw.githubusercontent.com/NobelNizam/buku_kating_bayessian/refs/heads/main/tools/Pendataan%20Peserta%20Magang%20CEO%20HMSD%202024%20(Responses)%20-%20Form%20Responses%201.csv')
st.dataframe(data_magang)  # Menampilkan beberapa baris data untuk referensi
data_magang =  data_magang.rename(columns={'8. Rating Kesibukan Saat Magang (1-5, 5 semakin sibuk)': 'Rating Kesibukan'})
kolom_J = data_magang['Rating Kesibukan']

st.header("Distribusi Rating Kesibukan saat Magang CEO HMSD Adyatama 2024")
sns.set(style="whitegrid")
plt.figure(figsize=(10, 7))
sns.histplot(kolom_J, bins=9, kde=True, color="purple")
plt.title("Distribusi Rating Kesibukan saat Magang")
plt.xlabel("Rating Kesibukan")
plt.ylabel("Jumlah Peserta")
plt.show()

st.header("Boxplot")
plt.figure(figsize=(8, 5))
sns.boxplot(x=kolom_J, color="#CBC3E3")
plt.title("Boxplot Rating Kesibukan saat Magang")
plt.xlabel("Rating Kesibukan")
plt.show()

st.header("Density Plot")
plt.figure(figsize=(10, 6))
sns.kdeplot(kolom_J, fill=True, color="#7851A9", alpha=0.5)
plt.title("Density Plot untuk Rating Kesibukan saat Magang")
plt.xlabel("Rating Kesibukan (1-5)")
plt.ylabel("Kepadatan Frekuensi")
plt.show()

