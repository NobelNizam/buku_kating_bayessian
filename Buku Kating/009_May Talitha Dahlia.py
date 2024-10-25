import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen MEDKRAF",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qXuXadCb2OMIBmU0If_ivtcnzYUJztoM", # Bang Gumilang
            "https://drive.google.com/uc?export=view&id=12wrrU3d5wuW8m1o04D09EKvkgQjYu8UV", # Bang Pandra
            "https://drive.google.com/uc?export=view&id=130M_Nhn7fRMTwxSFvhNjViwnKkAaZ3xp", # Kak Meliza
            "https://drive.google.com/uc?export=view&id=134dw_gxnsKW_elqJRLhUDdX8w_9w72J0", # Kak Putri
            "https://drive.google.com/uc?export=view&id=1388giqgs3FPgxSZKVsqhBSbq1iYnZu9i", # Kak Hartiti
            "https://drive.google.com/uc?export=view&id=1qDs13gWaVBEFHHiY7VNSBSqhV4T3ptmb", # Kak Nadilla

        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Kandis",
                "hobbi" : "Mendengerkan musik",
                "sosmed": "@gumilangkharisma",
                "kesan" : "Abang nya berkharisma banget",  
                "pesan" :"semangat terus banggg"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Abang nya baik banget",  
                "pesan" : "semangat terus kuliahnya bang"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Kakaknya baik banget",  
                "pesan" : "semangat terus kuliahnya kakk"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Semangat terus kakk"
            },
            {
               "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Semangat kuliahnya kakk"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Kakak nya baik",  
                "pesan" : "Semangat kuliahnya kakk"

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nS6Ocd65EsAfUoxRLPkJVMrQq2exDa9x", # Kak Tri Murniya
            "https://drive.google.com/uc?export=view&id=12gR6XPvKOsKfpf5eyJM0P5AQKbvJkeGK", # Kak Annisa Cahyani
            "https://drive.google.com/uc?export=view&id=12sqTaQty5HuFZh-UAuF7ti_ymWgvZZVU", # Kak Wulan
            "https://drive.google.com/uc?export=view&id=1n7WW0Jz_5R3A4Pui5fyiUyRWqUhwW3Dd", # Kak Annisa Dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Kak Anisa Fitriyani
            "https://drive.google.com/uc?export=view&id=12T6X_b35Uuqy2m1S6x8ZTsZRNw97vNbB", # Bang Feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Kak Renisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Kak Claudhea
            "https://drive.google.com/uc?export=view&id=1nBxIvIZ91QIsWhHpt7CW-VRyPNitsn_8", # Kak Mirzan
            "https://drive.google.com/uc?export=view&id=12lxIGWDTTtr2Ymei6zyzV962NaKP5fkr", # Kak Dhea Amelia 
            "https://drive.google.com/uc?export=view&id=1mjA9tRKvWyzE2VpuGBsRBOvLkHE58Uq5", # Bang Muhammad Fahrul Aditya
            "https://drive.google.com/uc?export=view&id=1nUrH0wE8xTCvSCMNiwh8sacfk6U5W9_3", # Kak Berliana enda putri
            "https://drive.google.com/uc?export=view&id=1pgVAmV15KynRjDC8DZ6tJQfIj0XRr_24", # Bang Jeremia





        ]
        data_list = [
            {
                "nama"  : "Tri Murniya Ningsih",
                "nim"   : "121450038",
                "umur"  : "21",
                "asal"  : "Bogor",
                "alamat": "Raden Saleh",
                "hobbi" : "Ngerjain TA",
                "sosmed": "@trimurniyaa_",
                "kesan" : "Kakak nya seru bangettt",  
                "pesan" : "semangat terus ya kakkk"
            },
            {
               "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "20",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi" : "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Semangat terus kuliahnya kakk"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakak nya baik dan sabar banget",  
                "pesan" : "Semangat terus kakk"
            },
            {
               "nama"  : "Annisa Dini Amalia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Semangat terus kakk"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450118",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bernungt, Pesawaran",
                "hobbi" : "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Feryadi Yulius",
                "nim"   : "12240087",
                "umur"  : "20",
                "asal"  : "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi" : "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan" : "Abang nya baik banget",  
                "pesan" : "Semangat terus kuliahnya bangg"
            },
            {
                "nama"  : "Renisha Putri Giyani",
                "nim"   : "12240079",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Claudhea Angeliani",
                "nim"   : "121450124",
                "umur"  : "21",
                "asal"  : "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan" : "",  
                "pesan" : ""
            },
            {
               "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan" : "",  
                "pesan" :""
            },
            {
               "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Bengkulu",
                "alamat": "Natar",
                "hobbi" : "Mengumpulkan tugas e-learning h-15 detik",
                "sosmed": "@_.dheamelia",
                "kesan" : "Kakak nya lucu, asikk dan baik banget",  
                "pesan" : "Semngat terus kuliahnya kakkk"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta",
                "alamat": "Sukarame",
                "hobbi" : "Badminton, melukis, hiking, berenang, dengar musik, minum kopi",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Abangnya baik banget",  
                "pesan" : "Semangat terus banggg"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Semnagat kuliahnya kakkk"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Billabong",
                "hobbi" : "Memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan" : "Bang jere baik bangettt",  
                "pesan" : "Semangat terus ya banggg"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11-kywdkA_brFU4lclJFtzs1BeOSwvO30", # Kak Annisa Luthfia
            "https://drive.google.com/uc?export=view&id=17PXgxMZavFctal48eXQ__toBcfaR_2FZ", # Bang Bintang
        ]
        data_list = [
            {
                "nama": "Annisa Lutffia Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kotabaru",
                "hobbi": "Dengerin kak Lutfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bangg !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16K4Jun6LG3GJtVCqMLOc1asyq4BiBTsQ", # Bang Econ
            "https://drive.google.com/uc?export=view&id=1QPUr1qWWksnut8PPkXY9s8uZnpeaHbd9", # Kak Abet
            "https://drive.google.com/uc?export=view&id=17LVEgn-HPBb340dndywcNZKV-gwCRX2o", # Kak Afifah
            "https://drive.google.com/uc?export=view&id=160IL5PF-PHk3vmSwJyBkCeEtl4hyjiO3", # Kak Allya
            "https://drive.google.com/uc?export=view&id=1QT2RaRVFJIH8JChjMmMFg9z8VFG0ihKa", # Kak Eksanty
            "https://drive.google.com/uc?export=view&id=17Jw0-D1Hw8BTPqueBROxvYp_jNcxzJLf", # Kak Hanum
            "https://drive.google.com/uc?export=view&id=172X-bhzqFF28_50MouBSROtnPlXjtRxL", # Bang Ferdy
            "https://drive.google.com/uc?export=view&id=16bsavNxEILg3rz4xuVCBVZN_RPICxYsX", # Bang Deri
            "https://drive.google.com/uc?export=view&id=16rBR51Lp_MwHKDY2OJ_a6-kRF-27heZs", # Kak Okta
            "https://drive.google.com/uc?export=view&id=178aats7Tw_fCLirSLJ-FVrAI1nge1bTg", # Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Ibnu Farhan
            "https://drive.google.com/uc?export=view&id=1-EXysfIIBunic0P_VphxtbPyROpKswND", # Kak Johannes
            "https://drive.google.com/uc?export=view&id=1690u3fW6Fr628MTKksPe3lrRACOR2Eov", # Bang Kemas
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Leonard
            "https://drive.google.com/uc?export=view&id=16R3u2op_gAZRgmF0c7dj7mXzJ1zOq0B5", # Kak Presilia
            "https://drive.google.com/uc?export=view&id=17IlZkVx6jMCOl3gsKK2WMwq5FlAB8qXT", # Kak Rafa Aqilla
            "https://drive.google.com/uc?export=view&id=1-9A_hmnpAOJmUCbrgLnk09L813BxRzwr", # Bang Sahid Maulana
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Kak Vanessa Olivia
            "https://drive.google.com/uc?export=view&id=16hMvidcYqi7YGW-4cjRQN9AxyzEkRnhW", # Bang M.Farhan
            "https://drive.google.com/uc?export=view&id=16EYLynzf1hOB8FYR070-vEORgUefzFr6", # Bang Gede Moana
            "https://drive.google.com/uc?export=view&id=174m01vWerEDDfIwGas0Rtxe7EgYNgYru", # Kak Jaclin
            "https://drive.google.com/uc?export=view&id=16GAKxRn5l2ew09KDlMrgOikftguySZC9", # Bang Rafly Prabu
            "https://drive.google.com/uc?export=view&id=16Ox5_Ldt8B9rrNQjPop14CSUDAWzcwhP", # Kak Syalaisha Andini 

        ]
        data_list = [
            {
                "nama": "Ericson Candra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang nya seru bangettt",  
                "pesan":"semangat terus kuliahnya bangg"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kak abet seru bangett",  
                "pesan":"semangat terus kuliahnya kakkk!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame ",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak nya asik dan seru bangettt",  
                "pesan":"semangat terus kuliahnya kak!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Ngukur Lampung",
                "sosmed": "@allyaislami_ ",
                "kesan": "Kakak nya seru banget",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Raajabasa",
                "hobbi": "Nitip Shalat",
                "sosmed": " @eksantyfebriana",
                "kesan": "Kakak nya asik banget dan seru",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak nya seru dan baik banget",  
                "pesan":"semangat terus kuliah nya kakkk !!!"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pangeran senopati raya, gerbang barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya ya bangg!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "Abang nya seru banget dan humble banget",  
                "pesan":"Semangat terus dan sukses selalu ya bang" 
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakak nya seru dan asik banget",  
                "pesan":"Semangat terus kuliahnya kakk!" 
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang nya seru dan humble banget",  
                "pesan":"Semngat terus kuliahnya bang" 
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "  ",
                "umur": "  ",
                "asal": "  ",
                "alamat": "  ",
                "hobbi": "     ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"   " 
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "Abang nya seru dan asik banget",  
                "pesan":"Semangat terus kuliahnya bang dan sukses selalu" 
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "Abang nya baik dan humble banget",  
                "pesan": "Semangat terus bangg dan sukses selalu" 
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "  ",
                "umur": "  ",
                "asal": "  ",
                "alamat": "  ",
                "hobbi": "  ",
                "sosmed": "@ ",
                "kesan": "  ",  
                "pesan":"   " 
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak nya baik banget",  
                "pesan":"Semangat terus kakk, dan sukses selalu kedepannya" 
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak nya baik banget, dan seru banget",  
                "pesan":" Semngat terus kak kuliahnya" 
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abangnya seru dan baik banget",  
                "pesan":"Semangat terus kuliahnya bangg" 
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak nya asik dan seru banget",  
                "pesan":" Semangat terus kuliahnya kakkk" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang nya seru banget",  
                "pesan":"Semangat terus kuliahnya banggg" 
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang nya baik banget",  
                "pesan":"Semangat terus kuliahnya bangg" 
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakak nya baik dan humble banget",  
                "pesan":"Semangat terus kuliahnya kakk" 
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Aabang nya seru dan baik banget",  
                "pesan":"Semangat terus kuliahnya bangg" 
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak nya baik dan humble banget",  
                "pesan":"Semangat terus kuliahnya kakkk" 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zCUwPpACjhziarhuBa6YUq0VH68-1cCZ", # Bang Rafi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Kak Annisa Novantika
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Mujadid Choirus
            "https://drive.google.com/uc?export=view&id=1X422lYSp9MRuelHjWTNTLa-7tOf81ZGt", # Bang Ahmad Sahidin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Fadhil Fitra
            "https://drive.google.com/uc?export=view&id=1Wyzut3jcc-hQW3an5lToyOkPjVD0VL91", # Bang Regi
            "https://drive.google.com/uc?export=view&id=13Z6_Ee7QvfmzMYapOsFtstL2T-0q7hrz", # Kak Syalaisha Andina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Natanael
            "https://drive.google.com/uc?export=view&id=1XAC_fxOgV2eYWRja6Zswg-Rv5p6AG9VQ", # Bang Anwar
            "https://drive.google.com/uc?export=view&id=13KGKLrWxlLnYQYOx5t8qfi_KLUaOaOwi", # Kak Deva
            "https://drive.google.com/uc?export=view&id=1X2HvS4BFdOpGXCFp2C1EPm7Do6S65QBO", # Kak Dinda Nababan
            "https://drive.google.com/uc?export=view&id=1z7Wdv8mG3lIRk-LQvQP0LZm3u6peCEZ4", # Kak Marleta
            "https://drive.google.com/uc?export=view&id=17rEEwGqvjk-DmnRN0EGBYcQuOiNA7mhp", # Kak Rut Junita
            "https://drive.google.com/uc?export=view&id=1X4VzFR3RZR35T3nMD2IwdlfRp9FhOxog", # Kak Puspa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Bang Abdurrahman
            "https://drive.google.com/uc?export=view&id=13U0HblrpPWXV79Ifhfw_IEtaxOfsDCPT", # Bang Aditya Rahman
            "https://drive.google.com/uc?export=view&id=13SKjmbCzUP5L9Yxr17DrC9D4rh4coeqL", # Bang Eggi 
            "https://drive.google.com/uc?export=view&id=13SUL50sHyPQ6-FGfAylyRNivmTWkk1Qo", # Kak Febiya
            "https://drive.google.com/uc?export=view&id=1z41N0_bf0PrASz_RB3pVJxkuuZGKM9z-", # Bang Happy Syahrul
            "https://drive.google.com/uc?export=view&id=1zGxreA6YogJr7Ax3ro1ZhddqIsvAVe5K", # Bang Randa
            "https://drive.google.com/uc?export=view&id=17neg-xHjAZdOJ8VNP6QkvBbaXZHrW2GN", # Kak Vita Anggraini
            
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafidhilillahh13",
                "kesan": "Abang nya baik dan seru banget",  
                "pesan":" SEmangat terus kuliahnya bang, dan sukses selalu kedepannya" 
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak nya baik banget",  
                "pesan":" Semangat terus kuliahnya kak" 
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@ ",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya asik dan seru banget",  
                "pesan":"Semangat terus kuliahnya bang" 
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya baik dan seru banget",  
                "pesan":"Semangat terus kuliahnya dan makin sukses kedepannya" 
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya baik banget",  
                "pesan":"SEmangat terus kuliahnya kak" 
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang nya baik banget",  
                "pesan":"Semanbgat terus kuliahnya bang dan makin sukses kedepannya" 
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak nya baik banget",  
                "pesan":"Semangat terus kuliahnya kakk" 
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": " ",
                "sosmed": "@dindanababan_",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@i",
                "kesan": "Abang ini asik saya suka belajar dengannya",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Vita Anggraini",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=129RE6rpbwCgQLOFP8aSS8BPRhYYIctL8", # Bang Yogy 
            "https://drive.google.com/uc?export=view&id=", # Kak Ramadhita
            "https://drive.google.com/uc?export=view&id=", # Kak Nazwa Nabilla
            "https://drive.google.com/uc?export=view&id=1XQoQf71YdqJ4eSptBW5hEpRA6riNCYbv", # Bang Bastian
            "https://drive.google.com/uc?export=view&id=127mSNKVd-dnfzQecZCmYoBpzA0P1qjof", # Kak Dea Mutia
            "https://drive.google.com/uc?export=view&id=", # Kak Esteria
            "https://drive.google.com/uc?export=view&id=12BIdqiFmCuJK3fzfDHbBfVNF9lFQJdrc", # Kak Natasya Ega 
            "https://drive.google.com/uc?export=view&id=1xCuBZjFLd5lvGAxp5fLUGqfQutNUOuPi", # Kak Novelia
            "https://drive.google.com/uc?export=view&id=128wMgi1KD_UZ85udYy3NEAX72e_OtNkB", # Kak Ratu Keisha Jasmine
            "https://drive.google.com/uc?export=view&id=1XMOW_rKUSRjc9szhN14P7m79xP7cGsvg", # Bang Tobias
            "https://drive.google.com/uc?export=view&id=1XV9I7jUNnJkceWug4TBn6En7Ekcldw7V", # Kak Yohana Manik
            "https://drive.google.com/uc?export=view&id=1xDCj4-lRaxKfijwuPCJo3McA-4k0drBn", # Bang Rizki
            "https://drive.google.com/uc?export=view&id=11wq-zoMdklOp4Jjdtqbb-jvS8h1CSHQB", # Bang Arafi
            "https://drive.google.com/uc?export=view&id=1xKrLy8WboDAN-QUrEH4kx4eR395M_0C4", # Kak Asa
            "https://drive.google.com/uc?export=view&id=1XZq7bBGaRm00H3M3gS2SOP0Xn7TuhzCV", # Kak Chalifia
            "https://drive.google.com/uc?export=view&id=1Xfkir1WXTl5OvdAmLt6ACtPbCbYBP_Za", # Bang Irvan
            "https://drive.google.com/uc?export=view&id=11vnQ0ynSmS5HvvKcRB9SzeUHeDBLxJtT", # Kak Izza
            "https://drive.google.com/uc?export=view&id=11v19zxBlyrYOoaDMecLzZJK-NGa7h6D8", # Kak Khaalishah Zuhrah
            "https://drive.google.com/uc?export=view&id=", # Bang Raid
            "https://drive.google.com/uc?export=view&id=1XJeDJyqGZGQ5w72bYBZDeT4MfQPptsmn", # Kak Yuna
        ]
        data_list = [
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vzxyxu6WYwZhk1PJbthJGd2PNyRZM8HX", # Bang Dimas 
            "https://drive.google.com/uc?export=view&id=1VuKRPH72qMnoGBHCvblDC8PHHLYsvcxH", # Kak Catherine
            "https://drive.google.com/uc?export=view&id=1VnyNCtoCcDLZTVqafR3ZOKtRSHA4PQ9m", # Bang Akbar
            "https://drive.google.com/uc?export=view&id=1pfa_WXJ_9TA9qH1MB3xRud6dMt5Z-8F7", # Kak Rani
            "https://drive.google.com/uc?export=view&id=1xO9WnrAp4T1qrn4WwA5Q61KO4zMFVp1d", # Bang Rendra
            "https://drive.google.com/uc?export=view&id=1pcdwzqkJOkWXI9tVvJxNX9Uxl5yuP2Wh", # Kak Salwa
            "https://drive.google.com/uc?export=view&id=1p_y4CQODX_wJwfum9j7bKhM7UffIVazh", # Kak Renta
            "https://drive.google.com/uc?export=view&id=17mL62uB13cFm2Ki4Y9zqWlW6Xh6VTie0", # Bang Yosia
            "https://drive.google.com/uc?export=view&id=1Vz9zvaIbDZQLeLTdWqozD72dK9DCOmo4", # Bang Ari Sigit
            "https://drive.google.com/uc?export=view&id=1p_Sl4_wlLfcou7hmd4Ws8aWktVx3-qFd", # Bang Joshua
            "https://drive.google.com/uc?export=view&id=1VhbO_XQ1_Jg5oqwtu_G6gY1Bv4Z-LQ6F", # Kak Meira 
            "https://drive.google.com/uc?export=view&id=1Vqzqm7jOQMO7v_2dLGuFRrDLGJ-KhW90", # Kak Rendi
            "https://drive.google.com/uc?export=view&id=1nnFU-qYG5dE1OzCuXoP0qivU-tHcriI-", # Kak Azizah
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang",
                "alamat": "Way Kandis",
                "hobbi": "Manjat Pohon Pinang",
                "sosmed": "@dimzrky",
                "kesan": "Bang Dimas public speaking nya keren banget",  
                "pesan":"semangat terus kuliah dan ngerjain TA nya bang !!!"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Airan",
                "hobbi": "Membaca Novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Kakak nya asik banget dan sangat menyenangkan",  
                "pesan":"Semangat dan sukses terus kedepannya kakkk !"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam (untung)",
                "hobbi": "Main sepeda ke gunung",
                "sosmed": "@akabar_resdika",
                "kesan": "Abang nya asik dan sabar banget",  
                "pesan":"semangat terus ya bang kuliahnya!"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@ranipu",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat terus kuliahnya ya kakak !"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari Buah Pisang",
                "sosmed": "@rendraepr",
                "kesan": "Abang nya seru dan sabar banget",  
                "pesan":"semangat terus ya bang kuliahnya dan sukses dalam segala hal !!!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhn_694",
                "kesan": "Kakak nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya kak"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "Kakak nya baik banget",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya ya bang!!!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang nya seru dan sabar banget",  
                "pesan":"semangat terus kuliahnya banggg, dan sukses terus bang!"
            },
            {
                "nama": "Joshua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Menonton dan lari",
                "sosmed": "@josuapanggabean16",
                "kesan": "Kakak nya asik banget",  
                "pesan":"semangat terus kuliahnya bang!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@meirasty_",
                "kesan": "Kakak nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya kakkk!"
            },
            {
                "nama":"Rendi Alexander Hutagalung",
                "nim": "121450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya ya bang!"
            },
            {
                "nama":"Azizah Kusuma Putri",
                "nim": "1212450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak nya asik banget",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1--wD_NnIO7D6h4NImOoCg_CkfTnf78wq", # Bang Andrian
            "https://drive.google.com/uc?export=view&id=15yK1oF9ouyy58XZA8XI2ATIAOndYAq28", # Kak Adisty
            "https://drive.google.com/uc?export=view&id=1WWSYlFt4KuWnYwW7VGJ9pfeONTQjmnEj", # Kak Nabila Azhari
            "https://drive.google.com/uc?export=view&id=1WXnVULWmFjQs3z4Bu3WVGBTZmnHgPXgZ", # Bang Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=1WXr41QyTKItZjYm0Q5hEmSkxEhCCWVKl", # Bang Danang
            "https://drive.google.com/uc?export=view&id=1zQwvNZuD4i9CsXLiW-BmMRxC18lH4cZJ", # Bang Farrel
            "https://drive.google.com/uc?export=view&id=1WXucjzxebirT1GzgaxrtpSgIfMH0w5Sw", # Kak Tessa
            "https://drive.google.com/uc?export=view&id=15n7io2EW8yDLNiZtshxPzSk4Nl1uMcJU", # Kak Nabilah Andika
            "https://drive.google.com/uc?export=view&id=1WTvoZ61_zFKKsv7RUH9yEkEP8J0_UXJe", # Kak Alvia
            "https://drive.google.com/uc?export=view&id=1-87odkeKmbKvSlTZyfqahe_MXTP2fGdx", # Bang Dhafin
            "https://drive.google.com/uc?export=view&id=1WE0OSHU3cnLlpnvSUvz7P2Xzl4udmBmi", # Kak Elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara lapas",
                "hobbi": "Nyari-Nyari Hobi",
                "sosmed": "@andriangaol",
                "kesan": "Kakak nya seru dan asik banget",  
                "pesan":"semangat terus kuliahnya banggg!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak nya seru banget",  
                "pesan":"semangat terus kuliahnya ya kakk!!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "Kakak nya asik dan baik banget",  
                "pesan":"semangat terus kuliah nya kakk!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukit Tinggi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abang nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya banggg!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "dananghk_",
                "kesan": "Aabang nya seru banget dan baik banget",  
                "pesan":"semangat kuliahnya dan sukses terus ya bangg !!!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.Lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abang nya seru, dan baik banget",  
                "pesan":"semangat terus kuliahnya bang dan sukses terus bangg!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak nya seru dan asik banget",  
                "pesan":"semangat terus kuliahnya ya kakkk!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Menonton",
                "sosmed": "@alviagnting",
                "kesan": "Kakak nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya kakkk!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl.Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya bangg, dan sukses selalu!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakak nya asik dan seru banget",  
                "pesan":"semangat terus kuliahnya kak dan sukses terus kak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=", # Bang Wahyudiyanto
            "https://drive.google.com/uc?export=view&id=", # Kak Elok
            "https://drive.google.com/uc?export=view&id=", # Kak Arsyiah
            "https://drive.google.com/uc?export=view&id=", # Kak Cintya Bella
            "https://drive.google.com/uc?export=view&id=", # Kak Eka Fidiya
            "https://drive.google.com/uc?export=view&id=", # Kak Najla
            "https://drive.google.com/uc?export=view&id=", # Kak Patricia
            "https://drive.google.com/uc?export=view&id=", # Kak Rahma Neli
            "https://drive.google.com/uc?export=view&id=", # Kak Try Yani
            "https://drive.google.com/uc?export=view&id=", # Bang Kaisar
            "https://drive.google.com/uc?export=view&id=", # Kak Dwi Ratna
            "https://drive.google.com/uc?export=view&id=", # Bang Gymnastiar
            "https://drive.google.com/uc?export=view&id=", # Kak Nasywa
            "https://drive.google.com/uc?export=view&id=", # Kak Priska
            "https://drive.google.com/uc?export=view&id=", # Bang Arsal
            "https://drive.google.com/uc?export=view&id=", # Bang Abit
            "https://drive.google.com/uc?export=view&id=", # Bang Akmal
            "https://drive.google.com/uc?export=view&id=", # Bang Hermawan
            "https://drive.google.com/uc?export=view&id=", # Kak Khusnun Nisa
        ]
        data_list = [
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
