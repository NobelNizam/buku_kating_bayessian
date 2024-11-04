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
        gambar_urls = [         # ini yang diubah dari id= ...link...
            "https://drive.google.com/uc?export=view&id=1BBuhYnmQsEqO4XJGSGtpOYOD3XbeUGRr", #bg Gumi
            "https://drive.google.com/uc?export=view&id=1mqs3_Fq5qK9QyUWf4dcqTDOfl9OoSb7Y", #bg Pandra
            "https://drive.google.com/uc?export=view&id=1vnu2_OlLbsLUcniq146LPM6UtjCT3o6I", #ka Meliza
            "https://drive.google.com/uc?export=view&id=1jYDOIqUaiGk3gW8g7sR6mKlmc4uaXXm9", #Ka Titi
            "https://drive.google.com/uc?export=view&id=1rRtdXP4tmHxYgkpSbXCKnikBofwjAYdr", #Ka Putri
            "https://drive.google.com/uc?export=view&id=1B9NBiRSJghCIa2PhcwlK6dqSBGVc8rjk", #Ka Nadilla
        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Kandis",
                "hobbi" : "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan" : "KEREENNNNN ",  
                "pesan" :"semangat dalam menjadi pemimpin himpunan bang"
            },
            {
                "nama"  : "Pandra Insani Putra Azwar",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  :"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan" : "Abang nya suka nyablak jadi lucu",  
                "pesan" :"Semoga sehat selalu dan fokus dengan TA nya bang!!"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  :"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Kakaknya receh",  
                "pesan" :"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  :"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "kakaknya asikk,baik, sama kerenn",  
                "pesan" :"Semoga kakak selalu aktif dan semangat"
            },
            {
                "nama"  : "Hartiti Fadhilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan" : "Kakaknya asik dan murah senyum guyss",  
                "pesan" :"Semoga dimudahkan dalam menyelesaikan perkuliahannya kakak"
            },
            {
                "nama"  : "Nadilla Andhara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  :"Metro",
                "alamat": "Kotabaru",
                "hobbi" : "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan" : "Kakaknya keliatan ambis dan semangat, pasti aktif di kelas",  
                "pesan" :"Terus semangat dalam berkuliah kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b6guo-L1JqpEQ1Nd6uEAAfumZoZx6Zqz", #kak tri murniya
            "https://drive.google.com/uc?export=view&id=1kOpWtlvf95gtAnTFKUjNdcTH-2YDxNLM", #kak annisa
            "https://drive.google.com/uc?export=view&id=1B1zbtXyr2U6nHhkDpICp55TPH4LDf4WO", #kak wulan
            "https://drive.google.com/uc?export=view&id=10rIgAFaAUXXTdkZtVlnWmhcNdTm5VONB", #kak anisa dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=19u5NtpMz3ftHlkNF27IvdQ4rX3HSlVBV", #bg feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1RSph3vQ5uBWnqUTSC8H2QbSWIi07ZP5T", #bg mirzan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1jlAwZEp9puYPYL4p-TBt-HuvpYPM0pB0", #kak dhea
            "https://drive.google.com/uc?export=view&id=1-plmapG9vabrxxyF1UcH1HmdhJKVkW8B", #bg fahrul
            "https://drive.google.com/uc?export=view&id=1BC41kh3dfn5XGRBj7vAaKLpNaceNFKds", #kak berliana
            "https://drive.google.com/uc?export=view&id=1l1zgZ2-XyEQdsE7dDlrTUBIlBQ9xvJEn", #bg jeremia
         
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
                "kesan" : "Kakak nya bagus banget publik speaking nya, baik dan seru banget",  
                "pesan" : "semangat terus ya kakkk, semoga TA nya cepet selesai"
            },
            {
               "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "20",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi" : "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Kakak nya baik, ramah banget",  
                "pesan" : "Tetap semangat terus kuliahnya kakk"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kak Wu;an baik, sabar, asik banget diajak ngobrolnya",  
                "pesan" : "Semangat ya kak kuliahnya dan ngerjain TA nya"
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
                "pesan" : "Semangat terus kakk kuliahnya"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450118",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bernungt, Pesawaran",
                "hobbi" : "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan" : "Kakak nya baik, dan seru banget",  
                "pesan" : "Semangat terus kuliahnya ya kakk"
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
                "kesan" : "Kakak nya baik banget",  
                "pesan" : "Tetep semangat kak kuliahnya"
            },
            {
                "nama"  : "Claudhea Angeliani",
                "nim"   : "121450124",
                "umur"  : "21",
                "asal"  : "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan" : "Kak Clau baik, seru banget",  
                "pesan" : "Semangat ya kak kuliahnya"
            },
            {
               "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan" : "Bnag Mirzan baik, dan keren banget",  
                "pesan" :"Semangat terus kuliahnya ya bang"
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
                "kesan" : "Abangnya baik, seru banget",  
                "pesan" : "Semangat terus banggg kuliahnya"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Kakak nya asik banget",  
                "pesan" : "Semangat kuliahnya kakkk"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Billabong",
                "hobbi" : "Memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan" : "Bang jere baik, seru bangettt",  
                "pesan" : "Semangat terus kuliahnya bang dan jaga kesehatan ya bangg"  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RB-pnsSbQ9urMC2vgqTAx7AR8K2gYxPv", #kak luthfia
            "https://drive.google.com/uc?export=view&id=15i6-_3Q1ZYDC3r85DnuiRN1aNYDmh_tm", #bg bintang

        ]
        data_list = [
            {
               "nama": "Anissa Lutfia Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":" Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "  ",  
                "pesan":"  "
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfi nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "  ",  
                "pesan":"  "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A8DaKjyDrUuFwF17sv013MM7D1jsYJqA", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1APWCzmOJqLiaCmQ5K5m0Pcdbrncd5-jg", #kak jeclin
            "https://drive.google.com/uc?export=view&id=1AXkD1PIJ3EvgHbbmY4ydjARNX5ncEFYw", #bg rafly
            "https://drive.google.com/uc?export=view&id=1A_Y16_gsPUG3y7RuU0zshlwD7PPaoeM5", #kak eksanty
            "https://drive.google.com/uc?export=view&id=1AbVQmRqxYGkvELvOlwiyDWviGFjPbSbw", #kak abet
            "https://drive.google.com/uc?export=view&id=1AcNbwrlJtvnx4Gvha-k0GeoXidEXLAlo", #kak lily
            "https://drive.google.com/uc?export=view&id=1Afj552XC7kMclGFcSp8HqJvN0VrgiiDS", #bg ericson
            "https://drive.google.com/uc?export=view&id=1AhgDmGphXX_DyOtCMjp3J4UsZRP6ivez", #kak rafa
            "https://drive.google.com/uc?export=view&id=1Aji-xVxpp1UGZFBsFgb9VsthRwDXeyA6", #bg deyvan
            "https://drive.google.com/uc?export=view&id=1AkxEsrQloQANGpB4Kl5eNePEcHbU6c-U", #bg sahid
            "https://drive.google.com/uc?export=view&id=1AoKAvo9IkanZeiEKzTy4-qhpuG8kbUYb", #bg jonathan
            "https://drive.google.com/uc?export=view&id=1AoYy15K7_YcH4a8H8sbJsbzaxyLuIbLw", #bg kemas
            "https://drive.google.com/uc?export=view&id=1ApJfwL_IslnP93WmbVUcwYDKCYKjuovM", #kak allya
            "https://drive.google.com/uc?export=view&id=1AtriuyLHT2xh_mbgKJRbyUJUepoIJHtI", #bg deri
            "https://drive.google.com/uc?export=view&id=1Axe3yM1U1K5-Dt_ql39mYKrK-woe8iDH", #kak hanum
            "https://drive.google.com/uc?export=view&id=1B-miHePJx_sulrWw7jzS5AngkbpS4RQj", #kak fifah
            "https://drive.google.com/uc?export=view&id=1x49qv8rQJyWGxE8-As3GDCPwqWCChyVj", #bg farhan
            "https://drive.google.com/uc?export=view&id=1dPBw_J7sxUSHmPwFxcAAvILlOkLqKN83", #bg gede
            "https://drive.google.com/uc?export=view&id=1H85PuHSdaRww6DZ-tE5-ss5WewZ3hU2g", #kak andini
            "https://drive.google.com/uc?export=view&id=1-gtCoNq6TUHwIylh_gzra5VmQQKlfhx-", #kak oktavia
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            
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
                "kesan": " keren ",  
                "pesan":" semangat " 
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
                "pesan":"semangat terus kuliahnya bang"
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
                "kesan": " keren ",  
                "pesan":"  semangat" 
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": " keren ",  
                "pesan":" semangat " 
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": " keren ",  
                "pesan":" semangat " 
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "keren  ",  
                "pesan":" semangattt " 
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": " keren ",  
                "pesan":" semangat " 
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": " keren ",  
                "pesan":"semangat  " 
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": " keren ",  
                "pesan":" semangat " 
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": " keren  ",  
                "pesan":" semangat " 
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": " keren ",  
                "pesan":" Semangattt " 
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Nyari Solar",
                "sosmed": "@yogyst",
                "kesan": "Abang nya seru dan sangat informatif dalam memberikan banyak masukan",  
                "pesan":"semangat terus kuliahnya ya banggg dan sukses selalu!!!"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakak nya asik, seru, dan sangat informatif",  
                "pesan":"semangat terus kuliahnya ya kakkke!!"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini asik banget dan sangat informatif",  
                "pesan":"tetap semangat terus ya kak kuliahnya !!!"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang nya Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan": "Semoga selalu dilancarkan semua urusannya bang, dan tetap semangat bang dalam menjalani kehidupan"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak nya sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan": "Tetap semangat dalam menjalani perkuliahannya kak"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Belwis",
                "hobi": "Surving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "Kakak nya sangat menginspirasi dalam kehidupan ",  
                "pesan": "Tetap semangat ya kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan Seribu",
                "alamat": "Way Halim",
                "hobi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "Kakak nya sangat baik dan sangat mengasyikkan ",  
                "pesan": "Semangat terus kak dalam menjalani perkuliahannya dan jaga kesehatan ya kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak nya sangat baik dan informatif dalam menjelaskan sesuatu",  
                "pesan": "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bnadung",
                "alamat": "Way Kandis",
                "hobi": "Menjahit Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan": "Semangat terus kak dalam menjalani hari-harinya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya sangat baik dan sangat mengasyikkan",  
                "pesan": "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak nyaSangat informatif dalam menjelaskan sesuatu",  
                "pesan": "Tetap semangat kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Abangnya sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat bang"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan" : "Aabangnya sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak nya Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan": "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan" : "Kakak nya sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jaga kesehatan ya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya sangat menginspirasi dalam kehidupan ",  
                "pesan": "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Bertemu anak pengmas",
                "sosmed": "@izzalutfia",
                "kesan" : "Kakak nya sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya dan jaga kesehatan ya kak"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Kakak nya sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Tetap semangat dalam menjalani dunia perkuliahan kak"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan" : "Abangnya sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya bang"
            },
            {
                "nama"  : "Tria Yunani",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan" : "Kakak nya sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
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
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara lapas",
                "hobbi": "Nyari-Nyari Hobi",
                "sosmed": "@andriangaol",
                "kesan": "abangnya seru dan asik banget saat materi",  
                "pesan":"semangat bang,jangan lupa istirahat"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "abangnya keren dan seru",  
                "pesan":"semangat bang kuliahnya"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "ramah dan asikk banget",  
                "pesan":"jaga kesehatan kakk, semangat teruss"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukit Tinggi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "abangnya keren dan humble",  
                "pesan":"sjangan lupa istirahat dan semangat"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "seru dan ramahh",  
                "pesan":"semangat kuliahnya bangg"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.Lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "abangnya baik dan seru banget",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak seru banget dan asik",  
                "pesan":"Jaga kesehatan ya kakk"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "seru banget kakaknya",  
                "pesan":"jaga kesehatan dan semangatt"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Menonton",
                "sosmed": "@alviagnting",
                "kesan": "kakaknya baik dan humble",  
                "pesan":"semangat kuliahnya kak, jaga kesehatan jugaa"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl.Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "ramah dan juga baik banget",  
                "pesan":"jaga kesehatan ya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "kakak baik dan ramahh",  
                "pesan":"semangat kuliahnya kakk"
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
            
        ]
        data_list = [
            {
                "nama"  : "Wahyudiyanto",
                "nim"   : "121450040",
                "umur"  : "22",
                "asal"  : "Makassar ",
                "alamat": "Sukarame",
                "hobbi" : "Nonton Film",
                "sosmed": "@wayuraja",
                "kesan" : "abang keren dan informatif sekali",  
                "pesan" : "jaga kesehatan dan semangat kuliahnya bang"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Ngedit",
                "sosmed": "@elokfiola",
                "kesan" : "kakaknya seru banget dan ramah jugaa",  
                "pesan" : "semangat kuliahnya kak, jaga kesehatan jugaa"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.",
                "kesan" : "kakak baik dan ramah jugaa",  
                "pesan" : "semangat kuliahnya kakk"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "ramah dan murah senyum",  
                "pesan" : "jangan lupa istirahat dan jaga kesehatan kak"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "seru banget dan ramah jugaa",  
                "pesan" : "kakak jaga kesehatan yaa"
            },
             {
                "nama"  : "Patricia Leonrea Diajeng Putri",
                "nim"   : "122450050",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi" : "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan" : "kak cia baik banget dan penuturannya lembut juga",  
                "pesan" : "jaga kesehatan mamii, jangan lupa istirahatt"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Jl.Pembangunan 5, Sukarame",
                "hobbi" : "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan" : "kakak baik dan ramahh",  
                "pesan" : "tetap semangat dan pantang menyerah untuk kuliahnya kakk"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "kakaknya baik dan humble",  
                "pesan" : "jaga kesehatan dan semangat kakk"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "abangnya seru dan asik",  
                "pesan" : "tetap semangat kuliahnya bang"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Pemda",
                "hobbi" : "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan" : "seru banget kakaknya",  
                "pesan" : "jaga kesehatan ya kakk, semangatt"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf",
                "hobbi" : "Nyari tuyul baskat",
                "sosmed": "@jimnn.as",
                "kesan" : "bang gym asik dan ramah",  
                "pesan" : "semangat kuliahnya bang"
            },
            {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1",
                "hobbi" : "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan" : "ramah dan juga baik banget",  
                "pesan" : "jangan lupa jaga kesehatan ya kakk"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Karaoke",
                "sosmed": "@prskslv",
                "kesan" : "kakaknya seru dan baik ",  
                "pesan" : "semangat terus kak menjalani kuliahnya"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi" : "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan" : "abangnya baik, trus kalo ngasih materi juga dijelaskan dengan baik",  
                "pesan" : "jaga kesehatan ya bang"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Main uno",
                "sosmed": "@abitahmad",
                "kesan" : "bang abit asik banget, trus lucu juga",  
                "pesan" : "jangan cape-cape ngehibur orang ya bangg"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan" : "abang sabar banget,trus ngebimbing kami dengan baik",  
                "pesan" : "Tetep jaga kesehatan ya papikuu"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Jalan dekat tol",
                "hobbi" : "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Abangnya seru tapi jahil",  
                "pesan" : "Bang jangan jahil mulu dong pas praktikumm"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi" : "Beantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Kakaknya asik, apalagi saat menjelaskan materi sangat nyambung",  
                "pesan" : "Jaga kesehatan ya kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
