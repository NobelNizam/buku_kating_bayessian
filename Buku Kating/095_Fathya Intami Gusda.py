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
            "https://drive.google.com/uc?export=view&id=1vaDENuJzAeO3zclXir2YuTJxrcrVSLbn", #Bang Gumilang
            "https://drive.google.com/uc?export=view&id=1w9gr57HqTJSPTGmUsz1LKvm5IxNGO79M", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=1w8W4xgpA0xvyiNX5B7i9eCb3KkN1c36k", #Kak Meiza
            "https://drive.google.com/uc?export=view&id=1w5IaHeIpxMn8djzj2oQ7N2-MbxZk0gNE", #Kak putri
            "https://drive.google.com/uc?export=view&id=1w3Oqkd9c4nTIaPHu5bsJE3cg8WH63xDc", #Kak hartiti
            "https://drive.google.com/uc?export=view&id=1vtbPnbTEPvyqRNwF3LEJ-hryxdAq26Bf", #Kak Nadilla
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
                "kesan": "keren banget abangnya ",  
                "pesan":"semangat terus bang kuliah dan semuanyaa"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "asik dan seru",  
                "pesan":"Sukses terus yaa bang pandraa"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Cantikkk sekalii",  
                "pesan":"semoga cepat lulus kakakkk !!!, semangattt kuliahnyaa"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "baikk sekali",  
                "pesan":"Semangattt terus kakak cantikk, semogaa lancarrr terus yaa hari-harinyaa"
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Ramah sekalii",  
                "pesan":"Semangat mss nya yaa kak!, semoga dipermudah terus sampai lulus"

            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Menyenangkann",  
                "pesan":"Lancar sampai wisuda ya kak, semangattt untuk semua kegiatannyaa kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1t3iM0B8vvkU9EQLCtWIbQ9xTCBR2Uq7U",
            "https://drive.google.com/uc?export=view&id=1tTq5rgI7QENnphPFAkNA5NDjUeBhiVQD",
            "https://drive.google.com/uc?export=view&id=1wIiEPT218qeXkHulIoRyRtwOKLjYAnJB",
            "https://drive.google.com/uc?export=view&id=1tLAIY3Iit_vv2yXvBbsaSCTfLJ_vsfD7",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1t8noecri9anuMunmAev7kBNyJRiEmLdj",
            "https://drive.google.com/uc?export=view&id=1ssvYz-a13R-yb36GFpgSKoi8Ldj1GR7F",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1t7Ct_l0gRzgGOHZkWWRLGXq894Mwvs3D",
            "https://drive.google.com/uc?export=view&id=1t2qaqGsJ2ZHTVvrbeXn6ZeYjq_stz6Hz",
            "https://drive.google.com/uc?export=view&id=1t6lh5S0uec8oIp5hPmP7MpUNJjg_LLHa",
            "https://drive.google.com/uc?export=view&id=1wITLWFBlc5yzyahUA6aI1OoXplJSNyM6",
        ]
        data_list = [
            {
                "nama": "Tri Murnia Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Ngerjain TA",
                "sosmed": "@trimurniaa_",
                "kesan": "baik dan seru banget kakaknya",  
                "pesan":"semangat mengerjakan TA nya kakak, lancarr terus yaaa"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Membaca novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "baik dan ramah",  
                "pesan":"ayoo kita main ke aeon kakk"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "cantikk bangett sihh kakk!!",  
                "pesan":"sukses selalu kakak cantik (kayak ibu peri)"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "ramah dan baik sekalii",  
                "pesan":"yo dream!!"# 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Cantikk",  
                "pesan":"Semangatt yaaa kakak cantikkk!!"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Badminton, melukis, hiking, berenang, dengar musik, minum kopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya keren dan ramah banget",  
                "pesan":"semangat mengerjakan TA abang, semoga dipermudah segalanyaa"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baik bett",  
                "pesan":"semangat ngasprak nya ya bang, jangan kapok ngaarin kita:)"# 1
            },
               {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Menonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Menyenangkan",  
                "pesan":"Semangatt semester 5 nya kakak!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengar musik ",
                "sosmed": "@fleurnsh",
                "kesan": "cantikkk bangett kakak",  
                "pesan":"semangattt ya kakak manisss"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "abangnya ramah",  
                "pesan":"semangatt ya abang, bahagia selalu abangg"# 1
            },
                        {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Mengumpulkan tugas di e-learning h-15 detik",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya lucu dan menyenangkan",  
                "pesan":"bahagia selalu kak dhea, semangatt teruss ya kakkk"# 1
            },
            {
                "nama": "Berliana Inda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berlyyanda",
                "kesan": "asikk kakaknyaa",  
                "pesan":"semangat terus kakak cantik buat kuliahnyaa"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "lucu, baik dan ramah",  
                "pesan":"jangan kapok buat ngajarin alpro ya bang :)"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ugmDjA8Cl6pjqTe4OJXj6-QPAfpvWx10",
            "https://drive.google.com/uc?export=view&id=1uhpjJDmH2mNgH1xXxnNm_-xeJlAQzXMx",

        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan": "Public Speaking kakaknya keren bangettt",  
                "pesan":"semangat mengerjakan TA nya kakakk, semoga dilancarkan terus semua urusannyaa, bahagia selalu ya kakak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin kak luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya sangat informatif",  
                "pesan":"semangat bang bintang untuk semua kegiatan dan juga kuliahnya!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Mr1a7QgOkyxublt69ohBFsWOHeE3eX03",
            "https://drive.google.com/uc?export=view&id=1KKezafEX_ID2PEMmUB6vQjrlSmxeVBRs",
            "https://drive.google.com/uc?export=view&id=1K-REwDE3pA9ZZ2UT65wt2qGbczUOZCzm",
            "https://drive.google.com/uc?export=view&id=1J3VM494b7m3VVifpr5lkTX45uSGamlQa",#bang dev
            "https://drive.google.com/uc?export=view&id=1JZBteNP7Mu698pRK6p_nral7gVNBU3hk",#bang ateng
            "https://drive.google.com/uc?export=view&id=1JkqVdJ6MMP5yBC7CgEqDtBlSJBmK3R2u",
            "https://drive.google.com/uc?export=view&id=1KG4btcMRRk1dtWbmtSBTYVgEvvMrvO8V",
            "https://drive.google.com/uc?export=view&id=1JwZICzP_S_dDV1v8mx8SoKAp7-McgSlu",
            "https://drive.google.com/uc?export=view&id=1KBxbtYlqjzhcGMh7cnnfXbaHHh35GFmr",
            "https://drive.google.com/uc?export=view&id=1Jmccp2U0J_zyGoJb-LKLaWCIOlXeNjJo",
            "https://drive.google.com/uc?export=view&id=1MsQ1cv8urI1Kwu8aTOGk2b3EBL2ggIUm",
            "https://drive.google.com/uc?export=view&id=1JNjZfaqJdiPCCWaZek4DUxMLarywzw-W",
            "https://drive.google.com/uc?export=view&id=1J7uubUFclDV2YJHiTT76is_2JJqjKIbp",
            "https://drive.google.com/uc?export=view&id=1J8B-H-VxrpHge_wx3nJrmZxR1_yH5Pn8",
            "https://drive.google.com/uc?export=view&id=1J7ig7uEQXzdVzaXT8lxBY2gJ_s4QCKQT",
            "https://drive.google.com/uc?export=view&id=1JFhprfq8iqjihY2gfas6mu_F7fI8fuK7",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Jbiu2yuFTQq5x-kUdsDrfvgXhAkVfe6W",
            "https://drive.google.com/uc?export=view&id=1JONpUAWAkZfP4fiwx-Q0j3DSwvuzY0n6",
            "https://drive.google.com/uc?export=view&id=1MlTCbQqZL86QZfwJu3EIYKwV1lyBAHnv",
            "https://drive.google.com/uc?export=view&id=1JR-gceVRXZRA6D_3AbGiCb1TlhihlgVT",
            
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "abangnya informatif",  
                "pesan":"semangat terus abang, lancar terus sampai luluss"
            },
            {
                "nama": "Elisabeth Claudia Simajuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Owen Kost",
                "hobbi": "Tertawa",
                "sosmed": "@celisabeth",
                "kesan": "kakaknya baik dan ramah",  
                "pesan":"semangat ya kakak kuliahnya, semoga hari-harinya lancar teruss, bahagia selalu juga kakak"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya cantikkk",  
                "pesan":"semangat kak kuliahnyaa, bahagia dan lancar selalu untuk semuanya kak"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya asik, ramahh dan lucuu",  
                "pesan":"semangat mss, semoga lancar sampai lulus, dan sukses selaluu abangg"# 1
            },
                        {
                "nama": "M Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya seru dan sangat informatif",  
                "pesan":"semangat mss dan lancar terus sampai lulus ya abang"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur Lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat, lancar dan sukses terus untuk kuliah dan seluruh kegiatannya kak, bahagia selalu ya kakk"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya baik ",  
                "pesan":"semangat ngaspraknya kak, semoga sukses terus, dan dilancarkan semuanyaa"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya asikk",  
                "pesan":"semangat terus ya kak, bahagia selaluu kakak"# 1
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pangeran Senopati Raya, Gerbang Barat",
                "hobbi": "Futsal",
                "sosmed": "@frdy_kevin",
                "kesan": "abangnya baik hati",  
                "pesan":"semangat dan lancar terus kuliahnya bang, sukses selalu ya bangg"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya seru dan asik",  
                "pesan":"semangat kuliahnya dan hari-harinya ya abang "# 1
            },
            {
                "nama": "Oktavia Nurwinda Puspita Sari",
                "nim": "122450041",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@oktavianrwnda",
                "kesan": "kakaknya baikk",  
                "pesan":"semangat dan bahagia selalu kakak cantikk"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar The Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakaknya cantikk sekalii",  
                "pesan":"semangat ngasprak strukdat kak, sukses terus kakak cantikk"
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": " Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "abangnya asik",  
                "pesan":"semangat mss dan kuliahnya bang kemass"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Airan",
                "hobbi": "Dengerin Musik",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"semangat, lancar dan sukses selalu untuk kegiatan dan kuliahnya bang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya baik dan cantik",  
                "pesan":"semangat kakak cantikk!!, lancar-lancar kegiatannya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya asik",  
                "pesan":"semangat ngaspraknya ya bang jo, sukses selalu"
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
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya asikk",  
                "pesan":"semangat kuliah dan mss nya ya abang"# 1
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakaknya baik dan ramah",  
                "pesan":"semangat kuliahnya dan lancar segala kegiatannya ya kak cantikk"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Mainn game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya baik",  
                "pesan":"semangat terus bang kuliahnyaa dan kegiatannya"# 1
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakaknya murah senyum",  
                "pesan":"semangat ya kakak!!, tidak menyangka kakak kembarr"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zZPUsqDt16KMm2eC6mZmw_YIGu6rLZqg",
            "https://drive.google.com/uc?export=view&id=1zXKu9E6Ng7EnJVdU0N0k0sMkw1ktChcO",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=11LfogME_p3cfezz23crHI4ifoDCDXnCW",
            "https://drive.google.com/uc?export=view&id=1SkU6dC_0GHjxDpL1saKdSeT84LuRoPsE",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1zl6vPRgZ_rs-mk3_T8mSbvebYuXQttXH",
            "https://drive.google.com/uc?export=view&id=1zxL8GnlIECVq781modEQ-LfIjdR_467C",
            "https://drive.google.com/uc?export=view&id=1zCVSsZUhCqs_A6PhtlKCyhuStasCDmra",
            "https://drive.google.com/uc?export=view&id=1-4pfqrABNf2d6TPwEJ5RaSPUnr_90Dc2",
            "https://drive.google.com/uc?export=view&id=1za6auSfFWYgrau5Yq5jfzp0xfQbenMrB",
            "https://drive.google.com/uc?export=view&id=1zt4W4FHjfp8Gxdu4bPuhf6mE3k0eUaCE",
            "https://drive.google.com/uc?export=view&id=1zBDuz0DrR-AxLW3qJdJ9koE8FEy5iMSr",
            "https://drive.google.com/uc?export=view&id=1za4W_mu1ttilV1l-9Z0aYWowtcujQK32",
            "https://drive.google.com/uc?export=view&id=1z9TLFIbYQfZKHwVkgMgWCtCb9qO6Q3YA",
            "https://drive.google.com/uc?export=view&id=1zMlDSWN1wHG50Nknuco7BZ8tJi-ZjdNg",
            "https://drive.google.com/uc?export=view&id=1zIprVyAgoFle_0m5iDw693YKjA6pJefa",
            "https://drive.google.com/uc?export=view&id=1ziMO_cGwh6wpSyPx9yHBskvpgTyEzFQX",
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
                "kesan": "abangnya baik dan ramah",  
                "pesan":"semangat abang kuliahnyaa, semoga lancar terus segala urusannya sampai lulus nantii" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakaknya cantikk",  
                "pesan":"semangatt terus sampai lulus kakak cantikkk " # 2
            },
            {
                "nama": "Mujajid Choirus Surya",
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
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "tidak terwawancarai",  
                "pesan":"- " # 8
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "tidak terwawancarai",  
                "pesan":"-" # 15
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya asikk ",  
                "pesan":"semangat terus kuliahnya ya abang, semoga lancar semuaaa" # 4
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya baik bangett",  
                "pesan":"semangat terus ya bang buat ngasprak rb :), juga kuliah dan kegiatannya" # 6
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
                "pesan":"-" #
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "murah senyum",  
                "pesan":"semangattt terus kakak untuk seluruh kegiatannya!" # 7
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "bang anwar baik sekaliii ",  
                "pesan":"semangatt abang, semangat buat ngasprak, kuliah dan kegiatan lainnya ya abangg!! " # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "kak deva baik dan ramah bangettt",  
                "pesan":"semangat dan sukses selalu kak deva cantikk " # 10
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": " kak dinda baik bangett ",  
                "pesan":"semangat terus kak dinda, semangat juga buat ngasprak ads RB :)" # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya cantik dan murah senyum",  
                "pesan":" semangatt dan sukses terus kuliah dan hari-harinya kakak cantikk" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya ramah",  
                "pesan":"semangat untuk kuliahnya, semoga ipk nya baguss" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya ramah dan asik ",  
                "pesan":"semangatt terus kakak baikkk" # 14
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya baik",  
                "pesan":"semangat, semoga lancar terus kuliahnya bang" # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abangnya seru dan ramah ",  
                "pesan":"semangatt terus kuliah dan hari-harinya bang" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakaknya cantik sekaliii",  
                "pesan":"semangat, lancar dan sukses terus ya kak" # 18
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"semangatt ya bang untuk semua kegiatannya" # 20
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abangnya baik ",  
                "pesan":"sukses dan semangat terus bang, semangat kegiatan mikfesnya" # 19
            },
            {
                "nama": "Vita Anggraini",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "tidak terwawancarai",  
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LUU940ronuYhnvNtqjOhccaCrK7TeFq-",
            "https://drive.google.com/uc?export=view&id=1LhOc8rYsIGBX4goUbT4j3Byh6lvkHVmF",
            "https://drive.google.com/uc?export=view&id=1L7mGEGDfONWMHhnjgVmRAjRy8k6qdmDa",
            "https://drive.google.com/uc?export=view&id=1LQMFu0O5QZnc7nwr-nszbgG3peEEb7dg",
            "https://drive.google.com/uc?export=view&id=1LoGmcOOcrs5e_XwD4aBVB1QMUC3sfprw",
            "https://drive.google.com/uc?export=view&id=1Kpxdcml6_U-KQt3htFoH2amYrEx6KN-S", #6
            "https://drive.google.com/uc?export=view&id=1SwsQVXb1cvmCkEgoBQdHXlRrFJGgF82j",
            "https://drive.google.com/uc?export=view&id=1KvowomZy_f3jhGZ2DOT-CLC-Ogmb5Uaa",#8
            "https://drive.google.com/uc?export=view&id=1KY1IyTOo7x8BYe21CAH0_YnEzMm7lann",#9
            "https://drive.google.com/uc?export=view&id=1SxREajwPlxJsBGYOcdx3ETHgTE6Ru1mP",
            "https://drive.google.com/uc?export=view&id=1T5EAgnxjuSOE83OHFc_hAJKbPllNexXs",
            "https://drive.google.com/uc?export=view&id=1SvqWNwqeEAQXfOka2mEjAOSsseHF6ke2",#12
            "https://drive.google.com/uc?export=view&id=1T6nWluHVoKUeYzWx8L6muXlS25EJ9DAS",
            "https://drive.google.com/uc?export=view&id=1SmN514GuxGl9q37Aq-3N4ol8RQ7F4EOL",
            "https://drive.google.com/uc?export=view&id=1T3jb20BNMF8I-cn4zdMcYE4PRa7Keg59",
            "https://drive.google.com/uc?export=view&id=1StbhQnjDk0o5WePICHkoLZ2JA7O6Y6KG",
            "https://drive.google.com/uc?export=view&id=1LDZqLWqcX2Ck1M80T8eF9QC3-6TgcT8z",
            "https://drive.google.com/uc?export=view&id=1LDGXJNv2wPqaFco2S1MspVjr7DzN2XTc",
            "https://drive.google.com/uc?export=view&id=1LFC7j4lguVjH94I9HIs_fGIBZrh_DkGW",
            "https://drive.google.com/uc?export=view&id=1KoleJoICT0Y3QnNtuuYc0IlRd6Ze8mG8",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Bukinapaso",
                "alamat": "Jatimulyo",
                "hobbi": "Nyari Solar",
                "sosmed": "@yogyst",
                "kesan": "abangnya seru dan baik",  
                "pesan":"lancar terus sampai lulus bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya asikk",  
                "pesan":"semangat dan sukses terus kakak, semoga dilancarkan sampai wisuda yaa"# 1
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya asikk dan seru",  
                "pesan":"lancar terus mss dan kuliahnya abang kadiv pengmass"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "25",
                "asal":"Bandar Lampung",
                "alamat": "Kandis",
                "hobbi": "Berantem",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya ramai jadi seruuu",  
                "pesan":"semangat terus untuk kegitan dan kuliahnya ya kak, seruu bangett kayaknya kalau temenan sama kakak"# 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "kirain abangnya ga asik, gatau nya seruu",  
                "pesan":"semangat kuliahnya bang arafiii, abang mirip temen saya hehehe"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu Anak Pengmas",
                "sosmed": "@izzalutfiaa",
                "kesan": "sangatt ramah, asik, dan seruuuu",  
                "pesan":"aku mau jadi kayak kak izzaa yang mudah berbaur sama siapapunn "# 1
            },
            {
                "nama": "Raid Muhammad Naufal ",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths",
                "kesan": "abangnya baik",  
                "pesan":"lancar terus semua kegiatan pengmas dan juga kuliahnya ya bang raid"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya ramah sekali",  
                "pesan":"lancar terus kuliahnya ya bang irvan, jaga kesehatann "# 1
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakaknya baik dan ramahh",  
                "pesan":"senyum kakak cantikk banget meleleh dehh, semangat kuliahnya kak alyaa cantikkk"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya asikk dan imutt",  
                "pesan":"semangat terus buat kuliah dan pengmasnya kak oca cantikk"# 1
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya murah senyum",  
                "pesan":"aku mau disukainn sama anak-anak kayak kak unaa"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "abangnya asikk",  
                "pesan":"abang ramah sekalii, semangat untuk seluruh kegiatan dan kuliahnya ya abang !!!"# 1
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal":"Bali",
                "alamat": "Sukabumi",
                "hobbi": "Surving sambil snorkling",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya ramahh",  
                "pesan":"semua yang baik untuk kakakk!!"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal":"Kepulauan Seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee_15",
                "kesan": "Kakaknya aktif yaa",  
                "pesan":"semangat untuk kegiatan dan lancar terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal":"Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "abangnya ramahh",  
                "pesan":"semangat terus untuk hari-harinya abang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal":"Makassar",
                "alamat": "Pemda",
                "hobbi": "Mainn Bowling",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya cantik dan lembut bangettt",  
                "pesan":"semangat dan bahagia selalu ya kakak cantikk"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin Musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya murah senyumm jugaa",  
                "pesan":"semangat ya kakak hublu nyaa, lancar terus semua kegiatannya"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak cantikkk",  
                "pesan":"terimakasii sudah menjadi orang yang baik kakak, semangatt ngaspraknya yaa kakak cantikk"# 1
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak cantik part keberpa inii",  
                "pesan":"semangat teruss untuk kuliahnyaa yaa kakakkk, sehatt teruss"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik, asik, ramahh jugaaa",  
                "pesan":"bahagia selalu kakak uyiii cantikkk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yawIImR6ZpqeDwida3Xs1kjzL3pCNfqb",
            "https://drive.google.com/uc?export=view&id=1ycNuAdOxuhcOTkNk8s6dIJpvGkoQd8Sn",
            "https://drive.google.com/uc?export=view&id=1y_3O_bMSVbYCtkKBpZYbItZCXDmyE_8d",
            "https://drive.google.com/uc?export=view&id=1yqsPDrWZDEYzJiJ_EywucaCXOJvdGlSv",
            "https://drive.google.com/uc?export=view&id=1yL11nXOBX7aKEp8YiXXnRMAT0wc9T48H",
            "https://drive.google.com/uc?export=view&id=1yQBJBVfuRzzKpD50ojYkD5pKt8ZT_Zs_",
            "https://drive.google.com/uc?export=view&id=1yrsAgMCPzLaj0UWpOiIx1qGxhClBPD8C",
            "https://drive.google.com/uc?export=view&id=1yMaqFhochxDmIxtqE5JH643fzG5haPuo",
            "https://drive.google.com/uc?export=view&id=1yMgWuUnGrwZzTOPwxPn-8bfMuCI_iSMs",
            "https://drive.google.com/uc?export=view&id=1ybR2QJkTSdIKOKCcbdR3lno8aGtMQmU9",
            "https://drive.google.com/uc?export=view&id=1ytgm5hBlsenj-vPaXzczDZq9VyOZoo02",
            "https://drive.google.com/uc?export=view&id=1ydgAHyyoaJKdPs4A8m8eQFxY2zxJSYrS",
            "https://drive.google.com/uc?export=view&id=1ydO_JOrKv8Sg5moJFA4f3u3T2berpbvv",
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhan",
                "nim": "121450027",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kobam",
                "hobbi": "Manjat pohon pinang",
                "sosmed": "@dimzrky_",
                "kesan": "abangnya seru dan informatif",  
                "pesan":"sukses terus bang, oiyaa di puspitek ada mie yamin enak lohh bangg :>"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Membaca Novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Cantik bangett kak",  
                "pesan":"semangat dan sukses selalu kakak :>"# 1
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Labuhan  Dalam",
                "hobbi": "Main sepeda ke gunung",
                "sosmed": "@akbar_restika",
                "kesan": "abangnya ramah dan baik",  
                "pesan":"sukses terus abangg, lancar sampai lulus ya bangg"# 1
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "ramah abangnya",  
                "pesan":"semangat kuliahnya bang!!, lancar terus kegiatan di kerohaniannya ya abangg"# 1
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya seru",  
                "pesan":"semangat terus kakak kuliahnyaaa!!, sukses terus kak "
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "abangnya seru dan asik, informatif jugaa",  
                "pesan":"semangat abang kuliahnyaa,  semoga kegiatan internal nya berjalan lancar terus ya bangg"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": " @slwfhn_694",
                "kesan": "Kakak baik dan murah senyum",  
                "pesan":"semoga lancar terus kuliahnya ya kak!, semangkaaa!!"# 1
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Tidurr",
                "sosmed": "@yosiabanurea",
                "kesan": "abangnya pendiem",  
                "pesan":"semangat abang kuliahnyaa, lancar terus sampai lulus ya abangg"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya pendiam tapi lucuuu",  
                "pesan":"semangat kuliahnya ya kakak manisss!!"# 1
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Siantar",
                "alamat": "Kost Kiya, Gerbang Barat",
                "hobbi": "Menonton dan lari",
                "sosmed": "@josuapanggabean_",
                "kesan": "abangnya baik",  
                "pesan":"semangat mss dan nyalain proyektornya bang!!, lancar sampai lulus"# 1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "baik dan ramah",  
                "pesan":"Semangkaaa!! Semangattt Kakaaa!"
            },
            {
                "nama": "Meyra Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@meyrasty_",
                "kesan": "Kakaknya baikk",  
                "pesan":"bahagia teruss yah kak, senyum kakak maniss"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "abangnyaa asikk",  
                "pesan":"terus jadi orang yang ramah ya banggg"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YEUjefayL0mYkgVb5rtqLKiwHIDC-VmK",
            "https://drive.google.com/uc?export=view&id=1Y6YyDvPNJh1zvlqOcTdw6zFX7hlUCuja",
            "https://drive.google.com/uc?export=view&id=1XyIUwr712NYLAjl89YfpPjWBZzqQbK51",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1YNgFZtwSLPxQIldaerhcPMRAYTzcmKPI",
            "https://drive.google.com/uc?export=view&id=1YJNjpivdxImUmO2SUDJQCpf-etEAZh2F",
            "https://drive.google.com/uc?export=view&id=1Y5fOtiV7C3uD5fjTaDGzTTsB1laWl6Ed",
            "https://drive.google.com/uc?export=view&id=1Xt5wi-yNIGtvCM23Ubh1S2Nv6adpl1Rf",
            "https://drive.google.com/uc?export=view&id=1Y3ZWAKs514NxXIUEICziNgNCPcfB5ZLO",
            "https://drive.google.com/uc?export=view&id=1Y1rj18c24HQ_PGFzYBWwYMohwm4zyWBH",
            "https://drive.google.com/uc?export=view&id=1YRxdBoxZ61ATTxPphZHdcFd2gRjaVYjg",
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Dekat Penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@andriangaol",
                "kesan": "baik dan ramah",  
                "pesan":"semangat mengerjakan TA dan MSS nya bang andrian"
            },
            {
                "nama": "Adisty Syawalda Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "cantik dan ramah",  
                "pesan":"aku mau belajar jualan pc dari kakak dehh"# 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "baikk dan ramah kakaknyaa",  
                "pesan":"Jaga kesehatan ya kak, semangattt terus "# 1
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya asikk",  
                "pesan":"terus jadi orang yang asik ya kak" # 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "baik abangnya, kalem",  
                "pesan":"semangat buat segala kegiatannya bang. sehat-sehat terus abang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "abangnya baik dan suka jualan",  
                "pesan":"terimakasii udah ngajar praktikum dengan baik bang, semangat ngaspraknya"# 1
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "bang farrel ramah dan informatif",  
                "pesan":"semangat terus bang supporterannya"# 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya murah senyummm",  
                "pesan":"semangat kuliah dan SSD nya kakak!"
            },
            {
                "nama": "Alvia Asrinda Br Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton",
                "sosmed": "@alviagnting",
                "kesan": "Kakaknya baik dan asikk",  
                "pesan":"lancar terus kuliahnya ya kakak cantikk"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya ramahh",  
                "pesan":"semangat dan lancar terus untuk kuliah dan segala kegiatannya abanggg"
            },
            {
                "nama": "Elia Meylani Simajuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya baikkk",  
                "pesan":"semangattt menjalani hari ya kakak, semangat dan bahagia selaluuuu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Ppx6-Og0sHvMLHmslje_Rxc1omaTBAY",
            "https://drive.google.com/uc?export=view&id=1-VjvJEQhDAd6Fchnx0NpD-nEoyRuCjXO",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=10fG1-S4b0ZHsbpMm2nxkTbAi8_kNerkP",
            "https://drive.google.com/uc?export=view&id=10n8IeKl79JqZG8AOgZiuENby8wHHKx-r",
            "https://drive.google.com/uc?export=view&id=10q4rKB1lkp7xCe_b8fViwL_C5zOfFXDR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=10DK-FqAkZmHGCxC2smgfxShFvUZSQpg3",
            "https://drive.google.com/uc?export=view&id=1-wQ3C2ILkH9LILSeitZze4bs6C1P2scQ",
            "https://drive.google.com/uc?export=view&id=10IKtiygSuBg4LPUxr7-35-dpYK6tTBf3",
            "https://drive.google.com/uc?export=view&id=1-XbNuqzDWsxLeiPvYUnaZ3ILx4PG-qXQ",
            "https://drive.google.com/uc?export=view&id=10oowmD9MsANEM4Wpvquz9kJN_PLMqnRW",
            "https://drive.google.com/uc?export=view&id=10kfBaAR9sRCXo3ypUqMaR_Gs_EjpwNxA",
            "https://drive.google.com/uc?export=view&id=1-YEioHA61kG33LEJVNeIcH-qAOyiP25L",
            "https://drive.google.com/uc?export=view&id=1-RJIsQ2IEsaGuq-wGYbUDH-12E_VEBdz",
            "https://drive.google.com/uc?export=view&id=1-RtAVwurZqlaYRj1X1Bu85dDirqR1C2X",
            "https://drive.google.com/uc?export=view&id=1-Hp0GVFBhZ-VUV862DAmnt-flNWJ-mmO",
            "https://drive.google.com/uc?export=view&id=1-8Y77tvRf9VtGxqUHadbHbiBd3vbVpZ5",  
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
                "pesan":" semangatt terus abangg, semoga dimudahkan sampai lulus " # 1
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
                "kesan": "tidak terwawancarai",  
                "pesan":"-" # 3
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
                "kesan": "tidak terwawancarai",  
                "pesan":"-" # 5
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "tidak terwawancarai",  
                "pesan":"-" # 6
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
                "pesan":"semangatt ya abanggg, bahagia selaluu " # 12
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
                "pesan":"semangat terus untuk semua kegiatannya kakak cantikk" # 13
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20 ",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "baik kakaknyaa",  
                "pesan":"semangatttt menjalani hari kakak cantikk" # 14
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
                "pesan":"semangattt ya bang, sukses dan bahagiiia selaluuu " # 18
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kakaknya ramah dan baikk ",  
                "pesan":"semangatt terus kakak cantikkk " # 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
