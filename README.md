# 🚲 Dicoding Bike Sharing Dashboard
```
Analisis data dengan bike sharing dataset by Nabs 🐱
```
## Setup Environment - Shell/Terminal
```bash
mkdir Submission
cd Submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit app
```bash
cd Dashboard
streamlit run dashboard.py
```

## 🗒️ Analisis Data dengan Google Colab

### Mendefinisikan Pertanyaan Bisnis
1. Bagaimana suhu (suhu yang dirasakan penyewa) mempengaruhi jumlah penyewa sepeda?
2. Bagaimana hubungan kecepatan angin dan kelembapan terhadap jumlah penyewa?
3. Bagaimana rata-rata perubahan jumlah penyewa di hari libur?
4. Bagaimana tren banyak penyewa sepeda pada tahun 2012?
5. Pukul berapa waktu (jam) paling banyak terjadi transaksi sewa sepeda dan paling sedikit tejadi transaksi sewa sepeda?

### Kesimpulan singkat yang Diperoleh 
1. Cuaca yang lebih hangat (suhu terasa lebih tinggi) cenderung lebih banyak orang untuk menyewa sepeda. 
2. Perubahan tingkat kelembaban tidak memberikan pengaruh yang signifikan terhadap jumlah penyewa sepeda. Kecepatan angin tinggi, cenderung kelembaban udara akan lebih rendah.
3. Hari libur memiliki pengaruh yang signifikan terhadap peningkatan jumlah penyewa.
4. Jumlah penyewa sepeda pada tahun 2012 mengalami peningkatan yang cukup signifikan dari bulan ke bulan. Terdapat periode di mana jumlah penyewa sangat tinggi, dan ada pula periode di mana jumlah penyewa rendah. Secara umum, tidak terlihat adanya tren kenaikan atau penurunan yang teratur sepanjang tahun.
5. Jumlah penyewa mencapai puncaknya pada jam 17 dengan total lebih dari 336.000 penyewa. Jumlah penyewa paling sedikit terjadi pada jam 4 dini hari dengan kurang dari 5.000 penyewa. Ini menunjukkan bahwa dini hari adalah waktu di mana minat masyarakat untuk menyewa sepeda sangat rendah. 

🌻 Streamlit Dashboard dari analisis data Bike Sharing Dataset by Nabs 🐱 => https://da-bikesharing-bynabs.streamlit.app/ 
