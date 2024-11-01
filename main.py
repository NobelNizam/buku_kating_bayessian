import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok Bayessian!",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/117_Nobel Nizam.py",
    title="117 - Nobel Nizam",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/042_Feby Wulandari.py",
    title="042 - Feby Wulandari",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/104_Fabio Banyu Cyto.py",
    title="104 - Fabio Banyu Cyto",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/077_Wan Nashwa Alhasni Yuska.py",
    title="077 - Wan Nashwa Alhasni Yuska",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/024_Natasya Amavisca.py",
    title="024 - Natasya Amavisca",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/009_May Talitha Dahlia.py",
    title="009 - May Talitha Dahlia",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/106_Haikal Fransisko Simbolon.py",
    title="106 - Haikal Fransisko Simbolon",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/082_Nayla Salsabila Fathianisa.py",
    title="082 - Nayla Salsabila Fathianisa",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/049_Rewina Audrya Melva Sari.py",
    title="049 - Rewina Audrya Melva Sari",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/095_Fathya Intami Gusda.py",
    title="095 - Fathya Intami Gusda",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/011_Eigi Artamevia.py",
    title="011 - Eigi Artamevia",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/043_Enggli Rahmadhani.py",
    title="043 - Enggli Rahmadhani",
    icon=":material/person:",
)


#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")
KREASIII = st.Page("tools/KREASIII.py", title="KREASIII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7,
                            Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII, KREASIII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

