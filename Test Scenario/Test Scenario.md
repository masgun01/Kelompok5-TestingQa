**TEST SCENARIO**

Website: PPDB SLB Sana Dharma (commit `70a38d9`)

Test Scenario ini disusun dari use case tiap role pada [Matriks dan Use Case](../Matriks%20dan%20Use%20Case/Matriks%20dan%20Use%20Case.md) dan [System Flowchart](../System%20Flowchart/), memakai teknik Use Case Testing: tiap skenario menguji alur utama dan alur alternatif satu use case, dengan kondisi valid (Positif) dan tidak valid (Negatif). Setiap skenario nanti dirinci lagi menjadi satu atau lebih Test Case, dengan teknik Equivalence Partitioning, Boundary Value Analysis, dan State Transition Testing. Prosedur pengujian tiap Test Case nanti ditulis dengan pendekatan *keyword-driven testing* sesuai ISO/IEC/IEEE 29119-5:2024. Penjelasan standar dan contoh penulisannya ada di [Test Plan](../Test%20Plan/Test%20Plan.md) bagian 1 dan 5.3.

Keterangan kolom:
- **Tipe**: Positif (input atau kondisi valid) atau Negatif (input atau kondisi tidak valid).
- **Prioritas**: High (Tinggi), Medium (Sedang), atau Low (Rendah), berdasarkan dampak dan urgensi kalau fitur itu gagal.

**USER – Autentikasi**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-AU-01 | Registrasi Akun | Memastikan user berhasil membuat akun dengan data yang valid dan menerima email aktivasi. | Positif | High |
| TS-AU-02 | Registrasi Akun | Memastikan sistem menolak registrasi dengan email yang sudah terdaftar. | Negatif | High |
| TS-AU-03 | Registrasi Akun | Memastikan tombol Daftar Sekarang tidak aktif jika password kurang dari 6 karakter, konfirmasi password tidak cocok, ada field kosong, atau Syarat dan Ketentuan tidak dicentang. | Negatif | Medium |
| TS-AU-04 | Aktivasi Akun | Memastikan akun menjadi aktif setelah link aktivasi di email dibuka. | Positif | High |
| TS-AU-05 | Login | Memastikan user berhasil login dengan akun yang valid dan diarahkan ke Beranda. | Positif | High |
| TS-AU-06 | Login | Memastikan admin berhasil login dengan akun yang valid dan diarahkan ke Dashboard Admin. | Positif | High |
| TS-AU-07 | Login | Memastikan sistem menolak login dengan password salah atau email yang tidak terdaftar. | Negatif | High |
| TS-AU-08 | Login | Memastikan sistem menolak login dari akun yang belum diaktivasi. | Negatif | Medium |
| TS-AU-09 | Logout | Memastikan pengguna berhasil logout dan tidak bisa membuka halaman Beranda atau Dashboard tanpa login ulang. | Positif | Medium |
| TS-AU-10 | Hak Akses | Memastikan pengguna yang belum login atau login sebagai pendaftar diarahkan ke halaman login saat membuka halaman admin. | Negatif | High |
| TS-AU-11 | Lupa Password | Memastikan link reset password terkirim ke email yang terdaftar. | Positif | Medium |
| TS-AU-12 | Lupa Password | Memastikan sistem menampilkan pesan jika email tidak terdaftar. | Negatif | Medium |
| TS-AU-13 | Reset Password | Memastikan password berhasil diganti melalui link reset yang valid, lalu bisa dipakai untuk login. | Positif | Medium |
| TS-AU-14 | Reset Password | Memastikan sistem menolak password baru yang kurang dari 6 karakter, konfirmasi yang tidak cocok, atau link reset yang tidak valid. | Negatif | Medium |

