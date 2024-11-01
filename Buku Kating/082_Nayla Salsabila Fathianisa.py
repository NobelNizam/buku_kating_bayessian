
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
                "hobbi": "Ngerjain TAr",
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
                "kesan": "Kakak nya cantikk",  
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
            "https://drive.google.com/uc?export=view&id=1SWjZ5z7mFrSf7AtW1TVzpFM_IOfBjKNX",
            "https://drive.google.com/uc?export=view&id=1irQpcxvbwUeVGeZKa6S6HyNLgfZ_Ovxs",
            "https://drive.google.com/uc?export=view&id=1LR4fnwV4om8GN7vXeuF4ROjp7hrQusTG",
            "https://drive.google.com/uc?export=view&id=1Otr4L5pJpkcEYEf3hs-cSlYc6y4cDcRG",
            "https://drive.google.com/uc?export=view&id=1EQEo5CJWYf-RA_PFb9Ly6VXt_yz54vSG",
            "https://drive.google.com/uc?export=view&id=1k8tb50EN-YFUA6Arp3wDtSwSvqvMkJpT",
            "https://drive.google.com/uc?export=view&id=1WoCEZRpNQdBSwKW5t3VKTvJYekj-08-B",
            "https://drive.google.com/uc?export=view&id=1UUGBJ3SeJIZrK94HhSOOogCOJ6gYy_Bt",
            "https://drive.google.com/uc?export=view&id=11eMGkmVDDloVrTQXQ5pG7XECpwxRxCa_",
            "https://drive.google.com/uc?export=view&id=1XIilrVa2Hd0DFvEMPQPCwP8Fsq6GBLd3",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            
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
                "asal":"Lampung T..",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak nya baikk",  
                "pesan":"semangat terus kuliahnya kakak"
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang nya seruu trus asik jugaa",  
                "pesan":"semangat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak nya baikk",  
                "pesan":"Bahagia dan jaga kesehatan selalu yaa kak"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=179XWbWjA0HJPAugtPThC7yIrY-RhiB1m",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=13arx-JTSiSNqadsn3rF6u9-pI2ITROJZ",
            "https://drive.google.com/uc?export=view&id=1UqoYoWSRdTqBhB1XV055hM6NljBv67ra",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1pIgf5zcf2hKGKfCrw6m6zUe0a-BrmORq",
            "https://drive.google.com/uc?export=view&id=1VMhWvt-C84gSEksMPxNGB6js9dbuaSp1",
            "https://drive.google.com/uc?export=view&id=179cw4bqNo5djCGRGVskrP65m0xw_8RBd",
            "https://drive.google.com/uc?export=view&id=1-rzs-6XSzws-GnDGyZOxxPKOs5xGuWNx",
            "https://drive.google.com/uc?export=view&id=1V9DEq-1ob_qDWsT90T8fKUCIkaMobQVP",
            "https://drive.google.com/uc?export=view&id=1M88WIbw9_rX276y8-2R4Zx1sC9u50clg",
            "https://drive.google.com/uc?export=view&id=1bm_VTn8TYfLGmtCjAJQm2IjLAU_gPzCH",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_3READwl0j8b4nkmI4fQjrjd7JG2QiDN",
            "https://drive.google.com/uc?export=view&id=137ZHo7EXWFXhLYriaaP2CpcoePnINN__",
            "https://drive.google.com/uc?export=view&id=1oyMVQf0rsIlIAo_Ee83k7u3Krc6LrR57",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=13L_5LnRkEodvh7o60rNT0TRxle6asbe4",
            "https://drive.google.com/uc?export=view&id=1uDCJYcDyOxVa4YtslhqNnG9k0UvuyB5k",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Burkinapso",
                "alamat": "Jatimulyo",
                "hobbi": "Nyari solar",
                "sosmed": "@yogyst",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semangat nyusun tugas akhirnya bang" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik",  
                "pesan":"Semangat nyusun tugas akhirnya yaa kakk" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kandis ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "  ",  
                "pesan":"  " # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "  ",  
                "pesan":"  " # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "  ",  
                "pesan":"  " # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "  ",  
                "pesan":"  " # 6
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "  ",  
                "pesan":"  " # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "  ",  
                "pesan":"  " # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "  ",  
                "pesan":"  " # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "  ",  
                "pesan":"  " # 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "  ",  
                "pesan":"  " # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "  ",  
                "pesan":"  " # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu anak Pengmas",
                "sosmed": "@izzalutfia",
                "kesan": "  ",  
                "pesan":"  " # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "  ",  
                "pesan":"  " # 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan": "  ",  
                "pesan":"  " # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "  ",  
                "pesan":"  " # 20
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Membaca Novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@akbar_restika",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rani Puspita Sari",
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
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@rendraepr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yosia Reatare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya indah",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ari Sigit",
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
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Banawang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@meirasty_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@rexander",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Adrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Panjibako",
                "alamat": "",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@adriangaol",
                "kesan": "baik dan ramah",  
                "pesan":"semangat mengerjakan TA nya bang adrian"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@adistysa_",
                "kesan": "cantik dan ramah",  
                "pesan":"semangat terus sampai wisuda ya kakak"# 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "",
                "sosmed": "@zhjung",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "ganteng bangettt bang ",  
                "pesan":"semangat kuliahnyaa abang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dananghk_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat kuliahnya bang danang"# 1
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farrel__julio",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus ya bang"# 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alvia Asrinda Br Ginting",
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
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka 1",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Elia Meylani Simajuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "korpri",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@wayyulaja",
                "kesan": "abangnya asikk dan baik ",  
                "pesan":" semangatt terus abangg " # 1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "lucuuu, imutt dan canciiii",  
                "pesan":"semangat dan sukses selalu ya kakak cantikk " # 2
            },
            {
                 "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "ramah dan asikkk",  
                "pesan":"semangatt kuliahnya kakak cantikk" # 3
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "cantik part keberapa ini ",  
                "pesan":"semangayyy ya kakak cantikk " # 4
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, lampung Selatan",
                "alamat": "Natar, lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "ramaahhh ",  
                "pesan":"semangkatik! semangat kakak cantikk! " # 5
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "kakaknya baikkk sekalii ",  
                "pesan":"semangat menjalani harinya kakak canciiii" # 6
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakak terbaikk, canntikk 1000000xx  ",  
                "pesan":"kak cia cantik, bayess yang punyaa " # 7
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Jl. Pembangunan Sukarame",
                "hobbi": "Makan geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "murah senyumm, canciiii ",  
                "pesan":" semangattt dan bahagia terus kakak cantikk" # 8
            },
             {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "cantik part sekiann ",  
                "pesan":"semangattt ya kak ciaa cantikk " # 9
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "abangnya asik dan seru  ",  
                "pesan":"semangat terus ya bang, sukses selalu " # 10
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwiratnn_",
                "kesan": "kakaknya asikk ",  
                "pesan":"semangattt dan bahagia selalu kakak cantikk " # 11
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Nyari tuyul buzzcut",
                "sosmed": "@jimnn.as",
                "kesan": "abangnya ramah  ",  
                "pesan":"semangatt ya abanggg " # 12
            },
             {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "kakaknya baikkk ",  
                "pesan":"semangat terus untuk ksemua kegiatannya kakak cantikk" # 13
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": " ",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "baik kakaknyaa",  
                "pesan":"semangatttt menjalani hari kakak cantikk" # 14
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Koleksi parfum",
                "sosmed": "@arsal.utama",
                "kesan": "ramah abangnya ",  
                "pesan":"sukses dan semangat terus ya banggg" # 15
            },
            {
                "nama": "A'bit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main Uno",
                "sosmed": "@abitahmad",
                "kesan": "abangnya asikk dan seruuu, ramah juga, baik jugaa ",  
                "pesan":"abang semangattt dan sukses selalu yaa " # 16
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang terbaik, baikkk bangettttt 1000000xx ",  
                "pesan":"semangatt, sukses dan bahagia selalu bang akmall, bayess lope bang akmall " # 17
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abangnya asikk ",  
                "pesan":"semangattt ya bang " # 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Muara Pilu, Bakauhuni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kakaknya ramah dan baikk ",  
                "pesan":"semangatt terus kakak cantikkk "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
