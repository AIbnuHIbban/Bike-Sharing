# Bike Sharing Analysis Dashboard

Dashboard ini menampilkan analisis data penyewaan sepeda menggunakan Streamlit. Dashboard ini memberikan wawasan tentang pengaruh cuaca terhadap jumlah penyewaan sepeda serta tren penyewaan sepeda selama satu tahun.

## Struktur Repository

- `streamlit_app.py`: Script utama yang berisi kode untuk menjalankan dashboard Streamlit.
- `requirements.txt`: File yang berisi daftar library Python yang dibutuhkan untuk menjalankan dashboard.
- `day.csv`: Dataset yang digunakan dalam analisis.

## Instalasi

1. Clone repository ini ke komputer Anda:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Buat virtual environment (opsional tapi disarankan):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk pengguna macOS/Linux
    .\venv\Scripts\activate  # Untuk pengguna Windows
    ```

3. Install library yang dibutuhkan menggunakan `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Dashboard

1. Pastikan Anda berada di direktori repository.
2. Jalankan Streamlit dengan perintah berikut:
    ```bash
    streamlit run streamlit_app.py
    ```

3. Dashboard akan terbuka di browser web default Anda.

## Fitur Dashboard

### Sidebar
- **Pilih Tahun**: Anda bisa memilih tahun (2011 atau 2012) untuk melihat analisis data penyewaan sepeda pada tahun tersebut.

### Halaman Utama
- **Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca**: Menampilkan grafik batang yang menunjukkan rata-rata penyewaan sepeda untuk setiap kondisi cuaca.
- **Tren Penyewaan Sepeda Selama Tahun yang Dipilih**: Menampilkan grafik garis yang menunjukkan tren penyewaan sepeda selama tahun yang dipilih.
- **Analisis Cluster Berdasarkan Kondisi Cuaca**: Menampilkan deskripsi statistik untuk setiap cluster kondisi cuaca.
- **Kesimpulan**: Ringkasan kesimpulan dari analisis data.

## Dataset
Dataset yang digunakan (`day.csv`) berisi informasi tentang penyewaan sepeda yang diambil dari sistem penyewaan sepeda di Washington D.C. untuk tahun 2011 dan 2012. Dataset ini mencakup berbagai fitur seperti tanggal, musim, cuaca, dan jumlah penyewaan.
