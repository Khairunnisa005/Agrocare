import pandas as pd
import os
import csv

# =========================
#  FILE DATABASE
# =========================
USER_FILE = "users.csv"
PRODUCT_FILE = "products.csv"
SALES_FILE = "sales.csv"

# =========================
#  REGISTRASI
# =========================
def register():
    os.system('cls')
    username = input("Buat Username: ")
    #while ini untuk memeastikan supaya input tidak kososng 
    #program tidak lanjut ke password jika tidak mengisi user name 
    while not username or username .isspace():
        print("Input tidak boleh kosong")
        username = input("Buat Username: ")

    password = input("Buat Pasword: ")
    while not password or password .isspace(): #.isspace ini untuk memastikan bahwa inputan tidak hanya berisi sepasi
        print("Input tidak boleh kosong")
        password= input("Buat Pasword: ")

    data_akun = pd.read_csv('users.csv')

    role = "pembeli"

    # Cek apakah username + password sudah ada
    akun_sama = ((data_akun['username'] == username)).any()
    #aku hapus yang paswwor nyaa aja kalok paswword sama ndak papa yang penting username nya aja beda
    if akun_sama:
        print("username sudah pernah terdaftar")
        input("Klik Enter untuk melanjutkan...")
    else:
        # Buat row baru
        row_baru = pd.DataFrame({
            'username': [username],
            'password': [password],
            'role': [role]
        })

        # Gabungkan data lama + data baru
        data_akun = pd.concat([data_akun, row_baru], ignore_index=True)

        # Simpan kembali ke CSV
        data_akun.to_csv('users.csv', index=False)
        print("Akun berhasil dibuat")
        input("Klik Enter untuk melanjutkan...")

# =========================
#  LOGIN
# =========================
def login():
    os.system('cls')   
# Baca CSV
    data_akun = pd.read_csv("users.csv")

    print("========================================================")
    print("============== SELAMAT DATANG DI AGROCARE ==============")
    print("====================== LOGIN ===========================")

    username = input("Masukkan Username : ")

    #cek username
    akun = data_akun[data_akun["username"] == username]

    if akun.empty:
        print("\n Username tidak terdaftar. Silahkan daftarr/register telebih dahulu.")
        input("Klik Enter untuk melanjutkan...") 
        return None, None #jika usn salah mka kembali ke menu

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
        input("Klik Enter untuk melanjutkan...")
        return None, None #jika pw salah mka kembali ke menu

    # jika usn dan pw benar cek role maka login berhasil
    role = password_benar.iloc[0]["role"]

    # Tampilan selamat datang sesuai role
    if role == "admin":
        print(f"\nLogin berhasil! Selamat datang ADMIN,", username)
        input("Klik Enter untuk melanjutkan...")
        menu_admin(username)
    else:
        print(f"\nLogin berhasil! Selamat datang di Agrocare,", username)
        input("Klik Enter untuk melanjutkan...")
        menu_pembeli(username)

# =========================
#  MENU ADMIN
# =========================
tambah_produk = ""
edit_produk = ""
hapus_produk = ""
lihat_produk = ""
beli_produk = ""
laporan_pembeli = ""
laporan_admin = ""

def menu_admin(username):
    os.system('cls')
    while True:
        print("=== MENU ADMIN ===")
        print("1. Kelola Produk")
        print("2. Laporan Penjualan")
        print("3. Kelola Akun")
        print("0. Logout")
        pil = input("Pilih: ")

        if pil == "1":
            print("\n1. Tambah")
            print("2. Edit")
            print("3. Hapus")
            print("4. Lihat Produk")
            sub = input("Pilih: ")

            if sub == "1": tambah_produk()
            elif sub == "2": edit_produk()
            elif sub == "3": hapus_produk()
            elif sub == "4": lihat_produk()
        elif pil == "2":
            laporan_admin()
        elif pil == "3":
            username = kelola_akun(username)
        elif pil == "0":
            break

