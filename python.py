import pandas as pd
import os

def register():

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

register()

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
        
