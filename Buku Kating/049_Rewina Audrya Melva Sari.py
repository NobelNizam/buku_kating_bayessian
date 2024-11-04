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
            "https://drive.google.com/uc?export=view&id=1WFeSCieSqniRkgm-9_6iGio_sVvrcyNX",#Kharisma Gumilang
            "https://drive.google.com/uc?export=view&id=1WI8Dwj3LVQMKbUSEaj1Hj4aRUbPVitRC",#Pandra
            "https://drive.google.com/uc?export=view&id=1WLCreDw3q7C4Y1yfOLLZVm4rXwM5GNrT",#Meiza
            "https://drive.google.com/uc?export=view&id=1WUHJQa1lPsaVXGWg5U-IkfuCtScIPiUH",#Hartiti
            "https://drive.google.com/uc?export=view&id=1WNAvZquWgZGWCYYYwt815GCBDR2UTQwM",#Putri Maulida
            "https://drive.google.com/uc?export=view&id=1WW1j38bPLEZmfjcx0OPrp891HxKgFWn9",#Nadilla

        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Kakak sesuai namanya, berkharisma",  
                "pesan":"Terus semangat pantang mundur kak menghadapi TA"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21 ",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": " waaahh abangnya kereenn ",  
                "pesan":" abang suka mainin lagu apa bang pake gitar? "# 1
            },
            {
                "nama": "Meiza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": " kakaknya imuut ",  
                "pesan":" semoga diperlancar ya kak lulus kuliahnyaa "# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "12150031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Kakak keliatan kalem tapi kayak ada aura yang unik gituu",  
                "pesan":" kakak suka nyanyi lagu apa kak?"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Panyukumbah, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": " pas denger hobi kakak aku kepikiran kakak suka nyanyi keknya ",  
                "pesan":" semangat kak jadi sekretaris! "# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": " kakaknya keliatan tegaas banget ",  
                "pesan":" kakak baca komik atau apa kak?"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sXoBf_tTL2VK8ifXY9D3lGB5u79Na0SC",#kak Tri 1
            "https://drive.google.com/uc?export=view&id=1sFVXW5X8EPBiHDjct1nm0DIb9lMup9IO",#Kak Annisa 2
            "https://drive.google.com/uc?export=view&id=1sAGHoaJSDa5lPrwzJsw-gI3DLeLQSTT5",#Kak Wulan 3
            "https://drive.google.com/uc?export=view&id=1sEfiG20SD4Da4DH_QKicsbbPDzRPbnY2",#Kak Anisa Dini 4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Claudhea 5 tdkk
            "https://drive.google.com/uc?export=view&id=1sbhCBn8VEfjoR7P_JmujOYUC1xEXvXtw",#Bg Feryadi 6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Renisha 7 tdkk
            "https://drive.google.com/uc?export=view&id=1sMPVvu_OSSvzgmXBK5Ye5_O15Cis41eB",#Bg Mirzan 8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Anisa Fitri 9 tdkkk
            "https://drive.google.com/uc?export=view&id=1s0pHIF6FXEnQQuCWwahrRISJJQzSslRe",#Kak Dhea 10
            "https://drive.google.com/uc?export=view&id=1sHMAzr72lwVgJODeKHb_iIEZokRNl2Cw",#Bg Fahrul 11
            "https://drive.google.com/uc?export=view&id=1sR0opJmtuDCiO4oosQImElMxA-k-P0PS",#Kak Berliana 12
            "https://drive.google.com/uc?export=view&id=1seVvBsdtR9EDaOdbCq3eyLVnF5yjAIsM",#Bg Jere 13
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Ngerjain TA",
                "sosmed": "@trimurniaa",
                "kesan": "kakaknya asikk sama publik speakingnya bagus banget",  
                "pesan":"semoga lancar ya kak ngerjain TA nya" #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakaknya kalem sekalii",  
                "pesan":" Rekomendasiin Novel yang seru kak" #2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "18",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "kakaknya cantiikkk",  
                "pesan":" rekomendasiin drakor dong kak" #3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "waaahh ternyata ada juga yang suka dracin",  
                "pesan":"rekomendasi dracin dong kak" #4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": " nama kakak baguuss ",  
                "pesan":" musik yang kakak suka apa kak?" #5
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abang Ferdy kalem sekalii",  
                "pesan": " baca bukunya jangan kedeketan ya bang nanti minus matanya " #6
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": " kakakk cantikk ",  
                "pesan":" kakak lebih suka pake headset atau nggak kak?" #7
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "abangnya maniss sama tinggi jugaa",  
                "pesan":"jangan kelamaan tidur ya bang" #8
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": " baca Webtoon",
                "sosmed": "@ansftynn_",
                "kesan": " kakaknya ramaahh",  
                "pesan":" rekomendasiin webtoon yang fantasy kak" #9
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "120",
                "asal": "Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mengumpulkan tugas di elearning h15 detik",
                "sosmed": "@myrrinn",
                "kesan": " waahhh hobinya sama kayak aku ",  
                "pesan":" yok kak bisa ngumpulin tugas 1 jam sebelum deadline " #10
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, hiking, berenang, dengar musik, minum kopi",
                "sosmed": "@shrul.pdf",
                "kesan": "abangnya positive vibe nya kerasa",  
                "pesan":" terus semangat bang menghadapi TA" #11
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "kakaknya maniss cantik gituu",  
                "pesan":" Kakaak film horror yang paling horror apa kak? " #12
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": " abang seruu, terus juga abangnya baiikkk",  
                "pesan":" Yok bang kurangin bikin emosi orang bang tapi tetap semangat ngasprak ya bang " #13
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BY12Ox3QiHp077OMYZUuroShjXD5wmu3", #Annisa
            "https://drive.google.com/uc?export=view&id=1Wczhi5WQ4VSDfBoup_zmA1jUeAO1-vcQ", #Rian Bintang
        ]
        data_list = [
            {
                "nama": "Annisa Luthfia Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfia_",
                "kesan": "Publik speaking kakak bagus dan tegas",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HkN4PRhdXHE_Psj11v_wVPsSJf8715hi", #Bg Econ 1
            "https://drive.google.com/uc?export=view&id=1Bz9ucQ_7Iyl8WAigfwmGbWVllTpLPElQ", #Kak Elisabeth 2
            "https://drive.google.com/uc?export=view&id=1Hd1kDEfBHptQUQjnqtlPDUvyeqnYFeaA", #Kak Afifah 3
            "https://drive.google.com/uc?export=view&id=1HJ5dmm597fhx_E5Vpqa73sFu4V44g9Wu", #Kak Allya 4
            "https://drive.google.com/uc?export=view&id=1HChI_M3d3_DIg0Bln_Wx52O8dVCgJEqc", #Kak Eksanti 5
            "https://drive.google.com/uc?export=view&id=1GoZx_beQZi81KjRevS1jBMe2em25y5HO", #Kak Hanum 6
            "https://drive.google.com/uc?export=view&id=1GQ7O7_3bA9HYku_1QYHS7YwflMn5SBBT", #Bg Ferdy 7
            "https://drive.google.com/uc?export=view&id=1HQ4Ih_CrKLR_IsU6zdfs6nZFvlPDQyMS", #Bg Deri 8
            "https://drive.google.com/uc?export=view&id=1GcwClJbTiiT5IKHuwrLdN1yfLZeBGSq0", #Kak Oktavia 9
            "https://drive.google.com/uc?export=view&id=144ZALQTo9YjFra7UdkT751UfPENKUnh7", #Bg Deyvan 10

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Ibnu 11 (tdkk)

            "https://drive.google.com/uc?export=view&id=145SbJ48UYW6E9X_dA0u4mgNcgZfMx0wu", #Bg Jo 12
            "https://drive.google.com/uc?export=view&id=1I_iU-Cg6Bpu9SGbh46SwS2_0JSNHFXHb", #Bg Kemas 13

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg leonard 14 (tidak)

            "https://drive.google.com/uc?export=view&id=1Ia0fLSThdDZTZX6stDx1P8lEPrhkEUdE", #Kak Presilia 15
            "https://drive.google.com/uc?export=view&id=145E5xgtQ6lFPfMk6BCkMJUbnXz6ZIJ2l", #Kak rafa 16
            "https://drive.google.com/uc?export=view&id=1J5uMnjcZlLRaEtcF6WV93Lqx8tUP44QZ", #Bg Sahid 17

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Vanessa 18 (tidak)

            "https://drive.google.com/uc?export=view&id=1HsnzoMIsDQcMA5Rr90-mCmTwjNaNXcrz", #Bg Ateng 19
            "https://drive.google.com/uc?export=view&id=1IRIqqL-BAqf63fEo9F2R59Ly6X8G0ffF", #Bg Gede 20
            "https://drive.google.com/uc?export=view&id=1ID5wy8j9deP6f8cdmYvwLBgSPDMOGlha", #Kak Jaclin 21
            "https://drive.google.com/uc?export=view&id=1ID5n2cH1-PpqkeZw7ptVy3KEd15dt6mH", #Bg Rafly 22
            "https://drive.google.com/uc?export=view&id=1IK5LgWWslS7y9y5ekZqpgeeGFGENV-tx", #Kak Syalaisha 23
        ]
        data_list = [
            {   #1
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": " keliatannya abang tegas, baiikkk ",  
                "pesan":" mau travelling kemana bang?  " # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": " kakak keliatanya kayak galak, terus rambut kakak baguuss ",  
                "pesan":" tips punya rambut bagus kaak " # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jailin Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": " kakakk cantiikkkk, imuutt ",  
                "pesan":" kasih tips punya kulit bagus kak " # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": " kakaknya tegaaas kalo senyum maniss bangett ",  
                "pesan":" jangan pantang nyerah ya kak, semangat teruuss sama tips  " # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": " kakaknya  ",  
                "pesan":"  " # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": " kak hanum cantik manis gitu, terus murah senyuum lagi ",  
                "pesan":" jangan kebanyakan minum kopinya ya kak " # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": " abangnya kalem tapi keliatan kayak serius gitu  ",  
                "pesan":" semangat bang futsalnyaa, sukses selaluu " # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": " abangnya kece ",  
                "pesan":" hati hati bang masuk angin " # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " kakaknya pendiaamm tapi punya hobi yang lumayan ngerii ",  
                "pesan":" terus semangat pantang mundur kak " # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450148",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": " abangnya ramaah terus lucuu ",  
                "pesan":" kasih tips supaya rajin belajar bang " # 10
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
                "pesan":"   " # 11
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": " abang orangnya humblee, seru jugaa diajak ngomong  ",  
                "pesan":" tetap semangat ngeaspraknya bang " # 12
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": " abang yang pinter ngoding ",  
                "pesan":" kapan kapan ajarin saya ngoding ya bang " # 13
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
                "pesan":"   " # 14
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": " kakaknya pendiamm, kalem, tapi cantiikk ",  
                "pesan":" ayuk kak lebih banyak interaksi kedepannya " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": " kakaknya kalem terus punya aura yang beda gitu ",  
                "pesan":" favorit webtoon kakak genre apaa? " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": " abang yang kalem terus bisa main gitar ",  
                "pesan":" Abangg ajarin aku gitar bang " # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": " ",
                "kesan": "  ",  
                "pesan":"  " # 18
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": " abangnya baiikk terus sabar lagi sama publik speaking abang baguuss ",  
                "pesan":" semangat terus bang mimpin orba, jangan lupain TA nya ya bang " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": " Abang orangnya baikk, ramahh tapi kayak masih banyak diamnyaa ",  
                "pesan":" jangan begadang ya bang " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": " kakaknya cantiikk terus ramah lagii ",  
                "pesan":" kakak suka renang gaya apa kak? " # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": " abang orangnya pendiam tapi ramaah  ",  
                "pesan":" bang rekomendasiin game yang seru dong bang" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": " kakaknya pendiaam terus kalem gituu ",  
                "pesan":" kakak suka baca buku apa kaakk? " # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=173n_sp5tCelkmZMmRGC0Nkv8NlqpuBgQ", # rafi
            "https://drive.google.com/uc?export=view&id=17Rl0TNN57ZVMsEibp19IyhFJGhvuSfwu", # annisa

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # mujadid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # ahmad

            "https://drive.google.com/uc?export=view&id=15arE0GLU9Uu8B8zYAKmxkEdXcbT6q5iu", # regi
            "https://drive.google.com/uc?export=view&id=11wL_gAVUSSX_6jlbmShsh6jnlJAWjvCT", # Syalaisha
            "https://drive.google.com/uc?export=view&id=175QiKjYoEOfOGDTMvPT_MRtbNOOgMtm1", # anwar

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Deva

            "https://drive.google.com/uc?export=view&id=17RQn0PCpApVin4qTuuG4YjeAUTh9Ql4Y", # DindA
            "https://drive.google.com/uc?export=view&id=176bFDlah9NxCU5eYii5mRjsqzBMuwoPu", # MARLETTA
            "https://drive.google.com/uc?export=view&id=121oPZ3Lydf9wR9M4i-XYUgMDjKRnqsms", # Rut Junita
            "https://drive.google.com/uc?export=view&id=17Hx5YTqp7JR_IuLEdl--pGRNjJuJvM3j", # Syadza
            "https://drive.google.com/uc?export=view&id=1cD8hK7NENS8onB4nmNpnb6fSuIpQ_jjn", # Eggi
            "https://drive.google.com/uc?export=view&id=17B8Ce_LLlDM0pKoqoU121Z1f3GX_1Otc", # Febiya

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Happy Syahrul
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Aditya
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
                "kesan": " abang keliatan keren ",  
                "pesan":" Semoga cepet dapet kerjaan ya bang " # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": " kakak yang kalem, cantiikk ",  
                "pesan":" kakak suka masak apa kak? " # 2
            },
            {
                "nama": "Mujajid Choirus Surya",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "  ",  
                "pesan":" abang semangat terus bang olahraganyaa " # 3
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": " abang tinggi bangett ",  
                "pesan":" semangat ngeasprak ADS ya bang, sekali sekali ajarin saya ya bang " # 4
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Review jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": " kakak yang kalem ",  
                "pesan":" semangat ngereview jurnalnya kak! " # 5
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": " waaah abangnya keliatan pendiam di grup tapi pas ketemu seruu",  
                "pesan":"makasih bang udah jawab kita dalam mengerjakan tugas kader inii jika kita tidak mengerti" # 6
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": " kakak cantiikk ",  
                "pesan":" semangat ngeresume webinarnya kak? paling suka dateng ke webinar apa kak? " # 7
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "  ",  
                "pesan":" baca jurnalnya jangan kedeketan sama mata ya kak nanti sakit matanya " # 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review Jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "  ",  
                "pesan":" kasih tips supaya suka ngereview jurnal kak " # 9
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Kepualauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Menghitung Akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membangkitkan bilangan",
                "sosmed": "@puspadrr",
                "kesan": "  ",  
                "pesan":"  " # 11
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan": "  ",  
                "pesan":"  " # 12
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "  ",  
                "pesan":"  " # 13
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "  ",  
                "pesan":"  " # 14
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Ngoding Wisata",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "  ",  
                "pesan":"  " # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1V-g9GPedSoY-t8HM19lg1-nrIYzvVcgX", # Yogy 1
            "https://drive.google.com/uc?export=view&id=1V-mODKMp5_aGxkcLg0bbryXt7lcRp02S", # Ramadhita 2
            "https://drive.google.com/uc?export=view&id=1Vf71d7lpVvPfB1zA4eJZwfVHg5IJuZG0", # Nazwa 3
            "https://drive.google.com/uc?export=view&id=1W5mFGSI0V2-u02mPtVcknxdyZIuzrk0Z", # Bastian 4
            "https://drive.google.com/uc?export=view&id=1W9x-CAR--dRwUWWPUNGaZrkrtdEVTRHg", # Dea 5

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Esteria 6
            
            "https://drive.google.com/uc?export=view&id=1V05sBS8mZJkbVKEhnMZZLC9htzlT4BsU", # Natasya 7
            "https://drive.google.com/uc?export=view&id=1ZLySVodVMLOuc9b0Nimi0I27G_gb9baB", # Novelia 8
            "https://drive.google.com/uc?export=view&id=1V3ltJ5j0g9JhWEeA1n7T0qUXFKvcNJdV", # Jasmine 9
            "https://drive.google.com/uc?export=view&id=1UpQCNfsIWdIpspyCJB1XkXYepz8dERJZ", # Tobias 10
            "https://drive.google.com/uc?export=view&id=1VmcJJGDlXgXy7sgyCxrgKvH9zz0_6c1b", # Yohana 11
            "https://drive.google.com/uc?export=view&id=1VvrWRKZ7jS-HbOZ27EekjlkcXzF-I0dK", # Rizki 12
            "https://drive.google.com/uc?export=view&id=16ETYDz4DkBzb4o2k7tOssCOxCt6HTN5r", # Arafi 13
            "https://drive.google.com/uc?export=view&id=1UvFjVh4N9GghLoDibaEf25xyBBqCZEyG", # Asa 14
            "https://drive.google.com/uc?export=view&id=1Vzg20q3U5T2DDFsq24J5SWg2JB-BAz8v", # Chalifia 15
            "https://drive.google.com/uc?export=view&id=1alEwJbZNmIqRUyojvOFFzIZqripO0wQX", # Irvan 16
            "https://drive.google.com/uc?export=view&id=1W4aTMjPtIwuczXpX7NCpbS75Ht0um1RI", # Izza 17
            "https://drive.google.com/uc?export=view&id=176pcqxvDErEwjZao7uz5fkLEMSCr-jWF", # Khaalishah 18
            "https://drive.google.com/uc?export=view&id=1W-ZeFyuRCUFsjJIn7BP5PN0neSkedw1_", # Raid 19
            "https://drive.google.com/uc?export=view&id=1W3FC4kX2YZwz4SPeHs3VW0CD0GFhMmrz", # Tria 20
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosmed": "@yogyst",
                "kesan": " BAB abang lancar sekali",  
                "pesan":" tips dong bang BAB teratur " # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": " kakaknya ramah terus punya aura tegas gitu ",  
                "pesan":"kakak biasanya jalan kemana kak?" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Korpri ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "waahh kakaknya keren suka main golf",  
                "pesan":"ajarin aku main golf kak, aku mau belajar main golf" # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": " abangnya tinggiii terus pendiam lagi ",  
                "pesan":" mau liat hasil gambar abang " # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": " kakaknya keliatan tegas terus tenang gitu ",  
                "pesan":" kakak suka nanem apa kak " # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "  ",  
                "pesan":" kakak semangat main golfnyaa!! " # 6
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": " kakaknya lucuu maniss gituu ",  
                "pesan":"kakaakk surfing dimanaa? ajak sama ajarin aku kak" # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": " cantiikkk pake kacamataa, baik jugaa suka mujii ",  
                "pesan":" jaga kesehatan ya kakk " # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": " waahh alamatnya sama kayak akuu ",  
                "pesan":" sehat selalu ya kakak " # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": " bang tobias terlihat badas ",  
                "pesan":" abang biasa jogging berapa lama bang? semangat ngaspraknya bang " # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": " kakak keliatan tegaass tapi aku tau kakak baiikk ",  
                "pesan":" nanti ajarin aku bowling ya kaak " # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": " kakaknya kaleemm ",  
                "pesan":" tips and trik bikin portofolio bang " # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": " abangnya keliatan pintar ",  
                "pesan":" abang ajarin aku cara bertanii " # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "kakak kaleem kalem tapi ternyata seru jugaa ",  
                "pesan":" nanti ajarin aku tepuk semangat ya kak " # 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": " kakakk yang cantiikk terus keliatan pintarr ",  
                "pesan":" terus semangat ya kak " # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": " abang yang seruuu ",  
                "pesan":" jangan begadang ya bang main gamenyaa " # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": " kakak yang kecee sama kereen banget ",  
                "pesan":" ajarin main rubik kak, saya cuman bisa 1 sisi doang soalnya " # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": " suara kakak kecil bangett waktu ituu ",  
                "pesan":" kakakk semangat terus ya kaakk organisasinyaa " # 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": " abangnya terlihat pintar terus pendiam ",  
                "pesan":" semangat bang larinyaa! " # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": " kakaknya cantik terus seruu, ramah jugaa ",  
                "pesan":" baca buku cerita atau pelajaran atau dua duanya? " # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=152LHFBxa8LkpR53hUPe789omVVOvaeVc", # Dimas 1
            "https://drive.google.com/uc?export=view&id=14trKRjj5XzQP4gphMDFEOtI1ek6I3VHJ", # Catherine 2
            "https://drive.google.com/uc?export=view&id=17h9IBOeXtGzUkK7frViTxfeb95kLlogD", # M. Akbar 3
            "https://drive.google.com/uc?export=view&id=15H-VhuMIsr7kA0bCdq_jBrtv1-0XTUfH", # Rani 4
            "https://drive.google.com/uc?export=view&id=157suAlJLDKccUTUJbMtfgHF5XGQZM35h", # Rendra 5
            "https://drive.google.com/uc?export=view&id=14akKdJjJs73MXqKH2mJaVfsOlIqwLXWT", # Salwa 6
            "https://drive.google.com/uc?export=view&id=14qX3ZnSfwpFijOduLxKmotNncFwBVkQe", # Yosia 7
            "https://drive.google.com/uc?export=view&id=14j53w4IWE1pFth5X4J4mfDZbZ4PH0zSL", # Ari 8
            "https://drive.google.com/uc?export=view&id=1SiAul4wKOnRKMw5qG8ipZg9jwcgAXO9Z", # Azizah 9

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Dearni 10

            "https://drive.google.com/uc?export=view&id=14vJJbGm1-YwC2oraLF_WH5ApkMQjSq2e", # Meira 11
            "https://drive.google.com/uc?export=view&id=14dTR3o-oJha0ne0Jf7UG0ifD2HLaLaue", # Rendi 12
            "https://drive.google.com/uc?export=view&id=13nWdWwYlf8ng7ReTFSr3YHFnhPtfoX1a", # Renti 13
            "https://drive.google.com/uc?export=view&id=17kg9DRGCNhxQIk9RK7Jvhit3kjHGBcRL", # Josua 14
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Manjat pohon pinang",
                "sosmed": "@dimzrky_",
                "kesan": "Public Speaking abang bagus banget terus semangat banget ngobrolnya",  
                "pesan":" semangat terus bang mimpin internall " #1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Airan",
                "hobbi": "Membaca novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "kakaknya cantik bgttt",  
                "pesan":" kakak suka novel genre apa kak? " # 2
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi": "Main sepeda ke gunung",
                "sosmed": "@akbar_resdika",
                "kesan": "abangnya kalem lucu gitu",  
                "pesan": "tips kuat naik ke gunung pake sepeda bang"# 3
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu ",
                "kesan": "kakanya keliatan tegas tapi ramaah",  
                "pesan":"kpop kakak denger juga nggak kak?" #4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "abangnya seruu, asiikk",  
                "pesan":" mau nyari buah pisang dimana bang?"# 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhn_694",
                "kesan": " kakaknya keliatan adem, kalem gituu",  
                "pesan":"kakak suka nonton anime nggak kak?"# 6
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450049",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": " abangnya kalemm ",  
                "pesan":" semoga sehat dan sukses selalu ya bang. semangat TA nya bang " #7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "futsal",
                "sosmed": "@ari_sigit17",
                "kesan": " abangnya keliatan kalem terus suaranya kecill ",  
                "pesan":" Semangat terus bang berorganisasinyaa bang "# 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": " kakaknya kalem sekalii",  
                "pesan":" semangat kak berkebunnyaa"# 9
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": " ",  
                "pesan":" " #10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "kakaknya lucu",  
                "pesan":" kakak suka nonton film atau anime atau sinetron kak?"# 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "abangnya lucuu",  
                "pesan":"bang apakah kamu bisa ngambang dilaut bang"# 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "kakaknya cantiii hihi",  
                "pesan":"kakaknya mirip temenku sekilas tw"# 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "12145001",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Gya Kos",
                "hobbi": "Nonton Film",
                "sosmed": "@josuapanggabean16_",
                "kesan": "abangnya kece",  
                "pesan":"semangat dan sehat selalu bang"# 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X0e6hEzoP9cAbxIDTyZ6C6ElNCWw0NbT", # Adrian 1
            "https://drive.google.com/uc?export=view&id=15cfXbVUmuJ4m_89XmBIshRrqKBYnVjEw", # Adisty 2
            "https://drive.google.com/uc?export=view&id=1Wye99y2heoho3jFN7vUanwp5aGCKqvME", # Nabila 3
            "https://drive.google.com/uc?export=view&id=1XS0jwAC1cmxBQISgbog1hLO4LMp-nJAz", # Ahmad 4
            "https://drive.google.com/uc?export=view&id=1X6SWDB-uPzAa5FGAHGVxKQ_o2A0YPmsC", # Danang 5
            "https://drive.google.com/uc?export=view&id=1X0awJwWoLJLAGs0pBJozZT1qsz3WFOqa", # Farrel 6
            "https://drive.google.com/uc?export=view&id=1luQJBf5W3eRVY_3sOJDnSqnDUrSVtdyy", # Tessa 7

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Nabilah 8

            "https://drive.google.com/uc?export=view&id=1X8MQt76Jmzdh6ywm6fjT_1kDS-6DWpiH", # Alvia 9
            "https://drive.google.com/uc?export=view&id=1WwfHGea1TYb88WJVlYqoiTtVisqqiKNL", # Dhafin 10
            "https://drive.google.com/uc?export=view&id=1XAWH96nRTl_GYs9COTFofTYBgb2tSJY4", # Elia 11

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Sindi Kalang",
                "alamat": "Dekat penjara lapas",
                "hobbi": "Nyari Hobi",
                "sosmed": "@andriangaol",
                "kesan": " abang keliatan tegaass ",  
                "pesan":" yuk bisa ketemu hobinya abang " # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": " kaknya kaleemm, cantiikk ",  
                "pesan":" film kesukaan kakak apa kak? " # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": " kakaknya keliatan tegas gituu ",  
                "pesan":" semangat kaakk TA nyaa, jangan lupa tidur kak " # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan 1",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": " keliatan pintaarr ",  
                "pesan":" tips bisa badminton ya bang " # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": " diem diem abangnya pintar jualan ",  
                "pesan":" semangat bang jualannyaa " # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": " abangnya sabar, terus jawabnya lancar banget ",  
                "pesan":" semangat bang mimpin suporterannya sama jualannyaa " # 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun, Sumut",
                "alamat": "Pemda",
                "hobbi": " Menulis",
                "sosmed": "@tesakanias",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "  ",  
                "pesan":"  " # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19mhrnMRkHdyBxj4_8TcuWaSMALZpTSpF", # Wahyu 1 tdk

            "https://drive.google.com/uc?export=view&id=1vBOGQZb1HU-cWCUb2RbhCSLFwm8heE5f", # Elok 2

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Arsyiah 3 tdk

            "https://drive.google.com/uc?export=view&id=1vr5t7mL3QHyl59TzzTwKlhvyNIflvS6H", # Chintya 4

            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Eka 5 tdk
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Najla 6 tdk

            "https://drive.google.com/uc?export=view&id=1u5rQy9NqhwkhJdEo6k6COfJCVbwNQPiI", # Patricia 7
            "https://drive.google.com/uc?export=view&id=1EYkg6JmU3ehWcoisi_WbbmVAp46upC2b", # Rahma 8
            "https://drive.google.com/uc?export=view&id=15X7WwU6XrdZKsUMXT9NZNkR35LO1JsXl", # Try Yani 9
            "https://drive.google.com/uc?export=view&id=15StBCV2kad6QgRAcZeIv60xRLDi9xvsv", # Kaisar 10
            "https://drive.google.com/uc?export=view&id=1Gu458qC1kjJ87ir21GhVzvTToNTEK07J", # Dwi 11
            "https://drive.google.com/uc?export=view&id=1G7FQKUgX8ab-bM9kTcjvk9gzCofNX9yj", # Gym 12
            "https://drive.google.com/uc?export=view&id=15WtP-SdtLP2a8JxQMUCAWsHGbsTGNXJA", # Nasywa 13
            "https://drive.google.com/uc?export=view&id=1HDF9s71In-7WdFP-gZvSTor0xp8aTx6-", # Priska 14
            "https://drive.google.com/uc?export=view&id=15MGjvloc7FlAw0RcS6F4ycYyHlXywVbQ", # Arsal 15
            "https://drive.google.com/uc?export=view&id=1tZu_kFOyOxpYC59OklFAlWhy6tIXF7q5", # Abit 16
            "https://drive.google.com/uc?export=view&id=1JtZpC6fMnRJosv19nZRpjHqB2Ba_dEj0", # Akmal 17
            "https://drive.google.com/uc?export=view&id=1KpJ8jtb-5PcoNgTHJ9XvvrX5gXz42gPd", # Hermawan 18
            "https://drive.google.com/uc?export=view&id=1L49j75KMEZzYIvT_himjLcc9yu0y_iDk", # Khusnun 19
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@wayuraja",
                "kesan": "  ",  
                "pesan":"  " # 1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya cantik sama lucuu",  
                "pesan":" semangat terus ngeditya kakk" # 2
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "  ",  
                "pesan":"  " # 3
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "  ",  
                "pesan":"  " # 4
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, lampung Selatan",
                "alamat": "Natar, lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "  ",  
                "pesan":"  " # 5
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "  ",  
                "pesan":"  " # 6
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": " lucuuu, cantik, seruuu ",  
                "pesan":" makasih kak udah jadi daplok paling cantik kamii" # 7
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Jl. Pembangunan Sukarame",
                "hobbi": "Makan geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwiratnn_",
                "kesan": "   ",  
                "pesan":"   " # 11
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Nyari tuyul buzzcut",
                "sosmed": "@jimnn.as",
                "kesan": "  ",  
                "pesan":"  " # 12
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "  ",  
                "pesan":" kak Nur tutor rajin bersih bersih kak " # 13
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "  ",  
                "pesan":"  " # 14
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Koleksi parfum",
                "sosmed": "@arsal.utama",
                "kesan": "  ",  
                "pesan":" aku mau liat koleksi parfum abang boleh nggak bang? " # 15
            },
            {
                "nama": "A'bit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main Uno",
                "sosmed": "@abitahmad",
                "kesan": "  ",  
                "pesan":" main uno bareng yok bang rame rame " # 16
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": " abang yang softspoken dan sabar banget ",  
                "pesan":" abang kalo kesel keluarin aja ya bang. makasih juga bang udah jadi daplok kelompok bayessian paling ganteng dan sabar sekalii" # 17
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "  ",  
                "pesan": " " # 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Muara Pilu, Bakauhuni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "waahh hobi kakak sama kayak aku",  
                "pesan":" Kakaakk ajarin aku ngedit videooo sama ngedit poto " # 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
