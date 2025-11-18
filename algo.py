import pandas as pd
import os

def login():

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
        return() 

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
        return() #jika pw salah mka kembali ke menu

    # jika usn dan pw benar cek role maka login berhasil
    role = password_benar.iloc[0]["role"]

    # Tampilan selamat datang sesuai role
    if role == "admin":
        print(f"\n Login berhasil! Selamat datang ADMIN,", username)
    else:
        print(f"\n Login berhasil! Selamat datang di Agrocare,", username)
        


def menu():
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
                login()
            elif pilihan == "2":
                register()
            elif pilihan == "3":
                print("Terimakasih telah menggunakan Agrocare. Sampai jumpa!")
                break #keluar dari while true / menghentikan program
            else:
                print("\n Pilihan tidak valid! Silahkan masukkan angka 1-3.\n")

menu()
