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
    while not username or username .isspace():
        print("Input tidak boleh kosong")
        username = input("Buat Username: ")

    password = input("Buat Pasword: ")
    while not password or password .isspace(): 
        print("Input tidak boleh kosong")
        password= input("Buat Pasword: ")

    data_akun = pd.read_csv('users.csv')

    role = "pembeli"

    akun_sama = ((data_akun['username'] == username)).any()
    if akun_sama:
        print("username sudah pernah terdaftar")
        input("Klik Enter untuk melanjutkan...")
    else:
        row_baru = pd.DataFrame({
            'username': [username],
            'password': [password],
            'role': [role]
        })

        data_akun = pd.concat([data_akun, row_baru], ignore_index=True)

        data_akun.to_csv('users.csv', index=False)
        print("Akun berhasil dibuat")
        input("Klik Enter untuk melanjutkan...")

# =========================
#  LOGIN
# =========================
def login():
    os.system('cls')   
    data_akun = pd.read_csv("users.csv")

    print("========================================================")
    print("============== SELAMAT DATANG DI AGROCARE ==============")
    print("====================== LOGIN ===========================")

    username = input("Masukkan Username : ")

    akun = data_akun[data_akun["username"] == username]

    if akun.empty:
        print("\nUsername tidak terdaftar. Silahkan daftarr/register telebih dahulu.")
        input("Klik Enter untuk melanjutkan...") 
        menu()
        return 

    password = input("Masukkan Password : ")

    password_benar = data_akun[
        (data_akun["username"] == username) & 
        (data_akun["password"] == password)
    ]
    if password_benar.empty: 
        print("\nPassword salah! Silahkan coba lagi.")
        input("Klik Enter untuk melanjutkan...")
        menu()
        return 

    role = password_benar.iloc[0]["role"]
    
    if role == "admin":
        print(f"\nLogin berhasil Selamat datang ADMIN," , username)
        menu_admin(username)
    else:
        print(f"\nLogin berhasil! Selamat datang di AgroCare,", username)
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
        print(f"Username saat ini: {username}\n")
        print("1. Ubah Username")
        print("2. Ubah Password")
        print("3. Kembali ke menu sebelumnya")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            username = ubah_username(username)
            return username
        elif pilih == "2":
            username = ubah_password(username)
            return username
        elif pilih == "3":
            print("Kembali ke menu sebelumnya")
            return username
        else:
            print("Pilihan tidak valid! silahkan tekan menu 1-3")
        
def ubah_username(username_lama):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================UBAH USERNAME================")
    print(f"Username saat ini: {username_lama}\n")

    username_lama = input("Masukkan username lama: ").strip()

    if username_lama not in data_akun["username"].values:
        print(f"Username '{username_lama}' tidak ditemukan. tidak bisa dilanjutkan")
        return
    print(f"Username saat ini: {username_lama}\n")

    while True: 
        username_baru = input("Masukkan username baru: ").strip()

        
        if not username_baru:
            print("Username tidak boleh kosong! Silahkan coba lagi")
            continue

        if username_baru == username_lama:
            print("Username baru tidak boleh sama dengan username lama")
            continue

        if username_baru in data_akun["username"].values:
            print("Username sudah digunakan oleh pengguna lain\n")
            continue
        break

    data_akun.loc[data_akun["username"] == username_lama, "username"] = username_baru
    data_akun.to_csv("users.csv", index=False)

    print(f"Username berhasil diubah menjadi: {username_baru}")
    return username_baru

