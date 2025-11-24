import pandas as pd
from datetime import timedelta
import os
import csv
import tabulate

# =========================
#  FILE DATABASE
# =========================
USER_FILE = "users.csv"
PRODUCT_FILE = "products.csv"
SALES_FILE = "sales.csv"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCT_FILE = os.path.join(BASE_DIR, "products.csv")

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
        return None #jika usn salah mka kembali ke menu

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
        return None #jika pw salah mka kembali ke menu

    # jika usn dan pw benar cek role maka login berhasil
    role = password_benar.iloc[0]["role"]
    
    #Tampilan selamat data sesuai role
    if role == "admin":
        print(f"\n Login berhasil Selamat datang ADMIN," , username)
        menu_admin(username)
    else:
        print(f"\n Login berhasil! Selamat datang di AgroCare,", username)
        menu_pembeli(username)


# =========================
#  LOGOUT
# =========================
def logout():
    os.system('cls')
    input ("Anda telah logout. Sampai jumpa!")
    os.system('cls')
    exit()

# =========================
#  PENGELOLAAN AKUN
# =========================
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
            return
        else:
            print("Pilihan tidak valid! silahkan tekan menu 1-3")
        
def ubah_username(username_lama):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================UBAH USERNAME================")
    print(f"Username saat ini: {username_lama}")
    username_baru = input("Masukkan username baru: ")

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
    #agar menu utama langsung memakai usn baru

def ubah_password(username):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================UBAH PASSWORD================")
    print(f"username saat ini: {username}")
    password_lama = input("Masukkan password lama: ")

    #cek apakah password lama benar, mencari baris di csv yg usn dan pw cocok, kalo tdk ada maka salah
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

    #update pw di csv
    data_akun.loc[data_akun["username"] == username, "password"] = password_baru
    data_akun.to_csv("users.csv", index=False)

    print("Password berhasil diubah!")

# =========================
#  MENU ADMIN
# =========================
def menu_admin(username): #fungsi menu admin, tampil saat masuk sebagai admin
    os.system('cls')
    if not username:
        print("Error: username kosong. Kembali ke menu utama.")
        return
    while True: #kemudian menampilkan perulangan menu yang dimiliki admin
        print("\n=== MENU ADMIN ===")
        print("1. Kelola Produk")
        print("2. Laporan Penjualan")
        print("3. Kelola Akun")
        print("0. Logout")
        pillihan = input("Pilih: ")

        if pillihan == "1": #pilihan yang akan mengantarkan pengguna ke menu kelola produk
            menu_kelola_produk()
        elif pillihan == "2": #pilihan yang akan mengantarkan pengguna ke laporan penjualan
            os.system('cls')
            laporan_admin()
        elif pillihan == "3": #pilihan yang akan mengantarkan pengguna ke menu kelola akun
            username = kelola_akun(username)
        elif pillihan == "0": #pilihan untuk keluar dari akun
            os.system('cls')
            break

# =========================
#  PENGELOLAAN PRODUK
# =========================
def ensure_product_file():
    if not os.path.exists(PRODUCT_FILE):
        df = pd.DataFrame(columns=["nama", "stok", "harga", "unit"])
        df.to_csv(PRODUCT_FILE, index=False)

def load_products() -> pd.DataFrame:
    # Baca produk dari CSV jadi DataFrame. Jika corrupt, bikin pesan dan kembalikan empty DF.
    ensure_product_file()
    try:
        df = pd.read_csv(PRODUCT_FILE)
        # pastikan kolom penting ada
        for col in ["nama", "stok", "harga", "unit"]:
            if col not in df.columns:
                df[col] = "" if col == "unit" else 0
        # normalisasi tipe
        df["nama"] = df["nama"].astype(str)
        # stok & harga jadi numeric (non-numeric -> 0)
        df["stok"] = pd.to_numeric(df["stok"], errors="coerce").fillna(0).astype(float)
        df["harga"] = pd.to_numeric(df["harga"], errors="coerce").fillna(0).astype(float)
        df["unit"] = df["unit"].fillna("").astype(str)
        return df
    except Exception as e:
        print("Gagal membaca file produk:", str(e))
        return pd.DataFrame(columns=["nama","stok","harga","unit"])

