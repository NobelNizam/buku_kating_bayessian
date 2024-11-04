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
            "https://drive.google.com/uc?export=view&id=1by4Gjat8K7CYE_YZ1kVb4UFX2OO1mwsa", #bang gumi
            "https://drive.google.com/uc?export=view&id=1Iv7_qab78nhor4x-pjjNf1HEQyVHVCzQ", #bang pandra
            "https://drive.google.com/uc?export=view&id=1os-wCTbQHgOoomDoHmcS8gnQaWH5-pcX", #kak meliza
            "https://drive.google.com/uc?export=view&id=1psVAUHsbLR4w630ziJBBFRkXGMp6N1FC", #kak putri
            "https://drive.google.com/uc?export=view&id=1GIzrAegTDPYrB-8IaWT4W_vztQici8-G", 
            "https://drive.google.com/uc?export=view&id=1afhRR-aYSH0Svz0BVbZZgxrAQjniVo6F", #kak nadilla
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
                "kesan": "abang ini seru",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "abang ini seru, ngasih saran juga pas wwc",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini lucu bgt",  
                "pesan":"semangat nulis TA nya kak"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin panda gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini lusyu bgt gkwat",  
                "pesan":"Terus berjuang ya kak"# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "kakaknya kalem",  
                "pesan":"Semoga bahagia kaak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "kakaknya lucu",  
                "pesan":"Stay strong ya kakakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15_tis34iRmXempdeF6G_CdousDPLcMM0", #kak niya
            "https://drive.google.com/uc?export=view&id=1mr2Lhuw5qJ85sk46fGLgHDDFJ_fC4Fg2", #kak Annisa Cahyani Surya
            "https://drive.google.com/uc?export=view&id=1dHLw0x3_SoJtHhUXFjZuoftXH0iQp38z", #kak Wulan Sabina
            "https://drive.google.com/uc?export=view&id=1cqOMsNDESg2ceToRVPq4pE6rQ4QIH89e", #kak Anisa Dini Amalia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Anisa Fitriyani
            "https://drive.google.com/uc?export=view&id=17okp7ls7OxFbI2EzsVH1PK4eMfVxrEo8", #kak Feryadi Yulius
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Renisha Putri Giani
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak Claudhea Angeliani
            "https://drive.google.com/uc?export=view&id=14AQIQ0f7BGwdyIIwlxCX-wc4QutYq4-R", #kak Mirzan Yusuf Rabbani
            "https://drive.google.com/uc?export=view&id=1CBZlBDaR61YYn5Wrz5iR8EkP5ktuFQYy", #kak Dhea Amelia Putri
            "https://drive.google.com/uc?export=view&id=1ewmt2zPYwHBdN2RGz4E7fYhbGHPN1izt", #kak Muhammad Fahrul Aditya
            "https://drive.google.com/uc?export=view&id=1gH7jMzOtoFU0NBPtMnWalu3KpuSEJ7Wr", #kak berliana enda putri
            "https://drive.google.com/uc?export=view&id=1JPU1dCUzxtSYsdYhdtczcuWc9H1ckkV3", #kak jere
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
                "kesan": "Kakak ini seru bgt terus lucuuu",  
                "pesan":"hidup sukses yaa kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini lucuw",  
                "pesan":"keep it fun!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya cantik bgt",  
                "pesan":"Tetap humoris ya kak"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "kakak ini pendiem dikitt, tp lucu",  
                "pesan":"jangan galak galak ya kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini lucu",  
                "pesan":"Jangan lupa have fun!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abang ini pendiem",  
                "pesan":"Stay cool ya bang"# 1
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "ak blm ketemu kakaknya, tp kynya kakak ini kalem",  
                "pesan":"Tetap santai, Kak"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "12145124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "kakak ini kalem",  
                "pesan":"Stay in touch, Kak"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini pendieeeem",  
                "pesan":"bang wibu mo cosplay lagi ak mw req jadi yuta jjk "# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mengumpulkan tugas h-5 detik di e-learning",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini kocak, seruu jugaa",  
                "pesan":"kak jangan garang kaya macan"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": " Badminton, melukis, minum kopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abang ini kaya abang abang teknik mukanya",  
                "pesan":"bang lain kali pose imut ya bang"# 1
            },
            {
                "nama": "berliana enda putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "Kakak ini pendiemm",  
                "pesan":"jangan kaku-kaku banget, kak"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "kojer kaya tengil",  
                "pesan":"tetap tersenyum seperti kaya ini bang (.◜◡◝)"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10SPqyVmqiLOWqB79UAlfYHB1qRMfkgMF",
            "https://drive.google.com/uc?export=view&id=18Zo6Sk_2aYnA1GLIxk16uMp9yZJQWgXH",
        ]
        data_list = [
            {
                "nama": "Anissa Lutfia  Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "Kakak kereen bgt, public speakingnya bagus",  
                "pesan":"Jangan kebanyakan stress yaa kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya serem",  
                "pesan":"Jangan lupa bahagia bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C0L23Em_-z3F9TMRY8NOMP60NOPGDR69", #bg econ
            "https://drive.google.com/uc?export=view&id=1MDfm3v-TQ2jrskVcwqDdsYsUNrML9dW0", #kk abeth
            "https://drive.google.com/uc?export=view&id=1soTE6CvXquXJFikzlL3gT3pcyuzdOF63", #kk pipah
            "https://drive.google.com/uc?export=view&id=1tBr5WueGhQo3b9DI-tS1Asx0dfMThOCd", #kk pasha
            "https://drive.google.com/uc?export=view&id=18amFqzT5OfVE3Vi-as3ScWlvEbcSL9hY", #kk eksanty
            "https://drive.google.com/uc?export=view&id=1jSjGBKixIiY9d-HVpNrLBu06z3GHhTz4", #kk farahanum
            "https://drive.google.com/uc?export=view&id=1K1aYFhxWi32Io_g49Ef0YMz4iCrN7bUa", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1VkuTCF_4lA1efuFyF72NWoKptiN5CPhb", #bg deri
            "https://drive.google.com/uc?export=view&id=16Z9GP_Z51wu5r4yc2fRdOp_E9PAb8a5q", #kk oktavia 
            "https://drive.google.com/uc?export=view&id=1milyviJTSNNpPWj-BUVi9fDe7_5vWHS4", #bg deyvan
            "https://drive.google.com/uc?export=view&id=1gNXSrVqVW-jUFtXpc831tT1k3G7GBthU", #bg jo
            "https://drive.google.com/uc?export=view&id=1tWJQYvKFugiUuevNWzIb7RvwahuSOew-", #bg kemas
            "https://drive.google.com/uc?export=view&id=11QchWf_zn207-Jafl_Yfji8_OKZLXzML", #kk presilia
            "https://drive.google.com/uc?export=view&id=1UN1CR6dtF2rH0Se7k1W52WLvVsslp71_", #kk rafa 
            "https://drive.google.com/uc?export=view&id=1pLsJDTfppEoviRWxm7-1hgmrTm8uauGh", #bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kk vanessa
            "https://drive.google.com/uc?export=view&id=1FVvR13zCZwsouNX_NOf4WKj-IWV9KV_9", #bg ateng
            "https://drive.google.com/uc?export=view&id=1WYmt3dbuxhw619iApYqSrvqzoF0DK_jg", #bg gede
            "https://drive.google.com/uc?export=view&id=1LMYoO3bfcK6x4Ynvs4em0qy_1wZ8Q-Qp", #kk jaclin
            "https://drive.google.com/uc?export=view&id=17JOjjrOtkCmP3ef87VfUiml9HrqtJ5wy", #bg rafly
            "https://drive.google.com/uc?export=view&id=1BtojKKEECYa_RAqQ2OxucLVJFW-U2dyF", #kk syalaisha
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
                "kesan": "abangnya seram",  
                "pesan":"Jangan galak ke adek adeknya bang"
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
                "pesan":"tetep ceria ya kak"# 1
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
                "pesan":"kak pipah jangan serem serem pwis"
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
                "pesan":"kak pasha semoga tidak galak seperti macan"# 1
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
                "pesan":"Tetap inspiratif walau kocak!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak ini manis bgt",  
                "pesan":"kak jangan keseringan minum kopi"# 1
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
                "pesan":"semoga dilancarkan semua urusannya bang"
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
                "pesan":"abang semoga kocak terus yh"# 1
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini diam diam mematikan",  
                "pesan":"Jangan lupa bahagia kak"
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
                "pesan":"semoga ipknya 4 terus bang"# 1
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
                "pesan":"tetap santai ya bang"
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
                "pesan":"bang main valo banh tp saya gajago"# 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak ini cantik bangeeettttt",  
                "pesan":"kak saran lagu the adams yg easy listening"
            },
            {
                "nama": "Rafa Aqila Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini pendiem",  
                "pesan":"kapan kapan kita hengot di pekanbaru yh kak"# 1
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
                "pesan":"saran lagu mcr tapi selain helena bang"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "belum wwc",  
                "pesan":""# 1
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
                "pesan":"banyak banget pahalanya bang menolong orang"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kopri Raya",
                "hobbi": "Belajar dan Main game",
                "sosmed": "@gedemoenaa",
                "kesan": "saya kira galak",  
                "pesan":"abang lain kali kita harus foto pose lucu"# 1
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumsel",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinacv_",
                "kesan": "kakaknya positif vibes bgt",  
                "pesan":"Kakak penuh energi positif"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "abang ini pendiem dikit",  
                "pesan":"abang main game apa bang"# 1
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
                "pesan":"kakak sehari baca berapa buku"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f1rT0k32ZDRTLtz8JDv0qm-HmS_WkKNM", #Rafi Fadhlillah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Mujajid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Annisa Novantika
            "https://drive.google.com/uc?export=view&id=1KMbsCJNs9zE_XJBxxWKBKia8lUAxl2oy", #Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Fadhil Fitra Wijaya
            "https://drive.google.com/uc?export=view&id=1mM1h8DpwAZCsks7_rfjs6hauAbaipEG8", #Muhammad Regi Abdi Putra 
            "https://drive.google.com/uc?export=view&id=10ycYhXg2DLDUIO3ONEiM4g1DIqG5Ttfv", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Natanael Oktavianus
            "https://drive.google.com/uc?export=view&id=1B3PthuMORDMBgDNQKWcGl2ZN5gCN0CgI", #Anwar Muslim
            "https://drive.google.com/uc?export=view&id=1nSirXNjoUDQmgsR93_6OHk_uTF93lox-", #Deva Anjani
            "https://drive.google.com/uc?export=view&id=1QPwJwi6wMVAuC5FESKo35OxBk0q7zH6N", #Dinda Nababan
            "https://drive.google.com/uc?export=view&id=1ffX3z9wcacN26AvtwrCt4BXK-1re4WEK", #Marleta Cornelia Leander
            "https://drive.google.com/uc?export=view&id=117mzJORyZ_ss09D5n2kLlenkKJX-RFJ2", #Rut Junita Sari Siburian
            "https://drive.google.com/uc?export=view&id=1dRx9u0MJw9ppu2WNQZgZeiQexfIQzUMF", #Syadza Puspadari Azhar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Abdurrahman Al-atsary
            "https://drive.google.com/uc?export=view&id=1zd4wg1Dq09ztUOOoDQWcPbFDfpCyd1Ky", #Aditya Rahman
            "https://drive.google.com/uc?export=view&id=1yfuQ4Kl5RVBWV5OV_lU3kSwESJYYh-DI", #Eggi Satria
            "https://drive.google.com/uc?export=view&id=1-88TmSJ3BdjGLBqiaupCrS-b5T0ixH75", #Febiya Jomy Pratiwi
            "https://drive.google.com/uc?export=view&id=1cajJug9A4Wv5zHL3XC_WOOOFJNkATTuQ", #Happy Syahrul Ramadhan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Randa Andriana Putra
        ]
        data_list = [
            {
                "nama": "Raffi Fadhillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumsel",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhhllahh13",
                "kesan": "abangnya seru",  
                "pesan":"abang olahraga apa bang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "22",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakaknya lucu",  
                "pesan":"kak ajarin aku masak wkwk"# 1
            },
            {
                "nama": "Mujajid Choirus Surya",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "belum wwc",  
                "pesan":""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya kocak bener",  
                "pesan":"rajin olahraga agar tidak jompo ya bang"# 1
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "main game",
                "sosmed": "@fadhilfwee",
                "kesan": "abangnya spt cwk kul",  
                "pesan":"bang mabar epep bang"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "25",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya kalem benerrr",  
                "pesan":"apa ga pusing ngasprak ADSnya bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Review Jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": "kakaknya lucuuu",  
                "pesan":"kak apa tidak mual membaca jurnal?"
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "belum ketemu abngnya",  
                "pesan":"keren banget abangnya"# 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "18",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.i",
                "kesan": "abang ini pendiem",  
                "pesan":"bang anwar keep the energy up!"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak ini lucu bgt hwhwh",  
                "pesan":"kak saranin film dong"# 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari bu mika",
                "sosmed": "@dindanababan_",
                "kesan": "kakaknya kaya garang:(",  
                "pesan":"sehari berapa kali baca jurnal bu mika kak?"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakak ini cantik bgtt",  
                "pesan":"apa tidak mual liatin jurnal terus kak?"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakak ini terlihat seperti kakak baik",  
                "pesan":"kak apakah ngeresume jurnal itu menyenangkan?"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakak ini kalem bgt",  
                "pesan":"apakah kakak membaca au"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "belum wwc",  
                "pesan":""
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya kaya bokem...maaf bang....",  
                "pesan":"abangnya keren bgt membuat wisata gg gimang"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abang ini terlihat berwibawa seperti bapak dosen",  
                "pesan":"keep it up bang buat cari konten untuk wisata"# 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": " Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakak ini pendiem T_T",  
                "pesan":"kak saran drakor yang seru dong"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abang ini baik",  
                "pesan":"bang info game yang seru dong"# 1
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya baik",  
                "pesan":"abangnya sehari tidur berapa jam bang" 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=136C0aNS9QCBQq4MTklFarMiUaXr793kX", #Yogy Sae Tama
            "https://drive.google.com/uc?export=view&id=12BVNbWDZIFgTmESVSXCEwXjbe6PcwSZm", #Ramadhita Atifa Hendri
            "https://drive.google.com/uc?export=view&id=1Ym4JbFrUZ-hZVwW3GieujgPoEy32VdWx", #Nazwa Nabilla
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bastian Heskia Silaban
            "https://drive.google.com/uc?export=view&id=14R-e-tXZqmQKsvzTbtXof6U9Uk6-PALQ", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=10cA5GNt3Ee3vcoCpZ7s8k8cHUIhBGEAM", #Esteria Rohanauli Sidauruk
            "https://drive.google.com/uc?export=view&id=13c10Cd4RRoUas_0pAKezBICylSw9OJox", #Natasya Ega Lina
            "https://drive.google.com/uc?export=view&id=1ZOP_3DHnviEdiUFGuo4eziLE6-Rzj7UR", #Novelia Adinda
            "https://drive.google.com/uc?export=view&id=14EMObU0pbOuR1F6K4cyg2pIdRTDM2YIY", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=1It4EOxYPlevt3TIK6JeeZhiKYyHveRsu", #Tobias David Manogari
            "https://drive.google.com/uc?export=view&id=1TzrZMPSIZLYh58oYVTn3YBIjRNjzIe9P", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=1_zFYAnR3ZGNGZYZUpcf9J8ETegwAtloG", #Rizki Adrian Bennovry
            "https://drive.google.com/uc?export=view&id=15tlADBYQZ6E5EDmXNo_2v7zKH25vemda", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=1bKwHWwbd_g3Hp0Va9ibK_NrtD4cosgIC", #Asa Do'a Uyi
            "https://drive.google.com/uc?export=view&id=1jzi6h_CVtxAGPfdvZoi9Qvur3c9_xjVY", #Chalifia Wananda
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=16fSfY3iWa1F199xSJpKFisiFmY0FOADp", #Izza Lutfia
            "https://drive.google.com/uc?export=view&id=16nz6JzTZwPupU3HkdnoXEF4FV-tA1eVV", #Khaalishah Zuhrah Alyaa Vanefi
            "https://drive.google.com/uc?export=view&id=1cIIOSGGceWc9NPd3t0a6Nr21HmeZeep3", #Raid Muhammad Naufal
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Tria Yunanni
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Burkinapaso",
                "alamat": "Jatimulyo",
                "hobbi": "nyari solar",
                "sosmed": "@yogyst",
                "kesan": "awalnya saya kira orang jepang karena nama abangnya",  
                "pesan":"tiap hari nyari solar kah bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya kalem",  
                "pesan":"kakaknya suka jalan kemana aja kak"# 1
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "kakaknya galak saya takut",  
                "pesan":"kak ajarin main golf"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "abangnya seru",  
                "pesan":"abangny wibu y?"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak ini lucuuu",  
                "pesan":"genre music kesukaan kakak apa"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal":"Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "kakak ini lucuuu",  
                "pesan":"seru ga kak snorkeling?"# 1
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal":"Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee_15",
                "kesan": "kak natee lucuuu",  
                "pesan":"kakak belajar main paralayang sendiri kah kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya kaya galak ternyata tida",  
                "pesan":"kakak nyaa lucu bgt hobinya tidur"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit Baju",
                "sosmed": "@jasminednva",
                "kesan": "kakak ini baik",  
                "pesan":"kak buka kursus menjahit ga kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal":"Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "abangnya sangarr",  
                "pesan":"abang pernah berenang ke jakarta ga bang"# 1
            },
            {
                "nama": "Yohanna Manik",
                "nim": "122450126",
                "umur": "19",
                "asal":"Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini galak ak takoed",  
                "pesan":"Kakak hebat"
            },
            {
                "nama": "Rizki Adrian Bennoviry",
                "nim": "121450073",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya baik",  
                "pesan":"bang udah pernah berenang dimana aja bang"# 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abang ini kalem",  
                "pesan":"pernah ditampar ekor kuda ga bang?"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "kakaknya kalem",  
                "pesan":"Kakak bisa menghadapi tantangan"# 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "kakaknya baik",  
                "pesan":"kak suka baca makalah ga kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya kaya pendiem",  
                "pesan":"apakah bang irvan adakah pasukan windut"# 1
            },
            {
                "nama": "Izza Luthfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "bertemu anak Pengmas",
                "sosmed": "@izzalutfiaa",
                "kesan": "KAKAKNYA EXTROVERT BGTTTTTT",  
                "pesan":"energinya kok bisa gaabis gitu kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "kakaknya baik",  
                "pesan":"keren kakaknya rajin ngaji"# 1
            },
            {
                "nama": "Rahid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan": "abangnya baik",  
                "pesan":"bang duduk diwico sambil merenung pernah ga bang"
            },
              {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "Kakanya manis bgt",  
                "pesan":"kak jangan keseringan tiduurr kakkk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sRARHbEFs0o-SgBgiCNH3eHks-7p4XX6", #Dimas Rizky Ramadhani
            "https://drive.google.com/uc?export=view&id=1_Kgme3VsTPkXFEOKb8ObywpD_oBvBTVr", #Catherine Firdhasari Maulina Sinaga
            "https://drive.google.com/uc?export=view&id=1e9j2ev2diE9O_AHOiKsUVyLUY0ZFfDX3", #Akbar Resdika
            "https://drive.google.com/uc?export=view&id=1lS3fQeF47Gh4oivxgPyzam65J1nmWTUh", #Rani Puspita sari
            "https://drive.google.com/uc?export=view&id=19eeiNbwGHzL4ehwBAMXSVeFAGexKNbtF", #Rendra Eka Prayoga
            "https://drive.google.com/uc?export=view&id=1nW7FEjxijh3cVDurA2csNRg9MO6wRmxC", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1mHR0JRJXje25mhefbR98YdrPavKJ7sCH", #yosia 
            "https://drive.google.com/uc?export=view&id=1S0Fu5J174XWdngcCf55KtHJuHJqIsRRn", #Ari Sigit
            "https://drive.google.com/uc?export=view&id=1TiANQodonaH53bcXSuNePyoyn2bswpng", #Azizah Kusumah Putri
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Dearni Monica Br Manik
            "https://drive.google.com/uc?export=view&id=1hAB24fVtr0fWwSQHDThXbTkuq-Ta7trM", #Meira Listyaningrum
            "https://drive.google.com/uc?export=view&id=1RCwxqszBsSgkfI0efhaOXO_MEqOTXzeW", #Rendi Alexander Hutagalung
            "https://drive.google.com/uc?export=view&id=1sMQyevEXP5-aTHS-E7hBd0EuUbUz94DV", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1tGYw3cnIpeUC1Z-LhM0axoDPkBpulqed", #Josua Panggabean
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
                "kesan": "Public Speaking abangnya bagus banget",  
                "pesan":"sukses terus bang"
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
                "pesan":"kakanya pembawaannya kalem bgt, gitu terus yaa kak"# 1
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi": "Main sepeda ke gunung",
                "sosmed": "@akbar_resdika",
                "kesan": "abangnya kalem lucu gituuu",  
                "pesan":"abang ga kecapean naik sepeda ke gunung?"# 1
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu ",
                "kesan": "kakaknya mukanya kaya galak mau makan orang",  
                "pesan":"kak whats ur music genre?"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "abangnya keren bgt kece",  
                "pesan":"bang tips kerennya dong"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhn_694",
                "kesan": "kakaknya cuu bgt",  
                "pesan":"kak saran film yang seru dong"# 1
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450049",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": "abangnya kocak abiez",  
                "pesan":"bang jangan garang bang kalo ngeliat orang bang"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "abang ini wah masyaAllah sekali",  
                "pesan":"Tetaplah rendah hati!"# 1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "kakaknya pendiem",  
                "pesan":"kakaknya pasti cewe coquette"# 1
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "belum diwawancarai",  
                "pesan":""
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
                "pesan":"kakaknya hobi nonton genre apa"# 1
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
                "pesan":"bang apakah kamu bisa ngambang dilaut bang"# 1
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
                "pesan":"kakaknya mirip temenku sekilas tw"# 1
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
                "pesan":"bang nonton venom ga bang?"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-cgz2IRvwJC0CuZuGsU8PW_vRxdpctvw", #Andrian Agustinus Lumban Gaol
            "https://drive.google.com/uc?export=view&id=1ihvza8hb2kOlXP0_58w0L9I5i45_d7u3", #Adisty Syawaida Ariyanto
            "https://drive.google.com/uc?export=view&id=1loIvdR6ZX60265WwXHu11z_TCd8W9Gd2", #Nabila Azhari
            "https://drive.google.com/uc?export=view&id=18ZWM_r3HeryyKx5g2TIdyRkw2o_-Tvw6", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=14c18OBebrjIUqB50uuPXRBG9AZ9si17a", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=1ThXMh-5gT-BO4fdkQDTq1_UBPW4zfgqn", #Farrel Julio Akbar
            "https://drive.google.com/uc?export=view&id=1iCCw793VyyJGEM8keaTk6OWF10RNZ8jC", #Tessa Kania Sagala
            "https://drive.google.com/uc?export=view&id=1hJ58ELGeMtSuvAZUyZPoLZdi82yHmLMU", #Nabilah Andika Fitriati
            "https://drive.google.com/uc?export=view&id=10QfKcwoDVlOGRi9u0GyoiYTB9ZbWfZp1", #Alvia Asrinda Br.Gintng
            "https://drive.google.com/uc?export=view&id=12EojTNNN8DA_KtWSqoMuFt_8JWi9qAhK", #Dhafin Razaqa Luthfi
            "https://drive.google.com/uc?export=view&id=1TJTKARnMBSprL_oC69RYXxbpoAeOZGA_", #Elia Meylani Simanjuntak
        ]
        data_list = [
            {
                "nama": "Adrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"SidiKalang",
                "alamat": "Deket penjara",
                "hobbi": "nyari hobi",
                "sosmed": "@adriangaol",
                "kesan": "aabang ini keren cklie",  
                "pesan":"sekarang masih nyari hobi ga bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakaknya asik banget diajak ngobrol",  
                "pesan":"Semoga kakak selalu diberi kekuatan"# 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "kakaknya kereen",  
                "pesan":"Teruslah berusaha, Kak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukit Tinggi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "abangnya keren bener bang",  
                "pesan":"kalo anak prodi ada yang joki dapet diskon ga bang?"# 1
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "abangnya keren bgtzzz",  
                "pesan":"abangnya touring kemana aja"# 1
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "abangnya sangar",  
                "pesan":"abang pasti bisa menggapai mimpi!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": " 122450040",
                "umur": "18",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "aku kira kakaknya galak ternyata enggaa ^^",  
                "pesan":"kakaknya suka nulis jurnal ga"# 1
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kakak ini lucuu bgt",  
                "pesan":"kak pernah ga kelamaan tidur bangun bangun malah pusing?"# 1
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "kakaknyaa lucuuu pipinyaa",  
                "pesan":"kak mari kita nonton windut bersama"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya baikk",  
                "pesan":"semoga sukses bang"# 1
            },
            {
                "nama": "Elia Meylani Simajuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "kakaknya kaya orang cinaa",  
                "pesan":"kakaknya keren bgt bisa main alat musikk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1J0W69Nr5jgQ484P0rBXYcWKK6A3Uef2f", #Wahyudiyanto
            "https://drive.google.com/uc?export=view&id=1-9YpHn4dUK_F8-YRDMqQoXXPIxbem8yn", #Elok Fiola
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Arsyiah Azahra
            "https://drive.google.com/uc?export=view&id=10KOscMgGsfowHefTk4e1jzwnELI1GpaN", #Cintya Bella
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Eka Fidiya Putri
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Najla Juwairia
            "https://drive.google.com/uc?export=view&id=1wGvG_MW5DqWml8FkXbaK9KxHo2nVwqum", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=1EoBBCP1k32GapIIPpZauPFjrTTB94ODD", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=1c_4Ov9mLXKjiCVa_V1vhEex94WvVMt9I", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=18lP9mYTimlIUm6f1MrxFppaW31x72Pv1", #Muhammad Kaisar Firdaus
            "https://drive.google.com/uc?export=view&id=1unRXCAsJwia3xKpfJEApdXeZESZ0JQkj", #Dwi Ratna Anggraeni
            "https://drive.google.com/uc?export=view&id=1wrNY33lT5G9n1VMO21o5FFP_i7jtdSKg", #Gymnastiar Al Khoarizmy
            "https://drive.google.com/uc?export=view&id=1ZY9UswimyxIEqS3HCnRn6rTqqk_R6WhW", #Nasywa Nur Afifah
            "https://drive.google.com/uc?export=view&id=1b3iboZG_TBmok1UuNCCjrO24-VAN8hlb", #Priska Silvia Ferantiana
            "https://drive.google.com/uc?export=view&id=1MVfTQKFC4NkFx95UHctM6q4Z47u_YW-p", #Muhammad Arsal Ranjana Utama
            "https://drive.google.com/uc?export=view&id=1u0-Q0Fh9qBx7DmgOu68FogNrRAHMO_HJ", #Abit Ahmad Oktarian
            "https://drive.google.com/uc?export=view&id=1JdQiCEbn9NvVfqOV7tBNLjhgbk5Wks9d", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1KajJnRXy1pUBOtZLtaKotIf4EYoF5__T", #Hermawan Manurung
            "https://drive.google.com/uc?export=view&id=1iKuKc6IjhjWGJqkTCMyuAYU1sy8HuXNH", #Khusnun Nisa
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
                "kesan": "abangnya keren",  
                "pesan":"bang seminggu nonton film berapa kali"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kakaknya cantiiik bangett",  
                "pesan":"tutor ngedit kak"# 1
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "belum ke wawancarai",  
                "pesan":""
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "kakaknya lucu bgt",  
                "pesan":"awal ngegym badannya sakit semua ga kak"# 1
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "blum wwc",  
                "pesan":"kak jangan kecapean ya"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "kakaknya bayik sekayi",  
                "pesan":"kakaknya ngestan kpop apa"# 1
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak ciaa cantiik bangeet",  
                "pesan":"Semoga kakak selalu bahagia"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Pembangunan Sukarame",
                "hobbi": "Makan geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "kakaknya ramah bangeet",  
                "pesan":"sehaat selalu kaak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakaknya lucuu bgttt",  
                "pesan":"sukses terus kakk"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih nyari",
                "sosmed": "@dino_kiper",
                "kesan": "abangnya kocak bener",  
                "pesan":"ini udah ketemu belum bang hobinya?"# 1
            },
           {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwiratnn_",
                "kesan": "kakanya murah senyum",  
                "pesan":"kak suka dengerin apa?" # 11
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Nyari tuyul buzzcut",
                "sosmed": "@jimnn.as",
                "kesan": "abangnya asik",  
                "pesan":"biasanya nemu tuyulnya dimana bang"# 1
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1 Pemda",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "kakaknya keren",  
                "pesan":"keren bgt pasti kakaknya rajin"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "kakaknya lucu",  
                "pesan":"kak kapan kapan karaoke sama bayes yaa kak"# 1
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "abangnya kece",  
                "pesan":"spill parfum yang paling best bang"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "main uno",
                "sosmed": "@abitahmad",
                "kesan": "abangnya ramah",  
                "pesan":"bang bewan uno bang"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya pendiem",  
                "pesan":"terimakasih bang sudah menjadi bapak yang baik buat anak anak bayes bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "jalan dekat tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abangnya friendly",  
                "pesan":"bang jangan kebanyakan bengong"# 1
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kakaknya lucuu",  
                "pesan":"kakak kalo udah berantakin kamar, dibersihin lagi ga kak?"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
