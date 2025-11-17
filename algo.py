import csv


def login_admin():
    print("====================================")
    print("              LOGIN ADMIN")
    print("====================================")

    username_input = input("Masukkan Username : ")
    password_input = input("Masukkan Password : ")

    try:
        file = open("admin.csv", "r")
        data = file.readline().split(",")   # admin hanya 1 baris
        file.close()
    except:
        print("File admin.csv tidak ditemukan!")
        return False

    username_admin = data[0]
    password_admin = data[1].strip()

    if username_input == username_admin and password_input == password_admin:
        print("\nLogin Admin Berhasil! Selamat datang Admin.")
        return True
    else:
        print("\nLogin Gagal! Username atau Password salah.")
        return False



def login_pembeli():
    print("====================================")
    print("             LOGIN PEMBELI")
    print("====================================")

    username_input = input("Masukkan Username : ")
    password_input = input("Masukkan Password : ")

    try:
        file = open("pembeli.csv", "r")
        data_pembeli = file.readlines()
        file.close()
    except:
        print("File pembeli.csv tidak ditemukan!")
        return False

    login_sukses = False

    for baris in data_pembeli:
        user, pw = baris.split(",")
        pw = pw.strip()

        if username_input == user and password_input == pw:
            login_sukses = True

    if login_sukses:
        print("\nLogin berhasil! Selamat datang di AgroCare.")
        return True
    else:
        print("\nLogin gagal! Username atau password salah.")
        return False


while True:
    print("\n====================================")
    print("               MENU UTAMA")
    print("====================================")
    print("1. Login Admin")
    print("2. Login Pembeli")
    print("3. Keluar")
    print("====================================")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        login_admin()

    elif pilihan == "2":
        login_pembeli()

    elif pilihan == "3":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")




