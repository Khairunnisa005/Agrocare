import pandas as pd
import os
import csv
import tabulate


USER_FILE = "users.csv"
PRODUCT_FILE = "products.csv"
SALES_FILE = "sales.csv"

def login():
    os.system('cls')
    #Baca CSV

    data_akun = pd.read_csv("users.csv")

    print("========================================================")
    print("============== SELAMAT DATANG DI AGROCARE ==============")
    print("====================== LOGIN ===========================")

    username = input("Masukkan Username : ")

    #cek username
    akun = data_akun[data_akun["username"] == username]

    if akun.empty:
        print("\n Username tidak terdaftar. Silahkan daftarr/register telebih dahulu.") 
        return None

    #kalo usn benar minta passwod
    password = input("Masukkan Password : ")

    #cek apakah pw dan usn benar
    password_benar = data_akun[
        (data_akun["username"] == username) & 
        (data_akun["password"] == password)
    ]
    #cek pw
    if password_benar.empty: 
        print("\n Password salah! Silahkan coba lagi.")
        return username #jika pw salah mka kembali ke menu

    # jika usn dan pw benar cek role maka login berhasil
    role = password_benar.iloc[0]["role"]

    # Tampilan selamat datang sesuai role
    if role == "admin":
        print(f"\n Login berhasil! Selamat datang ADMIN,", username)
        menu_admin(username)
    else:
        print(f"\n Login berhasil! Selamat datang di Agrocare,", username)
        menu_pembeli(username)
        
        



def ubah_username(username_lama):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================Ubah Username================")
    username_baru = input("Masukkan username baru: ")

    #cek apakah username baru sudah ada
    if username_baru in data_akun["username"]. values:
        print("username sudah sudah terdaftar!")
        return username_lama
        
    #update username
    data_akun.loc[data_akun["username"] == username_lama, "username"] = username_baru
    data_akun.to_csv("users.csv", index=False)

    print("username berhail di ubah!")
    return username_baru 


def ubah_password(username):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================Ubah Password================")
    password_lama = input("Masukkan password lama: ")

    #cek apakah password lama benar
    akun = data_akun[
        (data_akun["username"] == username) &
        (data_akun["password"] == password_lama)
    ]

    if akun.empty:
        print("Password lama salah: ")
        input("tekan enter untuk kembali...")
        return
    
    password_baru = input("masukkan password baru:" )
    while not password_baru.strip():
        print("password tidak boleh kosong!")
        password_baru = input("masukkan password baru: ")

    data_akun.loc[data_akun["username"] == username, "password"] = password_baru
    data_akun.to_csv("users.csv", index=False)

    print("password berhasil diubah!")



