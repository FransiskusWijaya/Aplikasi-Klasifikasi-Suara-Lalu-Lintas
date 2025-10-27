import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Karakteristik Kelas",
    page_icon="🔍",
    layout="wide"
)

# Judul Utama Halaman
st.title("🔍 Detail Karakteristik Setiap Kelas")
st.write(
    "Halaman ini menjelaskan ciri khas dari setiap kategori kondisi lalu lintas "
    "yang digunakan untuk melatih model, disertai dengan contoh visual dan audio-visual."
)

# Membuat Tab untuk setiap kelas
tab_macet, tab_lancar, tab_sepi = st.tabs(["🛑 Macet", "⚠️ Lancar", "✅ Sepi"])

# --- Konten untuk Tab MACET ---
with tab_macet:
    st.header("Karakteristik Kelas: Macet")

    st.write(
        """
        **Definisi Operasional:** Arus lalu lintas sangat padat, kecepatan rata-rata mendekati 0 km/jam, dengan jumlah kendaraan melintas sekitar **~15 kendaraan/menit**.
        
        **Ciri Khas Audio:**
        - Suara dominan adalah **mesin yang menyala tapi tidak bergerak (idle)**.
        - Terdengar pola suara **stop-and-go**: raungan mesin pendek saat mobil maju sedikit, lalu berhenti lagi.
        - Frekuensi **suara klakson yang panjang dan repetitif** sangat tinggi, menandakan frustrasi.
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Contoh Media")
        st.image("assets/images/macet.jpg", caption="Contoh visual kondisi lalu lintas macet.")
        st.video("assets/videos/macet.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/macet_spec.png", caption="Spektogram suara macet.")
        st.info(
            """
            **Analisis Spektogram (Macet):**
            - Terlihat **garis-garis horizontal tebal di frekuensi rendah**, yang merepresentasikan suara mesin idle.
            - Muncul **lonjakan energi vertikal yang tajam dan singkat (spikes)** pada frekuensi menengah-tinggi, yang merupakan ciri khas suara klakson.
            """
        )

# --- Konten untuk Tab LANCAR ---
with tab_lancar:
    st.header("Karakteristik Kelas: Lancar")

    st.write(
        """
        **Definisi Operasional:** Arus lalu lintas bergerak konstan dengan kecepatan stabil, jumlah kendaraan melintas sekitar **~80 kendaraan/menit**.
        
        **Ciri Khas Audio:**
        - Suara terdengar seperti **"dinding kebisingan" (wall of sound)** yang ramai dan kontinu.
        - Sulit untuk membedakan suara mesin secara individual karena semuanya **menyatu menjadi satu deru yang konstan**.
        - Suara klakson hampir tidak ada karena arus lalu lintas bergerak tanpa hambatan.
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Contoh Media")
        st.image("assets/images/lancar.jpg", caption="Contoh visual kondisi lalu lintas lancar.")
        st.video("assets/videos/lancar.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/lancar_spec.png", caption="Spektogram suara lancar.")
        st.info(
            """
            **Analisis Spektogram (Lancar):**
            - Energi suara **terdistribusi secara merata** di berbagai rentang frekuensi, menciptakan blok warna yang solid dan padat.
            - Tidak ada jeda atau keheningan yang jelas, menunjukkan kebisingan yang terus-menerus.
            """
        )

# --- Konten untuk Tab SEPI ---
with tab_sepi:
    st.header("Karakteristik Kelas: Sepi")

    st.write(
        """
        **Definisi Operasional:** Arus lalu lintas sangat lengang, dengan jeda waktu yang signifikan antar kendaraan. Jumlah kendaraan melintas sekitar **~30 kendaraan/menit**.
        
        **Ciri Khas Audio:**
        - Suara mesin kendaraan terdengar **sangat jelas dan terputus-putus**.
        - Terdapat **jeda hening** yang nyata di antara suara satu mobil dengan mobil berikutnya.
        - Suara dominan adalah kendaraan yang melintas cepat dan menghilang (efek Doppler).
        """
    )
    st.divider()

    # KONTENER 1: CONTOH MEDIA
    with st.container(border=True):
        st.subheader("Contoh Media")
        st.image("assets/images/sepi.jpg", caption="Contoh visual kondisi lalu lintas sepi.")
        st.video("assets/videos/sepi.mp4")

    # KONTENER 2: ANALISIS SPEKTROGRAM
    with st.container(border=True):
        st.subheader("Representasi Spektogram")
        st.image("assets/spectrograms/sepi_spec.png", caption="Spektogram suara sepi.")
        st.info(
            """
            **Analisis Spektogram (Sepi):**
            - Terlihat **blok-blok energi suara yang terpisah** dengan area gelap (hening) di antaranya.
            - Pola suara seringkali berbentuk seperti **lengkungan tipis**, menunjukkan perubahan frekuensi saat kendaraan mendekat lalu menjauh.
            """
        )