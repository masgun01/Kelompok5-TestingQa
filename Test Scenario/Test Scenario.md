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

**SISTEM – Smoke dan Sanity**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-SM-01 | Smoke Test | Memastikan 11 fitur utama dapat dibuka tanpa error setelah ada versi baru atau di awal sesi pengujian. | Positif | High |
| TS-SM-02 | Sanity Test | Memastikan perbaikan sebuah defect berhasil dan tidak merusak fitur terkait. | Positif | High |

**SISTEM – Integrasi**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-IN-01 | Alur Lolos | Memastikan alur penuh berjalan: registrasi, aktivasi, login, formulir, upload berkas, verifikasi dan Terima admin, hasil Lolos, lalu Daftar Ulang. | Positif | High |
| TS-IN-02 | Alur Gagal | Memastikan alur dengan hasil Gagal ditampilkan sebagai tidak lolos di Pengumuman dan Daftar Ulang tidak bisa dibuka. | Positif | High |
| TS-IN-03 | Alur Tolak | Memastikan pendaftar yang ditolak di menu Verifikasi tampil sebagai tidak lolos di Pengumuman dan Daftar Ulang tidak bisa dibuka. | Positif | High |
| TS-IN-04 | Email dan Link | Memastikan link di email aktivasi dan reset password mengarah ke alamat website yang benar dan berfungsi. | Positif | High |
| TS-IN-05 | Konsistensi Data | Memastikan data yang diisi pada Formulir sama di Beranda, Detail Pendaftar (admin), dan Daftar Ulang. | Positif | Medium |
| TS-IN-06 | Sinkron Dashboard | Memastikan angka Dashboard Admin berubah sesuai setelah aksi Terima. | Positif | Medium |

**NON-FUNGSIONAL – Kegunaan dan Kompatibilitas**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-NF-01 | Kegunaan | Memastikan pesan error dan validasi jelas, berbahasa Indonesia, dan tidak memuat istilah teknis. | Positif | Medium |
| TS-NF-02 | Kegunaan | Memastikan user baru dapat mengetahui langkah berikutnya dan selalu punya jalan kembali. | Positif | Medium |
| TS-NF-03 | Kompatibilitas | Memastikan halaman kunci tampil dan berfungsi sama di Chrome, Edge, dan Firefox. | Positif | Medium |
| TS-NF-04 | Kompatibilitas | Memastikan halaman kunci tampil baik pada lebar layar 360, 768, dan 1366 piksel. | Positif | Medium |
| TS-NF-05 | Aksesibilitas | Memastikan form dapat diisi hanya dengan keyboard dan label serta kontras terbaca. | Positif | Medium |

**NON-FUNGSIONAL – Performa**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-PF-01 | Waktu Muat | Memastikan halaman Login, Registrasi, Beranda User, dan Dashboard Admin selesai dimuat dalam 3 detik. | Positif | Medium |
| TS-PF-02 | Waktu Upload | Memastikan unggah berkas 2.000.000 byte selesai dengan pesan hasil dalam 10 detik. | Positif | Medium |
| TS-PF-03 | Load Testing | Memastikan halaman publik tetap merespons tanpa error pada 10 pengguna virtual selama 60 detik. | Positif | Low |

**NON-FUNGSIONAL – Keamanan (terbatas)**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-SC-01 | Transport | Memastikan website memakai HTTPS dengan sertifikat valid dan HTTP dialihkan ke HTTPS. | Positif | High |
| TS-SC-02 | Sesi | Memastikan cookie sesi memiliki atribut HttpOnly, Secure, dan SameSite. | Positif | Medium |
| TS-SC-03 | Otorisasi | Memastikan sesi user biasa tidak bisa menjalankan aksi admin lewat alamat langsung. | Negatif | High |
| TS-SC-04 | Penyimpanan Password | Memastikan password disimpan dengan hash modern bersalt (peninjauan kode). | Positif | High |
| TS-SC-05 | Input Khusus | Memastikan karakter khusus pada kolom teks tidak menyebabkan error dan tampil sebagai teks biasa. | Negatif | Medium |
| TS-SC-06 | Berkas Unggahan | Memastikan berkas unggahan tidak bisa dibuka tanpa login dan isi folder tidak bisa dilihat. | Negatif | High |
| TS-SC-07 | Pesan Error | Memastikan pesan ke pengguna tidak memuat detail teknis basis data (peninjauan kode). | Negatif | Medium |
| TS-SC-08 | Percobaan Login | Memastikan ada pembatasan setelah beberapa kali login salah beruntun. | Negatif | Medium |