def ubah_password(username):
    os.system('cls')
    data_akun = pd.read_csv("users.csv")

    print("================UBAH PASSWORD================")
    print(f"Username saat ini: {username}\n")

    password_lama = input("Masukkan password lama: ")

    akun = data_akun[
        (data_akun["username"] == username) &
        (data_akun["password"] == password_lama)
    ]

    if akun.empty:
        print("Password lama salah ")
        input("Tekan enter untuk kembali...")
        return username
    
    password_baru = input("Masukkan password baru: " ).strip()

    while not password_baru or password_baru == password_lama:
        if not password_baru:
            print("Password baru tidak boleh kosong!")
        else:
            print("Password baru tidak boleh sama dengan password lama!")
        password_baru = input("Masukkan password baru: ").strip()

    data_akun.loc[data_akun["username"] == username, "password"] = password_baru
    data_akun.to_csv("users.csv", index=False)

    print("Password berhasil diubah!")
    input("Enter untuk melanjutkan")
    return username 

# =========================
#  MENU ADMIN
# =========================
def menu_admin(username): 
    if not username:
        print("Error: username kosong. Kembali ke menu utama.")
        return
    while True:
        os.system('cls')
        print("\n=== MENU ADMIN ===")
        print("1. Kelola Produk")
        print("2. Laporan Penjualan")
        print("3. Kelola Akun")
        print("0. Logout")
        pillihan = input("Pilih: ")

        if pillihan == "1":
            menu_kelola_produk()
        elif pillihan == "2": 
            os.system('cls')
            laporan_admin()
        elif pillihan == "3": 
            username = kelola_akun(username)
        elif pillihan == "0": 
            os.system('cls')
            break
        else:
            print("Pilihan tidak dikenal. Coba yang bener, ya.")
            input("Enter...")

# =========================
#  PENGELOLAAN PRODUK
# =========================
def ensure_product_file():
    if not os.path.exists(PRODUCT_FILE):
        df = pd.DataFrame(columns=["nama", "stok", "harga", "unit"])
        df.to_csv(PRODUCT_FILE, index=False)

def load_products() -> pd.DataFrame:
    ensure_product_file()
    try:
        df = pd.read_csv(PRODUCT_FILE) 
        for col in ["nama", "stok", "harga", "unit"]:
            if col not in df.columns:
                df[col] = "" if col == "unit" else 0
        df["nama"] = df["nama"].astype(str)
        df["stok"] = pd.to_numeric(df["stok"], errors="coerce").fillna(0).astype(float)
        df["harga"] = pd.to_numeric(df["harga"], errors="coerce").fillna(0).astype(float)
        df["unit"] = df["unit"].fillna("").astype(str)
        return df
    except Exception as e:
        print("Gagal membaca file produk:", str(e))
        return pd.DataFrame(columns=["nama","stok","harga","unit"])

def save_products(df: pd.DataFrame):
    try:
        df.to_csv(PRODUCT_FILE, index=False)
    except Exception as e:
        print("Gagal menyimpan data produk:", str(e))

def print_products(df: pd.DataFrame):
    if df.empty:
        print("Belum ada produk.")
        return
    display_df = df.copy()
    display_df.index = range(1, len(display_df) + 1)  # user-friendly index
    print(tabulate.tabulate(display_df, headers='keys', tablefmt='fancy_grid'))

