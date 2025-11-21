
import pandas as pd
from datetime import timedelta
import tabulate
penjualan = pd.read_csv('sales.csv')
# Tidak perlu mengimpor datetime dari datetime lagi, cukup timedelta
penjualan['tanggal'] = pd.to_datetime(penjualan['tanggal'])

# Cari nilai maksimum (tanggal terbaru) di kolom 'tanggal'.
# .dt.normalize() memastikan kita mendapatkan tanggal terbaru yang bersih dari komponen waktu.
tanggal_terakhir_data = penjualan['tanggal'].dt.normalize().max()

# Tentukan batas akhir (Eksklusif): satu hari setelah tanggal terakhir di data.
# Contoh: Jika data terakhir adalah 2025-10-06, end_date akan menjadi 2025-10-07 00:00:00.
end_date = tanggal_terakhir_data + timedelta(days=1)


print("== pilih waktu nya ==")
print("1. data hari ini")
print("2. data 1 minggu ")
print("3. data 1 bulan")
pillihan = input("Masukkan perintah berupa angka 1/2/3: ")

if pillihan == "1":
    start_date = end_date - timedelta(days=1)
    filtered = penjualan[
        (penjualan['tanggal'] >= start_date) & 
        (penjualan['tanggal'] < end_date) 
    ]
    print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))

elif pillihan == "2":
    start_date = end_date - timedelta(days=7)
    filtered = penjualan[
        (penjualan['tanggal'] >= start_date) & 
        (penjualan['tanggal'] < end_date) 
    ]
    print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))

elif pillihan == "3":
    start_date = end_date - timedelta(days=30)
    filtered = penjualan[
        (penjualan['tanggal'] >= start_date) & 
        (penjualan['tanggal'] < end_date) 
    ]
    print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
