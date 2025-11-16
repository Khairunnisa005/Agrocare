import pandas as pd
import os

username = input("Buat Username: ")
password = input("Buat Pasword: ")


data_akun = pd.read_csv('Agrocare/users.csv')

role = "pembeli"
while True :
    if (data_akun['username'] == username,data_akun['password'] == password).any():
        print("akun sudah pernah di buat !!!")
        #register()
    else :
        menambahkan_datauser = pd.DataFrame({'username': [username], 'password': [password], 'role': [role]})
        data_user = data_user._append(menambahkan_datauser)
        data_user.to_csv('users.csv', index=False)
        print("akun berhasil di buat")
        #menu_loginmm
