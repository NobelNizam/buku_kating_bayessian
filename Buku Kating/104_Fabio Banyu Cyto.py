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
            "https://drive.google.com/uc?export=view&id=1hR6n7vwLyy_3foU73bI78QlDZdyact69", #Bang Gumilang
            "https://drive.google.com/uc?export=view&id=13Gelrkr1u6OCfXa7xpSmpls251skyMid", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=1tUR5FwDIVbF4ZJJIBFGg0MmS6jbLEZ9H", #Kak Meliza
            "https://drive.google.com/uc?export=view&id=1mFNePDj3QNbftyRODlZ9e6iajLfMux7g", #Kak hartiti
            "https://drive.google.com/uc?export=view&id=1jhFZFXD1pz6lmTAw7oxxmyarhldNgBLE", #Kak putri
            "https://drive.google.com/uc?export=view&id=1-YRvgLgnSfRRW7vSYjo0vmJmn8eu9wrS", #Kak Nadilla
        ]
        # capek anjay plis omagaaaaa
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Bang gumilang adalah orang yang berkarisma ",  
                "pesan":"semangat dalam menjadi pemimpin himpunan bang"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang pandra humoris dan serius dalam menjawab",  
                "pesan":"Semoga sehat selalu dan fokus dengan TA nya bang!!"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya asik dan seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Kakaknya asik dan murah senyum guyss",  
                "pesan":"Semoga dimudahkan dalam menyelesaikan perkuliahannya kakak"

            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya pintar dalam menjawab pertanyaan",  
                "pesan":"Semoga kakak selalu aktif dan semangat"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakaknya keliatan ambis dan semangat, pasti aktif di kelas",  
                "pesan":"Terus semangat dalam berkuliah kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12T81LbN2wg3iRrEKTdv-5z4iKoTXmdok", #Kak niya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak anissa blom
            "https://drive.google.com/uc?export=view&id=1LHl6jXNdCbH9ZoTJrWxriiwBeAzJM-hw", #kak Wulan
            "https://drive.google.com/uc?export=view&id=1ocytv_WKQU9WymPD7qYfQHRG-LdNV-cz", #kak anisa dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak claudhea blom
            "https://drive.google.com/uc?export=view&id=1q0xwU7IL1mg1KgNQoWbMlyZ29y0sYZFe", #bang feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak renisha blom
            "https://drive.google.com/uc?export=view&id=1saIpL9OApxH4ZveMlOpTXwCBWF-aDzaq", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Anisa fitriani blom
            "https://drive.google.com/uc?export=view&id=19m9ib6qSYvkkNFLaZ4VkODqJqUf0Apb9", #kak dhea amelia putri
            "https://drive.google.com/uc?export=view&id=1bmfaydPGxnmHK41_jLcOMRlDCmBezvkr", #Bang Fahrul
            "https://drive.google.com/uc?export=view&id=1RjZZlQq2U-4RwizP6Fgr60KGzii79wMG", #kak berliana
            "https://drive.google.com/uc?export=view&id=1BxzgwTzQchf655k9pmq0fD5bwnEs8lbT", #Bang Jeremi
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Ngerjain TA",
                "sosmed": "@trimurniaa",
                "kesan": "Asik banget kakak orangnya",  
                "pesan":"Semoga dilancarkan segala urusannya"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "keliatannya kakak ini rajin belajar",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "18",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Asik kakaknya",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "kakaknya baik",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "kakaknya keren dan asik",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "kakaknya baik dan seru",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@ansftynn_",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "120",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@myrrinn",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "kakak baik deh",  
                "pesan":"Semangat kak dalam menjalani kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OJyIszQS5AdApH_m36UvbPeCx9Rz0Bnh", #kak Anissa
            "https://drive.google.com/uc?export=view&id=11YMkk-fs9GifiU6NnzH4eRDgayaZAYtT", #bang bintang

        ]
        data_list = [
            {
                "nama": "Anissa Lutfia Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "-",  
                "pesan":"-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1auChLhCVZa-QNFM6Ma1khvkXgPqh7-gf", #bang econ
            "https://drive.google.com/uc?export=view&id=1lBC7pvOfcEDzjTNnXIvGQ0O5QOvb7ne3",
            "https://drive.google.com/uc?export=view&id=1Ku5S1gbZDnBCb3Oajei4J_escEDY7oIC", #kak nisrina afifah
            "https://drive.google.com/uc?export=view&id=12FQfsSLc-T2zeLcRRkVKj-IcDKFDsTJp",
            "https://drive.google.com/uc?export=view&id=1SayHZ7ktSgTgzQBpk5et941QIay9Y4yA",
            "https://drive.google.com/uc?export=view&id=1SVdJRE4Ddk-8SHjLj5xLhXLKrItSlazO",
            "https://drive.google.com/uc?export=view&id=1VEdiueM9kGV0DcKGgaVj85qhwGURMM-J",
            "https://drive.google.com/uc?export=view&id=1okhcgl3DpPfPYXt5EacNQHrNkxUF6fUE",
            "https://drive.google.com/uc?export=view&id=1XcXx5jt0ZhluCSylwMNXdtlrmMWFOvin",
            "https://drive.google.com/uc?export=view&id=1LhdWku354c1Msap4jXr9Mph6R2gMOgck",
            "https://drive.google.com/uc?export=view&id=1QMzQf4KB7YwFC4VbEbLOfOM4R8R4GNc4",
            "https://drive.google.com/uc?export=view&id=1N5JoC-e4v-k_BEaCCQlSA_VHBfVwI2KL",
            "https://drive.google.com/uc?export=view&id=1kCtU720c-d0Jv8CEIwdrMIkTKLd7I_vE",
            "https://drive.google.com/uc?export=view&id=1XF5flgCt0lVB38OSS70OwhJcO3fcmFZg",
            "https://drive.google.com/uc?export=view&id=177rJVhtDQ6CszP6Ysn_79uz4eT_VUh2x",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kosong Vanessa
            "https://drive.google.com/uc?export=view&id=1R7VOjZ3wgfPr4SniIx_hbGWNLHBp2wpt", 
            "https://drive.google.com/uc?export=view&id=14P98JqAIzi8C-dWYlGhH92CoZ9hjqZPU",
            "https://drive.google.com/uc?export=view&id=1a0ehC1xAdXX8Cwuta1mTKNiG-P2G2R7l",
            "https://drive.google.com/uc?export=view&id=1Ec0lxeUIBcUmg5gPwXqKOQHVh8Mpg1Qc",
            "https://drive.google.com/uc?export=view&id=1tv8lFC1yZOFvAioD8h4UJ8EbKEvf72i8",

        ]
        data_list = [
            {   #1
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "abangnya santuy",  
                "pesan":"semangat bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Tertawa",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya lucu ckalie",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": "jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak pipah cakep bgt",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknyaaa lucuuu",  
                "pesan":"semangat terus kuliahnya kak pashaa"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya galak",  
                "pesan":"semangat terus kuliahnya kakak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Minum kopi",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak ini manis bgt",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya pendiem",  
                "pesan":"semangat terus kuliahnya kakak bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "abang ini gokil",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik",  
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
                "kesan": "abangnya gokil",  
                "pesan":"semangat terus kuliahnya banh"# 1
            },
            {
                "nama": "Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "abangnya sangar",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "abangnya kece",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kakak"
            },
            {
                "nama": "Rafa Aqila Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini cantii",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl Airan Raya",
                "hobbi": "Dengerin MCR",
                "sosmed": "@sahid_maul19",
                "kesan": "abang ini seru",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Kopri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya seru",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kopri Raya",
                "hobbi": "Belajar dan Main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abang ini asik",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumsel",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinacv_",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "abang ini asik",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak ini lucu",  
                "pesan":"semangat terus kuliahnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES": #BLOM LENGKAP SEMUA NANTI WAJIB DI ISI
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zQ3YrJkr857GW6OwCb8FeDewNUbYpPSc", #Bang Rafi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Annisa Novantika
            "https://drive.google.com/uc?export=view&id=14z8GVjFK9yF3ME0mnvwzTBcY9lj2s935", #bang Mujadid
            "https://drive.google.com/uc?export=view&id=1Gr58U21kKAAU00-tVc7ty1yYqz6Wq3Js", #Bang Ahmad Sahidin
            "https://drive.google.com/uc?export=view&id=1bVxGEa1IINJyy4UJr4tfB2bUpQB9Ue6g", #Bang Fadhil Fitra
            "https://drive.google.com/uc?export=view&id=1y7jHNqHKEw-zx8jtejHTqAK-d62Jwkkv", #Bang Regi
            "https://drive.google.com/uc?export=view&id=1byWWQQmYT1J8NWymV9Qfy870B6FcsCYb", #kak Syalaisha Andina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bang Natanael
            "https://drive.google.com/uc?export=view&id=1T3Dvhjis278QIjp6Sivm8SemUhrlp87M", #Bang Anwar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Deva
            "https://drive.google.com/uc?export=view&id=1ydpcqmOxWEoQ7qiz8fAgCi5Up6aAGPvM", #kak dinda
            "https://drive.google.com/uc?export=view&id=1kPzHKemUlhbvTa-RQWlJluZ_yVfAeRib", #Kak marleta
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Junita
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Syadza Puspadari
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang Atsary
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bang Aditya
            "https://drive.google.com/uc?export=view&id=1fk0vl447X3xvNqUkqGdjnXC2uIJMWnN5", #bang Eggi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Febiya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bang Happy
            "https://drive.google.com/uc?export=view&id=1_8-m1rUIE-ubXvAdGcjR779Vh00zjc-p", #Bang Randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Vita
        ]
        data_list = [
            {   #1
                "nama": "Rafi Fadhillah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #2
                "nama": "Annisa Novantika",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #3
                "nama": "Mujadid Choirus Surya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #4
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #5
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #6
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #7
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #8
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #9
                "nama": "Anwar Muslim",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #10
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #11
                "nama": "Dinda Nababan",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #12
                "nama": "Marleta Cornelia Leander",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #13
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #14
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #15
                "nama": "Abdurrahman Al-atsary",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #16
                "nama": "Aditya Rahman",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #17
                "nama": "Eggi Satria",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #18
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #19
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {   #20
                "nama": "Randa Andriani Putra",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {   #21
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Kakak 3",
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
                "nama": "Kakak 4",
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
                "nama": "Kakak 5",
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
                "nama": "Kakak 6",
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
                "nama": "Kakak 7",
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
                "nama": "Kakak 8",
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
                "nama": "Kakak 9",
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
                "nama": "Kakak 10",
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
                "nama": "Kakak 11",
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
                "nama": "Kakak 12",
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
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Kakak 3",
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
                "nama": "Kakak 4",
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
                "nama": "Kakak 5",
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
                "nama": "Kakak 6",
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
                "nama": "Kakak 7",
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
                "nama": "Kakak 8",
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
                "nama": "Kakak 9",
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
                "nama": "Kakak 10",
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
                "nama": "Kakak 11",
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
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
