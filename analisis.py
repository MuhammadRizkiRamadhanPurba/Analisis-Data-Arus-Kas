import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Fungsi untuk menghasilkan data acak untuk setiap entri
def generate_random_data():
    tanggal = "2024-" + str(random.randint(1, 12)).zfill(2) + "-" + str(random.randint(1, 28)).zfill(2)
    tipe_sepatu = random.choice(["Sneakers", "Sandal"])
    produksi = random.randint(300, 800)
    persediaan_awal = random.randint(0, 1000)
    penjualan = random.randint(100, 500)
    harga_jual = random.randint(100000, 200000)
    persediaan_akhir = produksi - penjualan + persediaan_awal
    omset = penjualan * harga_jual
    biaya_produksi = random.randint(5000000, 20000000)
    laba_kotor = omset - biaya_produksi
    laba_bersih = laba_kotor * 0.7  # Asumsi laba bersih 70% dari laba kotor
    return {"Tanggal": tanggal, "Tipe Sepatu": tipe_sepatu, "Produksi (unit)": produksi, 
            "Persediaan Awal (unit)": persediaan_awal, "Penjualan (unit)": penjualan, 
            "Harga Jual (Rp/unit)": harga_jual, "Persediaan Akhir (unit)": persediaan_akhir, 
            "Omset (Rp)": omset, "Biaya Produksi (Rp)": biaya_produksi, "Laba Kotor (Rp)": laba_kotor, 
            "Laba Bersih (Rp)": laba_bersih}

# Data dalam bentuk list of dictionaries
data = [generate_random_data() for _ in range(500)]  # Menghasilkan 500 baris data

# Nama file CSV untuk menyimpan data
csv_filename = "data_sepatu_ratusan.csv"

# Menulis data ke file CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"File CSV '{csv_filename}' telah berhasil dibuat dengan {len(data)} baris data.")

# Membaca file CSV menjadi DataFrame menggunakan pandas
df = pd.read_csv(csv_filename)

# Menampilkan informasi dasar tentang DataFrame
print("\nInformasi Dasar tentang Data:")
print(df.info())

# Menampilkan lima baris pertama data
print("\nPreview lima baris pertama data:")
print(df.head())

# Statistik deskriptif untuk kolom-kolom numerik
print("\nStatistik Deskriptif:")
print(df.describe())

# Visualisasi data

# Histogram produksi sepatu berdasarkan tipe
plt.figure(figsize=(10, 6))
sns.histplot(df, x='Produksi (unit)', hue='Tipe Sepatu', kde=True)
plt.title('Histogram Produksi Sepatu Berdasarkan Tipe')
plt.xlabel('Produksi (unit)')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.legend(title='Tipe Sepatu')
plt.tight_layout()
plt.show()

# Boxplot penjualan sepatu berdasarkan tipe
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Tipe Sepatu', y='Penjualan (unit)', palette='Set3')
plt.title('Boxplot Penjualan Sepatu Berdasarkan Tipe')
plt.xlabel('Tipe Sepatu')
plt.ylabel('Penjualan (unit)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot omset vs laba bersih
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Omset (Rp)', y='Laba Bersih (Rp)', hue='Tipe Sepatu', palette='Dark2')
plt.title('Scatter plot Omset vs Laba Bersih')
plt.xlabel('Omset (Rp)')
plt.ylabel('Laba Bersih (Rp)')
plt.grid(True)
plt.tight_layout()
plt.show()
