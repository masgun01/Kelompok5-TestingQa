# Teknik White-box Tambahan

Dokumen ini melengkapi [White-box Testing](White-box%20Testing.md) dengan teknik white-box lain yang diajarkan di materi: Statement Coverage, Branch Coverage, Condition Coverage, Loop Testing, dan Data Flow Testing. Semua angka dihitung dari flow graph pada dokumen utama, memakai jalur yang benar-benar bisa dijalankan (cara UI atau DevTools).

## 1. Statement Coverage dan Branch Coverage

Statement Coverage = simpul yang dilalui / seluruh simpul x 100%. Branch Coverage = hasil keputusan (True dan False) yang dilalui / seluruh hasil keputusan x 100%.

| Unit | Simpul dilalui | Statement Coverage | Cabang dilalui | Branch Coverage |
|---|---|---|---|---|
| WB-01 | 19 dari 20 | 95,0% | 15 dari 16 | 93,8% |
| WB-02 | 16 dari 21 | 76,2% | 11 dari 16 | 68,8% |
| WB-03 | 22 dari 25 | 88,0% | 19 dari 22 | 86,4% |
| WB-04 | 26 dari 26 | 100,0% | 16 dari 18 | 88,9% |
| WB-05 | 18 dari 21 | 85,7% | 12 dari 16 | 75,0% |

Ini angka rencana. Setelah pengujian dijalankan, angka aktual dihitung ulang dari jalur yang benar-benar berstatus Pass, dan disalin ke Test Report.

Simpul yang tidak tercakup, dan alasannya:

| Unit | Simpul | Penyebab |
|---|---|---|
| WB-01 | 8 | Cabang password_verify hanya dipakai akun dengan hash bcrypt, tidak ada akun seperti itu (J7). |
| WB-02 | 6 | Pembuatan admin (J7 sampai J9) |
| WB-02 | 12 | Pembuatan admin |
| WB-02 | 16 | Pembuatan admin |
| WB-02 | 19 | Email aktivasi gagal terkirim (J6) |
| WB-02 | 20 | INSERT gagal (J5) |
| WB-03 | 3 | Folder upload belum ada (J4) |
| WB-03 | 23 | Query simpan gagal (J10) |
| WB-03 | 24 | move_uploaded_file gagal (J9) |
| WB-05 | 17 | Cabang cadangan sendNotification tidak mungkin tercapai (J8, J9) |
| WB-05 | 18 | Sama dengan simpul 17 |
| WB-05 | 20 | Query simpan gagal (J5) |

## 2. Condition Coverage

Condition Coverage menuntut setiap kondisi tunggal di dalam keputusan majemuk (&& atau ||) pernah bernilai True dan False. Berikut keputusan majemuk di lima unit, beserta variasi data uji yang dibutuhkan. Variasi yang sudah ada di dokumen utama ditulis dengan ID jalurnya; yang lain adalah variasi tambahan.

| ID | Lokasi | Kondisi tunggal | Variasi data uji | Cara |
|---|---|---|---|---|
| CC-01 | register.php baris 30 | email kosong | Kirim form dengan email kosong | DevTools |
| CC-02 | register.php baris 30 | password kosong | Kirim form dengan password kosong. Kondisi ini tidak pernah True karena password sudah di-md5 lebih dulu (temuan W-2) | DevTools |
| CC-03 | register.php baris 30 | nama lengkap kosong | Sama dengan WB-02-J3 | DevTools |
| CC-04 | register.php baris 30 | no HP kosong | Kirim form dengan no HP kosong | DevTools |
| CC-05 | upload-berkas.php baris 113 | uploadOk bernilai 1 dan ukuran lebih dari 2.000.000 | (T,T) WB-03-J6. (T,F) WB-03-J2. uploadOk 0: WB-03-J5 | UI |
| CC-06 | upload-berkas.php baris 118 | ekstensi bukan jpg, bukan png, bukan jpeg, bukan pdf | Unggah berkas .jpg (J2), .png, .jpeg, .pdf, dan .gif (J7). Tiap format valid membuat satu kondisi menjadi False | UI |
| CC-07 | upload-berkas.php baris 127 | ada baris verifikasi dan status verified | Belum ada baris (J2). Ada baris berstatus pending: unggah ulang dokumen yang belum diverifikasi. Ada dan verified (J8) | UI |
| CC-08 | verifikasi.php baris 22 | ada parameter action dan ada parameter id | Keduanya ada (J2). Tanpa action (J1). Dengan action tetapi tanpa id: buka ?action=terima | UI |
| CC-09 | pengumuman.php baris 38 | MailConfig ada, user target ada, hasil bukan pending | hasil pending (J6) membuat kondisi ketiga False. Dua kondisi lain tidak bisa False tanpa merusak sistem | UI |
| CC-10 | pengumuman.php baris 41 dan 45 | hasil lolos (atau gagal) dan method email ada | Hasil lolos (J2), gagal (J7). Kondisi method_exists tidak bisa False karena MailConfig memilikinya | UI |

