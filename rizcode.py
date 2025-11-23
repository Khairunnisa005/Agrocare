import pandas as pd
from datetime import timedelta
import tabulate
import os
#buat nyoba  eheehehehe


#==============
#== Shorting ==
#==============
def Shorting ():
    os.system('cls')
    #untuk membaca data jual beli
    penjualan = pd.read_csv('sales.csv')
    # program ini untuk merubah kolom 'tanggal' menjadi datetime
    penjualan['tanggal'] = pd.to_datetime(penjualan['tanggal'])

    # Cari nilai maksimum (tanggal terbaru) di kolom 'tanggal'
    tanggal_terakhir_data = penjualan['tanggal'].dt.normalize().max()

    # Tentukan batas akhir satu hari setelah tanggal terakhir di data.
    end_date = tanggal_terakhir_data + timedelta(days=1)

    while True:
        print("== pilih waktu nya ==")
        print("1. data hari ini")
        print("2. data 1 minggu ")
        print("3. data 1 bulan")
        pillihan = input("Masukkan perintah berupa angka 1/2/3: ")

        if pillihan == "1":
            #menentukan batas tanggal dari data yang ingin dikluarkan 
            start_date = end_date - timedelta(days=1)
            filtered = penjualan[
                (penjualan['tanggal'] >= start_date) & 
                (penjualan['tanggal'] < end_date) 
            ]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            Shorting()
        elif pillihan == "2":
            start_date = end_date - timedelta(days=7)
            filtered = penjualan[
                (penjualan['tanggal'] >= start_date) & 
                (penjualan['tanggal'] < end_date) 
            ]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            Shorting()
        elif pillihan == "3":
            start_date = end_date - timedelta(days=30)
            filtered = penjualan[
                (penjualan['tanggal'] >= start_date) & 
                (penjualan['tanggal'] < end_date) 
            ]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            Shorting()
        elif pillihan =="4":
            input("klik enter untuk lanjut.......")
            menu_utama()
        else :
            print("input ayang anda masukkan salah")