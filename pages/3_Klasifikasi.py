# ==============================================================================
# --- IMPORT LIBRARY YANG DIBUTUHKAN ---
# ==============================================================================
import streamlit as st
import tensorflow as tf
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import pandas as pd
import cv2  # Library untuk memproses gambar (mengubah ukuran spektrogram)
import json # Library untuk membaca file .json
from sklearn.preprocessing import LabelEncoder # Untuk membangun kembali encoder

# ==============================================================================
# --- FUNGSI-FUNGSI UTAMA (Tidak ada perubahan di sini) ---
# ==============================================================================

@st.cache_resource
def load_model_and_encoder():
    """
    Memuat model CRNN (.h5) dan membangun LabelEncoder dari file .json.
    Ini adalah metode yang paling kuat untuk menghindari error versi library.
    """
    try:
        # 1. Muat model deep learning Anda
        model = tf.keras.models.load_model('model_final_crnn_spectrogram.h5')
        
        # 2. Muat daftar kelas dari file JSON
        with open('label_classes.json', 'r') as f:
            class_names = json.load(f)
        
        # 3. Buat ulang objek LabelEncoder dari daftar kelas tersebut
        le = LabelEncoder()
        le.fit(class_names)
        
        return model, le
        
    except Exception as e:
        st.error(f"Error: Gagal memuat file. Pastikan 'model_final_crnn_spectrogram.h5' dan 'label_classes.json' ada di folder utama.\nDetail: {e}")
        return None, None

def extract_spectrogram_for_prediction(audio_data, sample_rate, target_shape=(128, 128)):
    """
    Mengekstrak Mel-Spektrogram untuk PREDIKSI MODEL.
    Fungsi ini HARUS SAMA PERSIS dengan yang digunakan saat training di Colab.
    """
    try:
        # 1. Buat Mel-Spectrogram dari data audio
        mel_spec = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate, n_mels=128)
        log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
        
        # 2. Ubah ukurannya agar sesuai dengan input model (misal: 128x128)
        resized_spec = cv2.resize(log_mel_spec, (target_shape[1], target_shape[0]))
        
        # 3. Reshape agar sesuai dengan format input model: (1, tinggi, lebar, 1)
        # Angka '1' di depan berarti kita hanya memprediksi satu sampel.
        reshaped_spec = resized_spec.reshape(1, target_shape[0], target_shape[1], 1)
        
        return reshaped_spec
    except Exception as e:
        st.error(f"Error saat mengekstrak fitur spektrogram: {e}")
        return None

# ==============================================================================
# --- TAMPILAN APLIKASI STREAMLIT (BAGIAN YANG DIUBAH ADA DI SINI) ---
# ==============================================================================

st.set_page_config(page_title="Klasifikasi Audio Lalu Lintas", page_icon="🚦")

# --- KONTROL DI SIDEBAR ---
st.sidebar.title("⚙️ Opsi Klasifikasi")
confidence_threshold = st.sidebar.slider(
    label="Ambang Batas Kepercayaan (%)",
    min_value=0,
    max_value=100,
    value=50, # Nilai default
    step=5,
    help="Hanya tampilkan prediksi jika tingkat kepercayaan model di atas nilai ini."
)
st.sidebar.info(f"Ambang batas saat ini: **{confidence_threshold}%**")

# --- KONTEN HALAMAN UTAMA ---
st.title("🚦 Analisis Kondisi Lalu Lintas via Suara")
st.write("Unggah rekaman suara kondisi lalu lintas untuk dianalisis oleh model CRNN.")

model, le = load_model_and_encoder()

# Hanya jalankan jika model dan encoder berhasil dimuat
if model is not None and le is not None:
    # PERUBAHAN 1: Hapus argumen 'type' dari file_uploader
    uploaded_file = st.file_uploader("Pilih file audio")
    
    # PERUBAHAN 2: Tambahkan blok validasi manual
    if uploaded_file is not None:
        # Cek tipe file secara manual
        is_valid_type = uploaded_file.name.lower().endswith(('.wav', '.mp3'))
        
        if is_valid_type:
            # Jika tipe file BENAR, jalankan kode seperti biasa
            st.audio(uploaded_file)
            
            if st.button("Analisis Kondisi Lalu Lintas"):
                with st.spinner('Model sedang menganalisis suara...'):
                    try:
                        audio, sr = librosa.load(uploaded_file, sr=None)
                        fitur_spectrogram = extract_spectrogram_for_prediction(audio, sr)
                        
                        if fitur_spectrogram is not None:
                            prediksi = model.predict(fitur_spectrogram)
                            top_index = np.argmax(prediksi[0])
                            confidence_score = prediksi[0][top_index] * 100
                            st.subheader("Hasil Analisis")

                            if confidence_score >= confidence_threshold:
                                predicted_class_name = le.inverse_transform([top_index])[0]
                                st.success(f"**Prediksi Kondisi:** {predicted_class_name.title()} ({confidence_score:.2f}%)")
                                
                                # Visualisasi... (kode ini tidak diubah)
                                st.subheader("Distribusi Kepercayaan Prediksi")
                                prob_df = pd.DataFrame({'Kelas Kondisi': le.classes_, 'Probabilitas': prediksi[0] * 100})
                                st.bar_chart(prob_df.set_index('Kelas Kondisi'))
                                
                                st.subheader("Visualisasi Mel-Spektrogram")
                                fig, ax = plt.subplots(figsize=(10, 4))
                                mels_for_display = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128)
                                log_mels = librosa.power_to_db(mels_for_display, ref=np.max)
                                img = librosa.display.specshow(log_mels, sr=sr, x_axis='time', y_axis='mel', ax=ax, cmap='magma')
                                fig.colorbar(img, ax=ax, format='%+2.0f dB')
                                ax.set_title(f'Mel-Spektrogram dari {uploaded_file.name}')
                                st.pyplot(fig)
                            else:
                                st.warning(f"Model tidak cukup yakin dengan prediksinya. Kepercayaan tertinggi hanya {confidence_score:.2f}%, di bawah ambang batas {confidence_threshold}%.")

                    except Exception as e:
                        st.error(f"Gagal memproses file. Mungkin formatnya tidak didukung atau file rusak.\nDetail: {e}")
        else:
            # PERUBAHAN 3: Jika tipe file SALAH, tampilkan pesan eror kustom Anda
            st.error(f"❌ Format File Salah! Anda mengunggah file '{uploaded_file.name}'. Harap unggah file audio dengan format .wav atau .mp3.")