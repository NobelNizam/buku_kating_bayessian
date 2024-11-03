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
                "kesan": "Abangnya keren dan sangat mengispirasi",  
                "pesan":"semangat terus kuliahnya dan suksess teruss ya bangg!!!"# 1
            },
            {
                "nama": "Pandra Insani Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@i",
                "kesan": "bang pandra pembawaanya asik bangett",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": " Meliza Wulandari",
                "nim": "121450065",
                "umur": "18",
                "asal":" Pagar Alam, Sumatera Selatan",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya cantikk bangett",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": " Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Gg.sakum",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Kakaknya cantikk bangett",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": " Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknyaa cantikk bangett",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": " Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "nadillaandr26",
                "kesan": "Kakaknya cantikk bangett",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MCjoQK-EGmdWdtdaV4_MOBxZHpEhfIPo", #Kak Niya
            "https://drive.google.com/uc?export=view&id=11MBM9IxgoPppHgNg4I56rB0MLK0f16kx", #Kak Annisa
            "https://drive.google.com/uc?export=view&id=1M95EfuMTa6XXeUpkqT3TSL9xvrJV1dV1", #kk wulan
            "https://drive.google.com/uc?export=view&id=1M6zXLLvYzMCfzwdd799DjtsCmyrDGciR", #kk dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kk claudea
            "https://drive.google.com/uc?export=view&id=1MH_ZlbpeKwTU9t-EwenwnFWFBzqOwcH2", #bg feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kk renisha
            "https://drive.google.com/uc?export=view&id=1LtAW9rmHdtaEf_-Y8rMYTr6dGdhyrwKx", #bg mirzan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kk nisa fitriyani
            "https://drive.google.com/uc?export=view&id=1M3zNZJ_-woBUr9NKpgDOWHz3OvUTRVvj", #kk dhea
            "https://drive.google.com/uc?export=view&id=1M9fynM_URRawW3G3S0YQfKKWaQdzgFt3", #bg fahrul
            "https://drive.google.com/uc?export=view&id=1M2_cR6oB83pfifzCfSV_anbuMFYtxFIj", #kk berliana
            "https://drive.google.com/uc?export=view&id=1MCruLVnpudQNuwJ0NVZ5W1Q2jW2dkE7-", #kojer
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
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "122450000",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Kak clau cantikk bangett",  
                "pesan":"semangat terus kuliahnya kak"# 1
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
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fleurnsh",
                "kesan": "Kakkaknya cantikk bangett",  
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
                "kesan": "Kakaknya cantikk bangett",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": " Mengumpulkan tugas 5 detik sebelum deadline",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya keren hobbi kita sama kak hahahaahaha",  
                "pesan":"semogaa tugas tugasnya dimudahkan yaa kakkk"
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
                "pesan":"semangat terus kuliahnya kojerrrr"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O7KKU-8e2SUoBiNsuiOI-NU0bItr1IdQ", #kak luthfi
            "https://drive.google.com/uc?export=1SJZAG7-xiAV7RFu10mwKsThku4mnATuh", #bang bintang
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
                "pesan":"semangat terus kuliahnya bang"# 1
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
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "abangnya sangat berjiwa pengembangan karakter",  
                "pesan":"sukses teroos banggg"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Tertawa",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya  ",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": "jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak pipah geuliss pisannnn",  
                "pesan":"kak pipah sering sering senyum yaa soalnya aku sukaa"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknyaaa wibanya 10000+++++++++++",  
                "pesan":"jangan galak galak terus yaa kakk"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya instagramable banget",  
                "pesan":"kak tutorin jadi cewe cewe asthetic dongg"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Minum kopi",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak farah manis bgt",  
                "pesan":"semangat terus kuliahnya yeaa kakk"# 1
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "ketika menjadi moderator prakader abangnyaa seruu bangett",  
                "pesan":"semoga dilancarkan kuliahnya bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "bang derr gokil gokil berwibawa",  
                "pesan":"semoga jokesnya semakin berkembang yaa bangg"# 1
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak matanyaa bikin takkuttt",  
                "pesan":"semoga sehat selalu kak"
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya seru, lucu, sukaa banget sama boxingannya",  
                "pesan":"semangat terus kuliahnya bang, semoga bisa jadi juara MMA"# 1
            },
            {
                "nama": "Johannes Khrisjon Silotonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "abangnya baik tapi kadang menakutkan juga",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "abangnya kayaa orang pinterrr bangettt",  
                "pesan":"semangatt teruss mengendalikan pythonnya bangg"# 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakak ini cantik bangeeett kayaa barbiee",  
                "pesan":"semogaa kuliahnya lancar ya kakkk"
            },
            {
                "nama": "Rafa Aqila Jungjungan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak cantikkk bangettt, positif vibes sekaliii",  
                "pesan":"semangat terus kuliahnya kakk"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl Airan Raya",
                "hobbi": "Dengerin MCR",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahidd selera musiknyaaa kereenn abiezzz",  
                "pesan":"ayoo bang kapan kapann tukeran playlist hehehh"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Kopri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kak namanyaaa baguss sekalii ",  
                "pesan":"semangat terus kuliahnya kakkk"# 1
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya seru dan jago bangett bikin lawakan",  
                "pesan":"adain lomba stand up comedy dongg bangg"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kopri Raya",
                "hobbi": "Belajar dan Main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya coll abiezzzz",  
                "pesan":"semangat terus kuliahnyaa bangg"# 1
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumsel",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinacv_",
                "kesan": "Kak ide fashinnya ga abis abis",  
                "pesan":"kakaknya baikkk bgt, sehat terus kak"
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
                "pesan":"semangatt terus kuliahnya bangg"# 1
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak orangnya soft spoken dan baikk bangett",  
                "pesan":"semoga kuliahnya dilancarinn ya asprak ads kuuu"
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
            "https://drive.google.com/uc?export=view&id=1ASS2cGZmJTKDNv0YlCC94lb04LY3-Q6V", #bg sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg fadill
            "https://drive.google.com/uc?export=view&id=1bl97586G8IjQsXMKXOrCSOTsgpW9fCJo", #bg regi
            "https://drive.google.com/uc?export=view&id=10inhDbfGxIzamZLeqR4Ac3WXGkJtoAWo", #kk andini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg natanael
            "https://drive.google.com/uc?export=view&id=1yqk_ZhS5UItj6jkqN8k7RNnFpSXdRHXE", #bg anwar
            "https://drive.google.com/uc?export=view&id=1-lRJdy8TZq-VvTZTlxFeAYIWY9NHD9Km", #kk deva
            "https://drive.google.com/uc?export=view&id=10Fou80ZnldVJMcOp0QX86b0uvJfZiBkq", #kk dinda
            "https://drive.google.com/uc?export=view&id=1dFeXasteIVTxYLsPiN8r5Ns61rRYqYUc", #kk marletha
            "https://drive.google.com/uc?export=view&id=11bDatG1uIZvoPxlpYIIs407vl3jRWDeE", #kk rut
            "https://drive.google.com/uc?export=view&id=104Gvjwy085JPXLpoCXeV8EWl2EZXulFN", #kk sydza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg abdur
            "https://drive.google.com/uc?export=view&id=1zgT6KqZqrAvyr4wo4TmOoW6XpCwXDetH", #bg adit
            "https://drive.google.com/uc?export=view&id=1yakjqt4uCFgGpt0Vlnyp-skm-fPOJjwZ", #bg aegi
            "https://drive.google.com/uc?export=view&id=1-_tzOqM95cwCOgNQbZL6rJCsslEr7xxF", #kk febiya
            "https://drive.google.com/uc?export=view&id=1cmOrYEbO8E491WxWgofZv4AhnIYLhKUh", #bg happy
            "https://drive.google.com/uc?export=view&id=1flkVc8a8VOMtZjil6sg1VkZI4pY8wGOK", #bg randra
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            
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
                "kesan": "abangnya keren",  
                "pesan":"semogaa juara badminton teruss bang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "22",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakaknya cancii amayy",  
                "pesan":"semangat terus kuliahnya kakkk"# 1
            },
            {
                "nama": "Mujajid Choirus Surya",
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
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya lucu banget",  
                "pesan":"spill bang tempat beli roti waktu supporteran tuuh"# 1
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fadhilfwee",
                "kesan": "abagnya spt cwk kul",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "25",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya kerenn bangett",  
                "pesan":"semangaat teruss kuliahnyaa bang duta genre"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Review Jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": "kakaknyaa seruu",  
                "pesan":"bagi tips niar nyaman membaca jurnal dong kak"
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
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "18",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.i",
                "kesan": "terimakasih sudah menyemangati sesama anak sumbar bangg",  
                "pesan":"ayoooo kita minangkan iteraa bang hahahahahahahaha"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknyaa seruuuu",  
                "pesan":"sehat teruus kakakk"# 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "kakaknya seruuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",  
                "pesan":"semangat dan sehat selalu kakk"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakak ini cantik bgtt potisipp vibezz bangettttttttttt",  
                "pesan":"semangaat teruus ngasprak strukdatnyaa kakkk"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kak kayaa orangg berwibawaa bangett",  
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
                "kesan": "kakak ini seruuuuuuuuuuuu",  
                "pesan":"semangat terus yaa kakk dan sehat selalu"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal":"Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya kaya imut lucuuu seperti akuuu",  
                "pesan":"semangat teruss kuliahnyaa bangg"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abang ini terlihat berwibawa seperti bapak rektor",  
                "pesan":"semangat terus bang ngodingnya"# 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": " Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakkaknyaa cantiiik amayyy",  
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
                "pesan":"infokan mabar plants vs zombie bangg"# 1
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
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
            "https://drive.google.com/uc?export=view&id=1InOoK-SqDg4eOK67QFxl0l8UYGJLRmcL", #bg bastian
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
            "https://drive.google.com/uc?export=view&id=1gaEHVhNYA7CAiCIDOXh3rhIW1u0VQeO-", #kk chalifia
            "https://drive.google.com/uc?export=view&id=1aS0mHxxCmdR4W1I3g5LPOvypeaqVbLGB", #bg irvan
            "https://drive.google.com/uc?export=view&id=16CM2GA3SDLpHpLkLVPAbObcMq4XS2EQR", #kk izza
            "https://drive.google.com/uc?export=view&id=16u2s0q4cxXrPe401qhRaPSczzz1TnFtT", #kk kalisa
            "https://drive.google.com/uc?export=view&id=1JO0jFyoYjp3g3tf-rnvQWYKUe1hIHtrH", #bg raid
            "https://drive.google.com/uc?export=view&id=1TOBD3bDR0ukcTByHISzP46KAgGl-Alfm", #kk tria
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
                "kesan": "namaa abngnyaaa bagusss",  
                "pesan":"mau nanya, abang blasteran jepang kahhh?"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya cantikkk seperti alpha women",  
                "pesan":"semangat teruss kuliahnyaa yaa kak"# 1
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "kakaknya gambaran alpha women",  
                "pesan":"sehat selaluuu yaa kak"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "bang aura nya seperti penonton anime",  
                "pesan":"sehat terusss ya bangg semoga cepat wisudaa"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya seruuuuuuuuuuuuuuuuuu",  
                "pesan":"ayoooo tukeran playlist kakkkkkkkkkkkk"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal":"Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "kakaknyaa seruuuuuuuuu",  
                "pesan":"ajakin akuuu dong kakk snorklinggg"# 1
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal":"Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee_15",
                "kesan": "kak natee seruuuuuuu",  
                "pesan":"sehat teruus yaaa kakkk"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya seruuuuuu",  
                "pesan":"kak hobi kita samaaaaaaa"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit Baju",
                "sosmed": "@jasminednva",
                "kesan": "kakkk cantikkkkkk bangettt",  
                "pesan":"ajarinnnn ngejahit dong kakkk, aku dh ada bakat kaki geter kokk"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal":"Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "awalnyaa ku kiraa abngnyaa bulee karna namanya heheh",  
                "pesan":"bangg namanyaa mirip seperti suami saya tobias eaton"# 1
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
                "pesan":"ajarin muka sangar dong kak"
            },
            {
                "nama": "Rizki Adrian Bennoviry",
                "nim": "121450073",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnyaa kecee abiezzz, dulu sering liat di tiktoknya hmsd",  
                "pesan":"banggg wajahnyaa bikin dejavuu huhuh"# 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abangnyaaa kerenn bnget, highlight ig nya jalan jalan muluu",  
                "pesan":"sehat truss bangg, jangann kepencet telpon lagii ya di dm ig sayaaa, sayaa panikk bangetttttt karna ga ngapa ngapain"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "kakaknya lucuuuu outpitnyaa",  
                "pesan":"sehat selalu kakk"# 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "kakaknya baik sekdep internalll ikmm",  
                "pesan":"semangat teruss kak kuliahnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "abang irvan jahat ga oncam pas wawancara sama sayaa",  
                "pesan":"terima saya next year buat ikutan sdm ya bangg"# 1
            },
            {
                "nama": "Izza Luthfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "bertemu anak Pengmas",
                "sosmed": "@izzalutfiaa",
                "kesan": "KAK IZZAAA AKU NGEFANS BANGETTT SAMA KAKKAKKKK",  
                "pesan":"ajarin akuu biar bisa sehebat kakak donggg"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "kakaknya seruuuuuuuuuuuu",  
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
                "pesan":"semangat terus bangg"
            },
            {
                "nama": "Tria Yunani",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidurr",
                "sosmed": "@tria_yo62",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "kesan": "BANG SAYA NGEFANS BANGET SAMA ABANGG, KERENN BANGETT, PEMBAWAANYA TENANGG, TENGILNYA DAPET TAPI WIBAWANYA 10000000000000000000++++",  
                "pesan":"lancarrr teruss yaa bangg urusannyaa, terimakasiii sudahh mengispirasi" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "kakkknyaa cantikkk dan kalemm bangett ",  
                "pesan":"semangatt terus kuliahnya kakkk " # 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "bang akbar seperti guru agamaaa ",  
                "pesan":"semangatt teruss kuliahnya yaa bangg " # 3
            },
            {
                 "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu ",
                "kesan": "kakaknya mukanya kaya judes bangettt",  
                "pesan":"semangat teruss kuliahya kak radioo"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "bang kalo nyanyi kayaa audisi indonesian idolll, abangnyaa juga soft spoken bangett",  
                "pesan":"semangatt terus ngasprak strukdatnya bangg semoga cepaet wisudaa"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhn_694",
                "kesan": "kakaknya seruu bgt",  
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
                "kesan": "bang hidupnya kaya pasrah bnagettt, alsannya ditarik tarik muluu",  
                "pesan":"bang semangat terus ya bang jangan loyooo"
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
                "pesan":"semangaat terus bang semoga sehat selalu"# 1
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
                "pesan":"sehat selalu kak"# 1
            },
            {
                "nama": "Dearni Monica Br Manik",
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
                "pesan":"semangat dan sehat selalu bang"# 1
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
            	"kesan": "auranya seperti orang banyak duit bangg  ",  
            	"pesan":"semogaa abang banyak dapet uangg  " # 1
        	},
        	{
            	"nama": "Adisty Syawaida Ariyanto",
            	"nim": "121450136",
            	"umur": "23",
            	"asal": "Metro",
            	"alamat": "Sukarame",
            	"hobbi": "Nonton film",
            	"sosmed": "@adistysa_",
            	"kesan": "kakak auranya kaya buibu banyakkk duitt ",  
            	"pesan":"spill film yang baguss kakkk  " # 2
        	},
        	{
            	"nama": "Nabila Azhari",
            	"nim": "121450029",
            	"umur": "21",
            	"asal": "Simalungun",
            	"alamat": "Airan",
            	"hobbi": "Menghitung Uang",
            	"sosmed": "@zhjung",
            	"kesan": "pasti kakak nilaii matematikanya bagusss  ",  
            	"pesan":"semoga cepat kaya raya kakkk " # 3
        	},
        	{
            	"nama": "Ahmad Rizqi",
            	"nim": "122450138",
            	"umur": "20",
            	"asal": "Bukit Tingi",
            	"alamat": "Airan",
            	"hobbi": "badminton",
            	"sosmed": "@ahmad.ris45",
            	"kesan": "abangnya kerenn bisa buka joki skripsii  ",  
            	"pesan":"ajarkan saya berbisnis bangg  " # 4
        	},
        	{
            	"nama": "Danang Hilal Kurniawan",
            	"nim": "122450085",
            	"umur": "21",
            	"asal": "Bandar Lampung",
            	"alamat": "Airan",
            	"hobbi": "Touring",
            	"sosmed": "@dananghk_",
            	"kesan": "bang danangg kerennn cocok buat jadi kadepp  ",  
            	"pesan":"nanti kalo jadi kadep ssd angkat saya ya banggg jadi sekdepp pasti saya berdedikasi dengan baikk " # 5
        	},
        	{
            	"nama": "Farrel Julio Akbar",
            	"nim": "122450110",
            	"umur": "20",
            	"asal": "Bogor",
            	"alamat": "Lapas",
            	"hobbi": "Bebas",
            	"sosmed": "@farel_julio",
            	"kesan": "bang farel kece capo suporteran  ",  
            	"pesan":"semangat terus supporterannya bangg " # 6
        	},
        	{
            	"nama": "Tessa Kania Sagala",
            	"nim": "122450040",
            	"umur": "20",
            	"asal": "Simalungun",
            	"alamat": "Pemda",
            	"hobbi": "Menulis",
            	"sosmed": "@tesakanias",
            	"kesan": "kakkk tesaa seruuu  ",  
            	"pesan":"ajarin saya berbisnis saya kak " # 7
        	},
        	{
            	"nama": "Nabilah Andika Fitriati",
            	"nim": "121450139",
            	"umur": "20",
            	"asal": "Kedaton",
            	"alamat": "Kedaton",
            	"hobbi": "Tidur",
            	"sosmed": "@nabilahanftr",
            	"kesan": "kakaknya seruuuuuuuuuu  ",  
            	"pesan":"ajarin saya berbisnis ya kakk  " # 8
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
            	"kesan": "bang dafinn lucuuu amayyy  ",  
            	"pesan":"didik saya menjadi sekdep bang ahahahah  " # 10
        	},
        	{
            	"nama": "Elia Meylani Simanjuntak",
            	"nim": "122450026",
            	"umur": "20",
            	"asal": "Bekasi",
            	"alamat": "Korpri",
            	"hobbi": "Main Alat Musik",
            	"sosmed": "@meylanielia",
            	"kesan": "kak elia positip vibezz sekalii  ",  
            	"pesan":"semogaa cepatt wisudaa kakk " # 11
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
        	"https://drive.google.com/uc?export=view&id=1dTpVvk36TyEbjDx6ICDa6mHlQE9zZUh1", #bg kaisar
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
            	"asal":"Makassar",
            	"alamat": "Sukarame",
            	"hobbi": "Nonton Film",
            	"sosmed": "@wayuraja",
            	"kesan": "abangnya kerennn",  
            	"pesan":"semogaa cepatt lulus yaa bangg"
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
            	"pesan":"kak elok definisi girl crush siii"# 1
        	},
        	{
            	"nama": "Arsyiah Azahra",
            	"nim": "121450035",
            	"umur": "21",
            	"asal":"Bandar Lampung",
            	"alamat": "Tanjung Senang",
            	"hobbi": "Nugas",
            	"sosmed": "@arsyiah.",
            	"kesan": "Kakak ini asik saya suka belajar dengan dia",  
            	"pesan":"semangat terus kuliahnya kakak !!!"
        	},
        	{
            	"nama": "Cintya Bella",
            	"nim": "122450066",
            	"umur": "20",
            	"asal":"Bandar Lampung",
            	"alamat": "Teluk",
            	"hobbi": "Ngegym",
            	"sosmed": "@cintyabella28",
            	"kesan": "kakaknya putiiihhh bangettt",  
            	"pesan":"semangat ngegymnya kaa cibell"# 1
        	},
        	{
            	"nama": "Eka Fidiya Putri",
            	"nim": "122450045",
            	"umur": "20",
            	"asal":"Natar",
            	"alamat": "Natar",
            	"hobbi": "Menyibukkan Diri",
            	"sosmed": "@ekafdyaptri",
            	"kesan": "Kakak ini asik saya suka belajar dengan dia",  
            	"pesan":"semangat terus kuliahnya kakak !!!"
        	},
        	{
            	"nama": "Najla Juwairia",
            	"nim": "122450037",
            	"umur": "19",
            	"asal":"Sumatra Utara",
            	"alamat": "Airan",
            	"hobbi": "Menulis, Membaca, fangirling",
            	"sosmed": "@nanana_minjoo",
            	"kesan": "Kakaknyaaa seruuuuuuuu",  
            	"pesan":"semangat terus kuliahnya kakak !!!"# 1
        	},
        	{
            	"nama": "Patricia Leondrea Diajeng Putri",
            	"nim": "122450050",
            	"umur": "20",
            	"asal":"Bandar Lampung",
            	"alamat": "Jatimulyo",
            	"hobbi": "Nyubit orang",
            	"sosmed": "@patriciadiajeng",
            	"kesan": "kak ciaa cantiik bangeet, aku sayangggg banget sama kak cyaa",  
            	"pesan":"sehat terus yaa kakkkuuuu i love you 300000000000000000000"
        	},
        	{
            	"nama": "Rahma Neliyana",
            	"nim": "122450036",
            	"umur": "20",
            	"asal":"Lampung",
            	"alamat": "Jl. Pembangunan Sukarame",
            	"hobbi": "Makan geprek",
            	"sosmed": "@rahmanellyana",
            	"kesan": "kakaknya seruuuu dan lucuu bangett",  
            	"pesan":"semangat terus nge mc nya kakkk"# 1
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
            	"kesan": "abangnya jompo banget kayanyaa sampai gamau foto berdiri",  
            	"pesan":"semangat nyari hobinya ya bang"# 1
        	},
        	{
            	"nama": "Dwi Ratna Anggraeni",
            	"nim": "122450008",
            	"umur": "20",
            	"asal":"Jambi",
            	"alamat": "Jl. Durian 5 Pemda",
            	"hobbi": "Dengerin musikr",
            	"sosmed": "@dwiratnn_",
            	"kesan": "Kakaknya seruuuuuuuuu",  
            	"pesan":"ayooooooooooo tukeran playlist kakkk"
        	},
        	{
            	"nama": "Gymnastiar Al Khoarizmy",
            	"nim": "122450096",
            	"umur": "20",
            	"asal":"Serang",
            	"alamat": "Lapangan Golf UIN",
            	"hobbi": "Nyari tuyul buzzcut",
            	"sosmed": "@jimnn.as",
            	"kesan": "abangnya lucuuuuuuuuuu",  
            	"pesan":"sejak kapan punya hobi se anti mainstream gtuu bangg????"# 1
        	},
        	{
            	"nama": "Nasywa Nur Afifah",
            	"nim": "122450125",
            	"umur": "20",
            	"asal":"Bekasi",
            	"alamat": "Jl. Durian 1 Pemda",
            	"hobbi": "Bersih-bersih",
            	"sosmed": "@nsywanaf",
            	"kesan": "kakaknya seruuuuuuuu",  
            	"pesan":"sehat selalu kakk"
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
            	"pesan":"semangat terus kuliahnyaa kaak"# 1
        	},
        	{
            	"nama": "Muhammad Arsal Ranjana Utama",
            	"nim": "121450111",
            	"umur": "21",
            	"asal":"Depok",
            	"alamat": "Jalan Nangka 3",
            	"hobbi": "Koleksi Parfum",
            	"sosmed": "@arsal.utama",
            	"kesan": "abangnya kece bangettt",  
            	"pesan":"akuu jugaa suka koleksi parfum banggg, abangnya harus cobain bali bouquet drewdrop siiii"
        	},
        	{
            	"nama": "Abit Ahmad Oktarian",
            	"nim": "122450042",
            	"umur": "20",
            	"asal":"Bandar Lampung",
            	"alamat": "Rajabasa",
            	"hobbi": "main uno",
            	"sosmed": "@abitahmad",
            	"kesan": "abangnya seruuuuuuuuu menghandle python",  
            	"pesan":"ayooo lawannn sayaa main unooo bangggg"# 1
        	},
        	{
            	"nama": "Akmal Faiz Abdillah",
            	"nim": "122450114",
            	"umur": "20",
            	"asal":"Bandar Lampung",
            	"alamat": "Perumahan Griya Sukarame",
            	"hobbi": "Tidur",
            	"sosmed": "@_akmal.faiz",
            	"kesan": "abangnyaaa baikk bangettt pembawaanyaa kaya seorang ayahhh",  
            	"pesan":"sehat terus dan banyak uang selalu yaaa papi kuuu"
        	},
        	{
            	"nama": "Hermawan Manurung",
            	"nim": "122450069",
            	"umur": "20",
            	"asal":"Bogor",
            	"alamat": "jalan dekat tol",
            	"hobbi": "Bengong",
            	"sosmed": "@hermawan.mnrng",
            	"kesan": "abangnya friendly abisss",  
            	"pesan":"satu kata, kentuttttttttt, abang yang bilang gituu ya waktu ngasprak alprosss"# 1
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
            	"pesan":"semangat dan sehat selalu kakkkk"
        	},
    	]
        display_images_with_data(gambar_urls, data_list)
        medkraf()


