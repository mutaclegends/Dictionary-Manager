import os

# ===== Fungsi Utility =====
def cls():
    """Membersihkan layar terminal (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_file(file_path):
    """Baca file dan kembalikan list kata. Kembalikan None jika file tidak ditemukan."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            kata_list = [line.strip() for line in f if line.strip()]
        print(f"[INFO] File '{os.path.abspath(file_path)}' berhasil dibuka. Jumlah kata: {len(kata_list)}")
        return kata_list
    except FileNotFoundError:
        print(f"[ERROR] File '{file_path}' tidak ditemukan.")
        return None
    except Exception as e:
        print(f"[ERROR] Gagal membuka file '{file_path}': {e}")
        return None

def save_file(file_path, kata_list):
    """Simpan list kata ke file, urutkan."""
    kata_sorted = sorted(set(kata_list), key=str.lower)
    with open(file_path, "w", encoding="utf-8") as f:
        for kata in kata_sorted:
            f.write(kata + "\n")
    print(f"[INFO] File '{os.path.abspath(file_path)}' berhasil diperbarui dan tersortir.")

# ===== Fungsi Menu =====
def tambah_kata(kata_list):
    kata_input = input("Masukkan kata yang ingin ditambahkan (pisah spasi jika banyak): ")
    cls()
    kata_baru = kata_input.split()
    for kata in kata_baru:
        if kata in kata_list:
            print(f"[SKIP] Kata '{kata}' sudah ada.")
        else:
            kata_list.append(kata)
            print(f"[ADD] Kata '{kata}' berhasil ditambahkan.")
    return kata_list

def hapus_kata(kata_list):
    kata_input = input("Masukkan kata yang ingin dihapus (pisah spasi jika banyak): ")
    cls()
    kata_hapus = kata_input.split()
    for kata in kata_hapus:
        if kata in kata_list:
            kata_list.remove(kata)
            print(f"[DEL] Kata '{kata}' berhasil dihapus.")
        else:
            print(f"[SKIP] Kata '{kata}' tidak ditemukan.")
    return kata_list

def cek_kata(kata_list):
    kata_input = input("Masukkan kata yang ingin dicek: ")
    cls()
    if kata_input in kata_list:
        index = kata_list.index(kata_input) + 1
        print(f"Kata '{kata_input}' ditemukan di lini {index} dengan {len(kata_input)} huruf.")
    else:
        print(f"Kata '{kata_input}' tidak ditemukan.")

def lihat_kata_per_lini(kata_list):
    total_kata = len(kata_list)
    print(f"Total kata di file: {total_kata}")
    print("Masukkan range lini yang ingin ditampilkan, format: start-end (maksimal 500 kata)")
    
    cls()

    while True:
        try:
            input_range = input("Range: ").strip()
            if '-' not in input_range:
                raise ValueError("Format harus start-end")
            start_str, end_str = input_range.split('-')
            start_line = int(start_str)
            end_line = int(end_str)

            if start_line < 1 or end_line > total_kata:
                print(f"[ERROR] Range harus antara 1 sampai {total_kata}.")
                continue
            if end_line < start_line:
                print("[ERROR] Lini akhir harus lebih besar atau sama dengan lini awal.")
                continue
            if end_line - start_line + 1 > 500:
                print("[ERROR] Maksimal jangkauan 500 kata.")
                continue
            break
        except ValueError as ve:
            print(f"[ERROR] Input tidak valid: {ve}")

    print(f"Menampilkan kata dari lini {start_line} sampai {end_line}:")
    for idx, kata in enumerate(kata_list[start_line-1:end_line], start=start_line):
        print(f"{idx}. {kata}")

def cari_awalan_akhiran(kata_list):
    pilihan = input("Cari berdasarkan (1) Awalan atau (2) Akhiran? ketik 1/2: ").strip()
    cls()
    if pilihan not in ("1", "2"):
        print("[ERROR] Pilihan tidak valid.")
        return
    pola = input("Masukkan string yang dicari: ").strip()
    hasil = []
    if pilihan == "1":
        hasil = [kata for kata in kata_list if kata.startswith(pola)]
        print(f"Kata dengan awalan '{pola}': {hasil}" if hasil else f"Tidak ada kata dengan awalan '{pola}'.")
    else:
        hasil = [kata for kata in kata_list if kata.endswith(pola)]
        print(f"Kata dengan akhiran '{pola}': {hasil}" if hasil else f"Tidak ada kata dengan akhiran '{pola}'.")

def statistik(kata_list):
    if not kata_list:
        print("Daftar kata kosong.")
        return
    panjang_kata = [len(k) for k in kata_list]
    print(f"Jumlah kata: {len(kata_list)}")
    print(f"Panjang kata terpendek: {min(panjang_kata)}")
    print(f"Panjang kata terpanjang: {max(panjang_kata)}")
    print(f"Panjang rata-rata kata: {sum(panjang_kata)/len(panjang_kata):.2f}")

def info_file(current_file):
    if not current_file:
        print("Belum ada file yang dipilih. Gunakan menu 0 untuk memasukkan file.")
        return
    try:
        full_path = os.path.abspath(current_file)
        size = os.path.getsize(current_file)
        with open(current_file, "r", encoding="utf-8") as f:
            lines = sum(1 for _ in f)
        print(f"=== INFO FILE ===")
        print(f"Path: {full_path}")
        print(f"Ukuran: {size} bytes")
        print(f"Jumlah line/baris: {lines}")
    except Exception as e:
        print(f"[ERROR] Tidak bisa mendapatkan info file: {e}")

# ===== Main Menu =====
def main():
    current_file = None
    kata_list = []

    while True:
        print("\n=== DAFTAR MENU ===\n")
        print("0. Masukkan / Ganti file path")
        print(f"1. Lihat kata per lini {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"2. Tambah kata {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"3. Hapus kata {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"4. Cek kata {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"5. Cari kata berdasarkan awalan/akhiran {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"6. Statistik kata {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print(f"7. Info file sekarang {'[TIDAK TERSEDIA]' if not current_file else ''}")
        print("8. Bersihkan layar (CLS)")
        print("9. Keluar\n")

        pilihan = input("Pilih aksi (0-9): ").strip()
        cls()
        print()

        if pilihan == "0":
            path = input("Masukkan file path: ").strip()
            if path:
                data = load_file(path)
                if data is not None:
                    current_file = path
                    kata_list = data
                    cls()
                    print(f"[INFO] Sekarang menggunakan file: {os.path.abspath(current_file)}")
        elif pilihan in ("1","2","3","4","5","6","7"):
            if not current_file:
                print("Mohon masukkan file yang dituju dari menu 0")
                continue
            if pilihan == "1":
                lihat_kata_per_lini(kata_list)
            elif pilihan == "2":
                kata_list = tambah_kata(kata_list)
            elif pilihan == "3":
                kata_list = hapus_kata(kata_list)
            elif pilihan == "4":
                cek_kata(kata_list)
            elif pilihan == "5":
                cari_awalan_akhiran(kata_list)
            elif pilihan == "6":
                statistik(kata_list)
            elif pilihan == "7":
                info_file(current_file)
        elif pilihan == "8":
            cls()
        elif pilihan == "9":
            if current_file:
                save_file(current_file, kata_list)
            print("Keluar program.")
            break
        else:
            print("[ERROR] Pilihan tidak valid. Masukkan angka 0-9.")

if __name__ == "__main__":
    main()
