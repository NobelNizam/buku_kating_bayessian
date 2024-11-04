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
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",#13
            "https://drive.google.com/uc?export=view&id=1PNPQY4fuslRsKLYN_Yy2cWjpB1ngNmmk",#12
            
            
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
            "https://drive.google.com/uc?export=view&id=1jl-v_hlQyoHSscHGB4XRSjp4mpV_-8Ec",#20
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
                "kesan": "Abangnya bener bener ngasah pikiran",  
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
                "kesan": "Kak abet asyikkk",  
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
                "kesan": "Kakak nya baik",  
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
                "kesan": "Kakak allya walaupun bercanda orang orang tetap was was wkwkwk",  
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
                "kesan": "Kakak nya seru",  
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
                "kesan": "abang nya lampung banget",  
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
                "kesan": "Kakak nya baik",  
                "pesan":"Semangat terus kuliahnya kakk!" 
            },
            {
                "nama": "Devyan Loxefal", #10
                "nim": "121450148",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang nya suka ngelawak",  
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
                "kesan": "Abang nya seru",  
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
                "kesan": "Abang nya pinter banget",  
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
                "kesan": "Kakak nya cantik",  
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
                "kesan": "Kakak nya baik",  
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
                "kesan": "Abangnya seru",  
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
                "kesan": "Kakak nya atlet banget",  
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
                "kesan": "abangnya menjawab pertanyaan aku banget ehehe",  
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
                "kesan": "Abang nya baik",  
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
                "kesan": "Kak Jeclin baik dan humble banget",  
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
                "kesan": "Aabang nya pendiem",  
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
            "https://drive.google.com/uc?export=view&id=1P_-skSrHvOb0Gy9pFFvALFSCWYYu12Gj", #1rafi
            "https://drive.google.com/uc?export=view&id=1Qr9ZhGopNpJnrJXsJVOX_aDRFnrDvopH", #annisa
            "https://drive.google.com/uc?export=view&id=1jZTHzQ8FFLr0nxDd5ADtlMLJp21V1qIv", #4sahid
            "https://drive.google.com/uc?export=view&id=1aLXZtR_O5_4qlnBv_fKwx4qTx_8MjKbW", #fadhil gada
            "https://drive.google.com/uc?export=view&id=1fNi9YHkQ9-Zp1A9-clbC3tG_WU4rdmk-", #regi
            "https://drive.google.com/uc?export=view&id=18uqLp-YLF3kVS7k66OPQG05i_Db0OZYL", #syalaisha
            "https://drive.google.com/uc?export=view&id=1aLXZtR_O5_4qlnBv_fKwx4qTx_8MjKbW", #nathanael gada
            "https://drive.google.com/uc?export=view&id=1jXzp7OKSnmywsnx1EPbQattBMIykTIQy", #anwar
            "https://drive.google.com/uc?export=view&id=1RkOA3ES_3fJ8bxfm7P_fRMX4TCHNExax", #deva
            "https://drive.google.com/uc?export=view&id=1QSFRRUqdIZOFC4rnpQYgAgA4Iytnhmuv", #dinda
            "https://drive.google.com/uc?export=view&id=1PUrWeMvcAxGwA9WArZNH3_QgCfTcOfYj", #marleta
            "https://drive.google.com/uc?export=view&id=1Rl3RTojfMk9P2hLBg9DTtzTFi4pTRZXC", #rut
            "https://drive.google.com/uc?export=view&id=1jOFhlJiyTaZhROv8fllB1kOAEGOj2gxq", #syadza
            "https://drive.google.com/uc?export=view&id=1aLXZtR_O5_4qlnBv_fKwx4qTx_8MjKbW", #abdurahman gada
            "https://drive.google.com/uc?export=view&id=1aLXZtR_O5_4qlnBv_fKwx4qTx_8MjKbW", #aditya gada
            "https://drive.google.com/uc?export=view&id=1Rc56rCSENKlorB1CObDgqN3F6v97PwSk", #eggi
            "https://drive.google.com/uc?export=view&id=1RdWGL1O5ri6yUaGAluOAFsMV3-aguZ-q", #febiya
            "https://drive.google.com/uc?export=view&id=1PTAVtzKXZBsUY0WrsyS1RvFhBmJzEGMe", #happy gada
            "https://drive.google.com/uc?export=view&id=1P_7jwzrUMGmQl1_fXh1gyk9fFjdhQkWb", #randa
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C", #vita

            
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
                "kesan": "Abang informatif banget",  
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
                "nama": "Ahmad Sahidin Akbar",      #4
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya seru banget",  
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
                "nama": "Muhammad Regi Abdi Putra Amanta", #6
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya mahasiswa aktif banget",  
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
                "kesan": "ga ekspek kalo kembar",  
                "pesan":"Semangat terus kuliahnya kak" 
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abangnya keren",  
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
                "kesan": "akhirnya ketemu mentor langsung wkwk",  
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
                "kesan": " keren bang ",  
                "pesan":" semangat kuliahnya" 
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "keren",  
                "pesan":" semangat kuliahnya" 
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
                "kesan": "Abangnya dulu astutor saya",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Vita Anggraini",
                "nim": "122450046",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ROSmwtz2uO08mXcqQ4hH3CGd06rfFVTg", # Bang Yogy 
            "https://drive.google.com/uc?export=view&id=1RNzPbYx93kD8PgsJf16LDvlcMbLh5PB4", # Kak Ramadhita
            "https://drive.google.com/uc?export=view&id=1R60vjvU1r8eoLlIuz93MwOhAKC7p-KDI", # Kak Nazwa Nabilla
            "https://drive.google.com/uc?export=view&id=1es6umH3sgPMGS4HOuP0oBU5z0OLBs3Pf", # Bang Bastian
            "https://drive.google.com/uc?export=view&id=1ek1Kkze695J4Hgdpnfwdz1rqmam75Amx", # Kak Dea Mutia
            "https://drive.google.com/uc?export=view&id=1ehWpqVNhVJLOG8ub31orQMT498VeWriP", # Kak Esteria
            "https://drive.google.com/uc?export=view&id=1RQfWOYhZyhtnbjqbzlpQrkPsiM-rMubg", # Kak Natasya Ega 
            "https://drive.google.com/uc?export=view&id=1R6ZUt7IINJvUkZOohISBUqxTRaW9UTfu", # Kak Novelia
            "https://drive.google.com/uc?export=view&id=1ZaURaEk4DUgV4gqXGs5xRMD9Fvf9VIvk", # Kak Ratu Keisha Jasmine
            "https://drive.google.com/uc?export=view&id=1evH_Odc0WXwqt-aEjUdaAkbQiONj6Z0J", # Bang Tobias
            "https://drive.google.com/uc?export=view&id=1f1M4fAlfz7AJvOzTBmVFE28mGYfJfQO6", # Kak Yohana Manik
            "https://drive.google.com/uc?export=view&id=1RACpTPOSYwYidRc9zqT2FHlKIIlIHCi2", # Bang Rizki
            "https://drive.google.com/uc?export=view&id=1RUJAeIJ4e60xwGxR2qWWgz-3ClrL-WYF", # Bang Arafi
            "https://drive.google.com/uc?export=view&id=1RmQWaeKHOp2jkFtbpCE-woae00P8MkiX", # Kak Asa
            "https://drive.google.com/uc?export=view&id=1ek1Kkze695J4Hgdpnfwdz1rqmam75Amx", # Kak Chalifia
            "https://drive.google.com/uc?export=view&id=1RmzlzRI6FsXuDafJN3iatBFulQk7QX4b", # Bang Irvan
            "https://drive.google.com/uc?export=view&id=11vnQ0ynSmS5HvvKcRB9SzeUHeDBLxJtT", # Kak Izza
            "https://drive.google.com/uc?export=view&id=1S_4VbhOa0R90ln06rlccKIHyKeXijwYS", # Kak Khaalishah Zuhrah
            "https://drive.google.com/uc?export=view&id=1euO1unb-gm4D0Qr4SZTauBkP6rzDN6G5", # Bang Raid
            "https://drive.google.com/uc?export=view&id=1R4wPuZijb2nhorDxtW3elL7tKyIXSaIm", # Kak Tri
        ]
        data_list = [
            {
                "nama": "Yogy Sa'e Tama",
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
                "hobbi": "Menggambar",
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
                "hobbi": "dengerin musik",
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
                "hobbi": "Surving sambil snorkeling",
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
                "hobbi": "Main Paralayang",
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
                "hobbi": "Tidur",
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
                "hobbi": "Menjahit Baju",
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
                "hobbi": "Berenang",
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
                "hobbi": "Main Bowling",
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
                "hobbi": "Berenang",
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
                "hobbi": "Berkuda",
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
                "hobbi": "Tepuk Semangat",
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
                "hobbi": "Membaca",
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
                "hobbi": "Nonton youtube",
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
                "hobbi": "Bertemu anak pengmas",
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
                "hobbi": "Mengaji",
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
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan" : "Abangnya sangat baik",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya bang"
            },
            {
                "nama"  : "Tria Yunani",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan" : "Kakak nya sangat baik",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K4s6zWGY-T_ciS0Gl-mtQtfH9scJOHEY",#dimas
            "https://drive.google.com/uc?export=view&id=1jlvous0r0MxeGiUOOZ9p3mGyYJZIGrIW",#cetrin
            "https://drive.google.com/uc?export=view&id=1K8q7JVpKXT0P4_mBojra5jKRGxLjtOA1",#akbar
            "https://drive.google.com/uc?export=view&id=1KCwyIaBPtvPiJezKcIRouist1rS0J6Qy",#rani
            "https://drive.google.com/uc?export=view&id=1K2lvNmwkrYL3pE7MQAAGcoC7kBikRmkY",#rendera
            "https://drive.google.com/uc?export=view&id=1KCsOei-3ytrm-6Lu27LdxW9KKVaNLb3n",#salwa
            "https://drive.google.com/uc?export=view&id=1KC1at7IU0cfvn8W_YET2Pstc2piBGxIf",#renta
            "https://drive.google.com/uc?export=view&id=1cpX6Bdy1GU8L5XzDgRp4erEHAtdxiNKR",#yosia
            "https://drive.google.com/uc?export=view&id=1jNiRLMS-91g2rff47JUUme27B1BpzRWA",#ari
            "https://drive.google.com/uc?export=view&id=1KBmqVrefAt_gDJZUU2Tv65uecvQdqYHS",#jo
            "https://drive.google.com/uc?export=view&id=1K5gkiilyB49ISpZQCpxng1HlVZ5pqGl5",#meira
            "https://drive.google.com/uc?export=view&id=1K9loMY57rMbxPP3iLcNKBKEDw-9Yy4ik",#rendi
            "https://drive.google.com/uc?export=view&id=1Pi-AxQWQSXVPnWVwD5RHvejgCfHmrs7i",#azizah
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
                "kesan": " public speaking nya bang dims keren banget",  
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
                "kesan": "Kakak nya asik ",  
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
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@ranipu",
                "kesan": "Kakaknya asik",  
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
                "kesan": "Abangnya seru dan sering ngejailin",  
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
                "kesan": "Kakak nya keren",  
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
                "kesan": "Abang nya agamis banget",  
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
                "kesan": "Bang jo asik",  
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
                "nim": "12450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Menyanyi",
                "sosmed": "@rexander",
                "kesan": "Abang nya seru",  
                "pesan":"semangat terus kuliahnya ya bang!"
            },
            {
                "nama":"Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak nya asik",  
                "pesan":"semangat terus kuliahnya ya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jg16aAkmmxd6c1NLDjqfHb6btKGLKb8-",#eror
            "https://drive.google.com/uc?export=view&id=1f9rntKRbfhEJJ2cwxIGFmQ0JFHSaZAc7",#adisty
            "https://drive.google.com/uc?export=view&id=1f6ivhD5wv772ppZkvUdMpmSgV0yFrJp5", #nabila
            "https://drive.google.com/uc?export=view&id=1jca99hM2WPoLJX5X8F68L7SwZHUNGcwT", #ahmad eror
            "https://drive.google.com/uc?export=view&id=1jcZMM4fOso_Ob9DRffTgBqSu0L0ganPY",#danang eror
            "https://drive.google.com/uc?export=view&id=1jaTj21Uy9c3_OvGDFb_JUKw62OuSWCST", #6farel eror
            "https://drive.google.com/uc?export=view&id=1fAwV2QxM87sgjPGblugmbol4u3mIkybq",#tessa
            "https://drive.google.com/uc?export=view&id=1fCBU51z6DrHjKfi0_3TBaYnIGQq-RcIg",#nabilah
            "https://drive.google.com/uc?export=view&id=1RuqYxcgxL4UtERPNIGhKfwjUEphg1G0f", #alvia
            "https://drive.google.com/uc?export=view&id=1RxKuv7Wbx7x21ozKhknVkLqL03OROKSo",#davin
            "https://drive.google.com/uc?export=view&id=1fCzVVS60Pzb69rH0mWo_9ygiz-wLxT34",#elia
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
                "kesan": "dapat banyak ilmu dari abangnya",  
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
                "kesan": "Kakak nya keren",  
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
                "kesan": "kakanya asik",  
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
                "kesan": "Abang nya kalem",  
                "pesan":"semangat terus kuliahnya ya banggg!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Abang nya seru banget",  
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
                "kesan": "seruu",  
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
                "kesan": "Kakaknya baik",  
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
                "kesan": "Kakaknya baikkk",  
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
                "kesan": "Kakak nya baik",  
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
                "pesan":"semangat kuliahnya"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Menyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakak nya asik",  
                "pesan":"semangat kuliahnya!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M0_IG_Fo7vX058EKo3ZeFms16Svji2Yy", #wahyudito
            "https://drive.google.com/uc?export=view&id=1QwHcqlbpxkq3rK-P26kHgyWYxLcIYrBo", #elok
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",#arsyiah gada
            "https://drive.google.com/uc?export=view&id=1QWOEkDAUMYLU3HYqYo90RtIB0ZulKEv9",#cintya
            "https://drive.google.com/uc?export=view&id=1aHZTjU1azuTMxrRNVHyx1lJlX9Elel-C",#najla
            "https://drive.google.com/uc?export=view&id=1mutd8zVggpr0e7QDLH-f2RLW4CdON5tt",#patricia
            "https://drive.google.com/uc?export=view&id=1QSUyQiis9a45zoImUuVIa3r9WMB4vwwP",#neli
            "https://drive.google.com/uc?export=view&id=1fkGfPH4LqHmU7zcOA__OcsssrQinSKn1",#try
            "https://drive.google.com/uc?export=view&id=1fhm9Xekoq6aXOmhOuD8M-mERb1Vydflz",#m. kaisar
            "https://drive.google.com/uc?export=view&id=1jIVn_YUaDwUlyCfqbyjsIeycd0E7KT8u",#dwi
            "https://drive.google.com/uc?export=view&id=1QXekgCOYbMFh8T1ZXMrVSc_7x0puSE_A",#gymnastiar
            "https://drive.google.com/uc?export=view&id=1fjhP3XUv5d_-kWOP-WhC899yYRRTI_9r",#nasywa
            "https://drive.google.com/uc?export=view&id=1QZVgvXWuC-gkjpTYqLa9mqlBY_JuUaNz",#priska
            "https://drive.google.com/uc?export=view&id=1QU078Q5rO2-kO4gyG_KWx7DJcMKhEMYL",#m. arsal
            "https://drive.google.com/uc?export=view&id=1Qh_FLYApWVrrJDkalBiz-4Uc733nDZDQ",#abit
            "https://drive.google.com/uc?export=view&id=1Qa3H8Q_1ERypnz3-D0HKa5DlVkWBt-n7",#akmal
            "https://drive.google.com/uc?export=view&id=1QcQHbsxkSumeOdKpii54IeL_Q1wLh_xp",#hermawan
            "https://drive.google.com/uc?export=view&id=1QccWn2qi6h9WhDxabKAlIjzUFljsYuvp",#khusnun
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
                "kesan" : "Abangnya sangat informatif",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinyaa"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Ngedit",
                "sosmed": "@elokfiola",
                "kesan" : "Kakak banyak memberikan motivasi",  
                "pesan" : "Tetap semangat kak kuliahnya"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.",
                "kesan" : "Kakak nya sangat baik, dan informatif",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "humble banget",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya ya kak"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Kakak nya baik dan sangat menginspirasi",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak"
            },
             {
                "nama"  : "Patricia Leonrea Diajeng Putri",
                "nim"   : "122450050",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi" : "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan" : "Kak cia baik,lembut banget, dan dabest banget",  
                "pesan" : "Tetap semangat kuliahnya ya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Jl.Pembangunan 5, Sukarame",
                "hobbi" : "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan" : "Kakak nya baik dan humble",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Kakak nya cantik ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Abangnya mageran wkwk",  
                "pesan" : "Tetap semangat dalam menjalani dunia perkuliahan bang"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Pemda",
                "hobbi" : "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan" : "Kakak nya baik",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf",
                "hobbi" : "Nyari tuyul baskat",
                "sosmed": "@jimnn.as",
                "kesan" : "Abangnya pdd banget",  
                "pesan" : "Semangat bang dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1",
                "hobbi" : "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan" : "Kakak nya cantik",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Karaoke",
                "sosmed": "@prskslv",
                "kesan" : "Kakaknya baik ",  
                "pesan" : "Tetap semangat kak kuliahnya"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi" : "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan" : "Abangnya sangat baik",  
                "pesan" : "Tetap semangat bang dalam menjalani kuliahnya"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Main uno",
                "sosmed": "@abitahmad",
                "kesan" : "Abangnya baik banget dan humble",  
                "pesan" : "Tetap semangat bang dalam menjalani kehidupan"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Bang Akmal baik banget, sabar banget, dan dabest juga",  
                "pesan" : "Tetap semangat kuliahnya ya bang dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Jalan dekat tol",
                "hobbi" : "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Abang nya sering ngeledek",  
                "pesan" : "Tetap semangat kuliahnya banggg"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi" : "Beantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Kakak nya baik",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya dan jaga kesehatan"
            },
        ]        
        display_images_with_data(gambar_urls, data_list)
    medkraf()
