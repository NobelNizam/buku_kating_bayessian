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
            "https://drive.google.com/uc?export=view&id=1jhFZFXD1pz6lmTAw7oxxmyarhldNgBLE", #Kak hartiti
            "https://drive.google.com/uc?export=view&id=1mFNePDj3QNbftyRODlZ9e6iajLfMux7g", #Kak putri
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Anisa fitriani blom
            "https://drive.google.com/uc?export=view&id=1q0xwU7IL1mg1KgNQoWbMlyZ29y0sYZFe", #bang feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak  renisha blom
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak claudhea blom
            "https://drive.google.com/uc?export=view&id=1saIpL9OApxH4ZveMlOpTXwCBWF-aDzaq", #bang mirzan
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
                "kesan": "kakak nia, Asik banget orangnya",  
                "pesan":"Semoga dilancarkan segala urusannya, fokus dengan apa yang dituju kak nanti keasikan buat peraturan di baleg wkwkwkw"
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
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Asik kakaknya",  
                "pesan":"kak wulan jangan sampai kelelahan, istirahat juga ya kak"
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
                "pesan":"Jangan lupa makan ya kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "kakakny asik dan baik banget",  
                "pesan":"teruslah mengejar apa yang di targetkan ya kak"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Cool parah ni abang serius",  
                "pesan":"bang feryadi jangan sampai kecapean yan bang, nanti kerenya ilang"
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "kakaknya  keren dan asik",  
                "pesan":"Semangat terus kak saat menjadi baleg ini"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Kak claudhea emang asik deh",  
                "pesan":"Semangat saat berkuliah ya kak",
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "bang mirzan cool dan sangar di waktu yang sama, sigma banget",  
                "pesan":"mangat ya bang, jangan sampai stress di perkuliahan.",
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "120",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": "ngumpulin tugas di e-learning h-5 detik",
                "sosmed": "@myrrinn",
                "kesan": "kak dhea lucu waktu liat di wwc kemarin",  
                "pesan":"Jangan lupa belajar dan tetap jaga kesehatan kak"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "bang fahrul emng aspirasi banget orangnya",  
                "pesan":"Semangat bang di kuliahnya ya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "Kak berlin emng cool banget",  
                "pesan":"Semangat terus kak jangan sampe sakit ya"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "abang jere emng asik banget dah orangnya",  
                "pesan":"teruslah menyebar kebahagiaan bagi banyak orang bang"
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
                "kesan": "Kak nissa emang berwibawa dan dewasa orangnya",  
                "pesan":"tetap menjadi isnpirasi bagi banyak orang ya kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang emang baik dan pengertian orangnya",  
                "pesan":"teruslah kejar apa yang abang inginkan ya bang"
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
            "https://drive.google.com/uc?export=view&id=1XF5flgCt0lVB38OSS70OwhJcO3fcmFZg",
            "https://drive.google.com/uc?export=view&id=1kCtU720c-d0Jv8CEIwdrMIkTKLd7I_vE",
            "https://drive.google.com/uc?export=view&id=177rJVhtDQ6CszP6Ysn_79uz4eT_VUh2x",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kosong Vanessa
            "https://drive.google.com/uc?export=view&id=1R7VOjZ3wgfPr4SniIx_hbGWNLHBp2wpt", 
            "https://drive.google.com/uc?export=view&id=14P98JqAIzi8C-dWYlGhH92CoZ9hjqZPU",
            "https://drive.google.com/uc?export=view&id=1a0ehC1xAdXX8Cwuta1mTKNiG-P2G2R7l",
            "https://drive.google.com/uc?export=view&id=1Ec0lxeUIBcUmg5gPwXqKOQHVh8Mpg1Qc",
            "https://drive.google.com/uc?export=view&id=12i_0FmHa8YCoX4xiQGNpn_tobEu_nUs0", #eror

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
                "kesan": "abangnya ambisius dan open dalam menerima pendapat",  
                "pesan":"jadilah pemimpin yang sabar dan bertanggung jawab ya bang" #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Tertawa",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya abet asik banget orangnya",  
                "pesan":"jangan mudah menyerah ya kak, tetap semangat!!"# 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": "jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak afifah orangnya ramah dan baik yaa",  
                "pesan":"Semangat kak dalam menjalani kegiatan yang sedang dilakukan sekarang" #3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "kak aliya orangnya tegas dan asik ya",  
                "pesan":"Jadilah orang yang sabar dan tetap tersenyum ya kak"# 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya baik banget, apalagi ke saya pulang sendiri ditanyain kenapa :)",  
                "pesan":"Selalu jadi orangn yang ceria dan murah senyum ya kak" #5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Minum kopi",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak hanum orangnya care dan asik pas ngobrol",  
                "pesan":"jangan lupa untuk jaga semangat dan kesehatan kakak ya"# 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya cool dan pendiam orangnya",  
                "pesan":"teruslah berkembang ya bang! Semangat!!" #7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "abangnya baik dan peduli",  
                "pesan":"jangan sampai kelelahan ya bang, lelaki harus kuat"# 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak okta emang semangat banget orangnya",  
                "pesan":"jangan lupa makan dan minum kak, nanti kalo gak sakit" #9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Bang devyan asik dan open",  
                "pesan":"Fokus apa yang menjadi tujuan awal abang masuk ITERA ya bang, jangan sampai lupa"# 10
            },
            {
                "nama": "Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "bang jo sebenernya baik dan ramah hatinya",  
                "pesan":"terus berkembang dan tetap maju ya bang, keep it what you have and improve it" #11
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "Bang kemas mah pro player nihh,  asik banget",  
                "pesan":"jangan sampai kecapean bang, istirahat juga penting"# 12
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kak presil anggun banget, asik lagi",  
                "pesan":"semangat terus kuliahnya kakak" #13
            },
            {
                "nama": "Rafa Aqila Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak rafa kalem dan seruu",  
                "pesan":"semangat ya kak dalam menjalani kehidupan perkuliahan"# 14
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl Airan Raya",
                "hobbi": "Dengerin MCR",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid emng asik dan semangat abizz",  
                "pesan":"jangan mudah  menyerah bang, terus improve" #15

            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Kopri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "kak vanesa itu seru orangnya",  
                "pesan":"mangat kak di PSDA yaa" # 16
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "bang farhan emng ambis dan peduli ke yang lain",  
                "pesan":"jangan mudah menyerah ya bang, jadilah pemimpin yang baik"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kopri Raya",
                "hobbi": "Belajar dan Main game",
                "sosmed": "@gedemoenaa",
                "kesan": "bang gede emng asik dan open orangnya",  
                "pesan":"teruslah improve dan semangat ya bang"# 1
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumsel",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinacv_",
                "kesan": "Kak jaclin orangnya seru ramah dan baik juga",  
                "pesan":"Tetaplah menyebar kebaikan dan senyuman ya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "bang rafly emng pendiem tapi asik juga waktu diajak ngobrol",  
                "pesan":"teruslah mengembangkan skill abang baik apapun itu"# 1
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kak dini emng pendiem juga, tapi ahli dibidangnya",  
                "pesan":"Sebarkan manfaat baik apapun itu ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES": #BLOM LENGKAP SEMUA NANTI WAJIB DI ISI
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zQ3YrJkr857GW6OwCb8FeDewNUbYpPSc", #Bang Rafi
            "https://drive.google.com/uc?export=view&id=1G3JuGZhbKhJU-erDTiIObHDtxGyQ5jV5", #Kak Annisa Novantika
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang Mujadid kosong
            "https://drive.google.com/uc?export=view&id=1Gr58U21kKAAU00-tVc7ty1yYqz6Wq3Js", #Bang Ahmad Sahidin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bang Fadhil Fitra kosong
            "https://drive.google.com/uc?export=view&id=1y7jHNqHKEw-zx8jtejHTqAK-d62Jwkkv", #Bang Regi
            "https://drive.google.com/uc?export=view&id=1byWWQQmYT1J8NWymV9Qfy870B6FcsCYb", #kak Syalaisha Andina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bang Natanael KOSONG
            "https://drive.google.com/uc?export=view&id=1T3Dvhjis278QIjp6Sivm8SemUhrlp87M", #Bang Anwar
            "https://drive.google.com/uc?export=view&id=1qiB5kybmO3BO2GAKO6zlfAMCpz7-G0o6", #kak Deva
            "https://drive.google.com/uc?export=view&id=1B0Clc4zTaTcCM7dhqFByvcTuNGx2W25S", #kak dinda
            "https://drive.google.com/uc?export=view&id=1kPzHKemUlhbvTa-RQWlJluZ_yVfAeRib", #Kak marleta
            "https://drive.google.com/uc?export=view&id=1ydpcqmOxWEoQ7qiz8fAgCi5Up6aAGPvM", #Kak Junita
            "https://drive.google.com/uc?export=view&id=16KA8PiZ2RkKI_WgG-tJN8irOTl_Qdze2", #Kak Syadza Puspadari
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang Atsary KOSONG
            "https://drive.google.com/uc?export=view&id=14z8GVjFK9yF3ME0mnvwzTBcY9lj2s935", #Bang Aditya 
            "https://drive.google.com/uc?export=view&id=1fk0vl447X3xvNqUkqGdjnXC2uIJMWnN5", #bang Eggi
            "https://drive.google.com/uc?export=view&id=1IIE98ilWTTql7i0TBe0DupGjXEW9GQ0d", #Kak Febiya
            "https://drive.google.com/uc?export=view&id=1bVxGEa1IINJyy4UJr4tfB2bUpQB9Ue6g", #Bang Happy
            "https://drive.google.com/uc?export=view&id=1_8-m1rUIE-ubXvAdGcjR779Vh00zjc-p", #Bang Randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Vita KOSONG
        ]
        data_list = [
            {   #1
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "bang rafi energi positifnya kenceng banget, bikin semangat!",  
                "pesan":"Semoga abang tetap jadi inspirasi dan pemimpin yang baik" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kak annisa emng pandai dan murah senyum banget ke kami",  
                "pesan":"Semoga semua mimpi kak anissa tercapai, kami akan support terus!!!" # 2
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@ ",
                "kesan": "Tidak diwawancarai",  
                "pesan":" " # 3
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "bang ahmad orangnya aktif dan friendly banget",  
                "pesan":"Semoga kakak makin berkembang dan sukses " # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "tidak diwawancarai",  
                "pesan":"-" # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Bang regi emang cool dan smart parah dah, jadi pingin kayak gitu",  
                "pesan":"Stay cool ya, Kak! Sukses selalu dan jangan pernah lelah berbagi." # 6
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "kak dina orangnya pendiem",  
                "pesan":"Semoga lancar terus ke depannya ya Kak! " # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "tidak diwawancarai",  
                "pesan":"-" # 8
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "bang anwar baik dan suka memberi arahan kepada kami secara jelas",  
                "pesan":"Jangan mudah lelah ya bang anwar, keep spirit in your heart" # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kak deva oraangnya kompeten dan serius",  
                "pesan":"jangan lupa makan dan terus semangat kak" # 10    

            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari bu mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kak dinda mirip banget sama kak junita, sama sama keren",  
                "pesan":"Semangat ya kak dinda, semoga dilancarkan tugas-tugasnya" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kak marleta emng asik dan baik bangettt",  
                "pesan":"Semoga apa yang kakak inginkan tercapai yahh, stay happy kakk" # 12

            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak junita emang mirip sama kak dinda, sama sama cool",  
                "pesan":"Jangan lupa untuk tetap jaga kesehatan kak junita" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakak oranya keren dan asik",  
                "pesan": "keep what you got kak" # 14
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "tidak diwawancarai",  
                "pesan": "-" # 15 
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "bang adit keren dan ngodingnya jago",  
                "pesan": "Sebarkan ilmu yang abagn miliki, karena itu akan jadi pahala bang" # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Bang Egi mah udah mah keren, cool, dan pinter lagi",  
                "pesan": "Sehat-sehat terus ya bang egii" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kak febi orangnya cool and calm",  
                "pesan": "Terus tingkatkan apa yang kakak punya" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Bang happy memang keliatan happy dan semangatnya",  
                "pesan": "Jangan lupa akademiknya ya bang" # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "bang randa emng pinter dan penyabar, cocok jadi dosen",  
                "pesan": "teruslah sebarkan ilmu dan tingkatkan lagi ya bang" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@",
                "kesan": "Tidak diwawancarai",  
                "pesan":"  " # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FRS0K6qdR7A6iX12fdzaTIhqB3cOUUFq",
            "https://drive.google.com/uc?export=view&id=19BALH991apgDckSJ0102W2EFoVMBJwvf",
            "https://drive.google.com/uc?export=view&id=1d3CrBSZsbePIiYru-sn83Aziu02oZ83g",
            "https://drive.google.com/uc?export=view&id=1Tgmsv4Pfx0hm5u2vVdz1z33fHQC_YVNY",
            "https://drive.google.com/uc?export=view&id=1hMmoZrP0I4nQwb084knGfO9_CkqR8GgO",
            "https://drive.google.com/uc?export=view&id=1AQXClai0PnUqplkf3N4wG6X98DA1myQi",
            "https://drive.google.com/uc?export=view&id=1TpoXX4ZV53EBeEjtlniM5r5RHDR9XSFV",
            "https://drive.google.com/uc?export=view&id=144SkcpgCTsEZyritw8lOhQrVMeYOzHlw",
            "https://drive.google.com/uc?export=view&id=1Ns_uDFMKK2lCv3Fy-yvGMkFIEr-4vTvB",
            "https://drive.google.com/uc?export=view&id=1IwKJO8TVor5WYnkObUUVIBGMu4jBRJbO",
            "https://drive.google.com/uc?export=view&id=1QKw-P2D5ti7o4oQMe8SZJZhxfdHnHOoW",
            "https://drive.google.com/uc?export=view&id=1x82Lp7TNZm6hXGzka_4VXptsTgyC3juq",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1zXxI0RPPUIOXuSREYIQ6ies1meUQfrhz",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1L0zVRegg5atekYQzimWPl3H-GOHMD9A3",
            "https://drive.google.com/uc?export=view&id=1KhreR2aiesS_njukRMY-H2YLyG8UNody",
            "https://drive.google.com/uc?export=view&id=1DAnkBMmxRH-2puuRQl58FNlP2XAsX060",
            "https://drive.google.com/uc?export=view&id=1Kin3xkoNfpsvFxntn-146WrIcGP3dbxi",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Bang yogy namanya keren dan unik bang, abang juga orangnya semangat banget",  
                "pesan":"Jadilah pemimpin yang baik dan bijak ya bang" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kaka orangya asik dan ramah ya",  
                "pesan": "jangan sampai kelelahan ya kak tetap semangat" # 2

            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kandis ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kak nazwa orangnya kelihatan bijak dan ambisius",  
                "pesan": "Jangan lupa jaga kesehatan ya kak" # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Bang bastian asik dan talk-active orangnya",  
                "pesan": "Jangan lupa untuk tersenyum terus ya bang" # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak orangnya kalem dan ramah",  
                "pesan": "Jadilah orang yang bisa memberikan inspirasi ya kak" # 5

            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "Kak esteria orangnya baik, lemah gemulai lagi",  
                "pesan": "Jangan lupa belajar ya kak, takutnya lupa" # 6
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "Kak natasya orangnya estetik banget, soalnya waktu foto milih spotnya yang bagus",  
                "pesan": "Kembangkan apa yang sudah bagus didalam diri kakak ya" # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kaget banget soalnya ini kakak NIM aku soalnya sama-sama ceria, hidup 104 ya kak!!",  
                "pesan": "Teruslah mengejar mimpi dan improve ya kak" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak ratu orangnya keren dan kelihatan ambis",  
                "pesan": "Jangan lupa untuk berdoa selalu ya kak, tanpa doa kita tidak bisa mencapai apa-apa" # 9

            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang tobias mah orangnya perhatian, semangat, dan asik parah",  
                "pesan": "Jangan lupa untuk terus giat dalam akademik ya bang" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "kak yohana pun orangnya ramah dan perhatian kok",  
                "pesan": "Jangan lupa untuk terus menambah relasi ya kak" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "bang adrian orangnya cheerful banget",  
                "pesan": "Fokus dengan apa yang menjadi tujuan abang ya" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Saya kaget bang arafi ternyata orang akamsi toh, tak kira perantau",  
                "pesan": "Teruslah berusaha bang, jangan pernah menyerah" # 13

            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kak uyi orangnya care, baik, dan murah senyum lagi",  
                "pesan": "jangan lupa untuk fokus dengan apa yang menjadi tujuan kak" # 14

            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "kakak orangya asik, baik, dan cool juga",  
                "pesan": "Semangat ya kak baik diperkuliahan atau kegiatan diluar kampus" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang irvan itu orangnya peduli dan pandai saat memimpin",  
                "pesan": "teruslah berkembang dengan apa yang abang miliki sekarang" # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu anak Pengmas",
                "sosmed": "@izzalutfia",
                "kesan": "Kak izza orangnya SEMANGAT BANGETT gak pernah lesu",  
                "pesan": "Terus sebarkan semangat dan kebahagiaan ke orang orang lain ya kak" # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakaknya asik dan baik kok",  
                "pesan": "jangan sampai kelelahan ya kak" # 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan": "Bang raid orangnya pendiam dan cool parah bat dah",  
                "pesan": "jangan lupa tersenyum yang bang, karena dengan senyuman hari-hari abang akan jadi lebih baik" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "kak tria orangnya baik dan asik juga ya ternyata",  
                "pesan": "jangan lupa untuk terus menambah ilmu ya kak, dan sebarkan ilmu tersebut" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m4AXnmuCv_GvTrbIA4yNuZKj4fsN4-TV",
            "https://drive.google.com/uc?export=view&id=1m0AkgyJm2VG-fYI04fJydxqt7n_U4cVX",
            "https://drive.google.com/uc?export=view&id=1Dw8eml07cJUT9ZVUGV6upzUaOz9gO41p",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kosong
            "https://drive.google.com/uc?export=view&id=1061G7KIsrNuVp-vVUZPcz4E8UUzKKzH2",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kosong
            "https://drive.google.com/uc?export=view&id=1GYv9XwGnBax1ZAAEF4B3De0Th01B74yG",
            "https://drive.google.com/uc?export=view&id=11YXlwQ9TEmSVp5xxq7rhUmTlKBUNuubv",
            "https://drive.google.com/uc?export=view&id=10b20SbNu8kg1L3Hgf0-UmwpcFSOy9s9G",
            "https://drive.google.com/uc?export=view&id=1Bi5mtdzSs5DW2Y4k35ARAtOgP1hreQkg",
            "https://drive.google.com/uc?export=view&id=1ZnGDvcCYcpzR72HpDdrfNCHgpLNPmynC",
            "https://drive.google.com/uc?export=view&id=1OueHoV588wD0EMN-QygnxlIAVsPC-uFT",
            "https://drive.google.com/uc?export=view&id=1BpcEH5OWALfygn7M0V5tNMDNMH6BdrvI",
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
                "kesan": " Bang dimas asik abis orangnya ",  
                "pesan":" Semanagat terus dalam menjadi pemimpin bang " # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakaknya kalem bangett ",  
                "pesan":"Selalu sukses kak" # 2
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobbi": " Main sepeda ke gunung",
                "sosmed": "@akbar_restika",
                "kesan": "abangnya ramah",  
                "pesan":"semangat dalam berkuliah bang"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya Asik dan kece",  
                "pesan":"Jangan lupa semangat terus kak"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "Seru banget ni abang rendraa",  
                "pesan":"terus maju bang dalam mengembangkan diri"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "kakaknya murah senyum banget",  
                "pesan":"Teruslah menyebarkan kebaikan dengan senyuman kak"# 1
            },
            {
                "nama": "Yosia Reatare Banurea",
                "nim": "121450049",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Tidurr",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang pendiam bangett",  
                "pesan":"Teruslah berkembang dalam memajukan Internal HMSD ya bang"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":" Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya cool abis",  
                "pesan":"Semangat terus ya kak"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abangnya ramah dan sabar",  
                "pesan":"Semangat di kerohaniannya ya bang"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pemantang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi": "Menonton dan lari",
                "sosmed": "@josuapanggabean_",
                "kesan": "Bang Jooo baik dan keren orangnyaa",  
                "pesan":"jangan lelah dan semangat di kuliahnya ya bang, terutama MSS"
            },
            {
                "nama": " Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azizahksma15",
                "kesan": "kalem banget kakaknya",  
                "pesan":"jangan lupa belajar dan semangat kuliah kak"
            },
            {
                "nama": "Meyra Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":" Pesawaran",
                "alamat": "Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@meyrasty_",
                "kesan": "baik banget kakaknya",  
                "pesan":"Keep up the spirit kakakk"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":" Tanggerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "abangnya cool dan kalem",  
                "pesan":"Mangat teruss abangkuhh"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IF87IEeOUq1tugMhPTelM8WLsDTq60rK",
            "https://drive.google.com/uc?export=view&id=1AefRzxb4iqTLI56fRjcMEcGnirUkrysh",
            "https://drive.google.com/uc?export=view&id=1r5sC9ofiHRfsj-fTnhdDYjp2FxGYVO-J",
            "https://drive.google.com/uc?export=view&id=1dotZqHGI3PPeY33tTLHZjbrRkYbVrrpP",
            "https://drive.google.com/uc?export=view&id=1gVN_Jah18ey2eC8B3QPhGB4fPFha3ahk",
            "https://drive.google.com/uc?export=view&id=1tCGxGmH_fZMKHBIDARgi6rfaAQ78nCQh",
            "https://drive.google.com/uc?export=view&id=11FgM8iolCbibytgl2WweZg16jrhVMgn2",
            "https://drive.google.com/uc?export=view&id=1aerEhGQc7Ls-3hAmo_DprJ4vRk5H_e4F",
            "https://drive.google.com/uc?export=view&id=1x2tTpvQPCeHdHMCQlPI4Z5-T_PKdOqr7", #eror
            "https://drive.google.com/uc?export=view&id=1rIxhtu7LFHRjpxl5rJoawDUdUGKbJZC8", #eror
            "https://drive.google.com/uc?export=view&id=14yAutFN38xJQU59Jh_G2b5i3lbm3zr-_",
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Sidikalang",
                "alamat": "dekat penjara",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Bang Andrian Kekar banget bang, pasti sering ngegym",  
                "pesan": "Semangat dalam berkuliah dan tetap ngegym ya bang" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya rapih dan imut",  
                "pesan": "Jangan lupa untuk terus berkembang ya kak" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "kak nabila stylish banget, keren outfit sehari-harinya",  
                "pesan": "teruslah bermimpi dan menggagpainya ya kak" # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Bang ahmad itu keren dan pendiam",  
                "pesan": "Jangan lupa untuk terus belajar ya bang" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Bang danang orangnya ceria dan asik",  
                "pesan": "Teruslah berkarya dalam dunia yang abang tekuni" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Bang farrel orangnya semangat dan ambisius",  
                "pesan": "Teruslah menjadi lebih baik dalam segala hal ya bang" # 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak tessa orangnya kalem dan jelas dalam menyampaikan suatu pesan",  
                "pesan": "Improve terus kak, siapa tau public speakingnya terus  meningkat" # 7

            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Pertama kali dengar rumahnya di kedaton saya kaget, berarti tetanggan kita kak",  
                "pesan": "Jadilah orang yang sukses dan bahagia ya kak" # 8

            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "kak alvia pendiam banget waktu wawancara, kalem",  
                "pesan": "Teruslah berkembang untuk kedepannya ya kak" # 9
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Bang dhafin orangnya keren dan asik kalau diajak ngobrol",  
                "pesan": "Jangan lupa untuk selalu berdoa ya bang" # 10

            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kak elia orangnya asik dan persuasif banget",  
                "pesan": "Semangat dalam menggapai cita-cita ya kak" # 11

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lr3Jyd4TOmzm3zHd448-neWr2qxNI_wQ",
            "https://drive.google.com/uc?export=view&id=1TOorjBfejp2KENN7rpn99MCflH0SNoUL",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3 kosong
            "https://drive.google.com/uc?export=view&id=1BZwgwK6ltuA1E_OdqkOk9g4PfF-2--Nl",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5 kosong
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6 kosong
            "https://drive.google.com/uc?export=view&id=1Y28i69Ih0MujTdyDA8CboWO61AT1vqzC",
            "https://drive.google.com/uc?export=view&id=1TIfI104UfZQu-KZf6tmhh8kmZEhrGcsv",
            "https://drive.google.com/uc?export=view&id=1Ot3Rw15kMC6CMGs35k_QWtLpLDHVP6cc",
            "https://drive.google.com/uc?export=view&id=1M21xxe9j5C6Mu0jXEu9nMDVzmx_8qpgw",
            "https://drive.google.com/uc?export=view&id=1NeE1nrYk66oQR3GDrWYCaijr-s9bfsBd",
            "https://drive.google.com/uc?export=view&id=1O3mcWOg6ZCC6QaE0dPb-_zUq59mGQaS3",
            "https://drive.google.com/uc?export=view&id=1ETeKwfeqEcedJCjI1weoAk1YM6MzbdND", #13
            "https://drive.google.com/uc?export=view&id=1sULi6TM7_eRUWSKkuv-9RQ73lRzV1e8g",
            "https://drive.google.com/uc?export=view&id=1QdCDUCBAzz46YTJYecVb9kWiQExjh-p-",
            "https://drive.google.com/uc?export=view&id=1YH0YlHm0csCETCfSH0LKpMfFPA8Gs6sc",
            "https://drive.google.com/uc?export=view&id=1GRau9TxTpUXJwAY8hzyTfiZf8oCWkYF2",
            "https://drive.google.com/uc?export=view&id=1b6YVSgx3kN0tmtDU8JOUB6H6yWj0GAnB",
            "https://drive.google.com/uc?export=view&id=1uk_FzqXk4pHELnTNTYTFgYmVI-Yfmlgv",

        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@wayuraja",
                "kesan": "bang tao, ganteng dan cool parah. Apalagi projeknya keren keren",  
                "pesan": "teruslah semangat dalam menggapai mimpi dan berprestasi ya bang, walau gagal teruslah mencoba"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kak elok jago banget skill editingnya, ngari banget jadi pengen belajar",  
                "pesan": "Kembangkanlah terus skill yang kakak punya, jangan berhenti"# 1
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah.",
                "kesan": "tidak diwawancarai",  
                "pesan": "-"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kak cibelll, cantik amat dah",  
                "pesan": "Semangat kak cibel, apalagi kalo pas bikin konten"# 1
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "tidak diwawancarai",  
                "pesan": "-"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat dalam berkuliah kak"
            },
            {
                "nama": "Patricia Leonrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak mah udah baik, cool, cantik, kreatif lagi. Vibesnya asik diajak ngobrol",  
                "pesan": "jaga kesehatan ya kak, walau kakak sibuk tetap perhatikan kesehatan"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Pembangunan 5, Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak neli aktif parah gak bohong, semangat bet orangnya",  
                "pesan": "tetap jadi orang yang ceria ya kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakanya keren lucu banget",  
                "pesan":"Teruslah menjaga akademik kakak ya"# 1
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Namanya keren kali bang, asik pula pas diajak foto. GG word for you bang",  
                "pesan": "Jangan lupa tetap tersenyum ya bang"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak keliatan kreatif orangnya, keliatan dari pose fotonya",  
                "pesan": "Jangan lupa tugasnya kak, kalo ke binxue terus nanti gak selesai tugasnya"# 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari tuyul baskat",
                "sosmed": "@jimnn.as",
                "kesan": "Abang gym memang keren abis orangnya!!",  
                "pesan": "Semangat ya bang, semoga menjadi fotograper profesional"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 2",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "kalo kakaknya cool dan pendiem pasti jago editing ",  
                "pesan": "tetap menyala ya kak dalam perkuliahannya"# 1
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kalo kata temenku kakak lucu, tapi memang lucu hihihi",  
                "pesan": "Semangat ya kak dalam menjalani kuliah yang berat ini"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Asik kabeh ni abang ne",  
                "pesan":"jangan lupa untuk tetap semangat ya bang"# 1
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main uno",
                "sosmed": "@abitahmad",
                "kesan": "Abang jago editing emang sejak pretama kalo liat",  
                "pesan":"Terus berkaya dan jangan lupa menyebarkan ilmu bang, biar jadi pahala"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "bang akmal sungguh baik hati, tidak sombong, dermawan, dan  selalu membantu orang lain",  
                "pesan": "Semoga sukses ya bang, atas semua kebaikan yang telah diberikan"# 1
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "jalan dekat tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Fire Up banget ni abang buset dah",  
                "pesan":"Teruslah menyebar senyuman dan kebaikan ya bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya asik banget kalo diajak ngobrol",  
                "pesan":"Jangan lupa belajar ya kak, akademik nomor 1"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