def kelola_akun(username):
    while True:
        os.system('cls')
        print("====== KELOLA AKUN ======")
        print(f"Username saat ini: {username}")
        print("1. Ubah Username")
        print("2. Ubah Password")
        print("3. Kembali ke menu sebelumnya")

        pilih = input(" Pilih menu: ")

        if pilih == "1":
            username = ubah_username(username)
        elif pilih == "2":
            ubah_password(username)
        elif pilih == "3":
            print("Kembali ke menu sebelumnya")
            return username
        else:
            print("Pilihan tidak valid! silahkan tekan menu 1-3")
        
def ubah_username(username_lama):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print(f"Username saat ini: {username_lama}")
    print("================UBAH USERNAME================")
    username_baru = input("Masukkan username baru: ").strip()

    #jika user tdk mengetik apa apa maka batal ubah usn, tetap usn lama
    if not username_baru:
        return username_lama

    #cek apakah username baru sudah digunakan orang lain
    if username_baru in data_akun["username"]. values:
        print("username sudah sudah terdaftar!")
        return username_lama
        #jika usn sudah digunakan maka batal,tetap usn lama

    #update username
    data_akun.loc[data_akun["username"] == username_lama, "username"] = username_baru
    data_akun.to_csv("users.csv", index=False)

    #tampilkan pesan sukses
    print("Username berhail di ubah!")
    return username_baru
    #agar menu utama langsun memakai usn baru

def ubah_password(username):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print(f"username saat ini: {username}")
    print("================UBAH PASSWORD================")
    password_lama = input("Masukkan password lama: ")

    #cek apakah password lama benar, mencaribaris di csv yg usn dan pw cocok, kalo tdk ada maka salah
    akun = data_akun[
        (data_akun["username"] == username) &
        (data_akun["password"] == password_lama)
    ]

    #jika pw lama salah maka kembali ke menu kelola akun
    if akun.empty:
        print("Password lama salah ")
        input("Tekan enter untuk kembali")
        return
    
    password_baru = input("Masukkan password baru:" )
    while not password_baru.strip():
        password_baru = input("Masukkan password baru: ")

    #uodate pw di csv
    data_akun.loc[data_akun["username"] == username, "password"] = password_baru
    data_akun.to_csv("users.csv", index=False)

    print("Password berhasil diubah!")
        


# =========================
#  LAPORAN ADMIN
# =========================
def laporan_admin():
    print("\n=== LAPORAN PENJUALAN ===")
    with open(SALES_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['tanggal']} | {row['pembeli']} | {row['produk']} | {row['jumlah']} | {row['total']}")

# =========================
#  MENU PEMBELI
# =========================
def menu_pembeli(username):
    os.system('cls')
    while True:
        print(f"username saat ini: {username}")
        print("=== MENU PEMBELI ===")
        print("1. Pembelian Produk")
        print("2. Laporan Pembelian")
        print("3. Kelola Akun ")
        print("0. Logout")
        pil = input("Pilih: ")

        if pil == "1":
            beli_produk(username)
        elif pil == "2":
            laporan_pembeli(username)
        elif pil == "3":
            username = kelola_akun(username)
        elif pil == "0":
            break

# =========================
#  LAPORAN PEMBELI
# =========================
def laporan_pembeli(username):
    print("\n=== LAPORAN PEMBELIAN ANDA ===")
    with open(SALES_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["pembeli"] == username:
                print(f"{row['tanggal']} | {row['produk']} | {row['jumlah']} | {row['total']}")


def menu():
    os.system('cls')
    while True: # menu akan terus mucul sampai user memilih keluar
        print("========================================================")
        print("=============== Selamat datang di Agrocare =============")
        print("========================================================")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        print("========================================================")

        pilihan = input("pilih menu (1/2/3):")

        if pilihan == "1":
            user = login()
            if user:
                if user["role"] == "admin":
                    menu_admin(usernname)
                else:
                    menu_pembeli(user["username"])
            
        elif pilihan == "2":
            register()

        elif pilihan == "3":
            print("Terimakasih telah menggunakan Agrocare. Sampai jumpa!")
            break #keluar dari while true / menghentikan program
        else:
            print("\n Pilihan tidak valid! Silahkan masukkan angka 1-3.\n")

menu()