## 3. Loop Testing

Kelima unit tidak memuat perulangan. Perulangan terdekat ada di fungsi `hitungUlangStatusBerkasUser()` pada `user/upload-berkas.php` baris 67 sampai 79 (`foreach` atas enam jenis berkas). Jumlah putarannya tetap enam karena daftar jenis berkas ditulis di kode, jadi kasus ujinya bukan mengubah jumlah putaran, melainkan melihat hasil putaran pada isi berkas yang berbeda:

| ID | Kondisi | Data uji | Hasil diharapkan |
|---|---|---|---|
| LP-01 | Pendaftar belum pernah mengunggah apa pun (baris tabel berkas belum ada) | Akun uji baru, buka Upload Berkas | Fungsi tidak sampai masuk perulangan. Halaman tampil dengan semua dokumen berstatus belum diunggah |
| LP-02 | Satu dari enam berkas terisi | Unggah hanya Foto Siswa | Status keseluruhan Menunggu Verifikasi (pending) |
| LP-03 | Empat berkas wajib terisi dan semuanya diverifikasi admin | Unggah Foto, Akta, KK, KTP Orang Tua, lalu admin verifikasi satu per satu | Status keseluruhan Terverifikasi (verified). Ijazah dan Surat Dokter yang opsional tidak menghalangi |
| LP-04 | Satu dokumen ditolak admin | Admin menolak satu dokumen dengan catatan | Status keseluruhan Ditolak (rejected) |

LP-03 dan LP-04 butuh kerja sama dengan Lintang (sisi admin). LP-01 sampai LP-04 dijalankan oleh Jumigih bersamaan dengan skenario Upload Berkas.

## 4. Data Flow Testing

Data Flow Testing memeriksa jalur dari tempat variabel diberi nilai (def) sampai tempat nilainya dipakai (use). Dua variabel dipilih karena nilainya menentukan keputusan penting.

**Variabel `$uploadOk` (user/upload-berkas.php)**

| Def (baris) | Use (baris) | Pasangan def-use | Dicakup jalur |
|---|---|---|---|
| 106 (nilai 1) | 113, 118, 124, 133 | 4 pasangan | WB-03-J2 |
| 110 (nilai 0, jenis berkas tidak valid) | 113, 118, 124, 133 | 4 pasangan | WB-03-J5 |
| 115 (nilai 0, ukuran) | 118, 124, 133 | 3 pasangan | WB-03-J6 |
| 120 (nilai 0, format) | 124, 133 | 2 pasangan | WB-03-J7 |
| 129 (nilai 0, sudah terverifikasi) | 133 | 1 pasangan | WB-03-J8 |

Seluruh 14 pasangan def-use `$uploadOk` tercakup oleh lima jalur yang bisa dijalankan.

**Variabel `$password_valid` (auth/login.php)**

| Def (baris) | Use (baris) | Dicakup jalur | Status |
|---|---|---|---|
| 22 (false) | 29 | WB-01-J8 | Dijalankan |
| 24 (true, MD5 cocok) | 29 | WB-01-J3 | Dijalankan |
| 27 (true, password_verify) | 29 | WB-01-J7 | Tidak dijalankan (butuh akun berhash bcrypt) |

Tercakup 2 dari 3 pasangan.

