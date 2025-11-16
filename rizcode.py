
import pandas as pd
import os

username = input("Buat Username: ")
password = input("Buat Pasword: ")

data_akun = pd.read_csv('users.csv')

role = "pembeli"

# Cek apakah username + password sudah ada
akun_sama = ((data_akun['username'] == username) & 
            (data_akun['password'] == password)).any()

if akun_sama:
    print("Akun sudah pernah dibuat !!!")
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
