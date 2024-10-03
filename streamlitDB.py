import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.markdown("""
    <style>
    /* General Layout */
    .main {
        background-color: #F3F4F6;
    }
    /* Title styling */
    .stApp h1 {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        color: #F0EBCE;
        background-color: #395144;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    /* Info box styling */
    .stAlert {
        background-color: #F0EBCE;
        color: #4A4947;
        font-size: 1.1rem;
        border-left: 5px solid #4E6C50;
    }
    /* Styling for expander */
    .st-expander {
        background-color: #AA8B56;
        border: 1px solid #D5CAB8;
        padding: 10px;
        border-radius: 5px;
    }
    /* Text and selectbox styling */
    .stSelectbox {
        font-size: 1.2rem;
        color: #333;
    }
    .st-bx .block-container {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚲 Bike Sharing Analysis by Nabs")

# Info Box Styling
st.info("Analisis data sederhana dengan Google Colab menggunakan Bike Sharing Dataset")

# Data Expander
with st.expander('Data yang sudah bersih'):
    st.write('**day.csv**')
    day = pd.read_csv('day-cleaned.csv')
    st.dataframe(day, height=150)
    st.write('**hour.csv**')
    hour = pd.read_csv('hour-cleaned.csv')
    st.dataframe(hour, height=150)

# Question Selector
question = st.selectbox("Pilih Pertanyaan", ["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4", "Pertanyaan 5"])

# Question 1
if question == "Pertanyaan 1":
    st.header("Bagaimana suhu (suhu yang dirasakan penyewa) mempengaruhi jumlah penyewa sepeda?")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(day['suhu_terasa'], day['total_penyewa'], alpha=0.5, color='#B17457')
    ax.set_xlabel('Suhu Terasa')
    ax.set_ylabel('Jumlah Penyewa Sepeda')
    ax.set_title('Hubungan antara Suhu Terasa dan Jumlah Penyewa Sepeda')
    ax.grid(True)
    st.pyplot(fig)

    if st.button("Lihat Kesimpulan Pertanyaan 1"):
            st.write("Titik-titik data tersebar cukup merata, menunjukkan adanya hubungan positif antara suhu terasa dan jumlah penyewa sepeda. Semakin tinggi suhu terasa, cenderung semakin banyak orang yang menyewa sepeda. Oleh karena itu, cuaca yang lebih hangat (suhu terasa lebih tinggi) cenderung lebih banyak orang untuk menyewa sepeda. Pada umumnya orang lebih suka beraktivitas di luar ruangan saat cuaca cerah dan hangat.")

# Question 2
elif question == "Pertanyaan 2":
    st.header("Bagaimana hubungan kecepatan angin dan kelembapan terhadap jumlah penyewa?")
    correlation_matrix = day[['kecepatan_angin', 'kelembapan', 'total_penyewa']].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='magma', fmt=".2f", ax=ax)
    ax.set_title('Korelasi antara Kecepatan Angin, Kelembapan, dan Jumlah Penyewa')
    st.pyplot(fig)

    if st.button("Lihat Kesimpulan Pertanyaan 2"):
            st.write("Terdapat korelasi negatif yang cukup kuat antara kecepatan angin dan jumlah penyewa (nilai -0.23). Ini berarti semakin tinggi kecepatan angin, cenderung semakin sedikit orang yang menyewa sepeda. Korelasi antara kelembaban dan jumlah penyewa sangat lemah (nilai -0.10). Artinya, perubahan tingkat kelembaban tidak memberikan pengaruh yang signifikan terhadap jumlah penyewa sepeda. Terdapat korelasi negatif yang cukup kuat antara kecepatan angin dan kelembaban (nilai -0.25). Ini menunjukkan bahwa ketika kecepatan angin tinggi, cenderung kelembaban udara akan lebih rendah. Oleh karena itu faktor yang paling berpengaruh terhadap jumlah penyewa sepeda adalah kecepatan angin. Semakin rendah kecepatan angin, semakin banyak orang cenderung menyewa sepeda. Faktor kelembaban, berdasarkan data ini, tidak memberikan pengaruh yang signifikan.")

# Question 3
elif question == "Pertanyaan 3":
    st.header("Bagaimana rata-rata perubahan jumlah penyewa di hari libur?")
    holiday_rental_counts = hour.groupby('holiday')['total_penyewa'].mean()
    colors = ['#4A4947', '#B17457']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(holiday_rental_counts.index, holiday_rental_counts.values, color=colors)
    ax.set_xlabel('Holiday')
    ax.set_ylabel('Rata-rata Jumlah Penyewa')
    ax.set_title('Perubahan Jumlah Penyewa di Hari Libur')
    ax.set_xticks(holiday_rental_counts.index, ['Tidak Libur', 'Libur'])
    st.pyplot(fig)

    if st.button("Lihat Kesimpulan Pertanyaan 3"):
            st.write("Kesimpulan yang diperoleh dari grafik adalah rata-rata jumlah penyewa pada hari libur jauh lebih tinggi dibandingkan hari biasa. Hal ini ditunjukkan dengan tinggi batang grafik yang lebih mencolok pada kategori Libur. Rata-rata jumlah penyewa pada hari biasa berada pada level yang lebih rendah. Oleh karena itu, hari libur memiliki pengaruh yang signifikan terhadap peningkatan jumlah penyewa. Kemungkinan alasannya adalah waktu luang, dimana pada hari libur, banyak orang memiliki lebih banyak waktu luang untuk melakukan aktivitas di luar ruangan, termasuk menyewa sesuatu. Selanjutnya adalah aktivitas rekreasi, hari libur seringkali dikaitkan dengan aktivitas rekreasi atau liburan, sehingga kebutuhan akan penyewaan barang atau jasa meningkat.")

# Question 4
elif question == "Pertanyaan 4":
    st.header("Bagaimana tren banyak penyewa sepeda selama tahun 2012?")
    data_2012 = day[day['tahun'] == 2012]
    day['tanggal'] = pd.to_datetime(day['tanggal'])
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data_2012['tanggal'], data_2012['total_penyewa'], color='#B17457', label='Total Penyewa 2012')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewa Sepeda')
    ax.set_title('Tren Jumlah Penyewa Sepeda Tahun 2012')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    if st.button("Lihat Kesimpulan Pertanyaan 4"):
            st.write("Kesimpulan yang diperoleh dari grafik adalah jumlah penyewa sepeda pada tahun 2012 mengalami peningkatan yang cukup signifikan dari bulan ke bulan. Terdapat periode di mana jumlah penyewa sangat tinggi, dan ada pula periode di mana jumlah penyewa rendah.Secara umum, tidak terlihat adanya tren kenaikan atau penurunan yang teratur sepanjang tahun. Jumlah penyewa cenderung naik turun secara tidak teratur.")

# Question 5
elif question == "Pertanyaan 5":
    st.header("Pukul berapa waktu (jam) paling banyak terjadi transaks sewa sepeda dan paling sedikit terjadi transaksi sewa sepeda?")
    hourly_rental_counts = hour.groupby('jam')['total_penyewa'].sum()
    jam_terbanyak = hourly_rental_counts.idxmax()
    jumlah_terbanyak = hourly_rental_counts.max()
    jam_tersedikit = hourly_rental_counts.idxmin()
    jumlah_tersedikit = hourly_rental_counts.min()
    st.write(f"Jam dengan jumlah penyewa terbanyak: {jam_terbanyak} (Jumlah: {jumlah_terbanyak})")
    st.write(f"Jam dengan jumlah penyewa tersedikit: {jam_tersedikit} (Jumlah: {jumlah_tersedikit})")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hourly_rental_counts.index, hourly_rental_counts.values, marker='o', color='#B17457')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Penyewa')
    ax.set_title('Jumlah Penyewa Sepeda per Jam')
    ax.grid(True)
    st.pyplot(fig)

    if st.button("Lihat Kesimpulan Pertanyaan 5"):
            st.write(f"Kesimpulan yang dapat diperoleh dari grafik adalah jumlah penyewa mencapai puncaknya pada jam 17 dengan total lebih dari 336.000 penyewa. Ini menunjukkan bahwa sore hari, terutama menjelang malam, adalah waktu di mana permintaan akan penyewaan sepeda paling tinggi. Sebaliknya, jumlah penyewa paling sedikit terjadi pada jam 4 dini hari dengan kurang dari 5.000 penyewa. Ini menunjukkan bahwa dini hari adalah waktu di mana minat masyarakat untuk menyewa sepeda sangat rendah. Secara umum, jumlah penyewa cenderung meningkat dari pagi menuju sore hari, mencapai puncaknya di sore hari, kemudian menurun drastis pada malam hari. Terdapat peningkatan yang cukup signifikan pada jumlah penyewa dari satu jam ke jam berikutnya.")

