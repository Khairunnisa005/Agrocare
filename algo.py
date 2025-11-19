import pandas as pd
import os

def login():

    #Baca CSV
    os.system('cls')
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

def menu_admin(username):
    while True:
        os.system('cls')
        print("==============MENU ADMIN==============")
        print(f"login sebagai admin: {username}")
        print("1. kelola akun")
        print("2. logout")

        pilih = input("pilihan menu:")

        if pilih == "1":
            kelola_akun(username)
        elif pilih == "2":
            print("logout berhasil")
            return
        else:
            print("pilihan tidak valid")
            input("tekan enter ..")
        



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
