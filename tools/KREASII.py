import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Data Peserta Magang CEO HMSD 2024")

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

# 2. Membersihkan Data
st.header("2. Membersihkan Data")
st.write("Membersihkan kolom 'Provinsi' untuk memastikan data konsisten.")
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()  # Membersihkan data provinsi

# 3. Analisis Statistika Deskriptif
st.header("3. Analisis Statistika Deskriptif")
st.write("""
Pada bagian ini, kita akan melihat statistik deskriptif dari jumlah peserta magang berdasarkan asal provinsi.
Kami akan menghitung jumlah peserta dari Lampung dan luar Lampung, serta nilai statistik lainnya seperti mean, median, range, 
variansi, standar deviasi, dan kuartil.
""")

# Menghitung jumlah peserta dari Lampung dan luar Lampung
data_lampung = data_magang[data_magang['1. Asal Provinsi'] == 'Lampung']
data_luar_lampung = data_magang[data_magang['1. Asal Provinsi'] != 'Lampung']