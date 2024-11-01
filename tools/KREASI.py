import streamlit as st

# Judul aplikasi
st.title("Kalkulator Bayesian Sederhana")

# Penjelasan singkat tentang kalkulator
st.write("""
Alat ini menghitung probabilitas **posterior** berdasarkan nilai **prior**, **likelihood**, dan **evidence**.
Perhitungan dilakukan menggunakan Teorema Bayes:
""")

st.latex(r'''Posterior = \frac{Likelihood \times Prior}{Evidence}''')

# Input pengguna untuk prior, likelihood, dan evidence
prior = st.number_input("Masukkan nilai Prior (Probabilitas Awal)", min_value=0.0, max_value=1.0, step=0.01)
likelihood = st.number_input("Masukkan nilai Likelihood (Probabilitas Bukti jika Hipotesis Benar)", min_value=0.0, max_value=1.0, step=0.01)
evidence = st.number_input("Masukkan nilai Evidence (Probabilitas Bukti)", min_value=0.0, max_value=1.0, step=0.01)

# Validasi nilai evidence tidak boleh nol
if evidence == 0:
    st.error("Evidence tidak boleh nol untuk menghindari pembagian dengan nol.")
else:
    # Perhitungan posterior
    posterior = (likelihood * prior) / evidence

    # Tampilkan hasil
    st.write("### Hasil Perhitungan")
    st.write(f"**Posterior**: {posterior:.4f}")
    
    # Visualisasi hasil
    st.bar_chart({"Probabilitas": {"Prior": prior, "Likelihood": likelihood, "Posterior": posterior}})