def save_products(df: pd.DataFrame):
    # Simpan DataFrame produk ke CSV. Tangani exception.
    try:
        df.to_csv(PRODUCT_FILE, index=False)
    except Exception as e:
        print("Gagal menyimpan data produk:", str(e))

def print_products(df: pd.DataFrame):
    # Cetak tabel produk dengan index mulai 1.    
    if df.empty:
        print("Belum ada produk.")
        return
    display_df = df.copy()
    display_df.index = range(1, len(display_df) + 1)  # user-friendly index
    print(tabulate.tabulate(display_df, headers='keys', tablefmt='fancy_grid'))

def tambah_produk():
    # Tambah produk baru dengan validasi. Menyimpan langsung ke CSV.
    df = load_products()
    print("\n=== TAMBAH PRODUK ===")
    print_products(df)
    nama = input("Masukkan nama produk: ").strip().capitalize()
    if not nama:
        print("Nama produk tidak boleh kosong. Batal menambah.")
        return

    # cek duplikat nama (case-insensitive)
    if (df["nama"].str.lower() == nama.lower()).any():
        print("Nama produk sudah terdaftar. Gunakan nama lain atau edit produk yang ada.")
        return

    # stok harus >= 0 dan bulat/float valid
    try:
        stok_in = input("Masukkan stok produk (angka, boleh desimal): ").strip()
        stok = float(stok_in)
        if stok < 0:
            print("Stok tidak boleh negatif. Batal.")
            return
    except ValueError:
        print("Stok harus berupa angka. Batal.")
        return

    # harga harus >=0
    try:
        harga_in = input("Masukkan harga per satuan (angka): ").strip()
        harga = float(harga_in)
        if harga < 0:
            print("Harga tidak boleh negatif. Batal.")
            return
    except ValueError:
        print("Harga harus berupa angka. Batal.")
        return

    unit = input("Satuan produk (contoh: kg, pcs) — boleh kosong: ").strip()

    row = {"nama": nama, "stok": stok, "harga": harga, "unit": unit}
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    save_products(df)
    print(f"Produk '{nama}' berhasil ditambahkan.")

def edit_produk():
    # Edit produk berdasarkan index (user-friendly 1..n) atau cari nama. Menyimpan perubahan ke CSV.
    df = load_products()
    if df.empty:
        print("Belum ada produk untuk diedit.")
        return

    print("\n=== EDIT PRODUK ===")
    print_products(df)
    choice = input("Pilih index produk untuk diedit atau ketik nama produk: ").strip()
    if not choice:
        print("Pilihan kosong. Batal.")
        return

    # tentukan index internal
    idx = None
    if choice.isdigit():
        idx_user = int(choice)
        if 1 <= idx_user <= len(df):
            idx = idx_user - 1
        else:
            print("Index di luar jangkauan.")
            return
    else:
        # cari nama (case-insensitive)
        matches = df[df["nama"].str.lower() == choice.lower()]
        if matches.empty:
            print("Nama produk tidak ditemukan.")
            return
        if len(matches) > 1:
            print("Lebih dari satu produk cocok dengan nama itu. Gunakan index.")
            print_products(matches)
            return
        idx = matches.index[0]

    # tampilkan data lama
    old = df.loc[idx]
    print(f"Produk yang dipilih: {old['nama']} | Stok: {old['stok']} {old['unit']} | Harga: {old['harga']}")
    print("Kosongkan input untuk mempertahankan nilai lama.")

    # input baru
    new_name = input(f"Nama baru [{old['nama']}]: ").strip()
    if new_name == "":
        new_name = old['nama']
    else:
        new_name = new_name.capitalize()
        # cek duplikat nama (kecuali sendiri)
        if (df["nama"].str.lower() == new_name.lower()).any() and new_name.lower() != old['nama'].lower():
            print("Nama baru sudah dipakai produk lain. Batal.")
            return

    stok_input = input(f"Stok baru [{old['stok']}]: ").strip()
    if stok_input == "":
        new_stok = float(old['stok'])
    else:
        try:
            new_stok = float(stok_input)
            if new_stok < 0:
                print("Stok tidak boleh negatif. Batal.")
                return
        except ValueError:
            print("Stok harus angka. Batal.")
            return

    harga_input = input(f"Harga baru [{old['harga']}]: ").strip()
    if harga_input == "":
        new_harga = float(old['harga'])
    else:
        try:
            new_harga = float(harga_input)
            if new_harga < 0:
                print("Harga tidak boleh negatif. Batal.")
                return
        except ValueError:
            print("Harga harus angka. Batal.")
            return

    new_unit = input(f"Satuan baru [{old.get('unit','')}]: ").strip()
    if new_unit == "":
        new_unit = old.get('unit', '')

    # apply
    df.at[idx, "nama"] = new_name
    df.at[idx, "stok"] = new_stok
    df.at[idx, "harga"] = new_harga
    df.at[idx, "unit"] = new_unit
    save_products(df)
    print("Produk berhasil diperbarui.")

