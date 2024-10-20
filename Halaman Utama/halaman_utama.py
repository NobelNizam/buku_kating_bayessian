import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width=True, width=500)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#295F98"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F316F",
            },
            "nav-link-selected": {"background-color": "#821131"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Kelompok Bayessian</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Bayessian merupakan kelompok ke-8 dalam kaderisasi Himpunan Mahasiswa Sains Data Adyatama 2024.
            Bayessian adalah metode yang memungkinkan untuk memasukkan informasi awal dan memperbaruinya secara dinamis saat data atau
            informasi berdasarkan bukti baru yang tersedia.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1CRdoVxMuJ1ODDp3q5KRKlSDXCJPd0Uvc"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Bayessian terdiri dari 14 manusia, 12 anggota dan 2 daplok yaitu bang akmal dan kak cia. 
                Semoga kelompok bayessian menjadi kelompok yang terbaik!</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>ini adalah Bayess!!!</h1>", unsafe_allow_html=True)
        gambar_urls = [             # ini foto profil masing-masing di about us
            "https://drive.google.com/uc?export=view&id=1AGp20DF2dUB2OdDyKLpm5kuWbeAfOjo1", # nobel     - done
            "https://drive.google.com/uc?export=view&id=1HglyJKcYaa0OWrxvSpz-WJ3Pe11sHelg", # feby      - done
            "https://drive.google.com/uc?export=view&id=1TxmWHUuxy9XmIoN193T9sclibuXk1qP1", # fabio     - done
            "https://drive.google.com/uc?export=view&id=1tjD3dCTC0pGeETD0B6BuJI99eyK8l9HT", # wawa      - done
            "https://drive.google.com/uc?export=view&id=11cQdkD6uMltnjv-VitjxFg2Xgznsfwht", # natasya   - done
            "https://drive.google.com/uc?export=view&id=1t5difluGEl7xRrKqZ-q53csRF2kY04gJ", # may       - done
            "https://drive.google.com/uc?export=view&id=1mkCi0eUBv1X5JykQx991zp55atnJvTOF", # haikal    - done
            "https://drive.google.com/uc?export=view&id=1su8NCe0Oo1hIGziv2i_hgpXQhBNpCqAS", # nayla     - done
            "https://drive.google.com/uc?export=view&id=1XGoKqRbKJnVrTiVDchkQTF5sY3x-WcA7", # rewina    - done
            "https://drive.google.com/uc?export=view&id=1HMYJfY0nY40W-Wha2gxi9CbhVElhhftn", # fathia    - done
            "https://drive.google.com/uc?export=view&id=1jQf1z9zvwS2ddsjZrv_zVuICgcHkuDer", # eigi      - done
            "https://drive.google.com/uc?export=view&id=11glrwFr23CS_i-5_eo8-kGBZPlU_VNS_", # engli     - done
        ]
        data_list = [
            {
                "nama": "Nobel Nizam Fathirizki",
                "sebagai": "Pak Lurah",
                "nim": "123450117",
                "fun_fact": "Sejak sekolah dasar cita-citanya kerja di google!",
                "motto_hidup": "fokus pada diri baru cari binii",
            },
            {
                "nama": "Feby Wulandari",
                "sebagai": "Bu Lurah",
                "nim": "122450042",
                "fun_fact": "I hate cucumber",
                "motto_hidup": "Banyak mimpi, kurang tidur",
            },
            {
                "nama": "Fabio Banyu Cyto",
                "sebagai": "Anggota",
                "nim": "123450104",
                "fun_fact": "Orangnya Pelupa tapi ganteng juga.",
                "motto_hidup": "Jadilah orang yang dapat memberikan kebebasan!",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "sebagai": "Anggota",
                "nim": "123450077",
                "fun_fact": "gasuka buah nangka",
                "motto_hidup": "hidup hanya untuk tidur",
            },
            {
                "nama": "Natasya Amavisca",
                "sebagai": "Anggota",
                "nim": "123450024",
                "fun_fact": "nyemilin garam kasar",
                "motto_hidup": "harus bahagia",
            },
            {
                "nama": "May Talitha Dahlia",
                "sebagai": "Anggota",
                "nim": "123450009",
                "fun_fact": "suka pink",
                "motto_hidup": "Berani mencoba, berani gagal",
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "sebagai": "Anggota",
                "nim": "123450106",
                "fun_fact": "Alis bisa naik sebelah",
                "motto_hidup": "Kebanyakan kegagalan berasal dari ketakutan sebelum mencoba",
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "sebagai": "Anggota",
                "nim": "123450082",
                "fun_fact": "Cat loverrr",
                "motto_hidup": "God, Goals, Growing",
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "sebagai": "Anggota",
                "nim": "123450049",
                "fun_fact": "Lagi mau benerin diri sendiri",
                "motto_hidup": "urus diri sendiri jadi yang terbaik dan nggak boleh pacaran!",
            },
            {
                "nama": "Fathya Intami Gusda",
                "sebagai": "Anggota",
                "nim": "123450095",
                "fun_fact": "I Love Strawberry",
                "motto_hidup": "Jalanin aja",
            },
            {
                "nama": "Eigi Artamevia",
                "sebagai": "Anggota",
                "nim": "123450011",
                "fun_fact": "stylus pen gaboleh ketinggalan",
                "motto_hidup": "Berani mengambil suatu langkah dan bertanggung jawab",
            },
            {
                "nama": "Enggli Rahmadhani",
                "sebagai": "Anggota",
                "nim": "123450043",
                "fun_fact": "my life is so fun and that's a fact",
                "motto_hidup": "beautiful things don't ask to attention",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
