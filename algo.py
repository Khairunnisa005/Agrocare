import pandas as pd
import os

# Baca CSV
data_akun = pd.read_csv("users.csv")

print("============= LOGIN =============")

username = input("Masukkan Username : ")
password = input("Masukkan Password : ")

# Cek kecocokan username & password
akun = data_akun[
    (data_akun["username"] == username) &
    (data_akun["password"] == password)
]

if akun.empty:
    print("\n Login gagal! Username atau password salah silahkan coba lagi.")
else:
    role = akun.iloc[0]["role"]

    # Tampilan selamat datang
    if role == "admin":
        print("\n Login berhasil! Selamat datang ADMIN,", username)
    else:
        print("\n Login berhasil! Selamat datang PEMBELI,", username)
