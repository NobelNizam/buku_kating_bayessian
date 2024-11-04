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
            "https://drive.google.com/uc?export=view&id=1ZrhSyzENmyrH4YmmvnLLu-eLgFNieQbv", 
            "https://drive.google.com/uc?export=view&id=1Ja__QL2jbk3CUeUbCkImr7dG01Fc0IUh", 
            "https://drive.google.com/uc?export=view&id=17RtV-LQrpwsihn-7tAcsY3l3TKvRat2j", 
            "https://drive.google.com/uc?export=view&id=13uR-Lmp3Ca4xczv_pdGSReDMne5vHC_n", 
            "https://drive.google.com/uc?export=view&id=1fw6JWlOjkAXTal7BuUptJxgMTHfWGrHB", 
            "https://drive.google.com/uc?export=view&id=1L-ZBSCAOpWeV6Kn7HBx1KRVaQ_2ELkly", 
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Sesuai dengan namanya, abang nya berkharisma",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abangnya humble",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak nya baik sekali",  
                "pesan":"Semangat terus kak semester 7"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra gitaran",
                "sosmed": "@ptrimaulidaa_",
                "kesan": "Kak Putri orangnya asik dan dari daerah yang sama",  
                "pesan":"Semangat selalu kak kuliahnya"# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak nya kalem, trus pengen denger kakaknya nyanyi",  
                "pesan":"Semangat ngerjain TA nya ya kakk"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak nya baik banget, trus juga lucu",  
                "pesan":"Semoga lancar sempro nya yaa kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ww7Ig_owcxQfRU3jwmUEZi7lPIvhhzVy",
            "https://drive.google.com/uc?export=view&id=11o55D6CGlTnoUxELSgrE1_-VJ_hZc2cL",
            "https://drive.google.com/uc?export=view&id=1l2-PeYce1EG464sS6p6l61cfiJpZFKlF",
            "https://drive.google.com/uc?export=view&id=1j-ODU4pNEGZwki_7RACg65KYv9jToZ2p",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=11fsDdVqEjjDyQew3B6zTAGLS0FNUoVUE",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Qn-WYjx3qJUYjM6RA8bsl_WqnMggJEIg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1JgMRF3ux9M_EFKoRhMOO2RinVkKde6Vq",
            "https://drive.google.com/uc?export=view&id=19ubX2jUBrRpUYrbwOF_8t1an_uCpeS-t",
            "https://drive.google.com/uc?export=view&id=1Vaq5SOX-4MjOXOKqHfcBGS3XGAYequdD",
            "https://drive.google.com/uc?export=view&id=16FQ9pA1OaWj3D3-UIV3RYgw-NFJyJ3r6",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Ngerjain TA",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak pembawaannya asik",  
                "pesan":"Semangat ngerjain TA nya ya kak, semoga lancar selalu ^^"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak nya cantikk, trus ramahh",  
                "pesan":"Semoga lancar sempro nya yaa kak"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak nya baikk trus humble juga",  
                "pesan":"Bahagia terus yaa kak"# 1
            },
            {
                "nama": "Anisa Dini Amelia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak nya seruu sama baik jugaa",  
                "pesan":"Semangat dan bahagia selalu kak"
            },
             {
                "nama": "Claudhea Angeliani",
                "nim": "121450087",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Kakak nya cantikk",  
                "pesan":"Semoga dilancarkan sempro nya ya kak"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang nya baik",  
                "pesan":"Semangat kuliah dan asprak nya bang"# 1
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak nya baikk",  
                "pesan":"Semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya ramah dan baik",  
                "pesan":"Semangat terus kuliahnya bang"
            },
             {
                "nama": "Annisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak nya ramahh",  
                "pesan":"Semangat dan bahagia selalu ya kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mengumpulkan tugas h-5 detik di e-learning",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak nya asik, orang nya juga humble",  
                "pesan":"Semangat kuliah nya kakk"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, hiking, renang, dengerin musik, minum kopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang nya keren karena hobi nya banyak",  
                "pesan":"Semoga sempro nya lancar ya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak nya baik, trus sama-sama dari Sumatera Barat",  
                "pesan":"Semangat kuliah nya ya kak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bilabong",
                "hobbi": "Memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jere orang nya asik",  
                "pesan":"Semangat kuliah sama jadi asprak nya bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ov3SE3_UcbW1nUaYMouxA3KzoX93DBDe",
            "https://drive.google.com/uc?export=view&id=1T5RDWS6E9l7Uxf7yZQ7nTI9qginqWlcJ",
        ]
        data_list = [
            {
                "nama": "Annisa Lutfia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "Kakak nya asikk trus keren bangett, kagum sama kakak nya",  
                "pesan":"Semangat terus kuliahnya kakakk"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang nya kerennn",  
                "pesan":"semangat terus kuliahnya bangg"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bfi7j-Na9RkP5qvsIwx6lpLzoH5P6oB6",
            "https://drive.google.com/uc?export=view&id=1FQ7_WDX669QX-xBNljoIXa301HG5DffA",
            "https://drive.google.com/uc?export=view&id=1Q5u9m_fwcvmavzuWMsDCayRTW-k933Ec",
            "https://drive.google.com/uc?export=view&id=1piMpmkiZTXjieilRj_GoJBwULRXwqAe1",
            "https://drive.google.com/uc?export=view&id=1gpiHWPs1pRMVIiZCTlSBQlXVEmu7yR-Z",
            "https://drive.google.com/uc?export=view&id=1jmjiDva-c6iyvpVVDcOO9NAW4TMT7AWM",
            "https://drive.google.com/uc?export=view&id=1dmdZLyoqVAPGj8u9DQXtoau3FRXARC3r",
            "https://drive.google.com/uc?export=view&id=1WzVTZgj42mEGebTBhJN9cR6nEwEVLLXE",
            "https://drive.google.com/uc?export=view&id=1U2yqC5_XbzwVaSApWFLqfs_hgKWiaW7k",
            "https://drive.google.com/uc?export=view&id=1LDdhIlE4unUMWjp53OUP1wMCeszQX0b8",
            "https://drive.google.com/uc?export=view&id=1irQpcxvbwUeVGeZKa6S6HyNLgfZ_Ovxs",
            "https://drive.google.com/uc?export=view&id=1LR4fnwV4om8GN7vXeuF4ROjp7hrQusTG",
            "https://drive.google.com/uc?export=view&id=1SWjZ5z7mFrSf7AtW1TVzpFM_IOfBjKNX",
            "https://drive.google.com/uc?export=view&id=1k8tb50EN-YFUA6Arp3wDtSwSvqvMkJpT",
            "https://drive.google.com/uc?export=view&id=1Otr4L5pJpkcEYEf3hs-cSlYc6y4cDcRG",
            "https://drive.google.com/uc?export=view&id=1EQEo5CJWYf-RA_PFb9Ly6VXt_yz54vSG",
            "https://drive.google.com/uc?export=view&id=1WoCEZRpNQdBSwKW5t3VKTvJYekj-08-B",
            "https://drive.google.com/uc?export=view&id=1UUGBJ3SeJIZrK94HhSOOogCOJ6gYy_Bt",
            "https://drive.google.com/uc?export=view&id=11eMGkmVDDloVrTQXQ5pG7XECpwxRxCa_",
            "https://drive.google.com/uc?export=view&id=1XIilrVa2Hd0DFvEMPQPCwP8Fsq6GBLd3",
            
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat selalu bang"
            },
            {
                "nama": "Elisabeth Claudia Simajuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Tertawa",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya asikk",  
                "pesan":"Semangat dan bahagia selalu ya kak"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak nya baikk",  
                "pesan":"Semangat teruss kakk"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak nya asikk",  
                "pesan":"Semangat dan jaga kesehatan yaa kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak nya baikk",  
                "pesan":"Semangat nge asprak nyaa kakk"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak nya lucu trus asik jugaa",  
                "pesan":"Bahagia selalu yaa kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pangeran Senopati Raya, Gerbang Barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat terus kuliahnya bangg"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "Abang nya asikk",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak nya baikk",  
                "pesan":"semangat terus kuliahnya kakak"
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang nya seruu trus asik jugaa",  
                "pesan":"semangat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang nya seruu trus asik orang nya",  
                "pesan":"Semangat ngeasprak nya bang"
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "Abang nya hebatt trus baik juga",  
                "pesan":"Semangat terus kuliahnya bangg"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak nya baikk",  
                "pesan":"Bahagia dan jaga kesehatan selalu yaa kak"
            },
            {
                "nama": "Rafa Aqilla Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak nya baikk",  
                "pesan":"Semangat terus kuliahnya kakak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Dengerin MCR",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat selalu bang"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya baikk, seru jugaa",  
                "pesan":"Semangat nyusun tugas akhir nya bangg"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat kuliah nya bangg"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakaknya baikk truss asikk jugaa",  
                "pesan":"Semangat dan bahagia selalu kakk"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat terus kuliahnya bangg"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya lucuu trus baik jugaa",  
                "pesan":"Semangat dan bahagia selalu kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fWjT-Tvm33VFI-WamFx85VR1ChuKnnl8",
            "https://drive.google.com/uc?export=view&id=1mmSwvczZRcdi8IiAQy6euMK7KjjghYLz",
            "https://drive.google.com/uc?export=view&id=1fgBnIlwwhoqbTvRWt7GXJ-81yhj8nOiJ",
            "https://drive.google.com/uc?export=view&id=1MowNipC77L6v-KkcV1K4ZsBfx-reM8Ng",
            "https://drive.google.com/uc?export=view&id=13B8DIvW-woeV91aIC48THGtNMhAmPRQI",
            "https://drive.google.com/uc?export=view&id=1jo29a0TGsCuVoAKPc6QJu8IVmbGBgKbz",
            "https://drive.google.com/uc?export=view&id=1DUpJ6PAxpLC9VDIoo3qmRT9mnjoI9nTk",
            "https://drive.google.com/uc?export=view&id=1O_E29l6iHjR1lvRJBAsJoSVXD14bjTK0",
            "https://drive.google.com/uc?export=view&id=1mimcOYbLL3CuTpXBWlL9t-r9riBYLLmb",
            "https://drive.google.com/uc?export=view&id=1HZOSdo-fs0o2izZj7SV2m1WD3Caz7ACJ",
            "https://drive.google.com/uc?export=view&id=19iWXVEuGEk81NxxcCgJhs_3KFPWa31Rl",
            "https://drive.google.com/uc?export=view&id=1SNcSv9oYAIPevkAIyTPARHAZz9_VpDxB",
            "https://drive.google.com/uc?export=view&id=1TeFj9nO96Z-2tEp9ZZTo_jpJs4fJ6N4n",
            "https://drive.google.com/uc?export=view&id=1sn-OSW8v-BROlHpTP1bz2FBH_cdgzEUZ",
            "https://drive.google.com/uc?export=view&id=1jCG40MKRpm-xZlGthUN5R0OTcnO0At2G",
        ]
        data_list = [  
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau, Sumsel",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Abang nya baik",  
                "pesan":"Semangat kuliah nya bang" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak nya baik",  
                "pesan":" Semangat selalu yaa kak" # 2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang nya baikk",  
                "pesan":"Semangat kuliah nya bang" # 3
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "Abang nya seruu, keren juga",  
                "pesan":"Semangat dan bahagia selalu bang" # 4
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Review jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya baikk",  
                "pesan":"Bahagia selalu yaa kak" # 5
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang nya asikk, trus baik jugaa",  
                "pesan":"Semangat selalu bangg" # 6
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak nya lucuu, baikk",  
                "pesan":"Jaga kesehatan dan bahagia selalu kak" # 7
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak nya baik sekalii",  
                "pesan":"Semangat ngeasprak nya yaa kak" # 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review Jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak nya baikk",  
                "pesan":"Bahagia selalu yaa kakk" # 9
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Kepualauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Menghitung Akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak nya asikk",  
                "pesan":"Semangat kuliah nya yaa kak" # 10
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membangkitkan bilangan",
                "sosmed": "@puspadrr",
                "kesan": "Kakak nya baikk",  
                "pesan":"Jaga kesehatannya yaa kakk" # 11
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@_egistr",
                "kesan": "Abang nya baikk, kerenn",  
                "pesan":"Semangat kuliahnya bangg" # 12
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak nya ramahh",  
                "pesan":"Bahagia terus yaa kak" # 13
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang nya baikk",  
                "pesan":"Semangat kuliahnya bangg" # 14
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Ngoding Wisata",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang nya baikk",  
                "pesan":"Semangat kuliahnya bangg" # 15
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya baikk, kerenn",  
                "pesan":"Semangat yaa bang ngejalanin hari-hari nyaa"
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat selalu kuliahnya ya bang" 
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abangnya baik",  
                "pesan": "Semangat kuliah dan sukses terus bang" 
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya kerenn",  
                "pesan": "Bahagia selalu yaa bangg" 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=179XWbWjA0HJPAugtPThC7yIrY-RhiB1m",
            "https://drive.google.com/uc?export=view&id=1Fj-1U-QdgXcAdhaLwVDt4klKBjaAVy0D",
            "https://drive.google.com/uc?export=view&id=13arx-JTSiSNqadsn3rF6u9-pI2ITROJZ",
            "https://drive.google.com/uc?export=view&id=1UqoYoWSRdTqBhB1XV055hM6NljBv67ra",
            "https://drive.google.com/uc?export=view&id=1yg3CwVPNvlFbA6MF7Zh48eKlBvoldcSS",
            "https://drive.google.com/uc?export=view&id=1pIgf5zcf2hKGKfCrw6m6zUe0a-BrmORq",
            "https://drive.google.com/uc?export=view&id=1VMhWvt-C84gSEksMPxNGB6js9dbuaSp1",
            "https://drive.google.com/uc?export=view&id=179cw4bqNo5djCGRGVskrP65m0xw_8RBd",
            "https://drive.google.com/uc?export=view&id=1-rzs-6XSzws-GnDGyZOxxPKOs5xGuWNx",
            "https://drive.google.com/uc?export=view&id=1V9DEq-1ob_qDWsT90T8fKUCIkaMobQVP",
            "https://drive.google.com/uc?export=view&id=1M88WIbw9_rX276y8-2R4Zx1sC9u50clg",
            "https://drive.google.com/uc?export=view&id=1bm_VTn8TYfLGmtCjAJQm2IjLAU_gPzCH",
            "https://drive.google.com/uc?export=view&id=1Hm4TIVeei-NCurg_fGya0xGytu1J-eFW",
            "https://drive.google.com/uc?export=view&id=1_3READwl0j8b4nkmI4fQjrjd7JG2QiDN",
            "https://drive.google.com/uc?export=view&id=137ZHo7EXWFXhLYriaaP2CpcoePnINN__",
            "https://drive.google.com/uc?export=view&id=1oyMVQf0rsIlIAo_Ee83k7u3Krc6LrR57",
            "https://drive.google.com/uc?export=view&id=13GlxZsbZSQ1mxs7OyPkmpD3v9Md7GszE",
            "https://drive.google.com/uc?export=view&id=1qlduvclbT5SB2WNmLrnvjNJdMPsBk0y3",
            "https://drive.google.com/uc?export=view&id=13L_5LnRkEodvh7o60rNT0TRxle6asbe4",
            "https://drive.google.com/uc?export=view&id=1uDCJYcDyOxVa4YtslhqNnG9k0UvuyB5k",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Nyari solar",
                "sosmed": "@yogyst",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat nyusun tugas akhirnya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya ramah dan baik",  
                "pesan":"Semangat nyusun tugas akhirnya kakakk" 
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kandis ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak nya cantikk",  
                "pesan":"Semangat nyusun tugas akhir kakk" 
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat kuliahnya ya bang" 
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak nya ramahh",  
                "pesan":"Bahagia dan jaga kesehatan terus kak" 
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya baik dan lucuu",  
                "pesan":"Semangat kuliahnya yaa kakak" 
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "Kakaknya lucuu, keren juga",  
                "pesan":"Semangat selalu kuliahnya yaa kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya ramahh",  
                "pesan":"Bahagia selaluu kakakk" 
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaaknya baik sekalii",  
                "pesan":"Semangat selalu ngejalanin hari-hari nya kakk" 
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat kuliahmya bang" 
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya keren",  
                "pesan":"Semangat selalu yaa kak" 
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat buat tugas akhirnya yaa bangg" 
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya baikk trus ramah juga",  
                "pesan":"Jaga kesehatan selalu yaa bang" 
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baikk, kerenn",  
                "pesan":"Semangatt selalu ya kak kuliahnya" 
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya lucuu",  
                "pesan":"Semangatt selaluu ya kak kuliahnyaa"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat kuliahnya bangg" 
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu anak Pengmas",
                "sosmed": "@izzalutfia",
                "kesan": "Kakaknya asik sekalii",  
                "pesan":"Semangat dan jaga kesehatan selaluu yaa kakk" 
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat selalu yaa kak" 
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan": "Abangnya baik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya ramah",  
                "pesan":"Semangat selalu yaa kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Us6_dQ-ZUE1zyPqTHGzCppPusdndR3wb",
            "https://drive.google.com/uc?export=view&id=14X-1OkBEF7MeWyokC91RqWcm6TJ0fp6H",
            "https://drive.google.com/uc?export=view&id=1_PaqMejV5cW6jTLNUmX7qkPz8dZq_8Hh",
            "https://drive.google.com/uc?export=view&id=14X5sWROHryf4aUHBJ59Q5RCwYkxy-kjt",
            "https://drive.google.com/uc?export=view&id=1Iv5cbNGM8sAOimMYZqYpMNEzIQHOufp5",
            "https://drive.google.com/uc?export=view&id=1rtLxlvMUv7cJjJHMig0t7P4FtAC-xjjs",
            "https://drive.google.com/uc?export=view&id=1VagAQm7nS0jQGgJJCmPEurd6ernlEQjt",
            "https://drive.google.com/uc?export=view&id=14-42HPXzENEMXFrpQT8jM7NMQeRvODyJ",
            "https://drive.google.com/uc?export=view&id=1EE0R3eRYN726wGCvgsdDGkk-3OTucMpw",
            "https://drive.google.com/uc?export=view&id=1MGY-RziYyG3g013HvBreZsAoygi3lFMG",
            "https://drive.google.com/uc?export=view&id=1fG0C8R2anp3nWbtlsRcIQwE8xNAIm71U",
            "https://drive.google.com/uc?export=view&id=1NwsfSmNYScVLeMwwWWQ7WuQp6NWgJhyI",
            "https://drive.google.com/uc?export=view&id=1d_zvwt_e-OUA1FSs6pK45FuQGIOhor7s",
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhan",
                "nim": "121450027",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kobam",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dimzrky_",
                "kesan": "Abangnya kerenn, baik jugaa",  
                "pesan":"Semangat buat tugas akhir yaa bangg"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Membaca Novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya cantikk, ramahh",  
                "pesan":"Semangatt buat tugas akhir nya yaa kakk"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat yaa bang nyusun tugas akhirnyaa"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat terus kuliahnya kakak"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya ramahh, baik jugaa",  
                "pesan":"Bahagia selalu dan jaga kesehatan ya bang"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakaknya baik sekalii",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Yosia Reatare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya indah",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya baik",  
                "pesan":"Semangat kuliah dan buat tugas akhirnya ya bang"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya ramah dan baikk",  
                "pesan":"Bahagia dan jaga kesehatan selalu ya kak"
            },
            {
                "nama": "Ari Sigit",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Abangnya baikk, trus ramah jugaa",  
                "pesan":"Semangat terus kuliahnya ya bangg"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abangnya kerenn, baik",  
                "pesan":"Semangat selalu bangg buat kuliahnya"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat selalu kakak!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Banawang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@meirasty_",
                "kesan": "Kakaknya ramahh, baik sangatt",  
                "pesan":"Bahagia selalu yaa kakk"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@rexander",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat selalu bangg"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QG8EwIhOL2YGGfgw6TV3tCGW9JmHKEbp",
            "https://drive.google.com/uc?export=view&id=1e9C2ORv4v6K-u8G09gvEXJIoudSGvEKu",
            "https://drive.google.com/uc?export=view&id=1ulncaLLLDZ9MuUtwxP6LDFsodY52LZeJ",
            "https://drive.google.com/uc?export=view&id=1WwiNHHXSKF1SGF7Frmeo0Q88J6ogammj",
            "https://drive.google.com/uc?export=view&id=1R29n_gAZyy4wLPHs-IhFKeQLSWkNcrzc",
            "https://drive.google.com/uc?export=view&id=1OnFECAgBmsneTUtvsiyhEApJmsHfAaHd",
            "https://drive.google.com/uc?export=view&id=1iewkvW708OCy0X2nBXT3H74_1k4kQ-sm",
            "https://drive.google.com/uc?export=view&id=1LA65b6jVq-w8buFEM-RunR-k0H-PSRjy",
            "https://drive.google.com/uc?export=view&id=1w7GhRHqf-zzR0II0FFUOQZomB_JoQEvD",
            "https://drive.google.com/uc?export=view&id=186Imw9W-nK93_TF2kBQLXDpoyojCIjDI",
            "https://drive.google.com/uc?export=view&id=1mMw7qNmaQGf3y76ApEb3Oq3Hlec981eF",
        ]
        data_list = [
            {
                "nama": "Adrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara lapas",
                "hobbi": "Nyari-nyari hobi",
                "sosmed": "@adriangaol",
                "kesan": "Abangnya kerenn trus ramah juga",  
                "pesan":"Semangat nyusun tugas akhirnya yaa bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya cantikk",  
                "pesan":"Semangatt yaa kak ngerjain tugas akhirnyaa, jaga kesehatann"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "Kakaknya kerenn, ramah juga",  
                "pesan":"Semangat selalu kakk buat tugas akhirnyaa"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abangnya kerenn",  
                "pesan":"Bahahgia selalu dan semangat terus ya bangg"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya kerenn, baik jugaa",  
                "pesan":"Semangat ngeasprak nya ya bangg"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl. Lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abangnya kerenn, trus ramahh",  
                "pesan":"Semangat kuliahnya bangg"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya asikk",  
                "pesan":"Bahagia dan jaga kesehatan selalu yaa kakk"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat selalu kakakk"
            },
            {
                "nama": "Alvia Asrinda Br Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakaknya ramahh, baik banget",  
                "pesan":"Semangat yaa kak kuliahnyaa"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat selalu bangg"
            },
            {
                "nama": "Elia Meylani Simajuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya ramahh, baik banget",  
                "pesan":"Bahagia selalu kakakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bv8TLVp_2K31ZnyDN89LHnPRScK-IdZk",
            "https://drive.google.com/uc?export=view&id=1MqovgKb6CA2gTIH-dcePIsF6nJjFOGNn",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1o7fPVp88dS0LGGjW0iNbDClH61KRjK4k",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1fkYODJje4Tt2E8qQ3AVAM0ct3R0MNO7E",
            "https://drive.google.com/uc?export=view&id=1zIjSuilQHgbWYdQBbJMFbNCIxDM2dlqY",
            "https://drive.google.com/uc?export=view&id=1HUIEnCXMdL4U8SgBfqkzEpUdSggL8-Ii",
            "https://drive.google.com/uc?export=view&id=1v-LfMWsLzV284QhRmuLaDyPRWeTn65nj",
            "https://drive.google.com/uc?export=view&id=1lLJpgE5Hj8xOH86qM40y40ZGskdpKpCh",
            "https://drive.google.com/uc?export=view&id=1ZykNmxEANXBqWQG12yRojVM7REw_eVgB",
            "https://drive.google.com/uc?export=view&id=1aAKRL5tXYPKoVBAfxt-8wltTsJ4SdTa0",
            "https://drive.google.com/uc?export=view&id=1vUBv0P_SiAAbGeAq7eRy9jVs8adYVE3l",
            "https://drive.google.com/uc?export=view&id=1w72HMazC4gjH3s6V0OUJ5fxwydcb6zgP",
            "https://drive.google.com/uc?export=view&id=1FIfaA9_s42x1X61CePbXPiYrhvsi4gqY",
            "https://drive.google.com/uc?export=view&id=1EvCiNpMBXyab25uZxPdGkLX1Zl5wOpd3",
            "https://drive.google.com/uc?export=view&id=1xFp2VV6zgetUDTk7DCprZnp8joUWkD0f",
            "https://drive.google.com/uc?export=view&id=1b3YPIspms94IX2lyWQTJJUbrl-sMsgCO",
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@wayuraja",
                "kesan": "Abangnya asikk orangnya ",  
                "pesan":"Semangat buat tugas akhirnya bangg"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya cantikk trus lucuu",  
                "pesan":"Semangatt dan bahagia selalu yaa kakk" # 2
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Tidak terwawancarai",  
                "pesan":"Semangatt kuliah kakk" 
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya tinggii trus cantikk ",  
                "pesan":"Semangat kuliahnya yaa kakk"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, lampung Selatan",
                "alamat": "Natar, lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya ramahh",  
                "pesan":"Semangatt selalu kakakk" # 5
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat kuliahnya kakakk" # 6
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak daplok yang ter the best, baik sekalii",  
                "pesan":"Bahgia selalu kak ciaa, jaga kesehatann" 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Jl. Pembangunan 5, Sukarame",
                "hobbi": "Makan geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakaknya ramahh dan baik sekalii",  
                "pesan":"Jaga kesehatan selalu ya kakakk" 
            },
             {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya ramah dan cantikk",  
                "pesan":"Semangat kuliahnya kakakk" # 9
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya asikk, seruu",  
                "pesan":"Semangat kuliah dan tugas akhirnya bangg" 
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakaknya seruu",  
                "pesan":"Semangat terus kuliahnya kakk"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Nyari tuyul buzzcut",
                "sosmed": "@jimnn.as",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat selalu bangg" 
            },
             {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya ramahh",  
                "pesan":"Bahagia selalu kakakk" # 13
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat kuliahnya kak" # 14
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Koleksi parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat tugas akhirnya bangg" # 15
            },
            {
                "nama": "A'bit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main Uno",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya baikk",  
                "pesan":"Semangat dan sukses selalu bangg" # 16
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abang ter the best, baik sekaliii",  
                "pesan":"Semangat kuliahnya yaa bang, jaga kesehatannyaa" # 17
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abangnya baikk, ramah jugaa",  
                "pesan":"Semangatt kuliahnya bangg" # 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Muara Pilu, Bakauhuni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya lucuu, ramahh",  
                "pesan":"Bahagia selalu kakakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
