# Daftar Keyword

Mengikuti ISO/IEC/IEEE 29119-5:2024 (keyword-driven testing), kolom Prosedur Pengujian ditulis sebagai urutan keyword: aksi bernama yang diikuti datanya. Nama keyword memakai istilah pengguna sistem, jadi test case tetap terbaca walaupun tampilan halaman berubah. Data uji ditulis di kolom Input Data, bukan di dalam langkah.

## Keyword aksi

| Keyword | Arti | Data yang dibutuhkan |
|---|---|---|
| Buka Halaman [nama] | Membuka halaman lewat menu atau alamat | Nama halaman |
| Buka alamat [path] langsung | Mengetik alamat halaman di browser | Path |
| Isi Form [nama] | Mengisi seluruh kolom pada form | Input Data |
| Isi [kolom] | Mengisi satu kolom | Nilai kolom |
| Centang [pilihan] | Mencentang kotak | - |
| Klik [tombol] | Menekan tombol atau tautan | - |
| Buka Link [jenis] dari email | Membuka tautan di email (Aktivasi, Reset) | Email uji |
| Unggah [berkas] | Memilih dan mengirim berkas pada Upload Berkas | Berkas uji |
| Pilih [opsi] | Memilih nilai pada daftar atau tab | Nilai |
| Tekan tombol Back browser | Kembali ke halaman sebelumnya | - |

## Keyword pemeriksaan

| Keyword | Arti |
|---|---|
| Amati [objek] | Mencatat apa yang tampil: pesan, tombol, halaman tujuan, isi kolom |
| Bandingkan [A] dengan [B] | Mencocokkan dua nilai, misalnya angka Dashboard dengan hitungan manual |

## Keyword gabungan

| Keyword | Terdiri dari |
|---|---|
| Login | Buka Halaman Login, Isi Form Login, Klik Masuk |
| Logout | Klik Logout |
| Registrasi | Buka Halaman Registrasi, Isi Form Registrasi, Centang Syarat dan Ketentuan, Klik Daftar Sekarang |

## Contoh

TC-AU-19, login password salah:

1. Buka Halaman Login
2. Isi Form Login (Input Data: email terdaftar, password salah)
3. Klik Masuk
4. Amati pesan

Hasil yang diharapkan: pesan "Email atau password salah!" tampil, tetap di halaman login.

## Catatan

Test Case Autentikasi sudah memakai pola ini. Test Case Sistem memakai keyword yang sama, tetapi sebagian langkahnya masih berupa kalimat bebas karena menyangkut alat lain (DevTools, Postman, k6). Test Case User dan Admin ditulis dengan keyword di atas oleh Jumigih dan Lintang.
