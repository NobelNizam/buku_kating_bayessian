import streamlit as st
import numpy as np
import time

def main():
    st.title("Kotak 3D Berputar")

    rows, cols = 5, 5  # Ukuran kotak 3D
    frames = []

    # Membuat kotak 3D dari simbol "#"
    cube = np.array([["#" for _ in range(cols)] for _ in range(rows)])

    # Menyusun frame-frame untuk animasi rotasi
    for angle in range(0, 360, 10):  # Rotasi dari 0 hingga 360 derajat
        frame = np.copy(cube)
        for i in range(rows):
            for j in range(cols):
                # Rotasi sederhana dengan menggeser posisi "#"
                if (i + j + angle // 10) % 2 == 0:
                    frame[i, j] = "#"
                else:
                    frame[i, j] = " "
        frames.append("\n".join(["".join(row) for row in frame]))

    # Menampilkan animasi
    for frame in frames:
        st.text(frame)
        time.sleep(0.1)  # Kecepatan animasi

if __name__ == "__main__":
    main()