**NON-FUNGSIONAL – API**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-AP-01 | Simpan Verifikasi Dokumen | Memastikan permintaan verifikasi dokumen yang valid menghasilkan JSON sukses dengan struktur lengkap. | Positif | High |
| TS-AP-02 | Simpan Verifikasi Dokumen | Memastikan parameter file_field atau status yang salah ditolak dengan pesan 'Permintaan tidak valid.' | Negatif | High |
| TS-AP-03 | Simpan Verifikasi Dokumen | Memastikan penolakan dokumen tanpa catatan, dan verifikasi dokumen yang belum diunggah, ditolak dengan pesan yang sesuai. | Negatif | Medium |
| TS-AP-04 | Terima Pendaftar | Memastikan aksi terima menghasilkan JSON gagal bila berkas belum terverifikasi dan JSON sukses bila sudah. | Positif | High |
| TS-AP-05 | Tolak Pendaftar | Memastikan aksi tolak dengan catatan menghasilkan JSON sukses dan data berubah. | Positif | High |
| TS-AP-06 | Hak Akses API | Memastikan pemanggilan endpoint admin tanpa sesi admin dialihkan ke login dan tidak mengubah data. | Negatif | High |

**AKSEPTASI – User Acceptance Testing**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-UA-01 | UAT User | Memastikan responden calon orang tua dapat menyelesaikan lima tugas user tanpa bantuan. | Positif | High |
| TS-UA-02 | UAT Admin | Memastikan responden petugas admin dapat memverifikasi satu pendaftar uji sampai hasil seleksi ditetapkan tanpa bantuan. | Positif | High |
| TS-UA-03 | Kriteria Penerimaan | Memastikan empat kriteria penerimaan terpenuhi dan hasilnya ditandatangani. | Positif | High |

**REGRESI**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-RG-01 | Regression Suite | Memastikan semua test case berprioritas High tetap lulus setelah defect diperbaiki atau commit berubah. | Positif | High |
| TS-RG-02 | Retest Defect | Memastikan setiap defect yang sudah diperbaiki tidak muncul lagi. | Positif | High |

**EKSPLORATORI**

| **ID** | **Fitur** | **Test Skenario** | **Tipe** | **Prioritas** |
| -------- | --------- | ----------------- | -------- | ------------- |
| TS-EX-01 | Formulir Pendaftaran | Menjelajahi Formulir Pendaftaran dengan data tidak biasa selama 30 menit. | Negatif | Medium |
| TS-EX-02 | Verifikasi Admin | Menjelajahi alur Verifikasi dan Kelola Pengumuman dengan urutan aksi tidak biasa selama 30 menit. | Negatif | Medium |
| TS-EX-03 | Autentikasi dan Navigasi | Menjelajahi login, sesi, dan navigasi (Back, Forward, dua tab) selama 30 menit. | Negatif | Medium |

**Catatan Pelaksanaan**

- Skenario Admin yang mengubah status (TS-AD-05 sampai TS-AD-11) hanya dijalankan pada akun uji milik tim, karena setiap aksi mengirim email ke pendaftar.
- TS-PD-14 sengaja menguji dua jalan menuju status tidak lolos (dari menu Pengumuman dan dari aksi Tolak di menu Verifikasi), karena kedua menu menyimpan nilai status yang berbeda di source code.
- Rincian data uji, nilai batas, langkah, dan hasil yang diharapkan ada di dokumen Test Case.
- Skenario TS-SM sampai TS-EX melengkapi skenario fitur di atas supaya seluruh materi pengujian tercakup. Rincian dan penanggung jawab ada di [Test Case Sistem](../Test%20Case/Test%20Case%20Sistem.xlsx).
- Skenario Performa (TS-PF-03) hanya dijalankan setelah pemilik website mengizinkan. Skenario Keamanan (TS-SC) bersifat pemeriksaan pasif dan peninjauan kode, bukan penetration testing.
- Skenario Integrasi (TS-IN) melibatkan dua orang: Jumigih di sisi user dan Lintang di sisi admin.

**Ringkasan**

| Kelompok | Bagian | Jumlah Skenario | Positif | Negatif |
|---|---|---|---|---|
| User | Autentikasi | 14 | 7 | 7 |
| User | Pendaftaran | 16 | 10 | 6 |
| Admin | Dashboard, Verifikasi, Pengumuman | 12 | 11 | 1 |
| Sistem | Smoke dan Sanity | 2 | 2 | 0 |
| Sistem | Integrasi | 6 | 6 | 0 |
| Sistem | Kegunaan dan Kompatibilitas | 5 | 5 | 0 |
| Sistem | Performa | 3 | 3 | 0 |
| Sistem | Keamanan (terbatas) | 8 | 3 | 5 |
| Sistem | API | 6 | 3 | 3 |
| Sistem | User Acceptance Testing | 3 | 3 | 0 |
| Sistem | REGRESI | 2 | 2 | 0 |
| Sistem | EKSPLORATORI | 3 | 0 | 3 |
| **Total** | | **80** | **55** | **25** |
