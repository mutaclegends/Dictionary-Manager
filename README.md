## Dictionary Manager (Python)

**Dictionary Manager** adalah skrip Python berbasis terminal untuk **mengelola daftar kata** secara interaktif. Cocok untuk keperluan dictionary, wordlist, atau file teks kata lainnya.

---

## Fitur Utama

| Menu | Fitur | Deskripsi |
|------|-------|-----------|
| 0 | Masukkan / Ganti file path | Memilih file dictionary yang akan dikelola. File divalidasi sebelum digunakan. |
| 1 | Lihat kata per lini | Menampilkan kata berdasarkan **range lini**. Format input: `start-end`. Maksimal 500 kata sekaligus. |
| 2 | Tambah kata | Menambahkan kata baru ke file. Bisa batch (pisah spasi). Duplikat otomatis dilewati. |
| 3 | Hapus kata | Menghapus kata dari file. Bisa batch (pisah spasi). Kata yang tidak ada akan dilewati. |
| 4 | Cek kata | Mengecek apakah kata ada di file. Menampilkan posisi (lini) dan jumlah huruf. |
| 5 | Cari kata awalan/akhiran | Mencari kata berdasarkan awalan atau akhiran tertentu. |
| 6 | Statistik kata | Menampilkan jumlah kata, panjang kata terpendek, terpanjang, dan rata-rata panjang kata. |
| 7 | Info file sekarang | Menampilkan info file aktif: full path, ukuran file (bytes), jumlah baris. |
| 8 | Bersihkan layar (CLS) | Membersihkan terminal agar tampilan lebih rapi. |
| 9 | Keluar | Menyimpan perubahan ke file dan keluar dari program. |

> ⚠️ Semua menu selain 0,8,9 terkunci sampai file berhasil dibuka menggunakan menu 0.

---

## Cara Menggunakan

1. **Clone repo atau download skrip**

```bash
git clone https://github.com/mutaclegends/Dictionary-Manager.git
cd Dictionary-Manager