def hapus_produk():
    # Hapus produk berdasarkan index. Ada konfirmasi.
    df = load_products()
    if df.empty:
        print("Belum ada produk untuk dihapus.")
        return

    print("\n=== HAPUS PRODUK ===")
    print_products(df)
    choice = input("Masukkan index produk yang ingin dihapus: ").strip()
    if not choice or not choice.isdigit():
        print("Input tidak valid. Harus berupa angka index.")
        return
    idx_user = int(choice)
    if not (1 <= idx_user <= len(df)):
        print("Index di luar jangkauan.")
        return
    idx = idx_user - 1
    nama = df.at[idx, "nama"]
    confirm = input(f"Yakin ingin menghapus '{nama}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Hapus dibatalkan.")
        return

    df = df.drop(index=idx).reset_index(drop=True)
    save_products(df)
    print(f"Produk '{nama}' berhasil dihapus.")

def lihat_produk():
    # Tampilkan daftar produk tanpa memodifikasi apa pun.
    df = load_products()
    print("\n=== DAFTAR PRODUK ===")
    print_products(df)

    try:
        data = pd.read_csv("products.csv")
    except:
        print("File products.csv tidak ditemukan!")
        input("\nKlik Enter untuk kembali...")
        return

    # Jika produk kosong
    if data.empty:
        print("Belum ada produk yang tersedia.")
        input("\nKlik Enter untuk kembali...")
        return

    # Tampilkan semua produk
    print("\n--- List Produk ---")
    print(data[["nama", "harga", "stok"]])

    print("\n===========================================")
    cari = input("Masukkan nama produk yang ingin dicari : ").strip().lower()

    # Cari produk berdasarkan nama (case-insensitive)
    hasil = data[data["nama"].str.lower() == cari]

    if hasil.empty:
        print("\n Hmm.. sepertinya produk itu belum tersedia ")
    else:
        print("\n Oke, Produknya ada. Ini detail lengkapnya:")
        print(f"Nama  : {hasil.iloc[0]['nama']}")
        print(f"Harga : {hasil.iloc[0]['harga']}")
        print(f"Stok  : {hasil.iloc[0]['stok']}")

    input("\nKlik Enter untuk kembali...")

