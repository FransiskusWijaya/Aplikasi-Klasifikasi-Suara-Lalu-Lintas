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

# --- BAGIAN BARU: ALUR KERJA PENGOLAHAN DATA ---
st.subheader("Alur Kerja Pengolahan Data")
st.write(
    """
    Sebelum data audio dapat dianalisis oleh model, data tersebut harus melalui serangkaian tahapan persiapan untuk memastikan kualitas dan konsistensi. Alur kerja ini terbagi menjadi dua langkah utama:
    """
)

# Menggunakan kolom untuk memisahkan setiap langkah
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("##### 1. Prapemrosesan Audio")
        st.write(
            """
            Tahap ini berfokus pada pembersihan dan standardisasi data mentah. Sampel yang mengandung *noise* signifikan (seperti suara angin atau percakapan) **dihapus dari dataset** untuk mencegah model mempelajari fitur yang tidak relevan. Audio yang lolos seleksi kemudian dinormalisasi amplitudonya.
            """
        )

with col2:
    with st.container(border=True):
        st.markdown("##### 2. Ekstraksi Fitur (Mel-Spectrogram)")
        st.write(
            """
            Setelah audio bersih, sinyalnya diubah menjadi **Mel-spectrogram**. Proses ini mentransformasi data deret waktu menjadi representasi gambar 2D yang memetakan spektrum frekuensi suara dari waktu ke waktu, menjadikannya input yang ideal untuk dianalisis oleh model.
            """
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

# KARTU 1: PENJELASAN CNN (VERSI BARU YANG LEBIH FORMAL)
with st.container(border=True):
    st.markdown("#### Convolutional Neural Network (CNN): Ekstraksi Fitur Spasial")
    
    # Mengatur layout dengan gambar di kiri dan teks di kanan
    col1, col2 = st.columns([1, 2], vertical_alignment="center") 
    
    with col1:
        # Menambahkan gambar arsitektur CNN
        st.image("assets/images/cnn_architecture.png", caption="Contoh Arsitektur CNN")
        
    with col2:
        # Mengganti teks lama dengan penjelasan yang baru
        st.write(
            """
            Blok *Convolutional Neural Network* (CNN) bertugas sebagai ekstraktor fitur visual. Fungsi utamanya adalah untuk menganalisis gambar Mel-spectrogram dan secara otomatis mengidentifikasi pola-pola spasial yang menjadi karakteristik pembeda untuk setiap kondisi lalu lintas.

            Proses ini dilakukan melalui serangkaian *filter* (kernel) digital yang dilatih untuk mengenali elemen-elemen spektral spesifik. Sebagai contoh:
            - Sebuah filter dapat menjadi terampil dalam mendeteksi **garis frekuensi vertikal yang tajam**, sebuah pola yang umumnya berkorelasi dengan suara klakson.
            - Filter lainnya mungkin mengidentifikasi **pita frekuensi horizontal yang lebar dan kontinu**, yang merupakan ciri khas dari deru mesin pada kondisi lancar.

            Hasil dari blok CNN ini adalah serangkaian *feature map*—representasi data yang ringkas namun kaya informasi—yang siap dianalisis lebih lanjut oleh lapisan berikutnya.
            """
        )

# KARTU 2: PENJELASAN LSTM (DENGAN TEKS BARU YANG LEBIH FORMAL)
with st.container(border=True):
    st.markdown("#### Long Short-Term Memory (LSTM): Analisis Dependensi Temporal")
    
    # Mengatur layout dengan teks di kiri dan gambar di kanan
    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.write(
            """
            Setelah blok CNN berhasil mengekstrak fitur-fitur spasial (*feature map*), tugas selanjutnya adalah menganalisis bagaimana fitur-fitur tersebut terangkai dari waktu ke waktu. Di sinilah peran blok **Long Short-Term Memory (LSTM)**.

            - **Fungsi Utama**: Jika CNN mengidentifikasi "apa" saja pola suara yang ada, maka LSTM bertugas memahami **"bagaimana" pola-pola tersebut berurutan secara temporal**. LSTM adalah jenis *Recurrent Neural Network* (RNN) yang memiliki kapabilitas memori, memungkinkannya untuk mempelajari dependensi jangka panjang dalam sebuah sekuens data.

            - **Proses Analisis**: LSTM menerima urutan *feature map* dari CNN dan menganalisis konteksnya. Sebagai contoh, model dapat belajar bahwa sekuens fitur yang menunjukkan **deru mesin konstan** merepresentasikan kondisi **Lancar**, sementara urutan yang menunjukkan pola **suara mesin diikuti jeda singkat** dapat diinterpretasikan sebagai pola *stop-and-go* yang khas dari kondisi **Macet**.
            """
        )
        
    with col2:
        # Tampilkan gambar di dalam kolom kanan
        st.image("assets/images/lstm_architecture.png", caption="Contoh Sel Memori LSTM")

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

# --- BAGIAN TENTANG PENULIS (DENGAN FOTO LEBIH BESAR DAN DI TENGAH) ---
st.subheader("Tentang Penulis 👨‍💻")
with st.container(border=True):
    # Mengatur layout utama dengan kolom untuk foto dan teks
    col1, col2 = st.columns([1, 3], vertical_alignment="center")
    
    with col1:
        # --- PERUBAHAN 2: MEMBUAT GAMBAR KE TENGAH ---
        # Kita buat 3 kolom lagi di dalam col1, dan taruh gambar di kolom tengah (sub_col2)
        sub_col1, sub_col2, sub_col3 = st.columns([1, 2, 1])
        
        with sub_col2:
            # --- PERUBAHAN 1: MEMPERBESAR GAMBAR ---
            # Ganti nilai width dari 150 menjadi 200 (atau angka lain sesuai selera Anda)
            st.image("assets/images/Profile.jpeg", width=1000) 
        
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