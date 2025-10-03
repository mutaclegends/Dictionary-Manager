# Dictionary Manager (Python)

**Dictionary Manager** adalah skrip Python berbasis terminal yang memungkinkan pengguna untuk **mengelola file daftar kata secara interaktif**. Skrip ini mendukung operasi tambah, hapus, cek, statistik, pencarian kata, dan manajemen file secara aman.

---

## Fitur

1. **Menu 0 – Masukkan / Ganti File Path**  
   - Memilih file dictionary untuk dikelola.  
   - Sistem otomatis memvalidasi file sebelum digunakan.  
   - Menampilkan full path file saat berhasil dibuka.  

2. **Menu 1 – Tambah Kata**  
   - Tambah kata baru ke file.  
   - Bisa batch, dipisah spasi.  
   - Menghindari duplikat otomatis.

3. **Menu 2 – Hapus Kata**  
   - Hapus kata dari file.  
   - Bisa batch, dipisah spasi.  
   - Kata yang tidak ada akan dilewati.

4. **Menu 3 – Cek Kata**  
   - Mengecek keberadaan kata.  
   - Menampilkan jumlah huruf dan posisi di file.

5. **Menu 4 – Lihat Semua Kata**  
   - Menampilkan daftar kata urut alfabet.

6. **Menu 5 – Cari Kata berdasarkan Awalan/Akhiran**  
   - Cari kata yang memiliki awalan atau akhiran tertentu.

7. **Menu 6 – Statistik Kata**  
   - Menampilkan jumlah kata, panjang terpendek, terpanjang, dan rata-rata panjang kata.

8. **Menu 7 – Bersihkan Layar (CLS)**  
   - Membersihkan terminal untuk tampilan lebih rapi.

9. **Menu 8 – Keluar Program**  
   - Menyimpan perubahan dan keluar dari aplikasi.

10. **Menu 9 – Info File Sekarang**  
    - Menampilkan informasi file aktif: path, ukuran file (bytes), jumlah baris.

---

## Contoh Penggunaan

=== MENU SUPER INTERAKTIF ===
0. Masukkan / Ganti file path
1. Tambah kata
2. Hapus kata
3. Cek kata
4. Lihat semua kata
5. Cari kata berdasarkan awalan/akhiran
6. Statistik kata
7. Bersihkan layar (CLS)
8. Keluar
9. Info file sekarang

Pilih aksi (0-9): 0
Masukkan file path: dictionary.txt
[INFO] File 'C:\Users\User\dictionary.txt' berhasil dibuka. Jumlah kata: 120
[INFO] Sekarang menggunakan file: C:\Users\User\dictionary.txt

Pilih aksi (0-9): 1
Masukkan kata yang ingin ditambahkan (pisah spasi jika banyak): Fisika Kimia Matematika
[ADD] Kata 'Fisika' berhasil ditambahkan.
[ADD] Kata 'Kimia' berhasil ditambahkan.
[ADD] Kata 'Matematika' berhasil ditambahkan.

---

## Cara Menggunakan

1. **Clone repo atau download skrip Python**  

```bash
git clone https://github.com/mutaclegends/Dictionary-Manager.git
cd Dictionary-Manager
