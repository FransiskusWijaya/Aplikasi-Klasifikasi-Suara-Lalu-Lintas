import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Home - Analisis Suara Lalu Lintas",
    page_icon="🚗",
    layout="wide"
)

# --- BAGIAN HEADER ---
# Menggunakan kolom untuk menata judul dan gambar
col1, col2 = st.columns([3, 1])

with col1:
    st.title("🚦 Analisis Kondisi Lalu Lintas Berdasarkan Suara")
    st.markdown("##### _Prototipe Penelitian untuk Membuktikan Hipotesis_")

with col2:
    # Ganti dengan path ke logo atau gambar yang relevan jika ada
    # Jika tidak ada, Anda bisa hapus baris ini
    st.image("assets/images/soundwave_logo.png", width=1500) # Contoh path, siapkan gambar ini

st.markdown("---")

# --- PENJELASAN SINGKAT ---
st.markdown(
    """
    Selamat datang! Aplikasi ini dirancang untuk menjawab sebuah pertanyaan utama:
    > **_Bisakah Kecerdasan Buatan (AI) membedakan kondisi lalu lintas—Sepi, Lancar, atau Macet—hanya dengan "mendengarkan" suara lingkungan?_**

    Aplikasi ini menggunakan model **Convolutional Recurrent Neural Network (CRNN)** untuk menganalisis rekaman suara dan mengklasifikasikannya.
    """
)

st.markdown("---")


# --- KARTU NAVIGASI ---
st.subheader("Mulai Eksplorasi 🚀")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("### 🔊 Klasifikasi Audio")
        st.write(
            "Unggah file audio lalu lintas Anda dan biarkan model kami menganalisisnya secara *real-time*."
        )
        # st.page_link("pages/Klasifikasi.py", label="Mulai Analisis", icon="➡️")

with col2:
    with st.container(border=True):
        st.markdown("### 🔍 Karakteristik Kelas")
        st.write(
            "Pelajari ciri khas audio, visual, dan spektogram dari setiap kondisi lalu lintas yang digunakan."
        )
        # st.page_link("pages/2_Karakteristik_Kelas.py", label="Lihat Detail", icon="➡️")

with col3:
    with st.container(border=True):
        st.markdown("### 📝 Tentang Proyek")
        st.write(
            "Dapatkan informasi mendalam mengenai arsitektur model, dataset, dan metodologi penelitian."
        )
        # st.page_link("pages/About.py", label="Baca Selengkapnya", icon="➡️")


# --- INFORMASI DI SIDEBAR (TETAP SAMA) ---
st.sidebar.success(
    """
    **Oleh:**\n
    Fransiskus Dharma Hadi Wijaya\n
    535220106\n
    Teknik Informatika / Universitas Tarumanagara
    """
)