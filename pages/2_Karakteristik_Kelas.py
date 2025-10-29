import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Karakteristik Kelas",
    page_icon="🔍",
    layout="wide"
)

# --- INJEKSI CSS KUSTOM UNTUK MEWARNAI TABS ---
st.markdown("""
<style>
    /* Mengatur gaya dasar untuk semua tab */
    button[data-baseweb="tab"] {
        font-size: 1.1em;
        font-weight: bold;
        border-radius: 8px 8px 0 0;
        border: 1px solid var(--gray-40);
        margin-right: 5px;
        padding: 10px 15px;
        flex-grow: 1;
        justify-content: center;
        color: white !important; /* Membuat teks selalu putih agar kontras */
    }

    /* --- MEWARNAI TAB BERDASARKAN URUTANNYA --- */

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


# Judul Utama Halaman
st.title("🔍 Detail Karakteristik Setiap Kelas")
st.write(
    "Halaman ini menjelaskan ciri khas dari setiap kategori kondisi lalu lintas "
    "yang digunakan untuk melatih model, disertai dengan contoh visual dan audio-visual."
)

# Membuat Tab untuk setiap kelas
tab_macet, tab_lancar, tab_sepi = st.tabs(["Macet", "Lancar", "Sepi"])

# --- Konten untuk Tab MACET ---
with tab_macet:
    st.header("Karakteristik Kelas: Macet")

    st.write(
        """
        **Definisi :** Arus lalu lintas sangat padat, kecepatan rata-rata mendekati 0 km/jam, dengan jumlah kendaraan melintas sekitar ~15 kendaraan/menit.
        
        **Ciri Khas Audio:**
        - Suara dominan adalah mesin yang menyala tapi tidak bergerak (idle).
        - Terdengar pola suara stop-and-go: raungan mesin pendek saat mobil maju sedikit, lalu berhenti lagi.
        - Terdengar juga suara klakson yang panjang dan berulang serta desisan suara rem kendaraan - kendaraan besar .
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Dokumentasi Situasi Kemacetan")
        st.image("assets/images/macet.jpg", caption="Contoh visual kondisi lalu lintas macet.")
        st.video("assets/videos/macet.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/macet_spec.png", caption="Spektogram suara macet.")
        st.info(
        """
        **Analisis Spektogram (Macet):**
        - **Pita Frekuensi Rendah yang Dominan:** Terlihat sebuah pita energi horizontal yang tebal dan persisten di spektrum frekuensi rendah (umumnya di bawah 1 kHz). Pola ini secara visual merepresentasikan suara deru mesin stasioner (*idle*) yang menjadi karakteristik audio utama pada kondisi macet.
        - **Lonjakan Energi Vertikal Sporadis:** Muncul beberapa lonjakan energi vertikal yang tajam, singkat, dan mencakup rentang frekuensi yang luas. *Spike* visual ini adalah ciri khas dari suara klakson yang sering terdengar saat lalu lintas tidak bergerak.
        """
    )

# --- Konten untuk Tab LANCAR ---
with tab_lancar:
    st.header("Karakteristik Kelas: Lancar")

    st.write(
        """
        **Definisi :** Kendaraan terus bergerak maju dengan lancar dan kecepatan yang relatif stabil.

        **Ciri Khas Audio:**
        - Suara yang terdengar cukup ramai dan terus-menerus (kontinu).
        - Suara mesin dari masing-masing kendaraan sulit dibedakan karena banyak suara kendaraan yang bergerak bersamaan.
        - Jarang atau hampir tidak terdengar suara klakson, menandakan arus lalu lintas yang bergerak tanpa hambatan.
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Dokumentasi Situasi Lancar")
        st.image("assets/images/lancar.jpg", caption="Contoh visual kondisi lalu lintas lancar.")
        st.video("assets/videos/lancar.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/lancar_spec.png", caption="Spektogram suara lancar.")
        st.info(
            """
            **Analisis Spektogram (Lancar):**
            - **Blok Energi yang Padat dan Kontinu:** Spektogram menampilkan blok energi yang solid dan tersebar di berbagai rentang frekuensi (rendah hingga menengah). Pola padat ini adalah representasi visual dari fenomena "wall of sound", di mana suara dari banyak kendaraan yang bergerak bersamaan menyatu menjadi satu.
            - **Absennya Pola Distingtif:** Berbeda dengan kondisi lain, tidak terlihat adanya lonjakan energi vertikal yang tajam (klakson) ataupun jeda keheningan yang signifikan. Tekstur visual yang cenderung homogen ini mengindikasikan bahwa arus lalu lintas bergerak secara stabil dan tanpa hambatan.
            """
        )

# --- Konten untuk Tab SEPI ---
with tab_sepi:
    st.header("Karakteristik Kelas: Sepi")

    st.write(
        """
        **Definisi :** Kondisi jalan sangat lengang, hanya ada sedikit kendaraan yang lewat dengan jarak yang cukup jauh antara satu sama lain. Jumlah kendaraan melintas sekitar ~30 kendaraan/menit.

        **Ciri Khas Audio:**
        - Suara setiap kendaraan yang lewat dapat didengar dengan sangat jelas dan terpisah satu sama lain.
        - Terdapat jeda hening yang nyata di antara suara satu kendaraan dengan kendaraan berikutnya.
        - Suara yang paling khas adalah bunyi kendaraan yang mendekat, melintas, lalu suaranya menghilang di kejauhan.
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Dokumentasi Situasi Sepi")
        st.image("assets/images/sepi.jpg", caption="Contoh visual kondisi lalu lintas sepi.")
        st.video("assets/videos/sepi.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/sepi_spec.png", caption="Spektogram suara sepi.")
        st.info(
            """
            **Analisis Spektogram (Sepi):**
            - **Jeda Keheningan yang Dominan:** Sebagian besar area spektogram berwarna gelap, merepresentasikan level energi suara yang sangat rendah. Ini adalah visualisasi dari jeda hening yang signifikan di antara setiap kendaraan yang melintas, yang merupakan ciri utama dari kondisi lalu lintas sepi.
            - **Peristiwa Akustik yang Terisolasi:** Muncul blok-blok energi yang jelas namun terpisah satu sama lain. Setiap blok ini mewakili satu peristiwa suara yang terisolasi, yaitu satu kendaraan yang sedang melintas.
            - **Pola Frekuensi Melengkung (Efek Doppler):** Seringkali, blok energi ini menunjukkan pola visual melengkung. Lengkungan ini adalah representasi dari **Efek Doppler**, di mana frekuensi (nada) suara kendaraan terdengar meningkat saat mendekat dan kemudian menurun saat menjauh.
            """
        )