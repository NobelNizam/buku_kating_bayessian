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
            "https://drive.google.com/uc?export=view&id=1Lig8KbuPNkrxR1qpVxck_r9_pJyh5Sg0", #bang gumi
            "https://drive.google.com/uc?export=view&id=11DEY_UPniAyxRr7X5nzYxa3nDYjq6GfX", #bang pandra
            "https://drive.google.com/uc?export=view&id=17oXUbpA_-MZibe7ARFL5Up0BYBez-RWL", #kak meliza
            "https://drive.google.com/uc?export=view&id=1hQWKNQvBVTk1u7uWdfC3TpoIFLqdzTiZ", #kak hartiti
            "https://drive.google.com/uc?export=view&id=1AkdXLJF56FI-ELklxXe4dZnJGxaR_k5l",
            "https://drive.google.com/uc?export=view&id=1LhkS-CbbfCtRbW1cpjW5Ojxg0egpkN0g",
        ]
        data_list = [
            {
                "nama": " Kharisma Gumilang",
                "nim": "121450142",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "kandis",
                "hobbi": "mendengarkan musik",
                "sosmed": "@gumilangkharisma",                
                "kesan": "Abangnya keren",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Pandra Insani Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Meliza Wulandari",
                "nim": "121450065",
                "umur": "18",
                "asal":" Pagar Alam, Sumatera Selatan",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Gg.sakum",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "nadillaandr26",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MCjoQK-EGmdWdtdaV4_MOBxZHpEhfIPo", #Kak Niya
            "https://drive.google.com/uc?export=view&id=11MBM9IxgoPppHgNg4I56rB0MLK0f16kx", #Kak Annisa
            "https://drive.google.com/uc?export=view&id=1M95EfuMTa6XXeUpkqT3TSL9xvrJV1dV1",
            "https://drive.google.com/uc?export=view&id=1M6zXLLvYzMCfzwdd799DjtsCmyrDGciR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1M6zXLLvYzMCfzwdd799DjtsCmyrDGciR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1LtAW9rmHdtaEf_-Y8rMYTr6dGdhyrwKx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1M3zNZJ_-woBUr9NKpgDOWHz3OvUTRVvj",
            "https://drive.google.com/uc?export=view&id=1M9fynM_URRawW3G3S0YQfKKWaQdzgFt3",
            "https://drive.google.com/uc?export=view&id=1M2_cR6oB83pfifzCfSV_anbuMFYtxFIj",
            "https://drive.google.com/uc?export=view&id=1MCruLVnpudQNuwJ0NVZ5W1Q2jW2dkE7-",
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
                "kesan": "Kakak kerenn bangett publik speakingnya",  
                "pesan":"semoga TA nya cepat selesai ya kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": " Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak anisa cancii amayy",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450050",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Kak wulan maniezz amayy",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobbi": "Menonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya seruuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "122450000",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya pembawaannya tenang banget",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"jakarta",
                "alamat": "korpri",
                "hobbi" : "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "bang mirzan kereen abiezzz",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": " Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": " Mengumpulkan",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya kerenn bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur":"22",
                "asal": "Surakarta",
                "alamat": "Sukarame ",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "bang fahrull cool abiezzz",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": " Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "Kakak orangnya keren bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "Memancing Emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "Kojer pembawaanya asyikk ",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O7KKU-8e2SUoBiNsuiOI-NU0bItr1IdQ", #kak luthfi
            "https://drive.google.com/uc?export=view&id1SJZAG7-xiAV7RFu10mwKsThku4mnATuh=", #bang bintang
        ]
        data_list = [
            {
                "nama": "Anissa Lutfia  Alifia",
                "nim": "121450093",
                "umur": "22 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "kak upii publik speakingnya kerenn bangett",  
                "pesan": "Semoga kuliahnya lancar sampai wisuda ya kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang kerenn",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BLU4DRE2wM0g12Uk_BkEwK2VHpu_olKa", #bg econ KADEP
            "https://drive.google.com/uc?export=view&id=1CVlWnwuiz41G0_Smoc5MpQhKz7rJZrmQ", #kak abet
            "https://drive.google.com/uc?export=view&id=1CNZJFxV-p_QyQT4EFh2mYJv78NeMIpy2", #kak fifah
            "https://drive.google.com/uc?export=view&id=1C2Bi0SDvBm4h2B3w1C0_eMxxr2tlyqmY", #kak allya
            "https://drive.google.com/uc?export=view&id=1CT6PQSi-8V-Q2yyFZeyi51q3RQSMyUhg", #kak ekshantyyy
            "https://drive.google.com/uc?export=view&id=1CIIhAsRLW9Lf0kaNG5V6e8Y4HfyJzEeU", #kak hanum
            "https://drive.google.com/uc?export=view&id=1Cd01lhTZeaQqYN2Zt8mZSM_aC4AY-R9a", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1CEa44d6pt4TKIR-dLNPBQvlokpFpo8tO", #bg dery
            "https://drive.google.com/uc?export=view&id=1CE9uUQUnTPyjUS_uemmtfHw5cZzpd7n4", #kak okta
            "https://drive.google.com/uc?export=view&id=19k1tM5XvJCSvm3bWhd0GErohSPOJHhkG", #bg devyan
            "https://drive.google.com/uc?export=view&id=1AiussSKDoB1sL8iuUdrLhMejR3PDgt8Y", #kk press
            "https://drive.google.com/uc?export=view&id=1A_BsosIv5R-3jLfsxuQx1CijMkdGdhVj", #bg jo
            "https://drive.google.com/uc?export=view&id=19xtMCp_aAZl7XNBlgGj1y4IrDXYUIBzO", #bg kemas
            "https://drive.google.com/uc?export=view&id=1A7v71gkmwh5oJm_br6srPO2tVkT11iID", #bg sahid
            "https://drive.google.com/uc?export=view&id=1A0bB0r9Fz6ojT5UGt0Ljhn_crHIRT_Hp", #kak akilla
            "https://drive.google.com/uc?export=view&id=1SBMj27MIe3EytEBQUIh2g-y-E8V1ALlP", #bg farhan
            "https://drive.google.com/uc?export=view&id=1B7eonxGPM58XFrH9tnFPNITfmHDpIPYH", #bg gede
            "https://drive.google.com/uc?export=view&id=1As9u-DBC-F-RRgcxTanDCvDA6o37ivG4", #kak jacklin
            "https://drive.google.com/uc?export=view&id=1AmdXomZ6fDZInZT2rL8mtdqpovcrN3uZ", #bg rafly
            "https://drive.google.com/uc?export=view&id=1Aw8_wuNd-AC8QUZxzHcngjEGFE-eyayt", #kk syeila
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "122450000",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak afifah cantikk bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20 tahun",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kak pasha badasss bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20 tahun",
                "asal": "Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20 tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "20 tahun",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19 tahun",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "Bang dery baik ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20 tahun",
                "asal": "Lampung ",
                "alamat": "Way huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "122450000",
                "umur": "21 tahun",
                "asal": "Duri",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20 tahun",
                "asal": "Bekasi",
                "alamat": "Kota baru",
                "hobbi": "Dengar me Adams",
                "sosmed":  "@presiliamg",
                "kesan": "Bang devyan lucuu dan kerenn bangettt",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": " Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19 tahun",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "20 tahun",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
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
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f2FQXe8bwsWUOXmYu7XNexcQWuDi33bI", #bg rafi
            "https://drive.google.com/uc?export=view&id=10T62Ll2kSd467SNLLrJWJmQ1U3dVxhpA", #kk annisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg mujadid
            "https://drive.google.com/uc?export=view&id=1iKV4Q0bKWzE0bUubHYEgV-tHqdTzcEK8", #bg sahid
            "https://drive.google.com/uc?export=view&id=1cmOrYEbO8E491WxWgofZv4AhnIYLhKUh", #bg happy
            "https://drive.google.com/uc?export=view&id=1cmOrYEbO8E491WxWgofZv4AhnIYLhKUh", #bg regig
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
                "sosmed": "@rafadhilillahh13",
                "kesan": "  ",  
                "pesan":"  " # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "  ",  
                "pesan":"  " # 2
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
                "pesan":"  " # 3
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
                "pesan":"  " # 4
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
                "pesan":"  " # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "  ",  
                "pesan":"  " # 6
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "  ",  
                "pesan":"  " # 10
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
                "pesan":"  " # 11
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
                "pesan":"  " # 12
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
                "pesan":"  " # 13
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
                "pesan":"  " # 14
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
                "pesan":"  " # 15
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
                "pesan":"  " # 16
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
                "pesan":"  " # 17
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
                "pesan":"  " # 18
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
                "pesan":"  " # 19
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "  ",  
                "pesan":"  " # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=135GW0XNPNdFWiUlRcF2k8S3cUtOz94NV", #bg yogy kadep
            "https://drive.google.com/uc?export=view&id=12yrNMy3ckkpzrDHe-VtIFOVqV9uTeN2d", #kk rahma sekdep
            "https://drive.google.com/uc?export=view&id=1YOsDy5Vj-Zv-CkJlRW9nAaDkbtcJPLaK", #kk nazwa
            "https://drive.google.com/uc?export=view&id=1m0o9uDTCEU_MthDOC4TpbdgiWCkprO1a", #bg bastian
            "https://drive.google.com/uc?export=view&id=14oW5uZM2gkZzUww88WD4qmGCX8pIjvt7", #kk dea
            "https://drive.google.com/uc?export=view&id=1XE2SmHc6VnR7Afh1xfXO5bggu4hRypaJ", #kk esteria
            "https://drive.google.com/uc?export=view&id=13xVNxhzcqkoatQBqRO3pm_wJvcqNRkEz", #kk naytasya
            "https://drive.google.com/uc?export=view&id=1ZTATTGKpXtqjp2OpqqHK1_x-4eGWWede", #kk novelia
            "https://drive.google.com/uc?export=view&id=1Z_zaVZzHdekJNqksjx-wfi-0z0oaeYop", #kak ratu
            "https://drive.google.com/uc?export=view&id=1EdaD_8KZXnHuiHQwgxMc9KrkEcy-EC9F", #bg tobias edison
            "https://drive.google.com/uc?export=view&id=1Y_Mi8Ua6AeJkyXPHMnrcDjhr8qrh_Ubb", #kk yohana
            "https://drive.google.com/uc?export=view&id=1_Uh3V-5NIGz7EvWYTCJpMa5MnSfHCyoV", #bgrizky
            "https://drive.google.com/uc?export=view&id=15rp5WDIY4epYEFGN4r8DcX4IIFCy2Bg0", #bg raffy
            "https://drive.google.com/uc?export=view&id=1ayRI02yD7yJfm8w5G-5Gomrd-o9IL9Gg", #kk asa
            "https://drive.google.com/uc?export=view&id=1voEuL1mdLucYdWAjQi3f4eoRLWyvItUM", #kk chalifia
            "https://drive.google.com/uc?export=view&id=1aS0mHxxCmdR4W1I3g5LPOvypeaqVbLGB", #bg irvan
            "https://drive.google.com/uc?export=view&id=16CM2GA3SDLpHpLkLVPAbObcMq4XS2EQR", #kk izza
            "https://drive.google.com/uc?export=view&id=16u2s0q4cxXrPe401qhRaPSczzz1TnFtT", #kk kalisa
            "https://drive.google.com/uc?export=view&id=1BFgLwJGF9TVwugZZ16S277Lj0pb0O94N", #bg raid
            "https://drive.google.com/uc?export=view&id=1TOBD3bDR0ukcTByHISzP46KAgGl-Alfm", #kk tria
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
                "kesan": " Bang yogy kerenn bangett ",  
                "pesan":" Semangat kuliahnya bang " # 1
            },
            {
                 "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kak rahma kalemm banget ",  
                "pesan":" Semangat kuliahnya kak" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Korpri ",
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
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "  ",  
                "pesan":"  " # 5
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
                "pesan":"  " # 6
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
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
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
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
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "  ",  
                "pesan":"  " # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
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
                "hobbi": "Q Time",
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
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "  ",  
                "pesan":"  " # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "  ",  
                "pesan":"  " # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
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
                "hobbi": "Nemenin Tobias lari",
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
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "  ",  
                "pesan":"  " # 20
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Mfx7nwiZ9UF2X0FZo6fuYslZrqKiR6nx", #bg dimas
            "https://drive.google.com/uc?export=view&id=1Mj3S0OHvCeYCCpC1s8sYOzja_OUTGDby", #kak ketrin
            "https://drive.google.com/uc?export=view&id=1a2CkZyyGWcfbhLfBeyKC2BcSG8FuByH7", #bg akbar
            "https://drive.google.com/uc?export=view&id=1MngchzGP8gclFUAI0O9grfXx7cN-mUcU", #kk rani
            "https://drive.google.com/uc?export=view&id=1SOzJhusBvImxE4qPghMm-d6KwkUduQo_", #bg rendra
            "https://drive.google.com/uc?export=view&id=1MkMeVYQ_U6R9pj99FbkQeGK_3N_d4r5a", #kk salwa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Mjcdko_wYmq8_DMhj3az-VJHnJL7A_b9", #bg ari sigit
            "https://drive.google.com/uc?export=view&id=1MqORMMTEGium_xQhMS0DxMTlFbqI_thp", #kk azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Mmd0YHb1F69FSDdVfpof3LHqtalBSFmX", #kk meyra
            "https://drive.google.com/uc?export=view&id=1MkKCsUg3d4jfyjrGMtMMorpD7kNoYZ7l", #bg rendi
            "https://drive.google.com/uc?export=view&id=1Mtx1D9wAIqlspGJL6Nopoh1teYa_xPd8", #kk renta
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
                "kesan": "  ",  
                "pesan":"  " # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "  ",  
                "pesan":"  " # 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "  ",  
                "pesan":"  " # 3
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "  ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 4
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "  ",  
                "pesan":"  " # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "  ",  
                "pesan":"  " # 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "  ",  
                "pesan":"  " # 8
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "  ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "  ",  
                "pesan":"  " # 11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "  ",  
                "pesan":"  " # 12
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "  ",  
                "pesan":"  " # 13
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "  ",  
                "pesan":"  " # 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M_SpmnygJnhdXrisWqRauyJPraN_gPmj", #bg adrian
            "https://drive.google.com/uc?export=view&id=1MYsWbiHc_8uB12E_W9D0rCKTS07nbNPE", #kak adysty
            "https://drive.google.com/uc?export=view&id=1MWfbzpT67tzElFk3EHgk2tuT9jyYNNsy", #kk nabila
            "https://drive.google.com/uc?export=view&id=1MZ971bFkFQfD_2diq_HmtYoLEIRzwHwI", #bg ahmad
            "https://drive.google.com/uc?export=view&id=1MccquFPriRoa67MksTPWigENv29JV7pb", #bg danang
            "https://drive.google.com/uc?export=view&id=1MZ1oMpY7qKSrUuCxfpIdHkySXXT7vXaF", #bg farel
            "https://drive.google.com/uc?export=view&id=1MXnDq7vYgzzDsgvJBg_WTfChQK10IbOL", #kk tesa
            "https://drive.google.com/uc?export=view&id=1MZbBoevrKUOOoXMys3kcado7M_vgiYYs", #kk nabila
            "https://drive.google.com/uc?export=view&id=1McSVuCgniICbMC4cocoErjOFlPaCyA0e", #kk alvia
            "https://drive.google.com/uc?export=view&id=1MbagsF1WneIku8TRw6rQyxJxRZsOHJuc", #bg dafin
            "https://drive.google.com/uc?export=view&id=1MTqjpdQahUVeXWn8iXRwk-sbWQyCNYCp", #kk elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "  ",  
                "pesan":"  " # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "  ",  
                "pesan":"  " # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "  ",  
                "pesan":"  " # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukit Tingi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "  ",  
                "pesan":"  " # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "  ",  
                "pesan":"  " # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "  ",  
                "pesan":"  " # 6
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
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
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
            "https://drive.google.com/uc?export=view&id=1InmJB05C1k4X9PXu3-SqbkLUA1HcdbuN", #kk wahyudin
            "https://drive.google.com/uc?export=view&id=1vyOl2M_uzg12xQXGk9JMnff3Ac1NJ3Lx", #kk elok
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1FlRgx0OwjQTPTVjOkr7UMoh45Wh87rdS", #kk cybell
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1xkU6L_m1GGwmKCBfU2zNIZOIxedvTwki", #kk cyaa
            "https://drive.google.com/uc?export=view&id=1F8Fll0mUA-ux_VS_LNlvkinBYLM0iV0r", #kk rahma
            "https://drive.google.com/uc?export=view&id=18u_F_IyvQ3RtBUoILj_fL6uvqLJTp2Wz", #kk cya
            "https://drive.google.com/uc?export=view&id=1kfW5othTvP3gOZNqJzXkuEl68sIw2dLU", #bg kaisar
            "https://drive.google.com/uc?export=view&id=1MRmNwCx9KDOmXKw3n1-nayUQ2nz542IK", #kk ratna
            "https://drive.google.com/uc?export=view&id=1Fv48PteYrQbFkqykcFg_JSBDLFRm7Vfi", #bg gymnas
            "https://drive.google.com/uc?export=view&id=1uHri5_bPqmQ7HwN7un-bM0T4jUjt49J0", #kk nasywa
            "https://drive.google.com/uc?export=view&id=1uXWGWr_Y1pFXpJvlUO3mRCxOtjR1n3yA", #kk priska
            "https://drive.google.com/uc?export=view&id=1FEXMIo6dMcCENyS4VLB5saSAnTK--n5g", #bg arsal
            "https://drive.google.com/uc?export=view&id=1u07hoG8eJVok3gr7scGqXFMkJxINCauV", #bg abit
            "https://drive.google.com/uc?export=view&id=10Jd5MdGngx_hYmG7Oa1bFWvRzpycm32B", #bg akmalll
            "https://drive.google.com/uc?export=view&id=1KwFhv291SiyCNQtuU2YbnMYyHNUEtxNP", #bg hermawan
            "https://drive.google.com/uc?export=view&id=1L56URB7nb7eYTipeiam4As0QqR_sg_Md", #kk khusnun
        ]
        data_list = [
            {
                 "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"  " # 1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "  ",  
                "pesan":"  " # 2
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
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "  ",  
                "pesan":"  " # 7
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
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
                "hobbi": "Lagi Nyar",
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
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "  ",  
                "pesan":"  " # 11
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
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
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "  ",  
                "pesan":"  " # 13
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": " ",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
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
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "  ",  
                "pesan":"  " # 15
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "  ",  
                "pesan":"  " # 16
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "  ",  
                "pesan":"  " # 17
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "  ",  
                "pesan":"  " # 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "  ",  
                "pesan":"  " # 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
