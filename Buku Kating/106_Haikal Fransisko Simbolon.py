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
            "https://drive.google.com/uc?export=view&id=1XAZHh2TwNH-lDiaQE9QCVLgeavMyDqEG", #bg Gumi
            "https://drive.google.com/uc?export=view&id=1XVZyPm1Bl32cHXki49QPRreToHccC7Fo", #bg Pandra
            "https://drive.google.com/uc?export=view&id=1XXVbztFjvJT_TSyuBr2S2axIjIkDnVMH", #ka Meliza
            "https://drive.google.com/uc?export=view&id=1X_706mc1nc0dy8y9zXskGm0sPZQcM_zh", #Ka Titi
            "https://drive.google.com/uc?export=view&id=1XZOCF9xQmrpxhKLSW1P34HzG2apzUdkC", #Ka Putri
            "https://drive.google.com/uc?export=view&id=1X14hzKP1ug5BEiz1vsrApWDcZH_Ad_7Q", #Ka Nadilla
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang ini keren dan asik",  
                "pesan": "Sukses selalu bang dan infokan tempat magang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Bukit Kemuning, Lampung Utara",
                "alamat": "Jl. Bawen 2",
                "hobbi": "Main Gitar",
                "sosmed": "@pandrainsani",
                "kesan": "Abang ini lucu, asik, keren",  
                "pesan": "Sukses selalu bangg, dan tetap selalu ngelawak"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya kerenn dan asikk",  
                "pesan": "Suksess selalu kak dan jangan dilupakan HMSD ini"# 3
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "Kakaknya keren jadi Bendahara Umum HMSD ",  
                "pesan": "Tetap dengan jiwa kebendaharaan dan sukses selalu kak"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "122450000",
                "umur": "18",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Keren banget dan betah banget dengerin bang Pandra gitaran",  
                "pesan": "Sukses ya kak dan Semoga bisa main gitar juga biar ga ngedengerin doang"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakaknya asik dan kerennn",  
                "pesan": "Sukses selalu kak dan tingkatkan jiwa kebendaharaan nya"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UiJmKQEawtDpLAd_AmX0Ha5jE9gzCs2y",#kak Tri
            "https://drive.google.com/uc?export=view&id=1UZasM7r7oYIcoHeikiG27MJwvkf1T_fr",#Kak Annisa
            "https://drive.google.com/uc?export=view&id=1UuU9ynMYrL492E2czXUJU-ifg4xVQvl_",#Kak Wulan
            "https://drive.google.com/uc?export=view&id=1U_Q5tvCiA8qTAsR7GDjbDE7-0oFwcIr4",#Kak Anisa Dini
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
            "https://drive.google.com/uc?export=view&id=1Uo2MmyKXCVfE6wE1s6R1eYVv3KAvzYjK",#Bg Feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Renisha
            "https://drive.google.com/uc?export=view&id=1UdZ6AMpXC-xOql9Y7iWs0eXYrkjgCJF6",#Bg Mirzan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#Kak Anisa Fitri
            "https://drive.google.com/uc?export=view&id=1Uv0Hm5UCaoMpDJDy2By0gCPIuRLxug8Y",#Kak Dhea
            "https://drive.google.com/uc?export=view&id=1TnrW_EDC6ZUN10MyQB7n5tObcOqaaLCz",#Bg Fahrul
            "https://drive.google.com/uc?export=view&id=1TtIFuOl8BxQTUbSIbEWbP2LXNnGdsLz-",#Kak Berliana
            "https://drive.google.com/uc?export=view&id=1UxZZppwdYBq2bOMr-_pGurcWUAlb79HV",#Bg Jere
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
                "kesan": "Kakak asik banget orangnya, keren lah pokoknya, suka ngelucu lagi",  
                "pesan": "Semoga dilancarkan segala urusannya, dan sukses selalu kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak keren dan pinter juga",  
                "pesan": "Sukses kak dan dilancarkan urusannya karna bentar lagi nyusun"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "18",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya baik, keren, asikk",  
                "pesan": "Semangat kulaihnya kak, dan dibawa santai aja kak"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya asikk, suka bercanda, dan orangnya ceria betul",
                "pesan": "Sukses kak kuliahnya dan dilancarkan segala usahanya"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini keren kalee, asikk, suka ngelawak",  
                "pesan": "Sukses lah bang dan lancar ngasprak nya"
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "-",  
                "pesan": "-"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya keren, asik, tinggi lagi",  
                "pesan": "Sukses bang dan lancar segala usahanya"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@ansftynn_",
                "kesan": "",  
                "pesan": "-"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asikk, lucu karena suka banget bercanda",  
                "pesan": "Sukses selalu kak, happy terus biar ga stres, suka bercanda nya kembangin terus"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "Abangnya keren, dan awal pertama saya lihat kukira abang orang batak ternyata tidak",  
                "pesan": "Semangatt bang, sukses selalu, dan ajarin badminton bang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "Kakaknya baik, keren, tapi agak pendiam ya kak (kira sama-sama pendiam kak)",
                "pesan": "Semangat kuliahnya kak, dibawa santai aja biar ga stres"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini keren dan suka banget ngelawak",
                "pesan": "Sukses selalu bang dan semangat terus ngelawak nya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XoJkbzDLOsNMFeocaAdnU3sIz_WbLR7C",
            "https://drive.google.com/uc?export=view&id=1XmQpdTEMqLtQy_CrqO-v95l12z0v1hsj",
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
                "kesan": "Public speaking kakaknya keren banget, pinter lagi, dan kadang saya takut dengan keseriusan kakaknya ",  
                "pesan": "Sukses selalu kakak senat, semangat terus kak dan ajarin saya agar bisa seperti kakak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfi nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini keren, baik", 
                "pesan": "Sukses selalu bang dan semangat kuliahnya "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TRS9FXmSj2-7XWxkG4gfRluKE3-UGLai", #Bg Econ
            "https://drive.google.com/uc?export=view&id=1d11olr6xwViF3YKaIudZFcag2D_Ti4eu", #Kak Elisabeth
            "https://drive.google.com/uc?export=view&id=1RHkYhEsB5svwboUh7SLdA_AS3IF_TBGF", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1UJULTEhULgC2Lf1KzWf-2NUPZfVp3Fsu", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1ctKPupUQ1vhd0RwXATVypOw1xCgWtqBZ", #Kak Eksanti
            "https://drive.google.com/uc?export=view&id=1RD1ouY5OM3JEEnPGE9ItNhrxC2C9Etvw", #Kak Hanum
            "https://drive.google.com/uc?export=view&id=1dNO-HXSsNjekbrbYT6jJmtSKknMCgPc1", #Bg Ferdy
            "https://drive.google.com/uc?export=view&id=1QZFUpsxUKmk9BrRW3uJnLUVHmrQmlIpM", #Bg Deri
            "https://drive.google.com/uc?export=view&id=1cxVfzzrd_YcGfAvI8PLcczSERD1dU39B", #Kak Oktavia
            "https://drive.google.com/uc?export=view&id=1SMvJrB-HaWkgH0Ck1ZHWBhF-QXzyr_on", #Bg Deyvan
            "https://drive.google.com/uc?export=view&id=1UDHFH-HDrzJUJK9xYdzrOXwBYPawZySj", #Bg Jo
            "https://drive.google.com/uc?export=view&id=1U2kpMXU1PrWqQmWSq5mwZcJ3WcWWJm1E", #Bg Kemas
            "https://drive.google.com/uc?export=view&id=1ZJoKibhydoyU_CR67mRU0A1VK8jROS0l", #Kak Presilia
            "https://drive.google.com/uc?export=view&id=1PY-lHddyZV04kjiC7DKpMFhMOzULHinl", #Kak rafa
            "https://drive.google.com/uc?export=view&id=1d18Y4jQyWBjX0aYZLa6eQjDlml3dLbPR", #Bg Sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
            "https://drive.google.com/uc?export=view&id=1dCVTtYt2k3yvrRsTA7EgNWIVUaeVUQlF", #Bg Ateng
            "https://drive.google.com/uc?export=view&id=1czEtR2Oh-TR0wIcJXqYwIkik-ASyKO16", #Bg Gede
            "https://drive.google.com/uc?export=view&id=1qYxaf7JqbMduHmg3xsYzM4K65JiG9Jlw", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1-d6IYoJ7rHRwzKHLxvEiATUgpxU-DP1s", #Bg Rafly
            "https://drive.google.com/uc?export=view&id=1dCDIKpZxBGRAF9hcdjfWXlJoiG8STTBf", #Kak Syalaisha
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya keren dan public speaking nya juga keren, tegas",  
                "pesan": "Sukses selalu bang kadep, semangat terus bang" # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya keren, caria banget kelihatannya",  
                "pesan": "Sukses kak, semangat terus kakkk" # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jailin Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakak nya baik dan kerenn dan asik juga tapi jangan jailin saya lagi kak",  
                "pesan": "Sukses terus kakak ketuplak, semangat terus ya kakkk" # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya keren dan tegas",  
                "pesan": "Jangan serem-serem kak, sukses selalu dan semangat terus" # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya Keren, Tegas juga, baik",  
                "pesan": "Semangat kak ngasprak kami yang banyak tidak mengertinya dan sukses selalu" # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya baik, asik, keren",  
                "pesan": "Semangat kak, sukses selalu, dilancarkan segala usahanya" # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini keren, baik, jago futsal tapi kek agak pendiem (gatau ya cuma ke angkatan 23)",  
                "pesan": "Semangat bangg, tingkatkan hobinya, dan sukses selalu" # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": "Abangnya baik, keren, senyum mulu bang",  
                "pesan": "Semangat terus bang dan semoga senyum terus sampai S1" # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya keren, baik, dan asik juga",  
                "pesan": "Sukses terus kak dan semangatt teruss" # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang ini keren, lucu, baik",  
                "pesan": "Sukses selalu bang, tetap lah ngelawak sampai kapanpun" # 10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": "Abangnya keren, asik, dan suka marah-marah",  
                "pesan": "Semangat terus bang dan kurangin marah-marah nya nanti cepat tua wkwk" # 12
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya keren, baik, cool, si sepuh ngoding",  
                "pesan": "Sukses terus bang dan ajarin saya lagi tentang codingan " # 13
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": "Kakaknya cantik, baik",  
                "pesan": "Semangat ngaspraknya kak, sukses selalu dimana pun" #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya kerenn, baik, suka belajar lagi beuhh",  
                "pesan": "Sukses selalu kak dan semangat belajarnya " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abangnya keren, baik, asik",  
                "pesan": "Semangat terus bang dan sukses selalu" # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak ini asik, jago basket, baik",  
                "pesan":"semangat terus kuliahnya kak dan tingkatkan basket data kita"# 1
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya keren, baik, asik",  
                "pesan": "Semangat terus bang dan sukse dimanapun dan gasken buat acara DSC lagi bang" # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya keren, baik, asik",  
                "pesan": "Sukses selalu dan tetap semangat bangg" # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakaknya baik, keren, cantik, ceria selalu",  
                "pesan": "Tetap ceria kak, semangat terus dan sukses selalu" # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang nya baik, pendiam",  
                "pesan": "Tetap semangat bang, sukses selalu" # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak nya baik, kembar lagi, jadinya kemarin saya kira satu orang",  
                "pesan": "Semangat terus kak dan sukses selalu dan buat perbedaan dikit lah kak sama Andina nya" # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bMbKxhIZWAddzfTqIH-e0_AygdKrcm9e", #Bg Rafi
            "https://drive.google.com/uc?export=view&id=1bKsSIPcHPptzZ2ja7LN4NXgzI-u0qzY4", #Kak Annisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Mujadid
            "https://drive.google.com/uc?export=view&id=1cFV1XA1o7qQc97iFElA5hAao8mXSjnrA", #Bg Ahmad Sahidin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Fadhil
            "https://drive.google.com/uc?export=view&id=1cORQ_9bJwCn22QXfYCFJQ_6PlY6M9Xrm", #Bg Regi
            "https://drive.google.com/uc?export=view&id=1bpJ2L7acmWKOsEdwVbDjyhZqF_tR9zeg", #Kak Syalaisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Natanael
            "https://drive.google.com/uc?export=view&id=1cIJY8d2rGx7yg0b-kgQ_VucI8xVUz7Il", #Bg Anwar
            "https://drive.google.com/uc?export=view&id=1aq7W1x7627RhSwkHmIFG4LaDg1UqBc7G", #Kak Deva
            "https://drive.google.com/uc?export=view&id=1cC_pvSLLqtOFiAk-AXzldB3C7-Sqe81E", #Kak Dinda
            "https://drive.google.com/uc?export=view&id=1beSZGRlpCpqxMZfRiPJJQW6ogmfqeJyi", #Kak Marleta
            "https://drive.google.com/uc?export=view&id=1akL5qQlLKNmmUu6_JVOYjouKBYisQqwp", #Kak Rut Junita
            "https://drive.google.com/uc?export=view&id=1cNoI-BBUMCOCV8Tj4Z23kIe-AyIeFRlE", #Kak Syadza
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Abdurrahman
            "https://drive.google.com/uc?export=view&id=1ageKRM6M0JX6kJGn7WAsGagR5ayUSpfG", #Bg Aditya
            "https://drive.google.com/uc?export=view&id=1apsAS1N2RmVukj1WfQZKByFDJk5uXYGc", #Bg Eggi
            "https://drive.google.com/uc?export=view&id=1buQlY10Zcm9rjE2hDvXeR0YmjweBaQlV", #Kak Febiya
            "https://drive.google.com/uc?export=view&id=1c8VGWi8vlB6KIdxQsfSeGJKiKKjx2OUA", #Bg Happy
            "https://drive.google.com/uc?export=view&id=1bDXQ3iQEwiDiB0RkQl-bQWtyS7TsGW-j", #Bg Randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
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
                "kesan": "Abangnya asik, pinter, keren",  
                "pesan": "Sukses selalu bang, tetap semangat dan ajarin saya coding" # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak nya baik, keren, asik",  
                "pesan": "semangat kuliah nya kak, bentar lagi nya ye kan kak, sukses selalu" # 2
            },
            {
                "nama": "Mujajid Choirus Surya",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "Belum ketemu abangnya",  
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
                "kesan": "Abangnya keren, asik, baik, sabar",  
                "pesan": "Semangat terus bang, jangan nge down lagi kalau voli wkwk" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya baik, keren, asik",  
                "pesan": "Semangat terus bang, sukses selalu" # 5
            },
            
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Kerenn, asik, baik",  
                "pesan": "Semangat kuliah nya bang, dibawa santai aja biar tidak stres" # 6
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya baik, tapi agak pendiam dikit, kembaran kak Andini",  
                "pesan": "Semangat terus kak, tolong berikan saya tanda perbedaan kakak dengan kak Andini" # 7
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Belum bertemu abngnya",  
                "pesan": "Semangat aja bang dan semoga kita ketemu"# 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya baik, keren, agak pendiam tapi pinter + sabar",  
                "pesan": "Sukses terus bang, semangat ngasprak nya juga" # 9
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknya asik, keren, baik",  
                "pesan": "Sukses ya kak, semangat terus, bawa santai aja di dunia ini" # 10
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": " ",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya baik, pinter, sabar",  
                "pesan": "Semangat ngasprakin kami kak, sukses terus" # 11
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya asik, baik, keren lah",  
                "pesan": "Semangat terus kak, sukses selalu, dan tetaplah menjadi orang yang asik dimata orang lain" # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya baik, keren, pinter",  
                "pesan": "Semangat terus kak, mari kita lancarkan acara riuh kita wkwk" # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya keren, baik, asik",  
                "pesan": "Tetap semangat ya kak, ceria kan terus dunia ini kak" # 14
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abangnya keren, baik",  
                "pesan": "Sukses selalu bang, terus semangattt" # 15
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abangnya baik, keren, asik, pinter",  
                "pesan": "Semangat terus bang, semoga abang menjadi pemateri lagi di kaderisasi selanjutnya" # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abangnya keren, asik, pinter",  
                "pesan": "Semangat terus bang, sukses selalu dan ajarin saya coding bang" # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya asik, keren, baik",  
                "pesan": "Tetap semangat kuliah nya kak, bawa santai aja dunia ini kak" # 18
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya keren dan baik banget",  
                "pesan": "Tetap semangat ya bang kuliahnya" 
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya keren, baik, asik juga ",  
                "pesan": "Sukses terus bang, semangat menjalani dunia yang penuh drama ini" # 20
            },
            {
                "nama": "Vita Anggraini",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "Kakak ini belum diwawancarai",  
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z0WEdgY8xcJ8gRlLHG76JTE1P10rY_U7", #Bg Yogi
            "https://drive.google.com/uc?export=view&id=1ZZTjHmRH-D6Ey3awl6S9vdt2gsgLVEg5", #Kak Ramadhita
            "https://drive.google.com/uc?export=view&id=1ZApD459P-lzMdYeSN8QVMw7ZVATc69q5", #Kak Nazwa
            "https://drive.google.com/uc?export=view&id=1_QKino364gs62LCgk7vyFiswSpu89zJ0", #Bg Bastian
            "https://drive.google.com/uc?export=view&id=1ZYinfEC-sbmuBtNKZfrpWfW5s9fc9qYl", #Kak Dea
            "https://drive.google.com/uc?export=view&id=1_RmDZeuk359EJw7LW-mBjHG2rKsw-BQA", #Kak Esteria
            "https://drive.google.com/uc?export=view&id=1ZHNyatPawKy4RJt9N6HzT4SDZCjNpCF_", #Kak Natasya
            "https://drive.google.com/uc?export=view&id=1Z3Ez1oWkvUsXCDa1umMW2pGr3s1wmRzZ", #Kak Novella
            "https://drive.google.com/uc?export=view&id=1ZRCo5u8usJT5QFFs-h46rv3cSCIIso5O", #Kak Jasmine
            "https://drive.google.com/uc?export=view&id=1_IJKa235z5IigSNJm_yqMVraq01hGGWL", #Bg Tobias
            "https://drive.google.com/uc?export=view&id=1_cwCmj3FCyF9KuT9DEmmsbOq98D9YAkB", #Kak Yohana
            "https://drive.google.com/uc?export=view&id=1ZEwzGqA723tJvYmcBfEKGzQdJvlzculF", #Bg Rizki
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Arifa
            "https://drive.google.com/uc?export=view&id=1ZAp8NkjlGLtDPQJl4K2R1uHyZD1Mm3zr", #Kak Uyi
            "https://drive.google.com/uc?export=view&id=1_apaVuIMQCf0Q2Xye18ZtbG08OsTwKmD", #Kak Chalifia
            "https://drive.google.com/uc?export=view&id=1ZKByOP3OsZ8HJX2gioVMh3oHa7ySbWEr", #Bg Irvan
            "https://drive.google.com/uc?export=view&id=1Yvh9DP39nyvG4gMXll2W3J6QJ2DEvOYk", #Kak Izza
            "https://drive.google.com/uc?export=view&id=13Ts9YzvkvTYURtDiuch_w_ovHHzGoY05", #Kak Khaalishah
            "https://drive.google.com/uc?export=view&id=1_B6f_c5S6wXRIqiwPjdXgchQHlHrVkvY", #Bg Raid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Tria

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
                "kesan": "Abang nya keren, asik, keknya suka roasting orang",  
                "pesan": "Semangat selalu bang, sukses lah di kadep periode ini" # 1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakaknya keren, baik, asik juga",  
                "pesan": "Sukses selalu kak, tetap semangat di gempuran drama dunia" # 2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kandis ",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya asik bangett, baikk juga",  
                "pesan": "Tetap asikin semua orang ya kak terutama angkatan 23 ini dan sukses selalu" # 3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang ini juga keren, baik juga",  
                "pesan": "Sukses selalu bang, tetap semangat 45" # 4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak nih keren, baik dan asik",  
                "pesan": "Semangat terus ya kakk" # 5
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Bali",
                "alamat": "Sukabumi",
                "hobbi": "Serving sambil snorkeling",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini asik dan nampak kali muka bataknya kak",  
                "pesan": "Tetap semangat kak, sukses selalu" # 6
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Kepulauan seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee__15",
                "kesan": "Kakaknya keren, asikk juga, baikk",  
                "pesan": "Semangat terus ya kak, dan tetap lah menjadi orang yang meng asikkan" # 7
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya cantik, baik, keren, asik",  
                "pesan": "Tetap asikin orang lain kak, semangattt" # 8
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini baik, sabar, keren, se NIM saya lagi",  
                "pesan": "Tetap semangat kak kuliahnya ataupun ngasprak nya" # 9
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal": "Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini baik, keren bgt gondrong nya bang",  
                "pesan": "Sukses selalu bang, dan tetap lah gondrong sejati" # 10
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya keren, muka kakaknya komdis bet",  
                "pesan": "Semangat kakk, jangan marah-marah kak nanti cepat tua loh" # 11
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang ini keren, baik, asik",  
                "pesan": "Sukses selalu bang dan tetap semangat" # 12
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya baik, asik, keren",  
                "pesan": "Teteplah menjadi diri sendiri ya bang, diri sendiri yang penuh semangat dan sukses" # 13
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik, keren, sabar, namanya keren juga",  
                "pesan": "Berikan saya arti nama kakak dong, semangatt terus ya kak" # 14
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "Kakak nya keren dan baik, asik juga",  
                "pesan": "Tetap semangat dan sukses selalu kak" # 15
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik, keren, sabar",  
                "pesan": "Semangatt ya kak, sukses selalu" # 16
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu anak Pengmas",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak nya asik bangettt, friendly bet dah, baik, sabarr, ",  
                "pesan": "Tetap lah pada pendirian yang mengasikkan kak, sukses dan tetap semangat" # 17
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini baik, keren, dan pinter",  
                "pesan": "Semangat kakk, sukses ya kak" # 18
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di wico",
                "sosmed": "@rayths_",
                "kesan": "Abang ini baik, keren, pinter juga",  
                "pesan": "Semangat kuliahnya bangg" # 19
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini keren, baik, dan sabar",  
                "pesan": "Semangat kuliahnya kak dan dibawa santai aja dunia yang penuh dengan drama ini" # 20
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aVUzIvdRe4-eurfWqUn5Lf9cyuUOH45J", #Bg Dimas
            "https://drive.google.com/uc?export=view&id=1afYRNnYVw7wWIJw47SzNiW-QthquqEcD", #Kak Catherine
            "https://drive.google.com/uc?export=view&id=1aaaMK0YShyLhpM0i9-icDriMsdB4MwNr", #Bg Akbar
            "https://drive.google.com/uc?export=view&id=1aIS3cWTblIUvCqZ6srThgShqD4uvqzyA", #Kak Rani
            "https://drive.google.com/uc?export=view&id=1aXMFEjU5VzACe4ixJyahbmkYmvxlEBk9", #Bg Rendra
            "https://drive.google.com/uc?export=view&id=1_deEmzAJAUOp_2iUDqfbz7lRKYgl6wE2", #Kak Salwa
            "https://drive.google.com/uc?export=view&id=1aHo-MKBtkODhOrau6rwXJyUXfpxvzy1f", #Bg Yosia
            "https://drive.google.com/uc?export=view&id=1aKCnRVLudFuPLLnwF5Yla9z6isjjFoOk", #Kak Renta
            "https://drive.google.com/uc?export=view&id=1_gtjlI64Y4jfjINx_hq_6oVmJCcf6t3B", #Bg Sigit
            "https://drive.google.com/uc?export=view&id=1_dYPu4CHVinpmFMSYtS_uxhMByb98iJS", #Bg Josua
            "https://drive.google.com/uc?export=view&id=1_jvIsQyVgiH28TIWWucfEAgOmsoGT9dF", #Kak Azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Dearni
            "https://drive.google.com/uc?export=view&id=1aZzwHPX96OK_hjig-rTnHuV4_zmibPam", #Kak Meira
            "https://drive.google.com/uc?export=view&id=1a9iLYfc-VLMFmbq9JRchJf1siH862DOG", #Bg Rendi
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
                "kesan": "Abangnya keren banget, baik, pinter,asik pula, sang mantan ketuplak PEMIRA",  
                "pesan": "Semangat terus bang menghadapi kesibukannya yang setiap hari" # 1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakak ini cantik, keren, baik banget, sabar banget",  
                "pesan": "Semangat terus kak, dan sukses selalu" # 2
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya keren, cool, pinter, asik",  
                "pesan": "Sukses selalu bang dan tetap semangat" # 3
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@ranipu",
                "kesan": "Kakak ini baik, keren, udh tau orang nya tapi belum foto",  
                "pesan": "semangat terus kuliahnya ya kakak!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya keren, asik dan baik",  
                "pesan": "Tetap semangat kuliahnya bang, dan sukses selalu menjadi ketuplak Riuh Wisudawan" # 5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakaknya baik, keren, sabar",  
                "pesan": "Tetap sabar ya kak, semangattt" # 6
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya keren, baik, asik",  
                "pesan": "Kok mau di tarik bang Dimas sih bang? wkwk semangat bangg" # 7
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakaknya baik, tapi agak pemalu sih keknya",  
                "pesan": "Semangat ya kakk" # 13
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang ini sabar banget, keren, cool, jago futsal lagi",  
                "pesan": "Tetap lah menjadi pria sejati di futsal bang, tetap semangat" # 8
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abang ini lucu, keren, baik",  
                "pesan": "Semangat bangg, lebih lucu lagi kedepannya" # 14
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya baik, keren, pinter, agak pendiam",  
                "pesan": "Semangat terus kuliahnya kak" # 9
            },

            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakaknya baik, sabar",  
                "pesan": "Semangat terus kak, sukses selalu" # 11
            },

            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abang ini keren, baik",  
                "pesan": "Sukses ya bang, tetaplah menjadi orang baik untuk selamanya" # 12
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dVuvFXENLh6csJQ6iwaNjgRm9crbNAtx", #Bg Adrian
            "https://drive.google.com/uc?export=view&id=1eTNCbr_s2J8cofyeKydCEqOlMxqYGPht", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1eJvmBWvKp5dUjSjpGOEuFamOTcJPOErO", #Kak Nabila
            "https://drive.google.com/uc?export=view&id=1fLCviEJa-QVraVBdyjZtsyuoEXju-Bv0", #Bg Ahmad
            "https://drive.google.com/uc?export=view&id=11ulv2m3i1leirV5GVWTCMdNJMDx9rUuj", #Bg Danang
            "https://drive.google.com/uc?export=view&id=11ngfWqIMR-CgV3jNV1syjjPz-sqFRknU", #Bg Farrel
            "https://drive.google.com/uc?export=view&id=1dvWUBvrrTufOQOGn2VLw9jlu19tA0FJr", #Kak Tessa
            "https://drive.google.com/uc?export=view&id=1eAp7zGIA20sBI9CyiF1em3mbfINGrehD", #Kak Nabilah
            "https://drive.google.com/uc?export=view&id=1fLdrUUYyh9TtjyF6pAFnsW2w3eUiXsit", #Kak Aliva
            "https://drive.google.com/uc?export=view&id=1dvWd_9DCUfS56gbdO3RjQ2N31tgLyX2V", #Bg Dhafin
            "https://drive.google.com/uc?export=view&id=1fClGmzZMwWshjvvNWrvVLWdOgUWPd-Wr", #Kak Elia
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Sidikalang",
                "alamat": "Dekat Penjara",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abang ini cool bet, baik, pinter, asik",  
                "pesan": "Semangat mencari uang nya bang, biar langsung nikah wkwk" # 1
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini baik, pinter, asik",  
                "pesan": "Sukses selalu kak, tetap semangat ya kak" # 2
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakaknya asik, baik, keren",  
                "pesan": "Semangat teruss kuliahnya kak" # 3
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittinggi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abangnya keren, cool, baik",  
                "pesan": "Tetap Stay cool dan semangat terus" # 4
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini keren, asik, asprak ADS saya",  
                "pesan": "Tetap semangat ngasprak nya bang, sukses selalu" # 5
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abang ini keren bet, badannya tinngi + bagus",  
                "pesan": "Ajarin saya gimana caranya punya badan begitu bang" # 6
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik, baik",  
                "pesan": "Semangat terus kak dan sukses selalu" # 7
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya baik, asik, sabar juga",  
                "pesan": "Semangat kuliahnya kakak" # 8
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "kakaknyaa lucu, baik, agak pendiam kelihatannya",  
                "pesan": "Semangat dan sukses selalu ya kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya keren, asik juga",  
                "pesan": "Sukses selalu bang, jangan lupakan Tuhan" # 10
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya keren, baik, asik, bilang saya mirip bang Andrian padahal tidak",  
                "pesan": "Tetap semangat dan jangan lupa berdoa kak" # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
    
elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WA2na6qDLH3uJ68N7_YgJI-_XfHx6Sa2",
            "https://drive.google.com/uc?export=view&id=1lcPE8TN2gRMss0TvkMHGCRCKBUfSiMNp",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3 kosong
            "https://drive.google.com/uc?export=view&id=1CO-K8V4MC5iG3Jj18CEcic051nivwTyO", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5 kosong
            "https://drive.google.com/uc?export=view&id=1VS-3BZXnIWfF0l-1_kWWLFyUxxcRiRQA",
            "https://drive.google.com/uc?export=view&id=1WQFklP5v1FZou85KCSOFoLzzsTf-Mj2y",
            "https://drive.google.com/uc?export=view&id=1WYWNTZdwXXYJkwJ2d34pmCUzp7yNaFv5",
            "https://drive.google.com/uc?export=view&id=1Wqm1jdzkxjgTdwEZyisfPCqvWiL1iQ6X",
            "https://drive.google.com/uc?export=view&id=1WP50i506HjzPVNeTOnTgutd3NaOaALcn",
            "https://drive.google.com/uc?export=view&id=1Vxtm7xBlmfS65q1lfA4gksFZcgvMcXP0",
            "https://drive.google.com/uc?export=view&id=1WXswbS7-yoRDxjmVdNjd2QwhL9MjgP17", #12
            "https://drive.google.com/uc?export=view&id=1W7qFh2ZJC45veEeAF43TYLMRzsOyo4km",
            "https://drive.google.com/uc?export=view&id=1WhWNAVR540l-OrbetiS3BCGvk0c6aops",
            "https://drive.google.com/uc?export=view&id=1VVvEs9MWDT0AgV39fFETH9ALUkRMvwEZ",
            "https://drive.google.com/uc?export=view&id=1WL-bXtSxXpAkQHGyTDTD9WKpnFnntDvz",
            "https://drive.google.com/uc?export=view&id=1WBNsWi_7JOck8D1TntDXErTO0MI0Eryy",
            "https://drive.google.com/uc?export=view&id=1WUYCbqf6MZR0s-b3dIadMFJ9P5WJtny5",
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
                "kesan": "Abangnya keren, baik, ",  
                "pesan": "Sukses selalu bang, semangat jadi kadep"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya baik, cantik, sabar, jago editing",  
                "pesan": "Semangatt kuliahnya kak dan ajarin saya ngedit kak"# 1
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah.",
                "kesan": "Kakak ini baik, sabar, keren",  
                "pesan": "Tetap lah menjadi pribadi yang baik dan sabar kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya keren banget, tinggi, baik dan tidak sombong",  
                "pesan": "Semangat ngegym nya kak, kapan ngegym bareng? wkwk"# 1
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakaknya asik, baik",  
                "pesan": "Semangat mengejar mimpu nya kak dan semoga tergapai dengan baik"
            },
            {
                "nama": "Patricia Leonrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini cantik, baik, asik, perhatian, sang daplok kami",  
                "pesan": "Tetap semangat membimbing kami ya kak dan semangat ngaspraknya di kelas sebelah"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Pembangunan 5, Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak nya baik, keren, asik",  
                "pesan": "Jangan kebanyakan makan geprek kak dan tetap semangat kuliahnya bukan makan geprek nya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini cantik, baik, sabar",  
                "pesan": "Semangat terus ya kak, bawa santai aja drama dunia ini kak biar ga stres"# 1
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Abang ini keren, cool, baik, asik",  
                "pesan": "Semoga hobinya cepat ketamu ya bang, tetap semangat kuliahnya dan mencari hobinya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak ini baik, asik juga kelihatannya",  
                "pesan": "Tetap semangat kuliahnya kak, sukses terus"# 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari tuyul baskat",
                "sosmed": "@jimnn.as",
                "kesan": "Abangnya keren, tegas, namanya keren juga",  
                "pesan": "Tetap semangat ya bang nyari tuyulnya, sering ngegym ga bang??"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 2",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya baik, sabar, kelihatan dari hobinya berarti orangnya bersih juga ini",  
                "pesan": "Tetaplah menjadi orang bersih kak, kapan nih kita bersih-bersih bareng??"# 1
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya lucu, baik, keren juga",  
                "pesan": "Semangat menggapai mimpi nya ya kak (bukan mimpi buruknya)"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Abang nya keren, baik, harum keknya",  
                "pesan": "Kapan ni saya dikasi salah satu parfum nya bang??"# 1
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main uno",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya asik, keren, diajak pose abang-abang teknik ternyata mau juga",  
                "pesan": "Semangat lah kuliahnya bang dan sukses selalu"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abang ini baik banget, keren, cool, pinter ngoding dan desain, suka bawain makanan pas kerja kelompok",  
                "pesan": "Sukses ya bang dan tetap semangat di gempuran drama dunia ini"# 1
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "jalan dekat tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang ini keren banget, aktif banget, baik dan tidak sombong",  
                "pesan": "Tetap lah menjadi pribadi yang tidak sombong dan baik hati ya bang, semangatt"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi": "Berantakin kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya lucu, baik, sabar, pinter",  
                "pesan": "Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
