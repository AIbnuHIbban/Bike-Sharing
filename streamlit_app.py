import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('day.csv')

# Preprocessing
data['dteday'] = pd.to_datetime(data['dteday'])

# Mapping for weather situation in Indonesian
weather_mapping = {
    1: 'Cerah, Sedikit berawan, Berawan sebagian',
    2: 'Kabut + Berawan, Kabut + Awan terpecah, Kabut + Sedikit awan, Kabut',
    3: 'Salju ringan, Hujan ringan + Badai petir + Awan tersebar, Hujan ringan + Awan tersebar',
    4: 'Hujan lebat + Es + Badai petir + Kabut, Salju + Kabut'
}
data['weather_desc'] = data['weathersit'].map(weather_mapping)

# Convert 'dteday' to string to avoid serialization issues
data['dteday'] = data['dteday'].astype(str)

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
year_option = st.sidebar.selectbox("Pilih Tahun", (2011, 2012))

# Filter data based on the selected year
data_filtered = data[data['yr'] == (year_option - 2011)]

# Title
st.title(f"Analisis Penyewaan Sepeda - {year_option}")

# Average Rentals by Weather Situation
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
weather_counts = data_filtered.groupby('weather_desc')['cnt'].mean()
fig, ax = plt.subplots()
weather_counts.plot(kind='bar', ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Jumlah Penyewaan')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig)

# Bike Rentals Over Time
st.subheader(f"Tren Penyewaan Sepeda Selama Tahun {year_option}")
fig, ax = plt.subplots()
data_filtered.set_index('dteday')['cnt'].plot(ax=ax)
ax.set_title(f'Rental Sepeda Selama Tahun {year_option}')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Cluster Analysis
st.subheader("Analisis Cluster Berdasarkan Kondisi Cuaca")
weather_conditions = data['weathersit'].unique()

for condition in weather_conditions:
    cluster = data[data['weathersit'] == condition]
    st.write(f"Cluster {weather_mapping[condition]}:")
    st.write(cluster.describe())

# Conclusion
st.subheader("Kesimpulan")
st.write("""
1. **Pengaruh Cuaca Terhadap Penyewaan Sepeda:**
   - Cuaca yang baik (cerah dan berawan sebagian) memiliki rata-rata jumlah penyewaan sepeda tertinggi.
   - Cuaca yang buruk (salju ringan, hujan ringan) memiliki rata-rata jumlah penyewaan sepeda terendah.

2. **Tren Penyewaan Sepeda:**
   - Tren penyewaan sepeda meningkat secara bertahap dari Januari hingga mencapai puncaknya sekitar bulan Juli dan Agustus.
   - Setelah bulan Agustus, tren mulai menurun hingga akhir tahun.
""")
