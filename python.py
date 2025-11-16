import pandas as pd
import os

username = input("Buat Username: ")
while not username or username .isspace():
    print("Input tidak boleh kosong")
    username = input("Buat Username: ")

password = input("Buat Pasword: ")
while not password or password .isspace():
    print("Input tidak boleh kosong")
    password
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

