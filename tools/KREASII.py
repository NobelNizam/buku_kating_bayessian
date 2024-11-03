import streamlit as st

# Judul halaman Kuiz Bayesian
st.title("Kuiz Bayesian")

# Soal dan jawaban
questions = [
    {
        "question": "Apa yang dimaksud dengan prior dalam Bayesian?",
        "options": [
            "Probabilitas awal sebelum bukti diperoleh",
            "Probabilitas setelah bukti diperoleh",
            "Tingkat kepercayaan pada model",
            "Probabilitas bukti tanpa hipotesis"
        ],
        "answer": "Probabilitas awal sebelum bukti diperoleh"
    },
    {
        "question": "Apa yang dimaksud dengan likelihood dalam Bayesian?",
        "options": [
            "Probabilitas bukti diberikan hipotesis benar",
            "Probabilitas bukti diberikan hipotesis salah",
            "Probabilitas awal dari suatu hipotesis",
            "Probabilitas akhir setelah bukti"
        ],
        "answer": "Probabilitas bukti diberikan hipotesis benar"
    },
    {
        "question": "Teorema Bayes digunakan untuk menghitung...",
        "options": [
            "Prior",
            "Likelihood",
            "Posterior",
            "Evidence"
        ],
        "answer": "Posterior"
    }
]

# Skor
score = 0

# Pertanyaan dan pilihan
for idx, q in enumerate(questions):
    st.write(f"**{idx + 1}. {q['question']}**")
    answer = st.radio("", q["options"], key=idx)
    if answer == q["answer"]:
        score += 1

# Tampilkan skor akhir
st.write("### Skor Anda:", score, "dari", len(questions))
if score == len(questions):
    st.success("Luar biasa! Semua jawaban benar.")
elif score > len(questions) / 2:
    st.info("Bagus! Anda menguasai dasar-dasar Bayesian.")
else:
    st.warning("Terus belajar! Coba lagi untuk hasil lebih baik.")