#pembelian
def beli_produk(username):
    os.system('cls')
    
    keranjang = [] #list untuk menampung banyak barang

    while True: #loop utama menambahkan item, akan terus berulang sampai pembeli
        #menjawab tidak pada petanyaan "mau beli produk lain?"
        os.system('cls')
        data = pd.read_csv(PRODUCT_FILE)

        print("==== BELI PRODUK ====")
        print(F"Login sebagai : {username}")
        print(tabulate.tabulate(data, headers="keys", tablefmt="fancy_grid"))
        #menampilkan tabel rapi pakai tabulate agara pembeli tau indeks, nama, dtok dan harga

        try: # jika bukan angka maka akan error dan tampil pesan  
            indeks = int(input("\nMasukkan Indeks produk yang ingin dibeli"))
        except ValueError:
            print("Input harus angka!")
            input("Klik enter")
            continue #continue (ulang dari awal loop)

        #indeks < 0 artinya penggunaa memasukkan angka negatif maka tidak mungkin menjadi baris tabel
        #inndeks >= len(data) jika jumlah prduk misal 3 maka len data 3, indeks valid nya yaitu 0,1,2
        if indeks < 0 or indeks >= len(data):
            print("indeks tidak valid!")
            input("Klik enter")
            continue

        #ambil baris produk yaitu nam, stok, harga
        produk = data.loc[indeks]

        #detail produk
        print("==== DETAIL PRODUK ====")
        print(f"Nama    : {produk['nama']}")
        print(f"Stok    : {produk['stok']}")
        print(f"Harga   : {produk['harga']}")

        try: # input harus angka jika tidak maka akan eror
            jumlah = int(input("Masukkan jumlah pembelian: "))
        except ValueError:
            print("Jumlah harus angka")
            input("klik enter")
            continue

        #cek stok cukup atau tidak, jika jumlahnya melebihi stok maka 
        #beripesan dan kembali ke pilih produk (loop continue)
        if jumlah> produk['stok']:
            print("Stok tidak cukup!")
            input("Klik enter")
            continue

        #hitunng sub total
        subtotal = jumlah * produk['harga']

        #masukkan ke keranjang
        #simpan indeks untuk (mengurangi stok) nama, jumlah dan harga perunit subtotal
        keranjang.append({
            "index": indeks,
            "nama": produk["nama"],
            "jumlah": jumlah,
            "harga": produk["harga"],
            "subtotal": subtotal
        })

        #tampilkan pesan
        print(f"\n {produk['nama']} x {jumlah} ditambahkan ke keranjang!")

        #tanya mau beli lagi
        #jika jawaban bukan 'y' maka keluar dari pengisian keranjang
        lanjut = input("Mau beli produk lain? (y/n): ").lower()
        if lanjut != "y":
            break

        #jika keranjang kosong, batalkan dan kembali ke menu
        if not keranjang:
            print("Keranjang kosong, tidak ada pembelian")
            input("enter")
            return
        
        #tampilkan isi keranjang
        os.system('cls')
    print("==== ISI KERANJANG ====")
    for item in keranjang:
        print(f" - {item['nama']} x {item['jumlah']} = Rp{item['subtotal']}")
        #menunjukkan tiap item dan subtotalnya

    #hitung total yang harus dibayar
    total_bayar = sum(item['subtotal'] for item in keranjang)
    print(f"TOTAL BAYAR = RP{total_bayar}")

    #konfirmasi pembayaran 
    #jika bukan 'y' maka batalkan transaksi (tidak mengubah stok, tidak menulis sales)
    konfirmasi = input("Lanjutkan pembayaran? (y/n): ").lower()
    if konfirmasi != "y":
        print("Pembelian dibatalkan")
        input("Enter")
        return
    
    #Proses kurangi stok
    #untuk setiap item di keranjang, stok baris dengan indeks dikurangi jumlah yang dibeli
    #stelah semua perubahan, tulis kembali seluruh dataframe data ke produk
    for item in keranjang:
        data.loc[item["index"], "stok"] -= item["jumlah"]
    data.to_csv(PRODUCT_FILE, index=False)

    #catat transaksi
    #buat timestamp sekarang 
    #buka sales csv dalam mode append untuk setiap item tulis baris baru
    #tanggal, usn, nama produk dan jumlah
    from datetime import datetime
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open (SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for item in keranjang:
            writer.writerow([tanggal, username, item["nama"], item["jumlah"]])
            #

    #output berhasl
    print("\n=== TRANSAKSI BERHASIL ===")
    print(f"Tanggal : {tanggal}")
    print(f"Total   : Rp{total_bayar}")
    print(f"Detail pembelian:")
    for item in keranjang:
        print(f"- {item['nama']} x {item['jumlah']}")
    input("klik enter untuk kembali ke menu")

# Simple menu helper untuk kelola produk (dipanggil dari menu utama)
def menu_kelola_produk():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== KELOLA PRODUK ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("0. Kembali")
        pilih = input("Pilih: ").strip()
        if pilih == "1": #jika memilih menu lihat(1) maka akan menjalankan fungsi lihat produk
            lihat_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "2": #jika memilih menu tambah(2) maka akan menjalankan fungsi tambah produk
            tambah_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "3": #jika memilih menu edit(3) maka akan menjalankan fungsi edit produk
            edit_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "4": #jika memilih menu hapus(4) maka akan menjalankan fungsi hapus produk
            hapus_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "0": #pilihan menu untuk kembali ke menu sebelumnya
            break
        else:
            print("Pilihan tidak dikenal. Coba lagi.")
            input("Tekan Enter...")

# Pastikan file siap jika modul ini dijalankan langsung
if __name__ == "__main__":
    ensure_product_file()
        

# =========================
#  MENU PEMBELI
# =========================
# beli_produk = ""

def menu_pembeli(username):
    os.system('cls')
    if not username:
        print("Error: username kosong. Kembali ke menu utama.")
        return
    while True:
        print(f"username saat ini: {username}")
        print("=== MENU PEMBELI ===")
        print("1. Pembelian Produk")
        print("2. Laporan Pembelian")
        print("3. Kelola Akun ")
        print("4. Cari Produk")
        print("0. Logout")
        pil = input("Pilih: ")

        if pil == "1":
            beli_produk(username)
        elif pil == "2":
            laporan_pembeli(username)
        elif pil == "3":
            username = kelola_akun(username)
        elif pil == "4":
            lihat_produk()
        elif pil == "0":
            break

# =========================
#  LAPORAN PEMBELI
# =========================
def laporan_pembeli(username): #fungsi laporan pembeli
    os.system('cls')
    print("\n=== LAPORAN PEMBELIAN ANDA ===")
    with open(SALES_FILE, "r", encoding="utf-8") as f: #membuka file csv dan membacanya, lalu disimpen dalam var. f
        reader = csv.DictReader(f) #membaca file csv
        for row in reader: #perulangan setiap baris dalam file csv
            if row["pembeli"] == username:
                print(f"{row['tanggal']} | {row['produk']} | {row['jumlah']} | {row['total']}") #tampilan laporan

#==============
#== Shorting ==
#==============
def laporan_admin():
    os.system('cls')
    #untuk membaca data jual beli
    penjualan = pd.read_csv('sales.csv')
    # program ini untuk merubah kolom 'tanggal' menjadi datetime
    penjualan['tanggal'] = pd.to_datetime(penjualan['tanggal'])

    # Cari nilai maksimum (tanggal terbaru) di kolom 'tanggal'
    tanggal_terakhir_data = penjualan['tanggal'].dt.normalize().max()

    # Tentukan batas akhir satu hari setelah tanggal terakhir di data.
    end_date = tanggal_terakhir_data + timedelta(days=1)

    while True:
        print("== Pilih waktu nya ==")
        print("1. Data hari ini")
        print("2. Data 1 Minggu ")
        print("3. Data 1 Bulan")
        print("4. Keluar ")
        pillihan = input("Masukkan perintah berupa angka 1/2/3/4: ")

        if pillihan == "1":
            #menentukan batas tanggal dari data yang ingin dikluarkan 
            start_date = end_date - timedelta(days=1)
            filtered = penjualan[end_date]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            laporan_admin()
        elif pillihan == "2":
            start_date = end_date - timedelta(days=7)
            filtered = penjualan[
                (penjualan['tanggal'] >= start_date) & 
                (penjualan['tanggal'] < end_date) 
            ]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            laporan_admin()
        elif pillihan == "3":
            start_date = end_date - timedelta(days=30)
            filtered = penjualan[
                (penjualan['tanggal'] >= start_date) & 
                (penjualan['tanggal'] < end_date) 
            ]
            print(tabulate.tabulate(filtered, headers='keys', tablefmt='fancy_grid'))
            input("klik enter untuk lanjut.......")
            laporan_admin()
        elif pillihan =="4":
            input("klik enter untuk lanjut.......")
            menu_admin(["username"])
        else :
            print("input ayang anda masukkan salah")

# =========================
#  MENU UTAMA
# =========================
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






# error handling ketika username salah
# menu pembelian error
# 'laporan pembelian anda\n'
# laporan penjualan rapiin tabelnya
# error handling untuk salah pilih menu di kelola akun