def tambah_produk():
    os.system('cls')
    df = load_products()
    print("\n=== TAMBAH PRODUK ===")
    print_products(df)
    nama = input("Masukkan nama produk: ").strip().capitalize()
    if not nama:
        print("Nama produk tidak boleh kosong. Batal menambah.")
        return

    if (df["nama"].str.lower() == nama.lower()).any():
        print("Nama produk sudah terdaftar. Gunakan nama lain atau edit produk yang ada.")
        return

    try:
        stok_in = input("Masukkan stok produk (angka, boleh desimal): ").strip()
        stok = float(stok_in)
        if stok < 0:
            print("Stok tidak boleh negatif. Batal.")
            return
    except ValueError:
        print("Stok harus berupa angka. Batal.")
        return

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
    os.system('cls')
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

    idx = None
    if choice.isdigit():
        idx_user = int(choice)
        if 1 <= idx_user <= len(df):
            idx = idx_user - 1
        else:
            print("Index di luar jangkauan.")
            return
    else:
        matches = df[df["nama"].str.lower() == choice.lower()]
        if matches.empty:
            print("Nama produk tidak ditemukan.")
            return
        if len(matches) > 1:
            print("Lebih dari satu produk cocok dengan nama itu. Gunakan index.")
            print_products(matches)
            return
        idx = matches.index[0]

    old = df.loc[idx]
    print(f"Produk yang dipilih: {old['nama']} | Stok: {old['stok']} {old['unit']} | Harga: {old['harga']}")
    print("Kosongkan input untuk mempertahankan nilai lama.")

    new_name = input(f"Nama baru [{old['nama']}]: ").strip()
    if new_name == "":
        new_name = old['nama']
    else:
        new_name = new_name.capitalize()
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
    os.system('cls')
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
    os.system('cls')
    df = load_products()
    print("\n=== DAFTAR PRODUK ===")
    print_products(df)
    data = pd.read_csv("products.csv")
    if data.empty:
        print("Belum ada produk yang tersedia.")
        input("\nKlik Enter untuk kembali...")
        return
    print("\n===========================================")
    cari = input("Masukkan nama produk yang ingin dicari : ").strip().lower()

    hasil = data[data["nama"].str.lower() == cari]

    if hasil.empty:
        print("\n Hmm.. sepertinya produk itu belum tersedia ")
    else:
        print("\n Oke, Produknya ada. Ini detail lengkapnya:")
        print(f"Nama  : {hasil.iloc[0]['nama']}")
        print(f"Harga : {hasil.iloc[0]['harga']}")
        print(f"Stok  : {hasil.iloc[0]['stok']}")

    input("\nKlik Enter untuk kembali...")
    menu_kelola_produk()

