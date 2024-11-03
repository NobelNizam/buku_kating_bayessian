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
            "https://drive.google.com/uc?export=view&id=1o3_pmknnpSF8upixt-GQEaAdd2NqNjQE",
            "https://drive.google.com/uc?export=view&id=13FBiyLN_YP-delSLFXh8hHh61s-g3yc-",
            "https://drive.google.com/uc?export=view&id=1adjuSYs8S33gSDqC8DCpacnRUIH1muqq",
            "https://drive.google.com/uc?export=view&id=1XgGC0dBjQBk1F3Dlwrkv3Wh9zS6-ceBI",
            "https://drive.google.com/uc?export=view&id=1fn_hP49qgSrz-hCwdLXS1O8T4oWKxYk5",
            "https://drive.google.com/uc?export=view&id=1GqFKCfLYiERKe9ovjNj_fv4k9UQT64MF",
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
                "kesan": "Abang Gumi selain ada kharismanya ada kocaknya juga",  
                "pesan":"smgt terus menjadi Kahim bang"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang Pandra sangatlah kocak",  
                "pesan":"Teruskan kocak bang!!"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "nama belakang nya sama",  
                "pesan":"Hai kak nama belakang kita sama"
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hartfdlh",
                "kesan": "mata kakaknya bagus cat eye",  
                "pesan":"Lancar-lancar terus kuliahnya kk!"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakanya imoetz sekali",  
                "pesan":"Semangat terus kak kuliahnya!!"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ini mukanya cocok jadi bendahara",  
                "pesan":"Semangat kak jadi bendaharanyaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aPiOvABdEt1kpI3z3aLKxb_AqdPInPGv",
            "https://drive.google.com/uc?export=view&id=1_24-9aC8mB_zvzy-QzUEa9JQbS_79Z2A",
            "https://drive.google.com/uc?export=view&id=1K285FM9T6y0wZZCNHVVnuL9Rpq64KGL9",
            "https://drive.google.com/uc?export=view&id=1IZnb1lCyTNzXzUbZdyzNAJwmxiT7Fnzp",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1jRvJW7SIT8eMvwojBg9IYbJgLTW8MrzX",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1yfstBvVGUqFyZbaS62pR6I3R7SR7-WhO",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1DTliGINQ7CQ8f6RrbHrkwK8tVFCp4f2a",
            "https://drive.google.com/uc?export=view&id=1H1Z-boU0aeqaHHA1qCfKFIPrp6LO2MYc",
            "https://drive.google.com/uc?export=view&id=1Uebf5D2vac3mVT2PHTHnEINa-ftEYQ1A",
            "https://drive.google.com/uc?export=view&id=1VyyGio0yM8ZlEsYadMKaUO08904e_utg",
        ]
        data_list =[
             {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Ngerjain TA",
                "sosmed": "@trimurniaa",
                "kesan": "kakak sangatlah asik",  
                "pesan":"Semoga dilancarkan TA nya ya kak!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis, Way Huwi",
                "hobbi": "Membaca Novel",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Style Outfit kk kece2",  
                "pesan":"ajarin aku kak mix n match baju yang cakep"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "18",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0",
                "kesan": "nama kita mirip kak",  
                "pesan":"Semangat kk kulyahnya!!!"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak orangnya tegas",  
                "pesan":"ternyata kakak beneran tegas dan galak sedikit"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@dylebee",
                "kesan": "Ada kejadian tidak terduga saat wwc",  
                "pesan":"Alhamdulillah, Puji Tuhan ya kak rejeki emang gak kemana"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Membaca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang Asprak Alpro nih abanggg",  
                "pesan":"Halo abang asprak alpro Q!!"
            },
            {
                "nama": "Renisha Putri Giyani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@fleurnsh",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama",
                "sosmed": "@myrrinn",
                "kesan": "Abang kyknya wibu ya bang?",  
                "pesan":"lanjutkan bang nge balegnya"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bernung, Pesawaran",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@ansftynn_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "120",
                "asal":"Bengkulu",
                "alamat": "Natar",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@myrrinn",
                "kesan": "kakak cheerful sekali",  
                "pesan":"teruskan kan cheerfulnya dan menjadi happy virus"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Badminton, melukis, minum kopo",
                "sosmed": "@shrul.pdf",
                "kesan": "sangar bang muka abang",  
                "pesan":"Lanjutkan bang ngebalegnyaa"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Menonton horror",
                "sosmed": "@berliyanda",
                "kesan": "kakak sepertinya pendiam",  
                "pesan":"meskipun kakak pendiam saya tetap mau ngobrol sama kk"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "12245022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong",
                "hobbi": "memancing emosi",
                "sosmed": "@jeremia_s_",
                "kesan": "abang ini pecinta hololep",  
                "pesan":"lanjutkan bang ngewibunya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vGUAav3J9pQjNUq0l6YpzbURAtqwHxee",
            "https://drive.google.com/uc?export=view&id=1WlpsomGfqoM6HG17F0nEVW24VhkMi5rF",

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
                "kesan": " kakak gemoy ",  
                "pesan":" semangat terus kak jadi senatornya!! "
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kontrakan Kota Baru",
                "hobbi": "Dengerin Kak Luthfi nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": " abang keren   ",  
                "pesan":" semangat terus bg kuliahnya "# 1
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BhhUWq8yT8_yjNZ9lj1t9tc1Dy7DQlyC", #
            "https://drive.google.com/uc?export=view&id=1-vUv5gsjpIP2cjpEp0WMV59-dRsdnCM1",
            "https://drive.google.com/uc?export=view&id=1u0HL00Ws4sdMYxUR97tQqYoXeOh2WEmk",
            "https://drive.google.com/uc?export=view&id=1BPRGzLWj7TfqXpZuCJQxQ0kdmZzbhLM8",
            "https://drive.google.com/uc?export=view&id=1Yb3fwBRL8lxsrfpPvbGfNt0z1HrxZ66R",
            "https://drive.google.com/uc?export=view&id=1uePixVGEcR12kbBWXTmGE0bVsvUUq_ch",
            "https://drive.google.com/uc?export=view&id=1vSQb9y89SPIedYp6aheGEf1Cr2Kmtq34",
            "https://drive.google.com/uc?export=view&id=1Bt2RbweNq5ENhp039Yfp7He-bt_a1myE",
            "https://drive.google.com/uc?export=view&id=1CxMPqkDybJeck_ZFYfV2wL0IyW-nFbw8",
            "https://drive.google.com/uc?export=view&id=1CF2WZ35fyYt5qVfRl-jZJgGUpl27wEr-",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #11
            "https://drive.google.com/uc?export=view&id=1FHGDaQ3RchIEvWzcmX_0rHe1kGixBqnx",
            "https://drive.google.com/uc?export=view&id=1tUHDcAeo-1jFXtoxSmKAGIEYBZiCjOF1",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #14
            "https://drive.google.com/uc?export=view&id=1RtTiO6p_tJWFluAZDDqUHEMNd6-dSbEK",
            "https://drive.google.com/uc?export=view&id=11TOQdSM5QsZRLGUgKvr20n0M0Z-NUbEl",
            "https://drive.google.com/uc?export=view&id=1ArYoHJFVBBhuDonkkHPB4rvP0pebER44",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #18
            "https://drive.google.com/uc?export=view&id=1MQFXdQIQE7bUadIsh7HOFlC15ihATFjx",
            "https://drive.google.com/uc?export=view&id=1dYO5NosDlg2i9M2i75aWwylW_tEWtT7J",
            "https://drive.google.com/uc?export=view&id=1zvsmu5ldObGkVoxwC2FtyYmXyMzMuJKh",
            "https://drive.google.com/uc?export=view&id=1Z8BiV5Y72JCnW-vgv244uH_b3tdmm7vb",
            "https://drive.google.com/uc?export=view&id=1R0J4k_cIpHUlLPVm5S3KhKNPFUNo1sK_",
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
                "kesan": " abang tegas ",  
                "pesan":" lanjutkan kadernya bg  " # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": " kakak cheerful bgt ",  
                "pesan":" semangat terus kak di psda " # 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jailin Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": " muka kakak klo marah serem ",  
                "pesan":" jangan sering2 marah kak " # 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Ngukur lampung",
                "sosmed": "@allyaislami_",
                "kesan": " muka kakak klo marah serem ",  
                "pesan":" kakak jangan marah2 trus plz " # 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": " kakak asprak ads ",  
                "pesan":" makasih byk kak sdh membantu saat prak ads " # 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": " kakak keren ",  
                "pesan":" semangat kak jadi panitia kadernya  " # 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "pangeran senopati raya, gerbang barat",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": " abang pendiam ",  
                "pesan":" semangat terus bang jadi panitia kadernya " # 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Raya Agung",
                "alamat": "Jl. Pagar Alam, Kedaton",
                "hobbi": "Nyari angin",
                "sosmed": "@dransyh_",
                "kesan": " abang suka ngatur parkiran pas kader ya bang ",  
                "pesan":"terima kasih telah menjaga motor2 kami bang  " # 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122350041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": " kakak jarang keliatan ",  
                "pesan":" semangat terus kak kuliahnya  " # 9
            },
            {
                "nama": "Devyan Loxefal",
                "nim": "121450128",
                "umur": "18",
                "asal": "Duri, Riau",
                "alamat": "Kobam Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": " abang suka ikut acara olahraga ",  
                "pesan":" lanjutkan bang olahraganya " # 10
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "  ",
                "umur": "  ",
                "asal": "  ",
                "alamat": "  ",
                "hobbi": "     ",
                "sosmed": "@",
                "kesan": "  ",  
                "pesan":"   " # 11
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan lapas",
                "hobbi": "Ngeasprak",
                "sosmed": "@johanneskrisjonn",
                "kesan": " abang extrovert banget ",  
                "pesan":" semangat terus bang jadi capo  " # 12
            },
            {
                "nama": "Kemas Verandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo Golf Asri",
                "hobbi": "Main uler digital",
                "sosmed": "@kemasverii",
                "kesan": " abang sepuh coding ",  
                "pesan":" semangat terus bang kuliahnya  " # 13
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": "  ",
                "umur": "  ",
                "asal": "  ",
                "alamat": "  ",
                "hobbi": "  ",
                "sosmed": "@ ",
                "kesan": "  ",  
                "pesan":"   " # 14
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengar me Adams",
                "sosmed": "@presiliang",
                "kesan": " kakak mirip kak rafa ",  
                "pesan":" semangat terus kak kuliahnya " #15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": " kakak mirip kak presilia ",  
                "pesan":" semangat terus kak kuliahnya " # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": " abang anak emo ya  ",  
                "pesan":" bagi playlist emo-nya dong bang " # 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "  ",  
                "pesan":"  " # 18
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abang seru ",  
                "pesan":"lanjutkan serunya bang Ateng " # 19
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": " abang orang bekasi",  
                "pesan":" semangat bang kuliahnya " # 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": " ternyata seumuran ya kak ",  
                "pesan":" semangat terus kak kuliahnya " # 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": " abang pendiam ",  
                "pesan":" semangat terus bang kuliahnya " # 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": " kakak ternyata kembar  ",  
                "pesan":" semangat terus kak kuliahnya " # 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eu4q2gOXJzzBCDl52XKH5OSelVrseIDO", #rafi
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #anisa
            "https://drive.google.com/uc?export=view&id=1M5wkOBIQTuXosiTZiEgPoc1fKhgD_5wL", #ahmad 
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #fadil
            "https://drive.google.com/uc?export=view&id=1JR26P9OjQ8lwLcGlfDx5V3VMI2RknsWi", #regi 
            "https://drive.google.com/uc?export=view&id=10kWxeGQGCju9d-gXW6Um2_o-XQfYLULY", #syalaisha
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #nathanael
            "https://drive.google.com/uc?export=view&id=1Y2jBmCF7KSz8Dp0STY4M9jTIvSivo6Mx", #anwar
            "https://drive.google.com/uc?export=view&id=1glL10AXrlyoA7Fbj_ImT7jk85Tt908Xf", #deva
            "https://drive.google.com/uc?export=view&id=1qviNUUOCvqn6oekMi85w-Xll52l7Lmt-", #dinda 
            "https://drive.google.com/uc?export=view&id=1dJUY25aF8Jh1qgylcA17xIL0Tob9N7Qk", #marleta
            "https://drive.google.com/uc?export=view&id=11ibLmuYa7JHp7a-c2DBhu7LhNq67Q2nn", #ruth
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #syadza
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #Abdur
            "https://drive.google.com/uc?export=view&id=1fpTPVkpRYndBpuugkYWpcNYYbj1ns5-1", #adit
            "https://drive.google.com/uc?export=view&id=1-uHLUsN3xYMhRThT1QYamcfVOlO2qoft", #eggi
            "https://drive.google.com/uc?export=view&id=1-Z6xiMPzd2Z7yBKSeoT0QGYnyv0bwjmt", #febiya
            "https://drive.google.com/uc?export=view&id=1g69JH8bRNmP4fvzmaAXetiX4f3ZACZvm", #randa
            "https://drive.google.com/uc?export=view&id=1cXxQTKmC57p6ZP6QJyTfA88ED0BJ72SE", #happy
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #vita
            

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
                "kesan": " abang keren ",  
                "pesan":" semangat kuliahnya bang " # 1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakak canci sekalii ",  
                "pesan":"mau dong kak" # 2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": " bang Ahmad aktif semua olahraga kyknya ya",  
                "pesan":" semangat bang olahraganyaaa" # 4
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": " keren bang hobinya main game ",  
                "pesan":"  semangat terus bang kuliahnya " # 5
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes hmsd",
                "sosmed": "@mregiiii_",
                "kesan": " abang asprak ads  ",  
                "pesan":" semangat terus bang jadi asprak " # 6
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": " kakak ternyata kembar ",  
                "pesan":" semangat terus kak kuliahnya  " # 7
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
                "kesan": " wew abang asprak strukdat  ",  
                "pesan":" semangat terus bang jd asprak strukdatnya " # 9
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kak deva mukanya manis bangett",  
                "pesan":"infokan rekomendasi film yang bagus kak" # 10
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": " ",
                "sosmed": "@dindanababan_",
                "kesan": " kakak asprak ads ",  
                "pesan":" semangat terus kak asprak adsnya  " # 11
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": " kakak tutor matdas tpb  ",  
                "pesan":" semangat terus kak kuliahnya " # 12
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": " kakak lucu ",  
                "pesan":"semangat terus kak meresume jurnalnyaaa " # 13
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakak kalem sekali",  
                "pesan":"ipokan rekmendasi novel yang bagus kak" # 14
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
                "kesan": " mukanya babyface bgt bang ",  
                "pesan":" semangat terus bang kuliahnya  " # 16
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": " abang terlihat sangat pintar ",  
                "pesan":" semangat terus bang kuliahnya " # 17
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": " kakak lucu ",  
                "pesan":"rekomendasiin drakor yang bikin emosi dong kak" # 18
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abang kyk orang Sunda ",  
                "pesan":" Berkembang gimana tuh bang hobinya?" # 20
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": " namanya lucu bang   ",  
                "pesan":" semangat terus bang kuliahnya " # 19
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13UiraF4jXiQh-M2mlz0OUhAJwzsCmyg7",
            "https://drive.google.com/uc?export=view&id=12C9TfX6ZvitxxDY5UPjRV8r3jo-dcr0D",
            "https://drive.google.com/uc?export=view&id=1YtQ21Cf62vSmkILkGy57oZkool3xRgu9",
            "https://drive.google.com/uc?export=view&id=1Rzlm4Zaiqgkq7kzRx609C1nhpX5XBdSx",
            "https://drive.google.com/uc?export=view&id=15ZDGpCv6zpK3EUyrKGglH-69iK8on09D",
            "https://drive.google.com/uc?export=view&id=1UYOm2w4gXcoM5FE5FOaeE0mhmkdLRxiH",
            "https://drive.google.com/uc?export=view&id=148fGaUt90_V60Mkvdra-x1trtx1-a3dO",
            "https://drive.google.com/uc?export=view&id=1ZGP5UA6Wqexxru3BNQKeqJhnyAcs-9Gr",
            "https://drive.google.com/uc?export=view&id=15NGm-At-AKiNVK2WRYRMu5sMciBsz3_l",
            "https://drive.google.com/uc?export=view&id=1kDOjNHIuJn-QothynZnscXI_kUTfrz1e",
            "https://drive.google.com/uc?export=view&id=1DISl-F-M_ryvt20wGP-LuxCucZjS8vVD",
            "https://drive.google.com/uc?export=view&id=1_uDLL2k-c7lvHgByvwp69akUXMtcesgQ",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1beyOhSjEutzbzHCLgjNS4AnkOps5ZPL1",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1aTK--nHwlmmejq8FIIjJu0C6dEbUqiFM",
            "https://drive.google.com/uc?export=view&id=16UEeOXOmaqG4r5TIust-a3ZH7srQuBDB",
            "https://drive.google.com/uc?export=view&id=16pEzD7yVjLejjrYJKfpj35jHZarpSxV4",
            "https://drive.google.com/uc?export=view&id=1Mi9u6BKGXokStLznr87qNzJ008UABpLV",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
        ]   
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"BUrkinapaso",
                "alamat": "Jatimulyo",
                "hobbi": "nyari solar",
                "sosmed": "@yogyst",
                "kesan": "Apakah abang masih saudaraan sama Saitama?",  
                "pesan":"Semangat bang"
            },
            {
                "nama": "Ramadhita Atifah Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat kakkk"# 1
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak agak galak",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin Musik",
                "sosmed": "@deaa.rsn",
                "kesan": "",  
                "pesan":" "
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal":"Bali",
                "alamat": "Sukabumi",
                "hobbi": "Surfing sambil Snorkling",
                "sosmed": "@esteriars",
                "kesan": "keren bgt kak hobinya",  
                "pesan":"Ajak-ajak kak snorkling ke Baliii"# 1
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal":"Kepulauan Seribu",
                "alamat": "Way Halim",
                "hobbi": "Main Paralayang",
                "sosmed": "@nateee_15",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Ajakin saya terjun paralayang sih kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "rambut curlynya bagus kak",  
                "pesan":"semangat trus yah kakak!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Menjahit Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asprak ADS saya yg sgtlah baikkk",  
                "pesan":"Teteh Jasmine teh geulis pisannn"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "19",
                "asal":"Kalianda",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang sangatlah seram",  
                "pesan":"Bang jangan galak2 saya takut"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal":"Makassar",
                "alamat": "Pemda",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_anamnk",
                "kesan": "Muka kakak garang",  
                "pesan":"Tapi kakak baik"
            },
            {
                "nama": "Rizki Adrian Bennoviry",
                "nim": "121450073",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Berenang",
                "sosmed": "@rzkdrnnn",
                "kesan": "Penjelasan abang sgtlah informatif",  
                "pesan":"sehat selalu bang"# 1
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang terlihat sangat santai dan calm",  
                "pesan":"Jangan lupa napas bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yipyy",
                "kesan": "Nama kakak unik banget, pasti artinya bagus ya kak",  
                "pesan":"sehat selalu kak"# 1
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya imut kyk masih sma",  
                "pesan":"semangat terus kakakk!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube",
                "sosmed": "@alfaritziirvan",
                "kesan": "abang mirip temen saya",  
                "pesan":"semangat terus bang di eksternall"# 1
            },
            {
                "nama": "Izza Luthfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Bertemu anak pengmas",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakak prenli abis",  
                "pesan":"Sehat-sehat ya kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak yang baik",  
                "pesan":"Kak ajarin saya tajwid yang benar dong"# 1
            },
            {
                "nama": "Rahid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Duduk di Wico",
                "sosmed": "@rayths_",
                "kesan": "Abang pendiam",  
                "pesan":"semangat bang"
            },
            {
                "nama": "Tria Yunani",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@tria_yo62",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ozQtg28CplqTrXNuzRYF-uhw_ejfA7PJ",
            "https://drive.google.com/uc?export=view&id=1ZcVcNoQoLUiaGtOIHJdza1ZyAoGGyhl8",
            "https://drive.google.com/uc?export=view&id=1osDUjBEysSzHcFW6RnTbW-4ek5R3eiWl",
            "https://drive.google.com/uc?export=view&id=1lQi6LFQslLk1gTEagQwWD4RWVKd6X8iV",
            "https://drive.google.com/uc?export=view&id=1sGx-koXY7YzaGl_oF276kYreoHjyfF_e",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1Tzzn7QVcXxvkjGLrCH8LS0RbWo2XEfU3",
            "https://drive.google.com/uc?export=view&id=1RjU7v8zylDEFe5DmMU25iCgcK6jx8Er9",
            "https://drive.google.com/uc?export=view&id=1TgesprK-HdjP-x6iIAoTggyApC4o1kG5",
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb",
            "https://drive.google.com/uc?export=view&id=1mQaTvYF6S3MeEOOSB_Tx_bfiMWK_7qf8",
            "https://drive.google.com/uc?export=view&id=1RbJqWP_KPokqGmM1Do3VJ4bzSLOlvohC",
            "https://drive.google.com/uc?export=view&id=1mP3wtGPmh59G5Gq4pGcZU7PeZJNw-v7F",
            "https://drive.google.com/uc?export=view&id=1tS6AU09LHqdIQ5UynigH-YrFF5S6L6SK",
        
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "122450027",
                "umur": "20",
                "asal":"Pamulang",
                "alamat": "Way Kandis(Kobam)",
                "hobbi": "Manjat pohon pinang",
                "sosmed": "@dimzrky_",
                "kesan": "Abang aktif bgt dah",  
                "pesan":"Kok Gak masuk Unpam aja bang"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Airan",
                "hobbi": "Membaca novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Kakak manis bgt sih kak",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "122450066",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam(Untung)",
                "hobbi": "Main Sepeda ke gunung",
                "sosmed": "@iakbar_resdika",
                "kesan": "Abangnya kalem",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450022",
                "umur": "20",
                "asal" : "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendegarkan musik",
                "sosmed": "@rannipu",
                "kesan": "Muka kakak sedikit galak",  
                "pesan":"semangat terus yah kak"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyari buah pisang",
                "sosmed": "@rendraepr",
                "kesan": "Abang suka joget di suporteran",  
                "pesan":"Sorry ya bang, tapi Basket Cikut > Basket Cipus"# 1
            },
            {
                "nama": "Salwa Farhantussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal" :"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwafhnn_694",
                "kesan": "Kakak mirip temen saya",  
                "pesan":"semangat terus kakk!!"# 1
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450049",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan": "Nama abang keren",  
                "pesan":"semangat terus ya bang"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Aura abang sangat MasyaAllah",  
                "pesan":"Semangat bang futsalnya"# 1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "kakanya pendiemm",  
                "pesan":"semangat terus kakk!"# 1
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
                "kesan": "Muka kakak babyface",  
                "pesan":"infokan rekomendasi filmnya kak"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di laut",
                "sosmed": "@rexander",
                "kesan": "abang skena bgt keliatannya",  
                "pesan":"apa bener abang klo ke pulau jawa berenang bukan naik kapal?"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakak kyk masih bocil",  
                "pesan":"kiyow sekali kakak ini"# 1
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450001",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Gya Kos",
                "hobbi": "Nonton film",
                "sosmed": "@josuapanggabean16_",
                "kesan": "bang Jos, kita sekelas mss bang",  
                "pesan":"Semangat bang jadi pj kelas mss nya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CPCM_gRxMFO3VG4-flzhu_6DuO_KUuid",
            "https://drive.google.com/uc?export=view&id=1isB7ycf93DzxFnb8bKxOavSysuBMIItG",
            "https://drive.google.com/uc?export=view&id=1lTP9IpzWeP578pfv1cGciGXL5M7Q4zrL",
            "https://drive.google.com/uc?export=view&id=1ymeFeUvEmbv-oAE2IIGnyeQQ6onJKYz5",
            "https://drive.google.com/uc?export=view&id=1-vC4mrov912fSd-If79G_xLKUjH2Sbmm",
            "https://drive.google.com/uc?export=view&id=1mL2N_xz_Dp3GwCsavIFDzKvat5o_t1eu",
            "https://drive.google.com/uc?export=view&id=1jMMHNRr1JW7NJHGBwy4j6y1a6HgqqXtM",
            "https://drive.google.com/uc?export=view&id=1hUUKkUkJV8iGE0REL4LQhbgsuraN4QO2",
            "https://drive.google.com/uc?export=view&id=1gdeHZbrVkR-MNsDsT-V8BtKJY-nJXpbV",
            "https://drive.google.com/uc?export=view&id=1gYgm7HSWf-3U58lrl9ZAkPVr9DDShNIE",
            "https://drive.google.com/uc?export=view&id=1gkZCXHevUlpAkebBuhHLlALLzzv_qu5y",
        ]
        data_list = [
            {
                "nama": "Adrian Agustinus Lumban Gaol",
                "nim": "121450095",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Jl.Belwis",
                "hobbi": "Mencari uang",
                "sosmed": "@andriangaol",
                "kesan": "Saya kira abang ini medkraf soalnya suka dokum2",  
                "pesan":"semangat terus bang mencari uangnya"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Nama belakangnya kyk gaasing kak, apakah kita satu bapak?",  
                "pesan":"semangat kak ngerjain TA nya!!"# 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung uang",
                "sosmed": "@zhjung",
                "kesan": "kakak lucu sekalii",  
                "pesan":"Semangat menghitung uangnya kak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "1224500138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang nih medis abadi ya bang?",  
                "pesan":"Keren bang gameplay badmintonnya saya udh liat"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini skill marketingnya bagus bgt",  
                "pesan":"Hati-hati bang touringnya"# 1
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Saya setiap liat abang naik motor kyk lgi liat sinetron anak jalanan",  
                "pesan":"jangan gakal-galak bg pas suporteran"# 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Muka kakak mulus bgttttttt",  
                "pesan":"spill skincarenya kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kacamatanya skena bgt kak",  
                "pesan":"semangat kak TA nya!!"# 1
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak bocil absen ya kak",  
                "pesan":"ayo kita nobar windut kak"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Nangka",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Saya jarang liat abang di kampus",  
                "pesan":"abang jangan diem2 aja bang"
            },
            {
                "nama": "Elia MEylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "",
                "sosmed": "@meylanielia",
                "kesan": "kakak aga boyish gtu tapi keren",  
                "pesan":"Semangat terus kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I10G482RGOt5eoGTsoVAdJYs8NodPHwA", #Wahyu
            "https://drive.google.com/uc?export=view&id=1vvqOAFNN1JvVoopTdcZUDsB7NND41PSE", #Elok
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #Arsyiah 
            "https://drive.google.com/uc?export=view&id=1vrBdVN7nuMwvpldl-tnDWIvadpF0Ht6r", #Cintya Bella
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", # Eka
            "https://drive.google.com/uc?export=view&id=1yPvO4a1UEVafC2jjI789GjRHat7-LTrb", #Najla Juwaria
            "https://drive.google.com/uc?export=view&id=1weNHEIXxsrGM93ADYS9yD06uj5jTO6Jn", # Kak Cia
            "https://drive.google.com/uc?export=view&id=1ElrYvt1SeCnGolKnZKYusBuBfrYUtv7T", # Neli
            "https://drive.google.com/uc?export=view&id=1tdkr6tQMcawanqcEAhFTOHirKwY7afzi", #Try Yani
            "https://drive.google.com/uc?export=view&id=1lxXsF0w_xCV_Hv9rcN4BraCbZ67Fse51", #Kaisar
            "https://drive.google.com/uc?export=view&id=1GQSHTGXuEU1srmuHIzk5zFVdVnEvwwju", #Dwi Ratna 
            "https://drive.google.com/uc?export=view&id=1G768_ReZCDpRiJOU1OCUZh5rEV8D6CJm", #Jim
            "https://drive.google.com/uc?export=view&id=1xt4ED6jrYIWNqpue8pRVWCPqksGm6ltU", #Nasywa
            "https://drive.google.com/uc?export=view&id=1U9Ujac4LPlMnhAuSGlBMZxGPd2yWuvIc", #Priska
            "https://drive.google.com/uc?export=view&id=1Xsp_1B3vxWRsbA_rr8Uct2rWw_At8SJ9", #Arsal
            "https://drive.google.com/uc?export=view&id=1tc5385whmXbbUOHYPGv-n5yj2g1JZC6v", #Abit
            "https://drive.google.com/uc?export=view&id=1JpyiSI7vAipVacvpEvXt3oU0RqCirsLz", #Akmal
            "https://drive.google.com/uc?export=view&id=1KifAP5pHPykpkAyj7qFcFk_6LfJmSJNW", #Hermawan
            "https://drive.google.com/uc?export=view&id=1L3nOKmS0rQFXJ1IU613zujT3YvbhtXSi", #Khununisa

        ]
        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@wayuraja",
                "kesan": "abang terlihat pendiam",  
                "pesan":"semangat ngerjain TA nya bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "BAndar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kakak imoetz n canci skali",  
                "pesan":"Lanjutkan kak ngeditnya"# 1
            },
            {
                "nama": "Arsyiah Azzahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah.",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "cintyabella28",
                "kesan": "kakak sgt menjulang tinggi",  
                "pesan":"semangat hidup sehat ngegymnya kak Cibel!"# 1
            },
            {
                "nama": "Eka Fidya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Menyibukkan diri",
                "sosmed": "@ekafdyaputri",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Najla Juwaria",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nyubit Orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak daplok q yg paling cantikkkk n imutttt",  
                "pesan":"Semangat trus daplok kesayang q"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
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
                "asal":"Lampung",
                "alamat": "Jl. Pembangunan Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak wangi banget sihhh",  
                "pesan":"Spill parfumnya kak"# 1
            },
            {
                "nama": "Tri Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal" : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak kyk unnie2 Korea",  
                "pesan":"semangat terus kuliahnya kak!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Masih Nyari ",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya suka nongkrong2 nih kayaknya",  
                "pesan":"Mau dibantuin gak bang nyari hobinya"# 1
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Jl. Durian 5 Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak lucuw sekali, outfit abunya matching bgt kak",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Nyari Tuyul Buzzcut",
                "sosmed": "@jimnn.as",
                "kesan": "gaya fotonya adm bgt bang",  
                "pesan":"Saya ada tuyulnya bang, tapi adanya yang mullet"# 1
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1 Pemda",
                "hobbi": "Bersih-bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kacamatanya cocok di kakak",  
                "pesan":"Semangat terus kakk kulyahnya!"
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
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. Nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya lucuw",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450011",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Keren amat bang hobinya",  
                "pesan":"Cuirga saya abang jangan2 reviewer parfum di tiktok"# 1
            },
            {
                "nama": "Abi't Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "main uno",
                "sosmed": "@abitahmad",
                "kesan": "abang sepuh coding ya bang",  
                "pesan":"bang byone uno bang"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang mirip daplok saya sih bang",  
                "pesan":"Ternyata emg daplok saya ya bang"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang mirip daplok saya sih bang",  
                "pesan":"Ternyata emg daplok saya ya bang"
            },
              {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan dekat tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Muka abang Bogor banget",  
                "pesan":"awas bang kesambet grgr bengong"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Pilu, Bakauheni",
                "alamat": "Belwis",
                "hobbi": "Berantakin Kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kakak mirip temen sekelas saya kak, namanya juga sama",  
                "pesan":"Semangat trus kak di Medkraf!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
