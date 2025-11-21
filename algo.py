import pandas as pd
import os
import csv
import tabulate

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




def menu_pembeli(username):
    while True:
        os.system('cls')
        print("==============MENU PEMBELI==============")
        print(f"login sebagai pembeli: {username}")
        print("1. kelola akun")
        print("2 logout")

        pilih = input("pilih menu: ")

        if pilih  == "1":
            kelola_akun(username)
        elif pilih == "2":
            print("logout berhasil.")
            return
        else:
            print("pilihan tidak valid")
            input("tekan enter ..")


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
    print("1. Cari Pengguna")
    print("2. Cari Produk")
    print("3. Cari Stok")
    print("4. Cari harga")
    pilih = input("pilih: ")

    #cari pengguna
    if pilih == "1":
        data = pd.read_csv("users.csv")
        keyword = input("Masukkan username: ").lower()
        hasil = data[data["username"].str.lower().str.contains(keyword)]
        #admin mengetik nama pengguna
        #.str.constain() = mencari usn dengan mengandung keyword
        #contoh "an" jadi cocok dengan "andika", "hana", "angga"
        #mengubah huruf jadi huruf kecil

    #cari produk(nama) seperti pupuk, dll
    elif pilih == "2":
        data = pd.read_csv("products.csv")
        keyword = input("Masukkan nama produk: ").lower()
        hasil = data[data["nama"].str.lower().str.contains(keyword)]

    #cari stok
    elif pilih == "3":
        data = pd.read_csv("products.csv")
        batas = float(input("tampilkan produk dengan stok <= "))
        hasil = data[data["stok"] <= batas]
        #Admin memasukkan batas stok misal 5
        #Program menampilkan produk dengan stok kurang dari atau sama dengan 5
        #cek produk hampir habis dan memantau stok barang


    #cari harga
    elif pilih == "4":
        data = pd.read_csv("products.csv")
        batas = float(input("Tampilkan produk dengan harga <= "))
        hasil = data[data["harga"] <= batas]
        #admin memasukkan batas harga contoh 10.000
        #Program menampilkan produk lebih murah atau sama dengan harga tersebut
        #Harga ≤ 10000  untuk menampilkan semua produk yang lebih murah


    elif pilih == "5":
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
    print("2. cari berdasarkan harga mininmum")
    print("3. kembali ke menu sebelumnya")
    print("4. Kembali")
    pilih = input("piliih: ")

    if pilih == "1":
        keyword = input("Masukkan nama produk: ").lower()
        hasil = data[data["nama"].str.lower().str.constains(keyword)]
        # keyword = ... lowes() dibuat huruf kecil agarpncarian tidak case sensitive
        #.str.cotains(keyword) untuk mencari teks mengandung keyword
       #contohnya cari pupuk, cocok dengan pupuk a, pupuk b
        #data["nama"].str.lower() nama produk dibuathufuf kecil
    elif pilih == "2":
        batas = float(input("Masukkan harga maksimun: "))
        hasil = data[data["harga"] <= batas]
         #batas = angka input dari user
         #datam["harga"] <= batas untuk menaplikan produk dengan harga lebih murah atau sama dengan batas
         #contoh jika batas = 10.000
         #maka hasilnya produk harga 5.000, 8.000
    elif pilih == "3":
        batas = float(input("Masukkan harga minimum:"))
        hasil = data[data["harga"] >= batas]
    
    elif pilih == "4":
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
        elif pilhan == "4":
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


     