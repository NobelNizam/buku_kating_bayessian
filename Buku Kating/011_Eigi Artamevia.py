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
            "https://drive.google.com/uc?export=view&id=1QP-fCZwoo2KNF8h9Pg7eoPtVaKFdpXTl", #bg Pandra
            "https://drive.google.com/uc?export=view&id=1M6D4jNMDNhRCepu0-7Xwf0-jU-331CUT", #ka Meliza
            "https://drive.google.com/uc?export=view&id=16t51k3uqbSM5_pAfc0Glik-8ANdQJUTA", #Ka Titi
            "https://drive.google.com/uc?export=view&id=1V2yoA-a0RVHzvRrXw5KXOolwprm3MywI", #Ka Putri
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
                "kesan" : "keren dan ramah",  
                "pesan" :"semangat kuliah dan mimpin himpunannya bang"
            },
            {
                "nama"  : "Pandra Insani Putra Azwar",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  :"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan" : "abangnya humble dan seru abiss",  
                "pesan" :"Semoga dilancarkan segala urusannya ya bang"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  :"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "seru banget sama kakakk",  
                "pesan" :"jaga kesehatan dan semangat teruss"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  :"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "baik dan ramah jugaa",  
                "pesan" :"jangan lupa istirahat kakk"
            },
            {
                "nama"  : "Hartiti Fadhilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan" : "ramah dan murah senyumm",  
                "pesan" :"sehat selalu kakk, semangatt"
            },
            {
                "nama"  : "Nadilla Andhara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  :"Metro",
                "alamat": "Kotabaru",
                "hobbi" : "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan" : "seru bangett sama kakak, dan juga ramah",  
                "pesan" :"semangat teruss kakk, jangan lupa istirahatt"
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
            "https://drive.google.com/uc?export=view&id=1QOHtlhhTBERNMzhAw1cmc5FT-4Ug98Ji", #kak dhea
            "https://drive.google.com/uc?export=view&id=1-plmapG9vabrxxyF1UcH1HmdhJKVkW8B", #bg fahrul
            "https://drive.google.com/uc?export=view&id=1BC41kh3dfn5XGRBj7vAaKLpNaceNFKds", #kak berliana
            "https://drive.google.com/uc?export=view&id=1EkVSmqS5UrO27Mae7TlrF7mQmaaFAcfb", #bg jeremia
         
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
                "kesan" : "public speaking kakak bagus bangett, ramah",  
                "pesan" : "semangat kuliahnya kakk, jangan lupa istirahat"
            },
            {
               "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "20",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi" : "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "baik dan humble jugaa",  
                "pesan" : "sukses selalu kakk"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "asik banget apalagi kalo lagi ngobrol",  
                "pesan" : "semoga dilancarkan segala urusannya kakk"
            },
            {
               "nama"  : "Annisa Dini Amalia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "baik banget dan ramah jugaa",  
                "pesan" : "jaga kesehatan kakk,semangat kuliahnya"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450118",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bernungt, Pesawaran",
                "hobbi" : "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan" : "Kakak seru banget dan asik",  
                "pesan" : "semangatt kakk, jangan lupa istirahat"
            },
            {
                "nama"  : "Feryadi Yulius",
                "nim"   : "12240087",
                "umur"  : "20",
                "asal"  : "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi" : "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan" : "abangnya humble",  
                "pesan" : "jaga kesehatan dan semangat kuliahnya bang"
            },
            {
                "nama"  : "Renisha Putri Giyani",
                "nim"   : "12240079",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan" : "kakaknya seru banget dan ramah jugaa",  
                "pesan" : "sukses selalu kakk"
            },
            {
                "nama"  : "Claudhea Angeliani",
                "nim"   : "121450124",
                "umur"  : "21",
                "asal"  : "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan" : "kakaknya baik dan humble",  
                "pesan" : "jaga kesehatan ya kakk, semangatt"
            },
            {
               "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan" : "abangnya seru dan asik",  
                "pesan" :"tetap semangat kuliahnya bangg"
            },
            {
               "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Bengkulu",
                "alamat": "Natar",
                "hobbi" : "Mengumpulkan tugas e-learning h-15 detik",
                "sosmed": "@_.dheamelia",
                "kesan" : "Kakaknya asik dan seru bangettt",  
                "pesan" : "jangan lupa istirahat dan jaga kesehatan kakk"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta",
                "alamat": "Sukarame",
                "hobbi" : "Badminton, melukis, hiking, berenang, dengar musik, minum kopi",
                "sosmed": "@fhrul.pdf",
                "kesan" : "abang seru bangett, dan juga asik kalo diajak ngobrol",  
                "pesan" : "sukses selalu bang!"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "kakaknya seru dan baik ",  
                "pesan" : "semangat terus kak menjalani kuliahnya"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Billabong",
                "hobbi" : "Memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan" : "abang seru dan lucu juga",  
                "pesan" : "Semoga dilancarkan perkuliahannya bang"  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hrs5HLSFepgz_fAIQ9MzheH0wPiztKPa", #kak luthfia
            "https://drive.google.com/uc?export=view&id=1exfXYVpIUA0X3c_kusDUTNr_iWLLua3s", #bg bintang

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
                "kesan": " menginspirasi banget kakaknya dan asik jugaa",  
                "pesan":"semangat kuliahnya kak,jangan lupa istirahat"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfi nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "asik dan seru banget kalo diajak ngobrol ",  
                "pesan":"sukses selalu perkuliahannya, bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Afj552XC7kMclGFcSp8HqJvN0VrgiiDS", #bg ericson
            "https://drive.google.com/uc?export=view&id=1AbVQmRqxYGkvELvOlwiyDWviGFjPbSbw", #kak abet
            "https://drive.google.com/uc?export=view&id=1B-miHePJx_sulrWw7jzS5AngkbpS4RQj", #kak nisrina
            "https://drive.google.com/uc?export=view&id=1ApJfwL_IslnP93WmbVUcwYDKCYKjuovM", #kak allya
            "https://drive.google.com/uc?export=view&id=1A_Y16_gsPUG3y7RuU0zshlwD7PPaoeM5", #kak eksanty
            "https://drive.google.com/uc?export=view&id=1Axe3yM1U1K5-Dt_ql39mYKrK-woe8iDH", #kak hanum
            "https://drive.google.com/uc?export=view&id=1A8DaKjyDrUuFwF17sv013MM7D1jsYJqA", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1AtriuyLHT2xh_mbgKJRbyUJUepoIJHtI", #bg deri
            "https://drive.google.com/uc?export=view&id=1Tq-bBT74tnRZfaVawMCC0lyEmbG0LgOZ", #kak okta
            "https://drive.google.com/uc?export=view&id=1Aji-xVxpp1UGZFBsFgb9VsthRwDXeyA6", #bg deyvan
            "https://drive.google.com/uc?export=view&id=1AoKAvo9IkanZeiEKzTy4-qhpuG8kbUYb", #bg jonathan
            "https://drive.google.com/uc?export=view&id=1AoYy15K7_YcH4a8H8sbJsbzaxyLuIbLw", #bg kemas
            "https://drive.google.com/uc?export=view&id=1AcNbwrlJtvnx4Gvha-k0GeoXidEXLAlo", #kak presilia
            "https://drive.google.com/uc?export=view&id=1AhgDmGphXX_DyOtCMjp3J4UsZRP6ivez", #kak rafa
            "https://drive.google.com/uc?export=view&id=1AkxEsrQloQANGpB4Kl5eNePEcHbU6c-U", #bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak vanesa
            "https://drive.google.com/uc?export=view&id=1x49qv8rQJyWGxE8-As3GDCPwqWCChyVj", #bg farhan
            "https://drive.google.com/uc?export=view&id=1dPBw_J7sxUSHmPwFxcAAvILlOkLqKN83", #kak gede
            "https://drive.google.com/uc?export=view&id=1APWCzmOJqLiaCmQ5K5m0Pcdbrncd5-jg", #kak jaclin
            "https://drive.google.com/uc?export=view&id=11AXkD1PIJ3EvgHbbmY4ydjARNX5ncEFYw", #bg rafly
            "https://drive.google.com/uc?export=view&id=1H85PuHSdaRww6DZ-tE5-ss5WewZ3hU2g", #kak andini
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
                "kesan": "abang asiik dan juga humble",  
                "pesan":"sukses selalu bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak", 
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "ramah bangett",  
                "pesan":"semangat kuliahnya kakk"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame ",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "asik dan baikk",  
                "pesan":"jaga kesehatan kakk, semangatt"
            },
            {
                "nama": "Allya Nurul Islami Pasha",  
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Ngukur Lampung",
                "sosmed": "@allyaislami_ ",
                "kesan": "asik dan seruu",  
                "pesan":"jaga kesehatan kak, jangan lupa istirahat"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty", 
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Raajabasa",
                "hobbi": "Nitip Shalat",
                "sosmed": " @eksantyfebriana",
                "kesan": "baik dan seru banget",  
                "pesan":"sukses selalu kakk"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah", 
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "humble dan murah senyum",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho", 
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pangeran senopati raya, gerbang barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya baik bangett dan juga ramah",  
                "pesan":"semoga diperlancarkan segala urusannya,bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "abang seruu dan juga asikk banget",  
                "pesan":"jangan lupa istirahat,bang. semangat kuliahnya" 
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@oktavianrwnda",
                "kesan": "asik dan humble juga",  
                "pesan":"sukses selalu kakk, jaga kesehatan juga" 
            },
            {
                "nama": "Devyan Loxefal", 
                "nim": "121450128",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "seru dan asik bangett",  
                "pesan":"semoga kuliahnya lancar, semangat bang" 
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "asik dan ramah juga",  
                "pesan":"semangat terus bang!" 
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "asik banget, tapi pas praktikum rada ngeselin terkadang",  
                "pesan": "sehat selalu bang, semangat kuliahnya" 
            },
            {
                "nama": "Presilia", 
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": "baik bangett dan juga ramahh",  
                "pesan":"semoga diperlancar kuliahnya kakk" 
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "humble dan seruu",  
                "pesan":"jangan lupa istirahat kakk, semangat!" 
            },
            {
                "nama": "Sahid Maulana", 
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "asik banget dan juga baikk",  
                "pesan":"jaga kesehatan bang, semangat kuliahnya" 
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "kakaknya asik dan juga ramah",  
                "pesan":"semangat kakk kuliahnya, sehat sehat selaluu" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "humble dan juga asikk",  
                "pesan":"jaga kesehatan bang, sehat selalu" 
            },
            {
                "nama": "Gede Moana", 
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "baik dan seruu",  
                "pesan":"jangan lupa istirahat kakk" 
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "ramah dan baik sekali",  
                "pesan":"jaga kesehatan dan tetap semamgatt" 
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "seru dan humble",  
                "pesan":"semangat kuliahnya, bangg" 
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "humble banget",  
                "pesan":"jangan lupa istirahat dan jaga kesehatan kak" 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14tQ-VmavQJP-BlIZ2GIa-8f2PTSWoXfH",
            "https://drive.google.com/uc?export=view&id=1NJO32xu4_DdZEtRMVB9QvluTwG9s97dK",
            "https://drive.google.com/uc?export=view&id=1GuU9IBjslmcxE-n9H8Q5lRYYC5ZFYmA7",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=19ECF7s0_-LRRD72_ViB9MNvNle5lB2Zo",
            "https://drive.google.com/uc?export=view&id=1UPv-1q4rf8SpaoVMENotsMTIZZPIyijv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1FBnOL4MkFoqUxHTTtd4vrb5ktjYS7lHC", #bg anwar
            "https://drive.google.com/uc?export=view&id=1vFeOz9VdvNAgIiBtLIGa6tNKlGfHAaAH",
            "https://drive.google.com/uc?export=view&id=1ZF11zTPmbkuR8QcbLvSPQtCIDXOnYhvu", #kak dinda
            "https://drive.google.com/uc?export=view&id=1c6qM44bTmjTq3IpRSrbwR9DzFN09FKH8",
            "https://drive.google.com/uc?export=view&id=1yklYd4MJvND9svJbhYO6yI5aWIblR3G8",
            "https://drive.google.com/uc?export=view&id=18Fj7Tn1ua2RmTvHx_a8G7O6MBpsmjPDM",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=19ceYplv3wZVEOX-VsOfOhhtn7BOvXnY5",
            "https://drive.google.com/uc?export=view&id=1dAsntwqwt_VCrAdHGMQI0pIErW-RrE-3",
            "https://drive.google.com/uc?export=view&id=1jAPE5P5sVhuwFrxcITOtUC_VVpahOHZ8",
            "https://drive.google.com/uc?export=view&id=15xcgpFyWpGcNBMKuzN4L2vFn1SRe1dDO",
            "https://drive.google.com/uc?export=view&id=1gucmZ6BBZaXTyz3PIgl_JfLgXRIgZtix",
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
                "kesan": "abangnya seru dan baik",  
                "pesan":"sukses selalu  bang!" 
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakaknya humble banget",  
                "pesan":"semangatt kakk kuliahnya,jangan lupa jaga kesehatan" 
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
                "kesan": "baik dan ramah",  
                "pesan":"Semangat bang kuliahnya" 
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya seru dan ramahh bangett",  
                "pesan":"jaga kesehatan bang,semangatt" 
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "menginspirasi banget dan baik juga",  
                "pesan":"sukses selalu bang, semangat kuliahnya" 
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "baik sekali dan asik jugaa",  
                "pesan":"jangan lupa jaga kesehatan kakk, semangatt" 
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "baik dan juga asik",  
                "pesan":"semangat kuliahnya bangg"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "informatif banget dan juga baik",  
                "pesan":"sehat selalu dan semoga diperlancarkan segala urusannya" 
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "humble dan baikk",  
                "pesan":"jaga kesehatan dan semangat kakk" 
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": " ",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak seru banget dan asik",  
                "pesan":" semangat terus kuliahnya ya kak!" 
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "keren banget dan menginspirasi",  
                "pesan":"jaga kesehatan kakk, semangat teruss" 
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakak baik dan ramah jugaa",  
                "pesan":"semangat kuliahnya kakk" 
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "ramah dan murah senyum",  
                "pesan":"jangan lupa istirahat dan jaga kesehatan kak" 
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "kakaknya baik dan humble",  
                "pesan":"jaga kesehatan dan semangat kakk" 
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya seru dan asik",  
                "pesan":"tetap semangat kuliahnya bang" 
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abangnya seru dan baik ",  
                "pesan":"Jaga kesehatan ya, bang" 
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "asik banget dan seru jugaa",  
                "pesan":"jaga kesehatan kakk" 
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "asik dan ramah",  
                "pesan":"semangat kuliahnya bang" 
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya baik, trus kalo ngasih materi juga dijelaskan dengan baik",  
                "pesan":"semangat terus kuliahnya bang, dan kesehatannya juga dijaga"
            },
            {
                "nama": "Vita Anggraini",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "baik, trus kalo ngasih materi juga dijelaskan dengan baik",  
                "pesan":"sehat selalu dan dimudahkan segala urusannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vSC1agdyRnFEAo-MpxMnE4SOa4J5QhkN",
            "https://drive.google.com/uc?export=view&id=18zotOUB5TcIJGdu3OhpWm18H4JJF17XM",
            "https://drive.google.com/uc?export=view&id=1NuCzVWDmmS-P3R7S7xTWptzxrxY-BQqb",
            "https://drive.google.com/uc?export=view&id=1PzM55GH3UjzAsuXCjmsKZYqy3pFJzrhv",
            "https://drive.google.com/uc?export=view&id=14DWo11S2baZaOwzVlbKdRZXGvlz_zwIr",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #
            "https://drive.google.com/uc?export=view&id=1Ac6cSNJrhE66N3JJPJrWrPYqxEFusBHz",
            "https://drive.google.com/uc?export=view&id=1TOV3tMRQ6q6e3DKhvgXQsu3wom0dvLXQ",
            "https://drive.google.com/uc?export=view&id=19K2MuNa_h93FwoRofF_ELpi9XjdIrPLT",
            "https://drive.google.com/uc?export=view&id=1qwLCyfYafqrsSgRs3NSW7kWcn9KLvyOb",
            "https://drive.google.com/uc?export=view&id=1wmJxVqb04wERceLNTUQMdhma4370kbRu",
            "https://drive.google.com/uc?export=view&id=1fOJ9RL0804_J_I6X9pbgQsdzUBr0u_w4",
            "https://drive.google.com/uc?export=view&id=19K_NqN4a_kCkOfyKqHAT22IOc-5ZIrI2",
            "https://drive.google.com/uc?export=view&id=1BZgGEFvpZhqEbxDxeVcVXS6KHLvEMCoh",
            "https://drive.google.com/uc?export=view&id=1lU7eXBw2bH0OjNC8SDV52qt_zRYRoeod",
            "https://drive.google.com/uc?export=view&id=1Os-01sGWERNNYr4W7Ux4zw4mJChot_nB",
            "https://drive.google.com/uc?export=view&id=19QIbgr_yeeMFEKuFghonnQcPt_r5fa2w",
            "https://drive.google.com/uc?export=view&id=19W4-9hiAu1Xd0qJNRng4N_ySGbIiY_SP",
            "https://drive.google.com/uc?export=view&id=1IAHVVHsPKLbQlqJZ4eU7cvpDaFHOIepw",
            "https://drive.google.com/uc?export=view&id=1E9dzjnqcUe4qFALIsPIFMUSF9QMJDTdC",
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
                "kesan": "seru dan asik banget",  
                "pesan":"semangat kuliahnya bang, jangan lupa istirahat"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "ramah dan seru banget",  
                "pesan":"sukses selalu perkuliahannya"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "ramah dan asik",  
                "pesan":"semoga dilancarkan segala urusannya kakk"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "seru dan baik",  
                "pesan": "sukses selalu dan jaga kesehatan bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "ramah dan baik banget",  
                "pesan": "jaga kesehatan ya kakk, semangatt"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Belwis",
                "hobi": "Surving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "humble dan seru abiss",  
                "pesan": "semoga dilancarkan kuliahnya kakk"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan Seribu",
                "alamat": "Way Halim",
                "hobi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "kakaknya asik banget juga ramah",  
                "pesan": "jangan lupa jaga kesehatan ya kakk"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "humble dan ramahh",  
                "pesan": "semoga dilancarkan perkuliahannya kakk"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bnadung",
                "alamat": "Way Kandis",
                "hobi": "Menjahit Baju",
                "sosmed": "@jasminednva",
                "kesan": "baik banget dan ramah jugaa",  
                "pesan": "jaga kesehatan kakk,semangat kuliahnya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "abangnya asik dan seru banget",  
                "pesan": "semoga dilancarkan perkuliahannya dan sehat selalu"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "kakaknya keren banget",  
                "pesan": "jaga kesehatan dan jangan lupa istirahat"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan" : "abangnya seru dan kece abis",  
                "pesan" : "semoga dilancarkan perkuliahannya bang"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan" : "abangnya keren dan seru",  
                "pesan" : "tetap semangatt bang kuliahnya"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "kakaknya asik bangett",  
                "pesan": "sukses selalu kakk, jaga kesehatan dan jangan lupa istirahat"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan" : "asik dan seru banget",  
                "pesan" : "jaga kesehatan kak, semangat kuliahnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya seru dan baik",  
                "pesan": "Tsukses selalu  bang!"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Bertemu anak pengmas",
                "sosmed": "@izzalutfia",
                "kesan" : "sama kak izza seru banget kalo lagi ngobrol",  
                "pesan" : "semangatt kakk kuliahnya,jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "kakaknya humble banget",  
                "pesan" : "jaga kesehatan kakk, semangatt kuliahnya"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan" : "baik dan ramah juga",  
                "pesan" : "Semangat bang kuliahnya"
            },
            {
                "nama"  : "Tria Yunani",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan" : "kakaknya seru dan ramahh bangett",  
                "pesan" : "jaga kesehatan kak,semangatt"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Sq9BmzDwe46ME8PZtZcxK8wxM91_-vGn", #bg dimas
            "https://drive.google.com/uc?export=view&id=1C78zpqJHJjH9oC6UJxbDdfvpp5g3Z44_", 
            "https://drive.google.com/uc?export=view&id=10nUAb7oyD0h4sB6ETBEM3iLa-EIt4vNW",
            "https://drive.google.com/uc?export=view&id=1wd5FjXywPcwfaebGFqx6xoBxNGbKyQNq",
            "https://drive.google.com/uc?export=view&id=1aHGaO4X7JHPiHFa2zwgjmz7EYil4lrLa",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=12TBgwP7IZRUqjdas8paPJmrzB7GvyQgV",
            "https://drive.google.com/uc?export=view&id=1bR6-IiI7f3BX8jBJ0z9l0xoZiZsU307V",
            "https://drive.google.com/uc?export=view&id=1vUwfC59aeXHPERz-IBfZ8aYcWMnWcZg3",
            "https://drive.google.com/uc?export=view&id=1swbZMaQKf34nBJTbHZULBlLcrqQ1QBFP",
            "https://drive.google.com/uc?export=view&id=1_eCja7d8PU7vI330py8ZANYOgazmc7kX",
            "https://drive.google.com/uc?export=view&id=1QMuHUfKm6p9-air6ogwEasOPXczhwfSM",
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
                "kesan": "bang dimas inspiratif banget, keren juga",  
                "pesan":"semangat ngerjain TA nya bang, jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Airan",
                "hobbi": "Membaca Novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "kakaknya seru dan ramah banget",  
                "pesan":"semangatt kakk, jangan lupa istirahat"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam (untung)",
                "hobbi": "Main sepeda ke gunung",
                "sosmed": "@akabar_resdika",
                "kesan": "abangnya keren dan seru abis",  
                "pesan":"semangat kuliahnya bang!"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@ranipu",
                "kesan": "baik sekali dan asik jugaa",  
                "pesan":"jangan lupa jaga kesehatan kakk, semangatt"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari Buah Pisang",
                "sosmed": "@rendraepr",
                "kesan": "bang rendra keren dan seru banget",  
                "pesan":"semangat kuliahnya bang, sukses selalu"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhn_694",
                "kesan": "ramah dan juga baik banget",  
                "pesan":"jaga kesehatan dan semangat kakk"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "seru banget dan informatif",  
                "pesan":"semangat kuliahnya kak dan jaga kesehatan"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": "humble dan ramah",  
                "pesan":"jangan lupa istirahat, bang"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "abangnya ramah dan seru diajak ngobrol",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Joshua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Menonton dan lari",
                "sosmed": "@josuapanggabean16",
                "kesan": "abangnya humble",  
                "pesan":"jangan lupa jaga kesehatan, bang"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@meirasty_",
                "kesan": "seru banget dan ramah jugaa",  
                "pesan":"jangan lupa jaga kesehatan ya kakk"
            },
            {
                "nama":"Rendi Alexander Hutagalung",
                "nim": "121450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "abangnya seru dan asik",  
                "pesan":"jaga kesehatan dan semangat kuliahnya bang"
            },
            {
                "nama":"Azizah Kusuma Putri",
                "nim": "1212450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak seru banget dan asik",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T6YWhhS4MN42LM1TteDlcRBAgyUXqvpZ",
            "https://drive.google.com/uc?export=view&id=1KGWJqIkUox_U0SIEsJRF1VeC2eddVYP8",
            "https://drive.google.com/uc?export=view&id=1rt4dmnjCwogBUWyrsCKUs8eqRu2s3EjZ",
            "https://drive.google.com/uc?export=view&id=14DG-g7n-Nb2aZ5K88aFn_1ZebPlBraf4",
            "https://drive.google.com/uc?export=view&id=1YoaLlONivqFtP6JcmhSopRO_0IucuVs8",
            "https://drive.google.com/uc?export=view&id=1QnbiTT_gRajy_vbcGcfdj2qvJvY1xK8W",
            "https://drive.google.com/uc?export=view&id=1PhqtOZYfARXDGiBWtr8bPT84aylXpfYC",
            "https://drive.google.com/uc?export=view&id=1Bj9RVthtfoknHOK5ruje7nPNXN3xeYmp",
            "https://drive.google.com/uc?export=view&id=1tfIvGIAjuYdlSVDuiC5GizV-qCavc9wy",
            "https://drive.google.com/uc?export=view&id=1K22XbXqxdtb3OTT093zoRLT6h3RrUhtO",
            "https://drive.google.com/uc?export=view&id=1V4jpbNN2jPev1r-S52PZL_BKedviEjck",
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
                "pesan":"jangan lupa istirahat dan semangat"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #
            "https://drive.google.com/uc?export=view&id=1nUk4PVpqeuISXLGhiV1sZDtJfG3W2_YX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=1CaYnpiJnpgCgeyp7IFVGY_jvw4gdE62w", #chintya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #najla
            "https://drive.google.com/uc?export=view&id=1A28XGABl6hRsaK_WCW_UwXVVoG6Jc-Nx", #cia
            "https://drive.google.com/uc?export=view&id=1KVHFSx7DZSEqHe4KDJMEYRIvNlwo0rXQ", #rahma
            "https://drive.google.com/uc?export=view&id=1Us75Qe82xk50zOL43KWKTUlWIUic3-WY", #tri yani
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg kaisar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kk dwi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #wiratna
            "https://drive.google.com/uc?export=view&id=1ivp7zwdfbPWPSK3iyDu2fCh9r9PREcft", #bg gym
            "https://drive.google.com/uc?export=view&id=1tWqwqa4Wrnq5yUPOqKxHspo7QcrNMrCL", #kk nashwa
            "https://drive.google.com/uc?export=view&id=1T1aU37k9vFCpfEKo95iJNtYp-qEXmw-i", #priska
            "https://drive.google.com/uc?export=view&id=1mPGl6XioWv9uN0-RGmykEiw4HhM_eaCi", #arsal
            "https://drive.google.com/uc?export=view&id=1pRDkjf0T65gBfwrkBd-g8wfZNUfONlaM", #abit
            "https://drive.google.com/uc?export=view&id=15iBvukt4Wco70Z7bdpUsuE7w1sxxDTPa", #bg akmal
            "https://drive.google.com/uc?export=view&id=10ByVmjZ2NtnSU1-0SBYyWQp9qpXnr1FC", #bg awan
            "https://drive.google.com/uc?export=view&id=1_8AffwZ4kwyY_pJA7rMj_NrGLXXljR-a", #kak husnun
            
            
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
