import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Judul halaman Kanvas Kreatif
st.title("Kanvas Kreatif")

# Kanvas pengaturan
st.write("Gambar bebas di kanvas ini dengan alat yang disediakan!")

# Pengaturan kanvas
drawing_mode = st.selectbox("Pilih Mode Gambar:", ("freedraw", "line", "rect", "circle", "transform"))
stroke_width = st.slider("Pilih Ketebalan Garis:", 1, 25, 3)
stroke_color = st.color_picker("Pilih Warna Garis:")
bg_color = st.color_picker("Pilih Warna Latar Belakang:", "#ffffff")

# Menampilkan kanvas
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.0)",  # Pilihan warna isian
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="kanvas_kreatif",
)

# Simpan hasil jika ada gambar di kanvas
if canvas_result.image_data is not None:
    st.write("Gambar Anda:")
    st.image(canvas_result.image_data)