**USER – Pendaftaran**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-PD-01 | Beranda | Memastikan Beranda menampilkan kelengkapan data, progress, dan status pendaftaran sesuai data pendaftar. | Positif | Medium |
| TS-PD-02 | Formulir – Jenjang | Memastikan user dapat memilih jenjang (TKLB, SDLB, atau SMPLB) dan lanjut ke langkah berikutnya. | Positif | High |
| TS-PD-03 | Formulir – Jenjang | Memastikan user tidak bisa lanjut tanpa memilih jenjang. | Negatif | Medium |
| TS-PD-04 | Formulir – Data Pribadi | Memastikan data pribadi yang lengkap tersimpan dan user dapat lanjut ke langkah berikutnya. | Positif | High |
| TS-PD-05 | Formulir – Data Pribadi | Memastikan sistem menolak penyimpanan jika field wajib dikosongkan. | Negatif | Medium |
| TS-PD-06 | Formulir – Surat Keterangan | Memastikan pilihan surat keterangan tersimpan. | Positif | Low |
| TS-PD-07 | Formulir – Data Orang Tua | Memastikan data orang tua atau wali tersimpan dan pendaftar diarahkan ke Upload Berkas. | Positif | High |
| TS-PD-08 | Upload Berkas | Memastikan berkas JPG, JPEG, PNG, atau PDF dengan ukuran sesuai batas berhasil diunggah. | Positif | High |
| TS-PD-09 | Upload Berkas | Memastikan sistem menolak berkas yang melebihi batas ukuran. | Negatif | High |
| TS-PD-10 | Upload Berkas | Memastikan sistem menolak berkas dengan format yang tidak diizinkan. | Negatif | High |
| TS-PD-11 | Upload Berkas | Memastikan berkas yang sudah diverifikasi admin tidak bisa diganti. | Negatif | Medium |
| TS-PD-12 | Pengumuman | Memastikan pengumuman menampilkan status "Sedang Diproses" saat hasil seleksi masih Pending. | Positif | Medium |
| TS-PD-13 | Pengumuman | Memastikan pengumuman menampilkan status diterima beserta catatan sekolah saat hasil seleksi Lolos. | Positif | High |
| TS-PD-14 | Pengumuman | Memastikan pengumuman menampilkan status tidak lolos saat hasil seleksi Gagal atau saat pendaftar ditolak di menu Verifikasi. | Positif | High |
| TS-PD-15 | Daftar Ulang | Memastikan user yang lolos dapat melihat data pendaftar, berkas yang harus dibawa, dan informasi pembayaran. | Positif | High |
| TS-PD-16 | Daftar Ulang | Memastikan user yang belum atau tidak lolos diarahkan ke halaman Pengumuman saat membuka Daftar Ulang. | Negatif | High |

**ADMIN**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-AD-01 | Dashboard | Memastikan Dashboard menampilkan jumlah total pendaftar, menunggu verifikasi, diterima, dan ditolak sesuai data. | Positif | Medium |
| TS-AD-02 | Dashboard | Memastikan tabel Pendaftar Terbaru menampilkan data dan status pendaftar dengan benar. | Positif | Low |
| TS-AD-03 | Verifikasi | Memastikan admin dapat mencari pendaftar berdasarkan nama, email, atau nomor HP. | Positif | Medium |
| TS-AD-04 | Verifikasi | Memastikan tab filter (Perlu Review, Berkas Perlu Dicek, Diterima, Ditolak, Belum Isi) menampilkan data sesuai status. | Positif | Medium |
| TS-AD-05 | Verifikasi – Detail | Memastikan admin dapat membuka detail pendaftar dan menandai setiap berkas sebagai terverifikasi atau ditolak. | Positif | High |
| TS-AD-06 | Verifikasi – Terima | Memastikan admin dapat menerima pendaftar yang semua berkas wajibnya sudah terverifikasi, dan email konfirmasi terkirim. | Positif | High |
| TS-AD-07 | Verifikasi – Terima | Memastikan sistem menolak aksi Terima jika berkas wajib belum terverifikasi. | Negatif | High |
| TS-AD-08 | Verifikasi – Tolak | Memastikan admin dapat menolak pendaftar dengan catatan, dan email pemberitahuan terkirim. | Positif | High |
| TS-AD-09 | Kelola Pengumuman | Memastikan admin dapat menetapkan hasil seleksi Lolos beserta catatan, lalu hasilnya tampil di halaman Pengumuman pendaftar. | Positif | High |
| TS-AD-10 | Kelola Pengumuman | Memastikan admin dapat menetapkan hasil seleksi Gagal, lalu hasilnya tampil di halaman Pengumuman pendaftar. | Positif | High |
| TS-AD-11 | Kelola Pengumuman | Memastikan admin dapat mengembalikan hasil seleksi ke Pending tanpa mengirim email. | Positif | Low |
| TS-AD-12 | Logout | Memastikan admin berhasil logout dari sistem. | Positif | Low |

**Catatan Pelaksanaan**

- Skenario Admin yang mengubah status (TS-AD-05 sampai TS-AD-11) hanya dijalankan pada akun uji milik tim, karena setiap aksi mengirim email ke pendaftar.
- TS-PD-14 sengaja menguji dua jalan menuju status tidak lolos (dari menu Pengumuman dan dari aksi Tolak di menu Verifikasi), karena kedua menu menyimpan nilai status yang berbeda di source code.
- Rincian data uji, nilai batas, langkah, dan hasil yang diharapkan ada di dokumen Test Case.

**Ringkasan**

| Role | Bagian | Jumlah Skenario | Positif | Negatif |
|---|---|---|---|---|
| User | Autentikasi | 14 | 7 | 7 |
| User | Pendaftaran | 16 | 10 | 6 |
| Admin | Dashboard, Verifikasi, Pengumuman | 12 | 11 | 1 |
| **Total** | | **42** | **28** | **14** |
