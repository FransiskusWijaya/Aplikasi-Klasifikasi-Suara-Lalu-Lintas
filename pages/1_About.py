import streamlit as st
import pandas as pd
import base64 # Library baru untuk mengubah gambar menjadi teks

# =================================================================
# --- FUNGSI BARU UNTUK MENGUBAH GAMBAR MENJADI BASE64 ---
# =================================================================
def get_image_as_base64(file_path):
    """Fungsi untuk membaca file gambar dan mengonversinya ke Base64."""
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =================================================================
# --- KODE UTAMA APLIKASI ---
# =================================================================

# Konfigurasi Halaman
st.set_page_config(page_title="Tentang Proyek", page_icon="📝", layout="wide")

st.title("📝 Tentang Proyek Penelitian")

st.info(
    "Aplikasi ini merupakan implementasi dari penelitian skripsi berjudul: "
    "**Analisis Kondisi Lalu Lintas Berdasarkan Suara Menggunakan Model Hibrida "
    "Convolutional Recurrent Neural Network**."
)

st.markdown("---")

# --- BAGIAN ARSITEKTUR MODEL ---
st.subheader("Arsitektur Model: CRNN Hibrida")
st.write(
    """
    Model yang digunakan adalah **Convolutional Recurrent Neural Network (CRNN)**, 
    sebuah arsitektur hibrida yang menggabungkan kekuatan dua jenis jaringan untuk "mendengar" dan "memahami" suara dari waktu ke waktu.
    """
)

# KARTU 1: PENJELASAN CNN (TETAP SAMA, SUDAH BENAR)
with st.container(border=True):
    st.markdown("#### 1. Convolutional Neural Network (CNN): Sang Ekstraktor Fitur")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("assets/images/cnn_architecture.png", caption="Contoh Arsitektur CNN")
    with col2:
        st.write(
            """
            Bayangkan CNN sebagai "telinga" model yang sangat tajam. Tugasnya bukan untuk mendengar suara secara keseluruhan, melainkan untuk **mengenali pola-pola atau fitur unik** di dalam representasi visual suara (Mel-spektrogram).
            - **Apa yang 'didengar'?** CNN belajar mengidentifikasi tekstur suara seperti deru mesin yang konstan, letupan klakson yang tajam, atau gesekan ban yang spesifik.
            - **Bagaimana caranya?** Ia menggunakan "filter" digital untuk memindai gambar spektogram dan mengekstrak fitur-fitur kunci ini, sama seperti mata kita mengenali bentuk dalam sebuah gambar.
            """
        )

# KARTU 2: PENJELASAN LSTM (MENGGUNAKAN HTML UNTUK CENTERING)
with st.container(border=True):
    st.markdown("#### 2. Long Short-Term Memory (LSTM): Sang Penganalisis Urutan")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write(
            """
            Setelah CNN mengekstrak "apa" saja suara yang ada, LSTM bertugas untuk memahami "bagaimana" suara-suara tersebut berhubungan seiring waktu. LSTM adalah "otak" dari model yang memiliki memori.
            - **Apa yang dianalisis?** LSTM menganalisis urutan fitur yang diberikan oleh CNN. Misalnya, ia belajar bahwa suara mesin idle yang diikuti oleh raungan pendek dan kemudian hening lagi adalah pola khas dari kondisi **Macet (stop-and-go)**.
            - **Bagaimana caranya?** LSTM memiliki "sel memori" yang memungkinkannya mengingat pola dari beberapa detik sebelumnya untuk memahami konteks suara saat ini.
            """
        )
    with col2:
        # --- PERUBAHAN DI SINI ---
        # 1. Konversi gambar ke Base64
        lstm_base64 = get_image_as_base64("assets/images/lstm_architecture.png")
        
        # 2. Tampilkan gambar di dalam HTML yang sudah di-styling untuk center
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{lstm_base64}" alt="LSTM Architecture" style="max-width: 100%;" />
            </div>
            <p style='text-align: center; color: grey;'>Contoh Sel Memori LSTM</p>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# --- BAGIAN DATASET (TETAP SAMA) ---
st.subheader("Dataset Pribadi")
st.write(
    """
    Dataset yang digunakan dalam penelitian ini adalah hasil rekaman pribadi yang dikumpulkan dari berbagai titik lokasi di Jakarta. Dataset terdiri dari sekitar 3000 klip audio berdurasi 5 detik yang telah dilabeli secara manual ke dalam tiga kategori utama: **Sepi, Lancar, dan Macet**.
    """
)
st.success(
    """
    **➡️ Ingin tahu lebih detail?**
    Setiap kelas memiliki karakteristik audio, visual, dan spektogram yang unik. Untuk melihat penjelasan lengkap, silakan kunjungi halaman **Karakteristik Kelas**.
    """
)
st.markdown("---")

# --- BAGIAN TENTANG PENULIS (TETAP SAMA) ---
st.subheader("Tentang Penulis 👨‍💻")
with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write("") 
    with col2:
        st.markdown(
            """
            **Fransiskus Dharma Hadi Wijaya**
            *Mahasiswa Teknik Informatika, Universitas Tarumanagara (535220106)*
            ---
            "Berawal dari pengamatan sehari-hari terjebak dalam kemacetan Jakarta, saya sering bertanya-tanya: bisakah kita memahami kondisi lalu lintas tanpa harus melihatnya secara langsung? Suara klakson yang bersahutan, deru mesin yang tak bergerak, dan keheningan jalanan di malam hari memiliki pola yang khas. 
            Hal ini memicu ketertarikan saya untuk menjembatani dunia **analisis audio** dengan **kecerdasan buatan**. Proyek ini adalah langkah awal saya untuk mengeksplorasi potensi tersebut."
            """
        )