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
        exit() #untuk stop program jika usn belum terdaftar

    #kalo usn benar minta passwod
    password = input("Masukkan Password : ")

#cek pw
    password_benar = data_akun[
        (data_akun["username"] == username) & 
        (data_akun["password"] == password)
    ]

    if password_benar.empty: 
        print("\n Password salah! Silahkan coba lagi.")
        exit()#untuk stop program jika paw salah

    # jika usn dan pw benar maka login berhasil
    role = password_benar.iloc[0]["role"]

            # Tampilan selamat datang
    if role == "admin dan pembeli":
        print("\n Login berhasil! Selamat datang ADMIN,", username)
    else:
        print("\n Login berhasil! Selamat datang di Agrocare,", username)
        
login()
        