# =========================
#  MENU PEMBELIAN PRODUK
# =========================
def beli_produk(username):
    os.system('cls')
    
    keranjang = [] 
    while True: 
        os.system('cls')

        data = pd.read_csv(PRODUCT_FILE)

        print("==== BELI PRODUK ====")
        print(F"Login sebagai : {username}")
        
        display_df = data.copy()
        display_df.index = range(1, len(display_df) + 1)
        print(tabulate.tabulate(display_df, headers="keys", tablefmt="fancy_grid"))

        try:
            indeks_user = int(input("\nMasukkan nomor produk (mulai dari 1): "))
        except ValueError:
            print("Input harus angka!")
            input("Klik enter")
            continue

        if indeks_user < 1 or indeks_user > len(data):
            print("Nomor produk tidak valid!")
            input("Klik enter")
            continue

        idx = indeks_user - 1
        produk = data.iloc[idx]

        print("================================")
        print("========= DETAIL PRODUK ========")
        print("================================")
        print(f"Nama    : {produk['nama']}")
        print(f"Stok    : {produk['stok']}")
        print(f"Harga   : {produk['harga']}")

        try:
            jumlah = int(input("Masukkan jumlah pembelian: "))
        except ValueError:
            print("Jumlah harus angka!")
            input("Klik enter...")
            continue

        if jumlah <= 0:
            print("Jumlah pembelian minimal 1! Tidak boleh 0!")
            input("Klik enter...")
            continue

        if jumlah > produk['stok']:
            print("Stok tidak cukup!")
            input("Klik enter...")
            continue

        subtotal = jumlah * produk['harga']

        keranjang.append({
            "index": idx,           
            "nama": produk["nama"],
            "jumlah": jumlah,
            "harga": produk["harga"],
            "subtotal": subtotal
        })

        print(f"\n{produk['nama']} x {jumlah} ditambahkan ke keranjang!")

        lanjut = input("Mau beli produk lain? (y/n): ").lower()
        if lanjut != "y":
            break

    if not keranjang:
        print("Keranjang kosong, tidak ada pembelian.")
        input("Enter")
        return

    os.system('cls')
    print("===============================")
    print("======== ISI KERANJANG ========")
    print("===============================")
    for item in keranjang:
        print(f" - {item['nama']} x {item['jumlah']} = Rp{item['subtotal']}")

    total_bayar = sum(item['subtotal'] for item in keranjang)
    print(f"\nTOTAL BAYAR = Rp{total_bayar}")

    konfirmasi = input("Lanjutkan pembayaran? (y/n): ").lower()
    if konfirmasi != "y":
        print("Pembelian dibatalkan.")
        input("Enter...")
        return

    for item in keranjang:
        data.loc[data.index[item["index"]], "stok"] -= item["jumlah"]

    data.to_csv(PRODUCT_FILE, index=False)

    from datetime import datetime
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(SALES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for item in keranjang:
            writer.writerow([tanggal, username, item["nama"], item["jumlah"], item["harga"], item["subtotal"]])
        

    print("================================")
    print("====== TRANSAKSI BERHASIL ======")
    print("================================")
    print(f"Tanggal : {tanggal}")
    print(f"Total   : Rp{total_bayar}")
    print("Detail pembelian:")
    for item in keranjang:
        print(f"- {item['nama']} x {item['jumlah']}")

    input("\nKlik enter untuk kembali ke menu")

# =========================
#  MENU KELOLA PRODUK
# =========================
def menu_kelola_produk():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== KELOLA PRODUK ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("0. Kembali")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1": 
            os.system('cls')
            lihat_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "2": 
            os.system('cls')
            tambah_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "3": 
            os.system('cls')
            edit_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "4": 
            os.system('cls')
            hapus_produk()
            input("Tekan Enter untuk kembali...")
        elif pilih == "0": 
            os.system('cls')
            menu()
        else:
            print("Pilihan tidak dikenal. Coba lagi.")
            input("Tekan Enter...")

if __name__ == "__main__":
    ensure_product_file()
        

# =========================
#  MENU PEMBELI
# =========================
def menu_pembeli(username):
    os.system('cls')
    if not username:
        print("Error: username kosong. Kembali ke menu utama.")
        return
    while True:
        print(f"Username saat ini: {username}\n")
        print("=== MENU PEMBELI ===")
        print("1. Pembelian Produk")
        print("2. Laporan Pembelian")
        print("3. Kelola Akun ")
        print("4. Cari Produk")
        print("0. Logout")
        pil = input("Pilih menu : ")

        if pil == "1":
            os.system('cls')
            beli_produk(username)
        elif pil == "2":
            os.system('cls')
            laporan_pembeli(username)
        elif pil == "3":
            os.system('cls')
            username = kelola_akun(username)
        elif pil == "4":
            os.system('cls')
            cari_produk()
        elif pil == "0":
            break
        else:
            print("Pilihan tidak dikenal. Coba yang bener, ya.")
            input("Enter...")

# =========================
#  MENU PENCARIAN PRODUK
# =========================
def cari_produk():
        os.system("cls")

        print("===== CARI PRODUK =====")

        df = pd.read_csv(PRODUCT_FILE)

        keyword = input("Masukkan kata pencarian: ").lower()

        hasil = df[df['nama'].str.lower().str.contains(keyword)]
        
        if hasil.empty:
            print("\n Produk tidak ditemukan!")
            input("Enter")
            return

        print("\n === HASIL PENCARIAN ===")
        print(tabulate.tabulate(hasil, headers="keys", tablefmt="fancy_grid"))
        print()

        input("Tekan enter untuk kembali")

# =========================
#  LAPORAN PEMBELI
# =========================
def laporan_pembeli(username):
    os.system('cls')
    print("=== LAPORAN PEMBELIAN ANDA ===")

    if not os.path.exists(SALES_FILE):
        print("Belum ada transaksi.")
        return

    with open(SALES_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        transaksi_map = {} 

        for row in reader:
            if row["pembeli"] != username:
                continue

            tgl = row["tanggal"]

            if tgl not in transaksi_map:
                transaksi_map[tgl] = []

            transaksi_map[tgl].append({
                "produk": row["produk"],
                "jumlah": row["jumlah"],
                "harga": row["harga"],
                "total": row["total"]
            })

    if not transaksi_map:
        print("Belum ada transaksi.")
        return

    tabel = []

    for tanggal, items in transaksi_map.items():
        produk_cell = ""
        total_semua = 0

        for item in items:
            produk_cell += f"{item['produk']} ({item['jumlah']}) - {item['total']}\n"
            try:
                total_semua += float(item["total"])
            except:
                pass

        produk_cell = produk_cell.strip()  

        tabel.append([tanggal, produk_cell, total_semua])

    print(tabulate.tabulate(
        tabel,
        headers=["Tanggal", "Produk", "Total Harga"],
        tablefmt="fancy_grid"
    ))

# =========================
#  SORTING & LAPORAN PENJUALAN
# =========================
def laporan_admin():
    os.system("cls")
    print("=== LAPORAN PENJUALAN (ADMIN) ===")

    if not os.path.exists(SALES_FILE):
        print("Belum ada data penjualan.")
        input("Enter...")
        return

    df = pd.read_csv(SALES_FILE)

    df["harga"] = pd.to_numeric(df["harga"], errors="coerce")
    df["total"] = pd.to_numeric(df["total"], errors="coerce")

    df["tanggal"] = pd.to_datetime(df["tanggal"])

    df = df.sort_values("tanggal", ascending=False)

    last_date = df["tanggal"].max().normalize()
    end_date = last_date + timedelta(days=1)

    while True:
        os.system("cls")
        print("=== PILIH FILTER WAKTU ===")
        print("1. Hari ini")
        print("2. 1 Minggu")
        print("3. 1 Bulan")
        print("4. Kembali")
        pilih = input("Masukkan pilihan: ")

        if pilih == "1":
            start_date = end_date - timedelta(days=1)
        elif pilih == "2":
            start_date = end_date - timedelta(days=7)
        elif pilih == "3":
            start_date = end_date - timedelta(days=30)
        elif pilih == "4":
            return
        else:
            print("Pilihan tidak valid.")
            input("Enter...")
            continue

        filtered = df[(df["tanggal"] >= start_date) & (df["tanggal"] < end_date)]

        if filtered.empty:
            print("Tidak ada transaksi di rentang ini.")
            input("Enter...")
            continue

        transaksi_map = {}

        for _, row in filtered.iterrows():
            tgl = row["tanggal"].strftime("%Y-%m-%d %H:%M:%S")

            if tgl not in transaksi_map:
                transaksi_map[tgl] = {
                    "pembeli": row["pembeli"],
                    "items": [],
                    "total_all": 0
                }

            item_str = f"{row['produk']} ({int(row['jumlah'])}) - Rp{row['total']}"
            transaksi_map[tgl]["items"].append(item_str)

            try:
                transaksi_map[tgl]["total_all"] += float(row["total"])
            except:
                pass

        tabel = []

        for tgl, dat in transaksi_map.items():
            produk_cell = "\n".join(dat["items"])
            tabel.append([
                tgl,
                dat["pembeli"],
                produk_cell,
                dat["total_all"]
            ])

        print("\n" + tabulate.tabulate(
            tabel,
            headers=["Tanggal", "Pembeli", "Produk", "Total Transaksi"],
            tablefmt="fancy_grid"
        ))

        input("\nEnter untuk lanjut...")

# =========================
#  MENU UTAMA
# =========================
def menu():
    os.system('cls')
    while True: 
        print("========================================================")
        print("=============== Selamat datang di Agrocare =============")
        print("========================================================")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        print("========================================================")

        pilihan = input("Pilih menu (1/2/3):")

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
            break
        else:
            print("\n Pilihan tidak valid! Silahkan masukkan angka 1-3.\n")
menu()