def kelola_akun(username):
    while True:
        os.system('cls')
        print("============== KELOLA AKUN ==============")
        print(f"Akun login: {username}")
        print("1. Ubah Username")
        print("2. Ubah Password")
        print("3. Kembali/Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            username = ubah_username(username)   # update username lokal

        elif pilih == "2":
            ubah_password(username)

        elif pilih == "3":
            print("Kembali ke menu sebelumnya...")
            return

        else:
            print("Pilihan tidak valid!")


def kelola_produk():
    os.system('cls')
    print("1. Tambah")
    print("2. Edit")
    print("3. Hapus")
    print("4. Lihat Produk")
    print("5. Kembali")
    sub = input("Pilih: ")

    if sub == "1": 
        os.system('cls')
        tambah_produk(PRODUCT_FILE)
    elif sub == "2":
        os.system('cls') 
        edit_produk(PRODUCT_FILE)
    elif sub == "3":
        os.system('cls') 
        hapus_produk(PRODUCT_FILE)
    elif sub == "4": 
        os.system('cls')
        lihat_produk(PRODUCT_FILE)
    elif sub == "5":
        os.system('cls')
        search_produk(PRODUCT_FILE)
    elif sub == "6":
        os.system('cls')
        menu_admin()



def search_admin():
    os.system('cls')

    print("======FITUR SEARCH ADMIN======")
    print("Login sebagai {username}")
    print("1. Cari Produk")
    print("2. Kembali")
    
    pilih = input("pilih: ")

    #cari produk(nama) seperti pupuk, dll
    if pilih == "1":
        data = pd.read_csv("products.csv")
        keyword = input("Masukkan nama produk: ").lower()
        hasil = data[data["nama"].str.lower().str.contains(keyword)]
        #admin mengetik nama produk
        #.str.constain() = mencari produk dengan mengandung keyword
        #contoh "pupuk" jadi cocok dengan "pupuk a", "pupuk b", "pupuk c"
        #mengubah huruf jadi huruf kecil

    elif pilih == "2":
        return
        #keluar dari fungsi dan kembali ke menu admin.

    else:
        print("Pilihan tidak valid!")
        input("Klik enter")
        return
        #Jika admin mengetik selain angka 1–5 maka muncul peringatan.
    
    #tampilkan hasil
    if hasil.empty:
        print("Data tidak ditemukan!")
    else:
        print(tabulate.tabulate(hasil, headers="keys", tablefmt="Fancy_grid"))
        #Jika tabel kosong maka tampil "Data tidak ditemukan"
        #Jika ada hasil maka tampil tabel rapi menggunakan tabulate
    
    input("Klik untuk melanjutkan")

def search_produk_pembeli(username):
    os.system ('cls')
    data = pd.read_csv("products.csv")

    print("====== CARI PRODUK ======")
    print(" loogin sebagai {username}")
    print("1. Cari berdasarkan nama produk")
    print("2. Kembali")
    pilih = input("piliih: ")

    if pilih == "1":
        keyword = input("Masukkan nama produk: ").lower()
        hasil = data[data["nama"].str.lower().str.contains(keyword)]
        # keyword = ... lowes() dibuat huruf kecil agarpncarian tidak case sensitive
        #.str.cotains(keyword) untuk mencari teks mengandung keyword
       #contohnya cari pupuk, cocok dengan pupuk a, pupuk b
        #data["nama"].str.lower() nama produk dibuathufuf kecil
    
    elif pilih == "2":
        return
    #mengembalikan user ke menu pembeli
    
    else:
        print("Pilihan tidak valid! silahkan pilih 1-4")
        input("klik enter")
        return
    
    if hasil.empty: # cek apakah dataframe kosong
        print("Produk tidak ditemukan!")
    else:
        print(tabulate.tabulate(hasil, headers="keys", tablefmt="fancy_grid"))

    input("tekan enter untuk kembali")
    #agar hasil tidak hilang kembali ke menu


def beli_produk(username):
    os.system('cls')
    
    keranjang = [] #list untuk menampung banyak barang

    while True:
        os.system('cls')
        data = pd.read_csv(PRODUCT_FILE)

        print("==== BELI PRODUK ====")
        print(F"Login sebagai : {username}")
        print(tabulate.tabulate(data, headers="keys", tablefmt="fancy_grid"))

        try:
            indeks = int(input("\nMasukkan Indeks produk yang ingin dibeli"))
        except ValueError:
            print("Input harus angka!")
            input("Klik enter")
            continue

        if indeks < 0 or indeks >= len(data):
            print("indeks tidak valid!")
            input("Klik enter")
            continue

        produk = data.loc[indeks]

        #detail produk
        print("==== DETAIL PRODUK ====")
        print(f"Nama    : {produk['nama']}")
        print(f"Stok    : {produk['stok']}")
        print(f"Harga   : {produk['harga']}")

        try:
            jumlah = int(input("Masukkan jumlah pembelian: "))
        except ValueError:
            print("Jumlah harus angka")
            input("klik enter")
            continue

        if jumlah> produk['stok']:
            print("Stok tidak cukup!")
            input("Klik enter")
            continue

        subtotal = jumlah * produk['harga']

        #masukkan ke keranjang
        keranjang.append({
            "index": indeks,
            "nama": produk["nama"],
            "jumlah": jumlah,
            "harga": produk["harga"],
            "subtotal": subtotal
        })

        print(f"\n {produk['nama']} x {jumlah} ditambahkan ke keranjang!")

        lanjut = input("Mau beli produk lain? (y/n): ").lower()
        if lanjut != "y":
            break

        #jika keranjang kosong 
        if not keranjang:
            print("Keranjang kosong, tidak ada pembelian")
            input("enter")
            return
        #tampilkan isi keranjang
        os.system('cls')
    print("==== ISI KERANJANG ====")
    for item in keranjang:
        print(f" - {item['nama']} x {item['jumlah']} = Rp{item['subtotal']}")

    total_bayar = sum(item['subtotal'] for item in keranjang)
    print(f"TOTAL BAYAR = RP{total_bayar}")

    konfirmasi = input("Lanjutkan pembayaran? (y/n): ").lower()
    if konfirmasi != "y":
        print("Pembelian dibatalkan")
        input("Enter")
        return
    
    #Proses kurangi stok
    for item in keranjang:
        data.loc[item["index"], "stok"] -= item["jumlah"]

    data.to_csv(PRODUCT_FILE, index=False)

    #catat transaksi
    from datetime import datetime
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open (SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for item in keranjang:
            writer.writerow([tanggal, username, item["nama"], item["jumlah"]])

    #output berhasl
    print("\n=== TRANSAKSI BERHASIL ===")
    print(f"Tanggal : {tanggal}")
    print(f"Total   : Rp{total_bayar}")
    print(f"Detail pembelian:")
    for item in keranjang:
        print(f"- {item['nama']} x {item['jumlah']}")
    input("klik enter untuk kembali ke menu")



def menu_admin(username):
    os.system('cls')
    while True:
        print("=== MENU ADMIN ===")
        print("1. Kelola Produk")
        print("2. Laporan Penjualan")
        print("3. Kelola Akun")
        print("4. Search")
        print("0. Logout")
        pillihan = input("Pilih: ")

        if pillihan == "1":
            kelola_produk()
        elif pillihan == "2": 
            os.system('cls')
            laporan_penjualan ()
        elif pillihan == "3": 
            username = kelola_akun(username)
        elif pillihan == "4":
            search_admin()
        elif pillihan == "0":
            os.system('cls')
            break


def menu_pembeli(username):
    os.system('cls')
    while True:
        print(f"username saat ini: {username}")
        print("=== MENU PEMBELI ===")
        print("1. Pembelian Produk")
        print("2. Laporan Pembelian")
        print("3. Kelola Akun ")
        print("4. Cari Produk")
        print("0. Logout")
        pil = input("Pilih: ")

        if pil == "1":
            beli_produk(username)
        elif pil == "2":
            laporan_pembeli(username)
        elif pil == "3":
            username = kelola_akun(username)
        elif pil =="4":
            search_produk_pembeli(username)
        elif pil == "0":
            break


def menu():
    os.system('cls')    
    while True: # menu akan terus mucul sampai user memilih keluar
        print("========================================================")
        print("===============selamat datang di Agrocare===============")
        print("========================================================")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        print("========================================================")

        pilihan = input("pilih menu (1/2/3):")

        if pilihan == "1":
            hasil = login()
            if hasil:
                username, role = hasil
                if role == "admin":
                    menu_admin(username)
                else:
                    menu_pembeli(username)
                    
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terimakasih telah menggunakan Agrocare. Sampai jumpa!")
            break #keluar dari while true / menghentikan program
        else:
            print("\n Pilihan tidak valid! Silahkan masukkan angka 1-3.\n")

menu()


     