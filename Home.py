import streamlit as st

st.set_page_config(
    page_title="Home - Analisis Suara Lalu Lintas",
    page_icon="🚦",
    layout="wide"
)

st.markdown("""
<style>
    button[data-baseweb="tab"] {
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 8px 8px 0 0;
        border: 1px solid var(--gray-40);
        margin-right: 5px;
        padding: 10px 15px;
        flex-grow: 1;
        justify-content: center;
        color: white !important;
    }

    /* Tab 1: Macet (Merah) */
    button[data-baseweb="tab"]:nth-of-type(1) {
        background-color: #ef9a9a; /* Warna merah muda (tidak aktif) */
    }
    button[data-baseweb="tab"][aria-selected="true"]:nth-of-type(1) {
        background-color: #e57373; /* Warna merah lebih pekat (aktif) */
    }

    /* Tab 2: Lancar (Kuning) */
    button[data-baseweb="tab"]:nth-of-type(2) {
        background-color: #fff59d; /* Warna kuning muda (tidak aktif) */
        color: #5d4037 !important; /* Teks gelap agar terbaca di background kuning */
    }
    button[data-baseweb="tab"][aria-selected="true"]:nth-of-type(2) {
        background-color: #ffee58; /* Warna kuning lebih pekat (aktif) */
        color: #5d4037 !important; /* Teks gelap agar terbaca di background kuning */
    }

    /* Tab 3: Sepi (Hijau) */
    button[data-baseweb="tab"]:nth-of-type(3) {
        background-color: #a5d6a7; /* Warna hijau muda (tidak aktif) */
    }
    button[data-baseweb="tab"][aria-selected="true"]:nth-of-type(3) {
        background-color: #81c784; /* Warna hijau lebih pekat (aktif) */
    }
</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 1], vertical_alignment="center")

with col1:
    st.title("Analisis Kondisi Lalu Lintas Berdasarkan Suara 🚦")
    st.markdown(
        """
        Selamat datang! Aplikasi ini adalah prototipe penelitian untuk menjawab sebuah pertanyaan utama:
        > **_Bisakah Kecerdasan Buatan (AI) membedakan kondisi lalu lintas—Sepi, Lancar, atau Macet—hanya dengan "mendengarkan" suara lingkungan?_**
        
        Aplikasi ini menggunakan model **Convolutional Recurrent Neural Network (CRNN)** untuk menganalisis rekaman suara dan mengklasifikasikannya.
        """
    )

with col2:
    st.image("assets/images/soundwave_logo.png", width=250)

st.divider()

st.subheader("Dengarkan Perbedaannya 🎧")

tab_macet, tab_lancar, tab_sepi = st.tabs(["Macet", "Lancar", "Sepi"])

with tab_macet:
    st.write("**Karakteristik:** Suara mesin idle, klakson, dan pola audio *stop-and-go*.")
    st.audio("assets/samples/Macet.wav")

with tab_lancar:
    st.write("**Karakteristik:** Deru kebisingan yang ramai dan konstan (*wall of sound*).")
    st.audio("assets/samples/Lancar.wav")

with tab_sepi:
    st.write("**Karakteristik:** Suara kendaraan yang jelas dan terputus-putus, diselingi jeda hening.")
    st.audio("assets/samples/Sepi.wav")

st.divider()

st.subheader("Mulai Eksplorasi 🚀")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("### 📝 Tentang Proyek")
        st.write("Dapatkan informasi mendalam mengenai arsitektur model, dataset, dan metodologi penelitian.")
        st.page_link("pages/1_About.py", label="Baca Selengkapnya", icon="➡️")

with col2:
    with st.container(border=True):
        st.markdown("### 📊 Karakteristik Kelas")
        st.write("Pelajari ciri khas audio dan spektogram dari setiap kondisi lalu lintas yang digunakan.")
        st.page_link("pages/2_Karakteristik_Kelas.py", label="Lihat Detail", icon="➡️")

with col3:
    with st.container(border=True):
        st.markdown("### 🔊 Klasifikasi Audio")
        st.write("Unggah file audio lalu lintas Anda dan biarkan model kami menganalisisnya secara *real-time*.")
        st.page_link("pages/3_Klasifikasi.py", label="Mulai Analisis", icon="➡️")

st.sidebar.success(
    """
    **Oleh:**\n
    Fransiskus Dharma Hadi Wijaya\n
    535220106\n
    Teknik Informatika\n
    Universitas Tarumanagara
    """
)