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
            "https://drive.google.com/uc?export=view&id=1SvkY0OHhlfqpRKsx1SN1B-WI2abiN_DU",
            "https://drive.google.com/uc?export=view&id=1ShhMBoB7xihd9GAdp64gmgnC6uVCb7S2",
            "https://drive.google.com/uc?export=view&id=1Spga9LcFQ93VqlYLU2xb9TsXn3To1hD6",
            "https://drive.google.com/uc?export=view&id=1SplO0KBS3ke0R90fMXVNVQQ3ciGLN0y3",
            "https://drive.google.com/uc?export=view&id=1SpRtvORtIVVhOkBki2hPIgluJ8sY_L8r",
            "https://drive.google.com/uc?export=view&id=1T0aD_-_tPYd87T670bGe4RPd210dAAc5",

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
            "https://drive.google.com/uc?export=view&id=1JwnD3hNXydtUOnNs9SMmnA6iLWNKXAfx", #1
            "https://drive.google.com/uc?export=view&id=1K2Fe95HI7VrNF9Jm1-NSkkOIn7SpbY-s",#2
            "https://drive.google.com/uc?export=view&id=1JzRXpo6aoRk2RTcKydcaUXHSgXkMgYu9",#3 
            "https://drive.google.com/uc?export=view&id=1PJYpLFsKxeksS0fKkA1Er1Hu2norXUGK",#4 
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",#5 gda
            "https://drive.google.com/uc?export=view&id=1SOmQXsot0haWxZO3kRMKX7R-gpeLfFBK",#6
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C", #7 gada
            "https://drive.google.com/uc?export=view&id=1K1-aqdEDAxz_lhOkGf_uEkxtrZ3RuOB8",#8 
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C", #9 gada
            "https://drive.google.com/uc?export=view&id=1K-jceOxwiTOzqtOTaGwPUxq6eSUaYKej",#10
            "https://drive.google.com/uc?export=view&id=1PMnQbaidao6YxyU3vPt0NDuBXn90St4B",#11
            "https://drive.google.com/uc?export=view&id=1PNPQY4fuslRsKLYN_Yy2cWjpB1ngNmmk",#12
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",#13
            
            
            
        ]
        data_list = [
            {
                "nama"  : "Tri Murniya Ningsih",
                "nim"   : "121450038",
                "umur"  : "21",
                "asal"  :"Bogor",
                "alamat": "Raden Saleh",
                "hobbi" : "Ngerjain TA",
                "sosmed": "@trimurniaa",
                "kesan" : "Asik banget kakak orangnya",  
                "pesan" :"Semoga dilancarkan segala urusannya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "20",
                "asal"  :"Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi" : "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "18",
                "asal"  :"Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Anisa Dini Amalia",
                "nim"   : "121450081",
                "umur"  : "20",
                "asal"  :"Tangerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Claudhea Angeliani",
                "nim"   : "121450124",
                "umur"  : "21",
                "asal"  :"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Feryadi Yulius", #6
                "nim"   : "122450087",
                "umur"  : "20",
                "asal"  :"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi" : "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Renisha Putri Giyani", #7gada
                "nim"   : "122450079",
                "umur"  : "21",
                "asal"  :"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi" : "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya" 
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan" : "keren",  
                "pesan" :"semangat kuliahnya"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi" : "Mainn Bola, Belajar",
                "sosmed": "@ansftynn_",
                "kesan" : "keren",  
                "pesan" :"semangat kuliah nya"
            },
            {
                "nama"  : "Dhea Amelia Putri", #10
                "nim"   : "122450004",
                "umur"  : "120",
                "asal"  : "Bengkulu",
                "alamat": "Natar",
                "hobbi" : "Mainn Bola, Belajar",
                "sosmed": "@myrrinn",
                "kesan" : "keren",  
                "pesan" : "semangat kuliahnya"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta",
                "alamat": "Sukarame",
                "hobbi" : "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan" : "kerenn",  
                "pesan" :"semangat bang" 
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "12245022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Billabong",
                "hobbi" : "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan" : "kerenn",  
                "pesan" : "semangat bang"
            },
            {
                "nama"  : "Berliana Enda Putri",
                "nim"   : "122450065",
                "umur"  : "20",
                "asal"  :"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi" : "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan" : "keren",  
                "pesan" : "semangattt"
            },
         
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KFUPYY9wR4PaJVOFlYBPPoMHc3uKWw5T",
            "https://drive.google.com/uc?export=view&id=1KHRvU7sTZC988Mt2ob35dQFD97GUL_Wj",
        ]
        data_list = [
            {
                "nama"  : "Anissa Lutfia Alifia",
                "nim"   : "121450093",
                "umur"  : "22",
                "asal"  : "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi" : "Nyanyi",
                "sosmed": "@annisaluthfi_",
                "kesan" : "Kakaknya keren, aku kagum banget karna aku awalnya mau masuk senat ehehe",  
                "pesan" : "cemungut"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi" : "Dengerin Kak luthfia nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan" : "aktif banget",  
                "pesan" :"semangat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_t_j2tCruM1n6_tsLMKZF3hiOpF6AHpY",#1
            "https://drive.google.com/uc?export=view&id=1_woYuD4fBNlkrHGr5aZ1sH80hwGnlFao",
            "https://drive.google.com/uc?export=view&id=1_Gy5XM4Dk0NrYonywTklc0PmBfoyNwu0",#3
            "https://drive.google.com/uc?export=view&id=1_zxRSCIex2ESE2PMz13Yq1ZdZNwSMBEM",
            "https://drive.google.com/uc?export=view&id=1_IDU0zsRo1qdNsn7rhdddNhU6MgED1my",#5
            "https://drive.google.com/uc?export=view&id=1aTOyYumUGGSfbpVKRij1MgAoJ5scejB1",
            "https://drive.google.com/uc?export=view&id=1a13gswZ7e8drn_NnzjgU7fZew_c7J1p4",#7
            "https://drive.google.com/uc?export=view&id=1_Gtl9GEunckd6VC4AnI0sEVCBynSPBFo",
            "https://drive.google.com/uc?export=view&id=1_Fp_8soSjpPrTW1DLC5UWxG4kajIJ0ue",#9
            "https://drive.google.com/uc?export=view&id=1_umZGdKQddFxgdEyQ4BtNZ8hd9JgEmYb",
            "https://drive.google.com/uc?export=view&id=1_OVBMKCY4PKhuObDElakvHu3oO1cjT4W",#11
            "https://drive.google.com/uc?export=view&id=1aTsU4MUwno4FM3qpitkQdp7EyVuLKcUD",
            "https://drive.google.com/uc?export=view&id=1_VK9HLHzUfTG-MnHhprVv9vFDua1pc69",#13
            "https://drive.google.com/uc?export=view&id=1_TeOULCsvui845XRkIH-8QaricBDOurc",
            "https://drive.google.com/uc?export=view&id=1a_Sw9NFFZvpICbtB9pEFSuX2KN_09s_3",#14
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",
            "https://drive.google.com/uc?export=view&id=1_ih3pTmm1gPWEaNdkbeiXnpGqSS9hj01",#16
            "https://drive.google.com/uc?export=view&id=1_dIDiuWkHBB4NNzt0y66GIZnNToV-ITT",
            "https://drive.google.com/uc?export=view&id=1_IDsAxBD6WLH8Ngw7scg-Vs0OPqaWPBV",#18
            "https://drive.google.com/uc?export=view&id=1_atWJcl0F9ffCmBhN5i_zjSwLU0estkk",
            "https://drive.google.com/uc?export=view&id=1QNgXyCyk6tQylONXIqxOhn4_eoeZTKea",#20
        ]
        data_list = [
            {
                "nama": "Ericson Candra Sihombing", #1
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
                "nama": "Elisabeth Claudia Simanjuntak", #2
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
                "nama": "Nisrina Nur Afifah", #3
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
                "nama": "Allya Nurul Islami Pasha",  #4
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
                "nama": "Eksanty Febriana Sukma Islamiaty", #5
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
                "nama": "Ferdy Kevin Naibaho", #7
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
                "nama": "Devyan Loxefal", #10
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
                "nama": "Presilia", #13
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
                "nama": "Sahid Maulana", #14
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
                "nama": "Gede Moana", #17
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
                "nama": "Rafly Prabu Darmawan",#19
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #19
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #20
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #21

            
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",  #1
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
                "nama": "Annisa Novantika",         #2
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
                "nama": "Ahmad Sahidin Akbar",      #4
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
                "kesan": "  ",  
                "pesan":"  " 
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta", #6
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
                "nama": "Syalaisha Andina Putriansyah", #7
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
                "pesan":"semangat terus kuliahnya bang !!!"
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
                "kesan": "  ",  
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
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
                "pesan":"  " 
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@i",
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
            "https://drive.google.com/uc?export=view&id=129RE6rpbwCgQLOFP8aSS8BPRhYYIctL8", # Bang Yogy 
            "https://drive.google.com/uc?export=view&id=", # Kak Ramadhita
            "https://drive.google.com/uc?export=view&id=", # Kak Nazwa Nabilla
            "https://drive.google.com/uc?export=view&id=1XQoQf71YdqJ4eSptBW5hEpRA6riNCYbv", # Bang Bastian
            "https://drive.google.com/uc?export=view&id=127mSNKVd-dnfzQecZCmYoBpzA0P1qjof", # Kak Dea Mutia
            "https://drive.google.com/uc?export=view&id=", # Kak Esteria
            "https://drive.google.com/uc?export=view&id=12BIdqiFmCuJK3fzfDHbBfVNF9lFQJdrc", # Kak Natasya Ega 
            "https://drive.google.com/uc?export=view&id=1xCuBZjFLd5lvGAxp5fLUGqfQutNUOuPi", # Kak Novelia
            "https://drive.google.com/uc?export=view&id=128wMgi1KD_UZ85udYy3NEAX72e_OtNkB", # Kak Ratu Keisha Jasmine
            "https://drive.google.com/uc?export=view&id=1XMOW_rKUSRjc9szhN14P7m79xP7cGsvg", # Bang Tobias
            "https://drive.google.com/uc?export=view&id=1XV9I7jUNnJkceWug4TBn6En7Ekcldw7V", # Kak Yohana Manik
            "https://drive.google.com/uc?export=view&id=1xDCj4-lRaxKfijwuPCJo3McA-4k0drBn", # Bang Rizki
            "https://drive.google.com/uc?export=view&id=11wq-zoMdklOp4Jjdtqbb-jvS8h1CSHQB", # Bang Arafi
            "https://drive.google.com/uc?export=view&id=1xKrLy8WboDAN-QUrEH4kx4eR395M_0C4", # Kak Asa
            "https://drive.google.com/uc?export=view&id=1XZq7bBGaRm00H3M3gS2SOP0Xn7TuhzCV", # Kak Chalifia
            "https://drive.google.com/uc?export=view&id=1Xfkir1WXTl5OvdAmLt6ACtPbCbYBP_Za", # Bang Irvan
            "https://drive.google.com/uc?export=view&id=11vnQ0ynSmS5HvvKcRB9SzeUHeDBLxJtT", # Kak Izza
            "https://drive.google.com/uc?export=view&id=11v19zxBlyrYOoaDMecLzZJK-NGa7h6D8", # Kak Khaalishah Zuhrah
            "https://drive.google.com/uc?export=view&id=", # Bang Raid
            "https://drive.google.com/uc?export=view&id=1XJeDJyqGZGQ5w72bYBZDeT4MfQPptsmn", # Kak Yuna
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
                "kesan": "Kakak nya seru dan asik banget",  
                "pesan":"semangat terus kuliahnya banggg!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak nya seru banget",  
                "pesan":"semangat terus kuliahnya ya kakk!!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "Kakak nya asik dan baik banget",  
                "pesan":"semangat terus kuliah nya kakk!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukit Tinggi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abang nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya banggg!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "dananghk_",
                "kesan": "Aabang nya seru banget dan baik banget",  
                "pesan":"semangat kuliahnya dan sukses terus ya bangg !!!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.Lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abang nya seru, dan baik banget",  
                "pesan":"semangat terus kuliahnya bang dan sukses terus bangg!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak nya seru dan asik banget",  
                "pesan":"semangat terus kuliahnya ya kakkk!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Menonton",
                "sosmed": "@alviagnting",
                "kesan": "Kakak nya baik dan seru banget",  
                "pesan":"semangat terus kuliahnya ya kakkk!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl.Nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya bangg, dan sukses selalu!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakak nya asik dan seru banget",  
                "pesan":"semangat terus kuliahnya kak dan sukses terus kak !!!"
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
                "nama"  : "Wahyudianto",
                "nim"   : "121450040",
                "umur"  : "22",
                "asal"  : "Makasar",
                "alamat": "Sukarame",
                "hobbi" : "Nonton Film",
                "sosmed": "@wayuraja",
                "kesan" : "Keren",  
                "pesan" : "semangat terus kuliahnya kakak !!!"
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
