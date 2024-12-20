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
            "https://drive.google.com/uc?export=view&id=1cd1vUD4JQ_WgSzMZxFaXTndy-MkhFCIz", # bang gumi
            "https://drive.google.com/uc?export=view&id=10UxWL15C0o56M45tRsUz8765XSb2GXCf", # bang pandra
            "https://drive.google.com/uc?export=view&id=1UJnNpXJk9KLQD0owheULnKZNOucM30YW", # kak melinza
            "https://drive.google.com/uc?export=view&id=1ay9-1LMfY88KdqDoDcwyl8MV9ch2qoUF", # kak maulida
            "https://drive.google.com/uc?export=view&id=1Ec9kbnOViKj0rX6sRmXhs4OfOPWpK7SZ", # kak titi
            "https://drive.google.com/uc?export=view&id=1_Ci5pwAUqLzSq3yc_LOlnZugMYtm_Il4", # kak nadila
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
                "kesan": "Bang gumi lucu banget kalo lagi ceritaa",  
                "pesan": "semoga saya bisa jadi pemandu seperti abang gumi"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang pandra keren asli",  
                "pesan": "sehat selalu bang, sukses dan kami riuhkan!"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "sekretaris hmsd yang keren!",  
                "pesan": "sehat-sehat ya kak, semoga bisa kami riuhkan dengan teman-temannya!"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kak lida asik dan seruu",  
                "pesan": "ajak aku ngobrol soal itera dong kak"
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "kak titi keren tau, kek kharismanya unik gitu",  
                "pesan": "semoga dapat jodoh dan lulus dari itera dengan mudah ya kak!"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "orangnya tegas dan profesional bangett",  
                "pesan": "semoga sukses ya kak dan semoga bisa kami riuhkan!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19AWfT_RwZJgoomIOah3lAs1KnCXlyUIp",#kak Tri
            "https://drive.google.com/uc?export=view&id=1hpLjgFJZscnAlnyVi51hj4wYIctEDJQE",#Kak Annisa
            "https://drive.google.com/uc?export=view&id=1o3-18_m56I74F1Hpd5BFXeVRxzG-Ybos",#Kak Wulan
            "https://drive.google.com/uc?export=view&id=1cdIFl-zVh4Bs-_FNdny38zQqHmWuwQLN",#Kak Anisa Dini 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Claudhea .
            "https://drive.google.com/uc?export=view&id=18phQCp8MbPv1_V3ahtLAbbnk5ouacJMH",#Bg Feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Renisha .
            "https://drive.google.com/uc?export=view&id=1Xjiy3S_3pvg5MWQ8-h0teeiIKKA9WlWh",#Bg Mirzan 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Anisa Fitri .
            "https://drive.google.com/uc?export=view&id=1hPUw2h2C9s3woS68mR0QdFMIHt9js1rL",#Kak Dhea 
            "https://drive.google.com/uc?export=view&id=1138Lxhdg3s3qHG1FAipa4jJpNzv0zJ8t",#Bg Fahrul
            "https://drive.google.com/uc?export=view&id=1qimUJvycTzg9yieFMOlwkcw4BufW28m9",#Kak Berliana 
            "https://drive.google.com/uc?export=view&id=1tL7ickfswEb6Ge6ooxtFqOgtg_jbnO4L",#Bg Jere
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
                "kesan": "saya suka sama vibes nya kak nia, seru, humble, lucu cakepp",  
                "pesan": "semoga saya bisa hadir di sempro kakak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kalem tapi keren, aura baleg nya ada banget",  
                "pesan": "tolong ajarin teman saya namanya ridho ya kak!"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "18",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "kak wulan tinggi banget",  
                "pesan": "next kita foto lagi ya kak"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "saya masih bingung bedain kak anisa yang lain",  
                "pesan": "maaf ya kak kalo saya ga hapal nama kakak baleg yang anisa :("
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "saya merasa ga enak karna waktu wwc motor kakak ilang...",  
                "pesan": "untung ketemu ya kak, lain kali lebih hati-hati yaa"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "kak fery sigma banget, kalem, cool, dinginn",  
                "pesan": "jangan demis ya bangg"
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengar musik ",
                "sosmed": "@fleurnsh",
                "kesan": "kakaknya diem diem aja waktu wawancaraa",  
                "pesan": "semangat kerjanya kak"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "bang mirzan mirip kak egi",  
                "pesan": "abang jangan demis pokoknya!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "seruuu",  
                "pesan": "semangat kuuliahnya jangan malas kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "120",
                "asal": "Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@myrrinn",
                "kesan": "kak dhea lucu banget waktu wwc, asik dan menghibur kamii",  
                "pesan": "semoga dilancarkan segala urusan dan jangan demis kak!"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "bang fahrul saya kira abang prodi elektro",  
                "pesan": "next kita foto lagi bang saat abang wisuda!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "kalem banget",  
                "pesan": "ikut nimbrung ya kak, jangan demis jugaa"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "keren dan asikk",  
                "pesan": "jangan demis bang plis"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O7NYaUg0mfAq-SNl9vtxJHJckmUmsTpK",
            "https://drive.google.com/uc?export=view&id=1aJlMt7gsmsitfFvbzSpsgOYJibRjwRpK",
        ]
        data_list = [
            {
                "nama": "Anissa Lutfia Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "saya suka cara kakak publik speaking",  
                "pesan": "ayo kita ngobrol yang banyak kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfi nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Keren manajemen waktu dan kepemimpinannya!",  
                "pesan": "Semoga saya bisa menjadi seperti bang bintang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I1TKRx-BO7xQWHsb87ppXkhchz1ubmja",# bg econ
            "https://drive.google.com/uc?export=view&id=1HRZGuf773sCV1zTtbxuGdGVO2d2kvOhO",# kak abeth
            "https://drive.google.com/uc?export=view&id=1IUcWbDtM-eAOYFAV5C1lni_CSDg6AvZ5",# kak afifah
            "https://drive.google.com/uc?export=view&id=1IAPiNeeA27cV2wqaP14eZ0Qm7BtZPdOQ",# kak aliya
            "https://drive.google.com/uc?export=view&id=1HseY-UYnWuPk9ppmqoOXzV91qu-5rYXo",# kak eksanty
            "https://drive.google.com/uc?export=view&id=1IR3VJ4dNuDhJR7fbA63hNMI8XMfldpL5",# kak hanum
            "https://drive.google.com/uc?export=view&id=1ncbwDDIJ7l7hGrw68FDmQrFtosEKgdrm",# bg ferdy
            "https://drive.google.com/uc?export=view&id=1IDltliWG_CyvUYj7M3dJlFa85tiXKB0w",# bg deri
            "https://drive.google.com/uc?export=view&id=1np3SSOnDL6NKIWcymdQPMxuWo25rwIre",# kak oktav
            "https://drive.google.com/uc?export=view&id=1HbaFfZXvGemhHaBVjq17MK_N-TaelPLy",# bg depan
            "https://drive.google.com/uc?export=view&id=1HRdQ5NXv3xBQeRjVU3BqiUy_KjOJdMTN",# bg jo
            "https://drive.google.com/uc?export=view&id=1HaEGu2CVuZQXHUt9iaT2USGfQezmsKJK",# bg kemas
            "https://drive.google.com/uc?export=view&id=1Hylsx1zL4gC6X3K3wRldhSlZ78tn-Q4H",# kak lili
            "https://drive.google.com/uc?export=view&id=1I23yiRTlScVgYL1V-MP4KWGuEkmFivMs",# kak rafa
            "https://drive.google.com/uc?export=view&id=1HUp1mfRUtlbr7P8QSpRds_A9RBMIr8I2",# bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1o1bCt7WTlrRSTs8CsLnGFOFvOOLo3h3p",# bg ateng
            "https://drive.google.com/uc?export=view&id=1o5lmDMv0g12zV4ErDSoZ47-6HrInrUtU",# bg gede
            "https://drive.google.com/uc?export=view&id=1oMbx7MBmnbO2y3Qve2-xzTWMi30LGVhs",# kak jaclin
            "https://drive.google.com/uc?export=view&id=1okDeu2WtZVsrT0_HUSnhbHkUnM-K7zhK",# bg rafly
            "https://drive.google.com/uc?export=view&id=1oVS9PjDUV6b-71vCpRelafv2ST3Qb_jI",# kak andini
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Kobam",
                "hobbi": "jalan-jalan",
                "sosmed": "@ericsonchandra99",
                "kesan": "sangar tapi baik dan merangkul adik-adiknya",  
                "pesan": "semoga tahun depan saya bisa hadir di sempro abang yah"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "kemiling",
                "hobbi": "Tertawa",
                "sosmed": "@celisabethh_",
                "kesan": "asik tapi ternyata galak juga kadang",  
                "pesan": "semoga langgeng ya sama bang jo"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "beauty and the beast",  
                "pesan": "semangat kuliah dan organisasinya kak, next saya ambil estafetnya!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "asik, baik, hatinya mungil tapi jadi komdis yang profesional. Rispek!",  
                "pesan": "jangan dipikirin pandangan orang ya kak, bnyk yg benci kakak tapi saya tidak akan."
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "elegan, saya suka gayanya",  
                "pesan": "tetep jadi elegan dan cantik yahh"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "gemes namanya, kak anumm",  
                "pesan": "semoga dipertemukan jodoh yang kaya raya!"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "diam-diam tapi sangar juga dipikir-pikir",  
                "pesan": "yok bang jadi kadep, lalu saya estafet!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "korlap banget auranya",  
                "pesan": "abang jangan demis bangg"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "pendiem bangett",  
                "pesan": "semoga dilancarkan kuliahnya kak wenda!"
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "bang depan lucu banget sumpah komedian alami!",  
                "pesan": "semoga bang depan bisa di riuhkan dengan teman-temannya!"
            },
            {
                "nama": "Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "langsung rispek pertama kali ketemu di wardat",  
                "pesan": "makasih bang jo sudah memberi wejangan, semoga langgeng sama kak abet!"
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "bang kemas saya kira dari mikfes ternyata...",  
                "pesan": "ayo bang kita belajar bareng!"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presiliang",
                "kesan": "kak lili cantik banget woi",  
                "pesan": "semoga dapet jodoh yang setara yah!"
            },
            {
                "nama": "Rafa Aqila Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kek ada auranya gitu, tapi gtau apa...",  
                "pesan": "lanjut psda lagi ya kak, jangan demis!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl Airan Raya",
                "hobbi": "Dengerin MCR",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid baik banget ya ampun",  
                "pesan": "makasih ya bang udah baik ke saya, semoga saya bisa jadi orang baik!"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "tidak terwawancarai",
                "pesan": "-", 
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "tidak terwawancarai",  
                "pesan": "-"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "bang ateng baik banget, sangat mengayomi adik-adiknya!",  
                "pesan": "semoga abang sehat selalu dan bisa di riuhkan oleh kami bang!"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kopri Raya",
                "hobbi": "Belajar dan Main game",
                "sosmed": "@gedemoenaa",
                "kesan": "saya kira julukan aja gede, ternyata nama aslinya",  
                "pesan": "ayo kita mabar bang!"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumsel",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinacv_",
                "kesan": "kak jaclin elegan cakep cui, namanya juga keren",  
                "pesan": "jangan demis ya kak, saya mau kerja sama kakak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "saya kira abang bukan bph karna sekelas ads",  
                "pesan": "jangan demis bang plis, ayo kita lanjutkan psda!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kak andini baik udah bantuin saya lomba io billiard",  
                "pesan": "saya belum liat kembaran kakak :("
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f8vniOCSPquxdw6YLwHnxhSHwBLLM5vV", #Bg Rafi
            "https://drive.google.com/uc?export=view&id=1fh-3OMDd1aPsme7yM2kjHwwCnRgCkdlI", #Kak Annisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Mujadid
            "https://drive.google.com/uc?export=view&id=1LGfnP0yvrwXtgitYCur8wW33SqvWzXXf", #Bg Ahmad Sahidin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Fadhil
            "https://drive.google.com/uc?export=view&id=1nb5J2k9DXQQp1s5eBFd6cOd2pBKEkJog", #Bg Regi
            "https://drive.google.com/uc?export=view&id=11wf6573_FIkx7wKV5_3pyJxis_A--WTV", #Kak Syalaisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Natanael
            "https://drive.google.com/uc?export=view&id=1acXpN4XLxJ23kjkfBi2EhR-8sQP1iEOP", #Bg Anwar
            "https://drive.google.com/uc?export=view&id=1gn4XQXkEcYivbBniH-goLBs1ni-W4FSY", #Kak Deva
            "https://drive.google.com/uc?export=view&id=1ldGOLTYq2qZJZINjNAHJ-7yK7UuQ8UL8", #Kak Dinda
            "https://drive.google.com/uc?export=view&id=1dnSNZOqkm2amg1aCXAC-ZxlZgoU3OyWB", #Kak Marleta
            "https://drive.google.com/uc?export=view&id=1238Yh9fk0WaTKHrnhblY3VWWbNVjFxRT", #Kak Rut Junita
            "https://drive.google.com/uc?export=view&id=1bS4f4p1jIGE1uAon9CTOQ971NXsyKfBk", #Kak Syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Abdurrahman
            "https://drive.google.com/uc?export=view&id=1zh3x4BUGyvLlMRitAfMiIm0dV07aEKRs", #Bg Aditya
            "https://drive.google.com/uc?export=view&id=1y_fNEChoaBWsWKPfsVsGBaWLvcmdDU71", #Bg Eggi
            "https://drive.google.com/uc?export=view&id=1-iWTnwODtKfMHZlR1wTty1lnpZ0IZ2Hi", #Kak Febiya
            "https://drive.google.com/uc?export=view&id=12A2aBdlrAXsnQSmn9gE4xn3dS9N2761n", #Bg Happy
            "https://drive.google.com/uc?export=view&id=1y2vC0_VRCBKZYo6tMVpT6V-7pIvbvYYD", #Bg Randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Vita
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "abang keren kepikiran buat buting ini untuk kami, makasih bang!",  
                "pesan": "semoga abang bisa dapet kerjaan yang keren juga!"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "cantikk imutt gemes",  
                "pesan": "semoga sehat selalu kakk"
            },
            {
                "nama": "Mujajid Choirus Surya",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "tidak terwawancarai", # non-wwc
                "pesan": "-"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya kalem tapi keren tegas calon kahim",  
                "pesan": "ayo bang main voli"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "tidak terwawancarai",
                "pesan": "-", 
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "keren, saya kira bukan dari mikfes",  
                "pesan": "jangan demis ya bang pliss"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "kembar ternyata sama kak andini psda",  
                "pesan": "next kita foto bareng sama kak andini ya kakk"
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "tidak terwawancarai",
                "pesan": "-", 
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "bang anwar pendiem banget, saya awalnya gatau ternyata abang pj tugas kelompok kami",  
                "pesan": "jangan diem-diem ya bang"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "kak deva cantik anggunn",  
                "pesan": "next kita foto lebih imut lagi ya kak sayanya hehe"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari bu mika",
                "sosmed": "@dindanababan_",
                "kesan": "saya kira kakak psda soalnya timekeeper materi",  
                "pesan": "semangat kak jangan demis dlu yaa"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kak eta cantik bangett",  
                "pesan": "next kita foto lagi kak pose love hehe"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya pendiem",  
                "pesan": "semoga kita bisa ngobrol banyak ya kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kak puspa imut banget mungil",  
                "pesan": "jangan demis dlu ya kak, ayo kita kerja bareng" 
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "tidak terwawancarai",
                "pesan": "-", 
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "bang adit ganteng putih banget cuy",  
                "pesan": "jangan panas-panas yak bang" 
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "pinter banget codingan nya sumpah",  
                "pesan": "semoga kita bisa belajar bareng ya bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kak feby cantikk mirip feby jugaa",  
                "pesan": "semoga dilancarkan kuliahnya ya kak, jangan demiss"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "jarang banget keliatan bang hapy",  
                "pesan": "sering muncul ya bang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "bang randa dari jauh keren loh",  
                "pesan": "jangan demis ya bang tetep lanjutkan biru emas kita"
            },
            {
                "nama": "Vita Anggraini",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "tidak terwawancarai", # non-wwc
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13_W5cc3j97Smb8Rx9_kb8BDkyDv2OxwD", #Bg Yogi
            "https://drive.google.com/uc?export=view&id=12gLrX3nXgRVTJB2R_bUMaSXDu8yL3tev", #Kak Ramadhita
            "https://drive.google.com/uc?export=view&id=1Z2Ncx6iVgrPA4S66ll7DFwZpgaWosZ52", #Kak Nazwa
            "https://drive.google.com/uc?export=view&id=1IF78Tq3ZAILZFJztVlynUew_1DtYHtVF", #Bg Bastian
            "https://drive.google.com/uc?export=view&id=155mv3kk1s5ayFr2swKWXItm5Jy8Ye1oH", #Kak Dea
            "https://drive.google.com/uc?export=view&id=1ClE12-K7-xbUvE1Mp-qo8D6-oAUcche7", #Kak Esteria
            "https://drive.google.com/uc?export=view&id=13yf3vmIUbbqAal7tuIBwKf0egscjK1f_", #Kak Natasya
            "https://drive.google.com/uc?export=view&id=1Z_Ts_oZc8uyy4bnAmHAXbCpJ4jXA1oGk", #Kak Novella
            "https://drive.google.com/uc?export=view&id=1Zc8U_7-0KGSx_CgNU0AP_froi_nmYmRS", #Kak Jasmine
            "https://drive.google.com/uc?export=view&id=1Y04Xy-lc3gC39T-mRmZXL_xzDFgzgVil", #Bg Tobias
            "https://drive.google.com/uc?export=view&id=1N1DTqIvZGv9snIkTMzS2LlSKmjxDgtPP", #Kak Yohana
            "https://drive.google.com/uc?export=view&id=1_24Yt7ymhu_gwbRU8R8TPfI4D5exFtVw", #Bg Rizki
            "https://drive.google.com/uc?export=view&id=1Y9UtC4ACmeR3ZBZeFW53xm4l-6IZEdDL", #Bg Arifa
            "https://drive.google.com/uc?export=view&id=1b8b5b3qA9BNDaJ74Yc-iJr8FW2EPIA2M", #Kak Uyi
            "https://drive.google.com/uc?export=view&id=1YCaIzh1zOVSIM978QyyzVBD10qkGAN_z", #Kak Chalifia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Irvan
            "https://drive.google.com/uc?export=view&id=17-bY6A9a9fNOsVV0_vXu1L2IpOhyy7Ym", #Kak Izza
            "https://drive.google.com/uc?export=view&id=16kMBd4gxXrkApZ5RTbnL3U3yUIK7mSBZ", #Kak Khaalishah
            "https://drive.google.com/uc?export=view&id=1J8HtoJSZbswa67wizM5tqnJVqi8zl-fB", #Bg Raid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Tria
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Nyari solar",
                "sosmed": "@yogyst",
                "kesan": "bang yogi asik tapi tegas",  
                "pesan": "infokan magang bang plis"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kak rama juga tegas orangnya",  
                "pesan": "semoga dilancarkan dan bisa kami diriuhkan ya kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kandis ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "awalnya jutek tapi asik banget ternyata",  
                "pesan": "kakak juga semoga dilancarkan ya, jangan jutek kakk"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "pernah ketemu waktu projek pak ardika",  
                "pesan": "kita projek lagi ntar ya bangg"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "kak dea mungil banget",  
                "pesan": "sehat-sehat ya kakk"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "namanya keren banget baru pertama kali dngerr",  
                "pesan": "hati-hati ya kak, banyak pencurian motor akhir2 ini"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "kak natasya cantikk elegann",  
                "pesan": "sehat selalu ya kak jangan demis duluu"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kak dinda cantik dan tinggi bangett, asprak sayaa",  
                "pesan": "jangan demis dlu kak plis saya mau kerja bareng kakak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "kak keisha juga cantikk berkharismaa",  
                "pesan": "hati-hati dijalan ya kakk takut kesandung"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "ganteng banget namanya juga kerenn",  
                "pesan": "semoga kita bisa kerja bareng di himpunan ya bangg"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "galak banget waktu jadi komdis tapi diluar itu baik bangett",  
                "pesan": "jangan demis ya kak saya masih mau lihat kakak di kepanitiaan hmsd"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "bang rizki kaya oppa koreaa",  
                "pesan": "jadii BA hmsd gasih bangg"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abang mirip bang ahmad ssd tau",  
                "pesan": "sehat terus ya bang jangan demis dulu"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "saya suka kak uyi namanya unikk lucuu",  
                "pesan": "jaga kesehatan ya kak, kakak IM kann"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "mirip kak khusnun",  
                "pesan": "hati-hati di jalan ya kak, sehat selaluu"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "gede banget kak irvan sigmaa",
                "pesan": "hati-hati dijalan ya bang bnyk begal di sukarame"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "asik banget kak izza, vibes ekstrovert ny kerasa banaget",  
                "pesan": "ntar kita projek lagi ya kak, jangan demis duluu!"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "cantikk gemeshh",  
                "pesan": "semangat ya kak kuliahnya!"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "mirip bang adrian ssd",  
                "pesan": "jadi asprak kami dong bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": " tidak terwawancarai", #non-wwc  
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xBj_MBINd4_WQN_UkFMMMs3JULDHliTD", #Bg Dimas
            "https://drive.google.com/uc?export=view&id=1lK8RSTv-aZ5mf0wqHvYp_BKt6Ehe5Oou", #Kak Catherine
            "https://drive.google.com/uc?export=view&id=1ydmZOxPXkY9prue1LcGgNhOfwPyjv-4W", #Bg Akbar
            "https://drive.google.com/uc?export=view&id=1nUerNlDlMVmf069gfvWorlIR25pUhDPR", #Kak Rani
            "https://drive.google.com/uc?export=view&id=1lgVDLT90-cHF0z_32LC7H0cnwp-x_g__", #Bg Rendra
            "https://drive.google.com/uc?export=view&id=1s2p07W4h9TxTt4Z3k8yXST9Ak95MZn0j", #Kak Salwa
            "https://drive.google.com/uc?export=view&id=1m7Jf4MbpKYgQxpiy59r8rzacii2FiEnz", #Bg Yosia
            "https://drive.google.com/uc?export=view&id=1lCREZl-OcoDkht4VN_M5XOzIW46m87X4", #Bg Sigit
            "https://drive.google.com/uc?export=view&id=1TwAJw93SXCrrWOEiJH4NfSNhVd03f4px", #Kak Azizah
            "https://drive.google.com/uc?export=view&id=13DUTfvwwFj-ZSobye2s00yDrrR0rfr4E", #Kak Meira
            "https://drive.google.com/uc?export=view&id=1QvoTPY0rmtITNuiIWkM-PUJ4ENZpiCkJ", #Bg Rendi
            "https://drive.google.com/uc?export=view&id=1sav7deq-OMGp-73shXQNAx12p-5VJ5VK", #Kak Renta
            "https://drive.google.com/uc?export=view&id=1taC2O1HNW-zVyQghaNZl8WYdja1IlEI5", #Bg Josua
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "menunggu ayam jantan bertelur",
                "sosmed": "@dimzrky_",
                "kesan": "sibuk banget coy",  
                "pesan": "semoga saya bisa jadi seperti bang dimas"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "cakepp imut, ketebak kristennya",  
                "pesan": "next saya mau jadi panitia natal kak"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "masyaallah sangat alim",  
                "pesan": "ntar solat bareng lagi ya bang"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@ranipu",
                "kesan": "mirip kak yohana",  
                "pesan": "jangan galak galak ya kak"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari Buah Pisang",
                "sosmed": "@rendraepr",
                "kesan": "filosofis banget",  
                "pesan": "semangat jadi ketuplak riuhnya bang saya dukung jadi kahim"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "pendiem tapi asik",  
                "pesan": "next kita nonton bareng internal kak"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": "keren abangnya internal banget",  
                "pesan": "semoga kami bisa riuhkan abang dengan bangga"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "abangnya unik tegas ada auranya gitu",  
                "pesan": "next rohani kami ramaikan bang!"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "baru ini ketemu yang hobi nya berkebuun",  
                "pesan": "semangat berkebunnya kakk"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@meirasty_",
                "kesan": "kakaknya baik, pendiem, lucu, masyaallah",  
                "pesan": "next rohani bakal jadi rame ya kak!"
            },
            {
                "nama":"Rendi Alexander Hutagalung",
                "nim": "121450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "pendiem",  
                "pesan": "semangat bang"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "keliatan kakaknya pendiem tapi berhati baikk",  
                "pesan": "jangan diam-diam terus ya kakk"
            },
            {
                "nama": "Joshua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Menonton dan lari",
                "sosmed": "@josuapanggabean16",
                "kesan": "batak banget",  
                "pesan": "makasih bang udah jadi asprak saya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n978aJvH3MO6O7i6WWuESs6EbeqDEeGf", #Bg Adrian
            "https://drive.google.com/uc?export=view&id=1mF0toPXZcvtqprzN7VpikBBFP_I2D8Vu", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1huaaHEOPgYufRqMssY4yY0VGI8Qnco3D", #Kak Nabila
            "https://drive.google.com/uc?export=view&id=1j9k2OoLVzbE1gELtitYeYRWrpGBXHfI7", #Bg Ahmad
            "https://drive.google.com/uc?export=view&id=1KCcp5q4_t5BfvuHbe5lQu2TaZm3pqSb8", #Bg Danang
            "https://drive.google.com/uc?export=view&id=1CDXTxs2oRWBqxTVYzPqRBYfrEx9c8TFb", #Bg Farrel
            "https://drive.google.com/uc?export=view&id=1hviN7krPzMZ49meWpa6Go5ECRJkGjMgS", #Kak Tessa
            "https://drive.google.com/uc?export=view&id=1hajF0rnpDv66CQLP33BWfkIYk-4RRWoV", #Kak Nabilah
            "https://drive.google.com/uc?export=view&id=1mrY18xNXlqODAau40SLGvEWKmHYvcsc4", #Kak Aliva
            "https://drive.google.com/uc?export=view&id=1n-e-iWhqX3QRktIW4OdKhFDRn8vUCiMz", #Bg Dhafin
            "https://drive.google.com/uc?export=view&id=1XCmQZISp9PgT_TdpFmpfwSGh7LniM68i", #Kak Elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Sidikalang",
                "alamat": "Dekat penjara lapas",
                "hobbi": "Nyari-Nyari Hobi",
                "sosmed": "@andriangaol",
                "kesan": "suaranya berat, keren",  
                "pesan": "abang jangan sibuk sibuk kali la bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "cakepp namanya juga unik baru dnger",  
                "pesan": "next kita nnton bareng kak hehe"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "cakeppp jugaa",  
                "pesan": "semangat kuliah s2 nya kak aamiin"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "tinggi banget ternyata",  
                "pesan": "semangat jadi panitia nya bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "dananghk_",
                "kesan": "banyak ilmunya",  
                "pesan": "makasih bang udah jadi pemateri kami"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "gede banget bang parel",  
                "pesan": "semoga badan saya bisa jadi kaya abang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "saya kira kakak internal", 
                "pesan": "semaangat jadi panitia nya ya kak jangan demis juga"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kakaknya cakepp, ga nyangka di ssd",  
                "pesan": "sehat-sehat ya kak, next kita jualan bareng"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Menonton",
                "sosmed": "@alviagnting",
                "kesan": "baik banget, lembut juga cara ngmongnya",  
                "pesan": "semaangat kuliahnya kak jangan demis dulu"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "pendiem tapi ternyata aktif",  
                "pesan": "semangat bang jadi panitia apapun itu, jangan demiss!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "suaraanya bagusss",  
                "pesan": "next kita nyanyi barengg kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HabgVJasr2BLi9kdFDlv68RlgF6f7rJ8", #Bg Wahyu
            "https://drive.google.com/uc?export=view&id=1_nJaIb55wvZkZPBVGCU-jvfHXT3Co3cr", #Kak Elok
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Arsyiah
            "https://drive.google.com/uc?export=view&id=1tWjcjARhA2H2Pabxu7coTelp7NuhdAtQ", #Kak Chibel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Eka
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Najla
            "https://drive.google.com/uc?export=view&id=1_pDfjKuq1UZaAY4i0uEyHxk4WaC3c6aI", #Kak Patricia
            "https://drive.google.com/uc?export=view&id=1ErbESH99DVf0KZAG-GdSHp2Y95m4s13T", #Kak Rahma
            "https://drive.google.com/uc?export=view&id=1_iAJ44a65WQFPecqpmQKOHgfj0nH7_QD", #Kak Try Yani
            "https://drive.google.com/uc?export=view&id=1vdsnm5nbwG5NGMBvMs1AmciHLo09-SET", #Bg Kaisar
            "https://drive.google.com/uc?export=view&id=1GHDCG4Q64VSMDYy85M3HwK77OCxAWbwE", #Kak Dwi
            "https://drive.google.com/uc?export=view&id=1G3kVvtpO_HL2W6nVEoc__8n_GJ3pxM_D", #Bg Gym
            "https://drive.google.com/uc?export=view&id=12mXgSiKF7ZgXMyRb_hpM-Udn2ayL49-Q", #Kak Nasywa
            "https://drive.google.com/uc?export=view&id=1HAFmc6K-BDOKvbDNxd-ifQBnww_r4Rbl", #Kak Priska
            "https://drive.google.com/uc?export=view&id=1rG35d1N-meXdgh1Yge2NwdqrGR8LZLl8", #Bg Arsal
            "https://drive.google.com/uc?export=view&id=1_yVWwed41xzBubmi2gKQBQwS6QYXUfh8", #Bg Abit
            "https://drive.google.com/uc?export=view&id=1JuGewzaLpS5Kva6WdHEBEsM57fz7K78Y", #Bg Akmal
            "https://drive.google.com/uc?export=view&id=1KRE6ltDSFrZNoBQJW6zDj6N_7WF6YF_m", #Bg Hermawan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Khusnun
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
                "kesan" : "tegas banget, keren",  
                "pesan" : "semoga saya bisa jadi seperti abang"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Ngedit",
                "sosmed": "@elokfiola",
                "kesan" : "kak elok cantik banget sumpah",  
                "pesan" : "next kita foto lagi kak"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah.",
                "kesan" : "tidak terwawancarai", # non-wwc
                "pesan" : "-"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "kak cibel cantik lucu panggilannya, tinggi banget jugaa",  
                "pesan" : "sehat selalu ya kak cibel, next kita foto lagi"
            },
            {
                "nama"  : "Eka Fidiya Putri",
                "nim"   : "122450045",
                "umur"  : "20",
                "asal"  : "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi" : "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan" : "tidak terwawancarai", # non-wwc 
                "pesan" : "-"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "tidak terwawancarai", # non-wwc
                "pesan" : "-"
            },
             {
                "nama"  : "Patricia Leonrea Diajeng Putri",
                "nim"   : "122450050",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi" : "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan" : "friendly bangett",  
                "pesan" : "hati-hati dan selalu jaga kesehatan yaa daplokkuu"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Jl.Pembangunan 5, Sukarame",
                "hobbi" : "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan" : "cocok banget jadi MC nya kak saya sukaa",  
                "pesan" : "jadi mc lagi ya kakk"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "namanya unik banget tapi dipanggilnya kak cia juga",  
                "pesan" : "next kita fotooo bareng kak patricia kakkk"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "tinggi dan nyantuuy banget orangnyaa lucu jugaa",  
                "pesan" : "semangat ya bang, jangan ngilangg"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Pemda",
                "hobbi" : "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan" : "cantikk, suaranya baaguss",  
                "pesan" : "next kita karoke ya kak"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf",
                "hobbi" : "Nyari tuyul baskat",
                "sosmed": "@jimnn.as",
                "kesan" : "bang gym keren banget, pinter lagii, berani jugaa",  
                "pesan" : "semoga saya bisa jadi seperti abang"
            },
            {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1",
                "hobbi" : "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan" : "saya kira kakak mikfes",  
                "pesan" : "semoga semakin rajin kuliah dan organisasinya ya kak jangan demiss"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Karaoke",
                "sosmed": "@prskslv",
                "kesan" : "auranya keren tapi galak keknya",  
                "pesan" : "jangan galak beneran ya kak"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi" : "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan" : "keren jadi asprak saya, pinter banget ngodingnya",  
                "pesan" : "makasih bang udh bantuin saya di praktikum"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Main uno",
                "sosmed": "@abitahmad",
                "kesan" : "ketemu lagi kita bang di itera, sebelum nya di SMP yak",  
                "pesan" : "semangat bang kuliahnya, abang keren udh bnyk skill dan pengalaman!"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan" : "baikkk bangett jadi daplok, layak jadi best daplok sepertinya",  
                "pesan" : "jangan diem-diem ya bang, jangan demis juga, semoga kita masih bisa bersama!"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Jalan dekat tol",
                "hobbi" : "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "saya kira abang angkatan 21 dan kadep medkraf hehe",  
                "pesan" : "makasih bang udh bnyak bantuin angkatan 23"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi" : "Beantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "mirip nisa 23, mungil tapi pinterr bangett",  
                "pesan" : "makasih kak udah banyak memberi ilmu pada angkatan 23!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
