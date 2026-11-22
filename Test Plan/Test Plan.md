# TEST PLAN

## PPDB SLB Sana Dharma

| Informasi | Keterangan |
|---|---|
| ID Dokumen | TP-PPDB-01 |
| Versi | 0.1 (draft) |
| Disusun oleh | Kelompok 5 – 07TPLE002 |

### 1. Pendahuluan

Dokumen Test Plan ini menjadi pedoman pelaksanaan pengujian pada website PPDB SLB Sana Dharma. Pengujian dilakukan untuk memastikan fitur utama berjalan sesuai fungsinya, mulai dari pembuatan akun sampai daftar ulang di sisi user, serta verifikasi dan pengumuman hasil seleksi di sisi admin.

Pengujian mencakup pengujian fungsional secara manual (Black-box) dan pengujian alur logika program (White-box) pada fungsi inti fitur utama.

Standar acuan yang dipakai adalah ISO/IEC/IEEE 29119-5:2024
yaitu bagian kelima dari rangkaian standar pengujian perangkat lunak ISO/IEC/IEEE 29119 yang membahas *keyword-driven testing*.
Inti pendekatannya ada pada cara menulis test case: aksi pengujian yang berulang diberi nama baku beserta parameternya, lalu test case disusun dari rangkaian nama aksi itu.
Nama yang dipilih mengikuti istilah pengguna sistem, bukan nama elemen halaman, sehingga prosedurnya tidak perlu ditulis ulang setiap kali tata letak halaman berubah. Pasal 5.1 standar tersebut menyatakan pendekatan ini tetap dapat dipakai walaupun automasi tidak direncanakan, dan hal itulah yang menjadi dasar pelaksanaan pengujian manual pada proyek ini. Penyebutan standar di sini bersifat acuan penyusunan dokumen, bukan klaim pemenuhan persyaratan kesesuaian (*conformance*) pada Pasal 7 yang memang ditujukan bagi penyedia kerangka kerja pengujian.

### 2. Test Objectives

Tujuan pengujian adalah:

1. Memastikan 11 fitur utama berjalan sesuai fungsi yang ditampilkan di website dan yang tertulis di source code.
2. Memastikan setiap role (User dan Admin) hanya dapat mengakses fitur sesuai haknya.
3. Memastikan validasi input menolak data yang tidak valid dan menerima data yang valid, termasuk pada nilai batas.
4. Memeriksa alur logika program pada fungsi inti fitur utama melalui Basis Path Testing.
5. Mengidentifikasi dan mendokumentasikan kesalahan (defect) beserta bukti.
6. Mendokumentasikan hasil pengujian sebagai dasar evaluasi kualitas sistem.

### 3. Test Scope

#### 3.1 Test Item

| Item | Keterangan |
|---|---|
| Nama | PPDB SLB Sana Dharma |
| URL | https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/ |
| Versi | Commit `70a38d9` (21 November 2026) |
| Jenis | Aplikasi web, PHP 8.2 tanpa framework, basis data MySQL |

Jika ada perubahan kode di tengah masa pengujian, nomor commit baru dicatat dan test case yang terdampak diuji ulang.

#### 3.2 In Scope

Pengujian dilakukan terhadap fitur-fitur berikut:

| **No** | **Role** | **Fitur yang Diuji** |
| ------ | -------- | -------------------- |
| **1** | **User** | Registrasi Akun, Login & Logout, Lupa Password, Beranda, Formulir Pendaftaran, Upload Berkas, Pengumuman, Daftar Ulang |
| **2** | **Admin** | Login & Logout, Lupa Password, Dashboard, Verifikasi Pendaftar, Kelola Pengumuman |

Selain fitur di atas, ruang lingkup juga mencakup:

**A. Functional Testing (Black-box, manual)**
- Pengujian fungsi berdasarkan Test Scenario dan Test Case.
- Pengujian hak akses tiap role terhadap halaman fitur utama.

**B. White-box Testing (Basis Path)**
- Pengujian alur logika pada fungsi inti fitur utama berdasarkan source code (daftar unit ada di bagian 5.4).

#### 3.3 Out of Scope

Pengujian tidak mencakup:

| No | Bagian | Alasan |
|---|---|---|
| 1 | Menu Laporan, Data User, dan ekspor data (admin) | Bukan fitur utama yang disepakati tim |
| 2 | Halaman landing (beranda publik, info, alur, FAQ) | Hanya berisi informasi statis |
| 3 | Performance, Load, dan Stress Testing | Website berjalan di server yang sedang dipakai. Memberi beban buatan berisiko mengganggu layanan. |
| 4 | Security Testing / Penetration Testing | Di luar fokus fitur utama dan memerlukan izin khusus |
| 5 | Compatibility Testing di banyak browser dan perangkat | Pengujian dilakukan pada satu lingkungan (lihat bagian 6) |
| 6 | Isi dan tampilan email secara detail | Yang diperiksa hanya apakah email terkirim dan link di dalamnya berfungsi |
| 7 | Automation Testing | Pengujian cuma dilakukan sekali untuk tugas ini, jadi bikin skrip otomatis tidak sebanding dengan manfaatnya. Test case tetap dijalankan secara manual |

### 4. Test Basis

Test basis adalah dasar yang dipakai untuk merancang pengujian. Website ini tidak memiliki dokumen spesifikasi kebutuhan (SRS) resmi. Dasar perancangan pengujian adalah:

1. Source code versi yang diuji (commit `70a38d9`).
2. Tampilan dan pesan yang muncul di website.
3. [System Overview](../System%20Overview.md), [Matriks dan Use Case](../Matriks%20dan%20Use%20Case/Matriks%20dan%20Use%20Case.md), dan [System Flowchart](../System%20Flowchart/) yang disusun tim dari dua sumber di atas.

Karena tidak ada SRS, hasil yang diharapkan pada test case diturunkan dari aturan di source code dan teks yang ditampilkan website. Jika keduanya bertentangan, hal tersebut dicatat sebagai temuan.

### 5. Test Strategy

#### 5.1 Test Level dan Test Type

| Aspek | Pilihan | Alasan |
|---|---|---|
| Test level | System Testing | Website diuji sebagai satu sistem utuh yang sudah terintegrasi dan berjalan, bukan per unit atau per modul |
| Test type | Functional Testing | Fokus pada apakah fitur utama bekerja sesuai fungsinya |
| Pelaksanaan | Manual, terskrip | Test case ditulis sebelum dijalankan, lalu dieksekusi langsung lewat browser |

#### 5.2 Teknik Perancangan Pengujian

Ada lima teknik Black Box Testing yang diajarkan: Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, State Transition Testing, dan Use Case Testing. Dari situ, tim memilih empat yang paling cocok dengan fitur utama PPDB SLB Sana Dharma:

| Teknik | Jenis | Dipakai Untuk |
|---|---|---|
| Equivalence Partitioning (EP) | Black Box Testing | Membagi input (email, password, jenis berkas, jenjang) ke kelas valid dan tidak valid |
| Boundary Value Analysis (BVA) | Black Box Testing | Menguji nilai batas, yaitu panjang password (5, 6, 7 karakter) dan ukuran berkas (sekitar batas 2 MB) |
| State Transition Testing | Black Box Testing | Menguji perubahan status akun (belum aktif ↔ aktif), status berkas (menunggu, terverifikasi, ditolak), dan hasil seleksi (Pending, Lolos, Gagal) |
| Use Case Testing | Black Box Testing | Menguji alur utama dan alur alternatif setiap use case pada [Matriks dan Use Case](../Matriks%20dan%20Use%20Case/Matriks%20dan%20Use%20Case.md), dari awal sampai akhir per role |
| Basis Path Testing | White Box Testing | Menguji setiap jalur independen pada fungsi inti fitur utama |

EP biasanya perlu dilengkapi teknik lain seperti BVA, supaya nilai batas tidak terlewat. Decision Table Testing tidak dipakai sebagai teknik tersendiri, karena kombinasi kondisinya (misalnya syarat Terima pada Verifikasi Pendaftar) sudah tercakup dalam Use Case Testing dan EP.

#### 5.3 Black-box Testing

Langkah perancangan dan pelaksanaan:

1. Turunkan Test Scenario dari use case tiap role (Use Case Testing) dan dari flowchart fitur utama.
2. Untuk setiap skenario, tentukan kelas ekuivalensi dan nilai batas input (EP dan BVA), serta perubahan status yang terlibat (State Transition Testing).
3. Tulis test case dengan kolom: ID Pengujian, Deskripsi Pengujian, Lingkup Pengujian, Teknik Pengujian, Input Data, Type (Positif/Negatif), Prosedur Pengujian, Hasil yang Diharapkan, Kriteria Penerimaan, Hasil Pengujian Aktual, dan Status. Mengikuti pendekatan pada bagian 1, Prosedur Pengujian ditulis sebagai urutan aksi bernama beserta datanya, bukan kalimat bebas. Skenario login dengan password salah, misalnya, cukup ditulis dua langkah: Login memakai email terdaftar dan password yang salah, lalu periksa apakah pesan "Email atau password salah!" muncul.
4. Jalankan test case di website, catat hasil aktual dan status (Pass, Fail, Blocked), lalu simpan bukti tangkapan layar.
5. Laporkan setiap kegagalan sebagai defect.

Contoh nilai batas (Boundary Value Analysis) yang akan diuji:

| Input | Aturan di Sistem | Nilai Uji |
|---|---|---|
| Panjang password (registrasi dan reset) | Minimal 6 karakter | 5 (ditolak), 6 (diterima), 7 (diterima) |
| Ukuran berkas | Ditolak jika lebih dari 2.000.000 byte | 1.999.999 byte (diterima), 2.000.000 byte (diterima), 2.000.001 byte (ditolak) |

Catatan: website menampilkan batas "2 MB", sedangkan source code memakai angka 2.000.000 byte. Karena itu nilai batas diambil dari angka di source code.

Contoh status (State Transition Testing) yang akan diuji:

| Objek | Status Awal | Pemicu | Status Akhir |
|---|---|---|---|
| Akun | Belum aktif | Klik link aktivasi di email | Aktif |
| Status berkas | Menunggu verifikasi | Admin menandai valid / menandai tolak | Terverifikasi / Ditolak |
| Status pendaftar | Menunggu verifikasi | Admin memilih Terima / Tolak | Diterima / Ditolak |
| Hasil seleksi | Pending | Admin menetapkan Lolos / Gagal pada menu Pengumuman | Lolos / Gagal |

Transisi yang tidak diizinkan (misalnya Terima tanpa semua berkas wajib terverifikasi, atau mengubah berkas yang sudah Terverifikasi) diuji sebagai skenario negatif.

#### 5.4 White-box Testing

Langkah pengujian Basis Path Testing:

1. Buat flowchart dari potongan kode yang diuji.
2. Ubah flowchart menjadi flow graph (node dan edge).
3. Hitung Cyclomatic Complexity V(G) dengan tiga rumus: jumlah Region, E − N + 2, dan P + 1. Ketiganya harus menghasilkan angka yang sama.
4. Tentukan jalur independen sebanyak V(G).
5. Buat satu test case untuk setiap jalur, lalu jalankan dengan memasukkan data lewat website sehingga jalur tersebut dilalui.

Unit yang diuji:

| ID | Unit | Lokasi di Source Code |
|---|---|---|
| WB-01 | Pemeriksaan login | `auth/login.php` (proses POST) |
| WB-02 | Pemeriksaan registrasi | `auth/register.php` (proses POST) |
| WB-03 | Pemeriksaan upload berkas | `user/upload-berkas.php` (proses POST) |
| WB-04 | Aksi Terima dan Tolak pendaftar | `admin/verifikasi.php` (proses `action`) |
| WB-05 | Penyimpanan hasil seleksi | `admin/pengumuman.php` (proses POST) |

### 6. Test Environment

| **Komponen** | **Keterangan** |
|---|---|
| Sistem Operasi | Windows 11 |
| Browser | Google Chrome versi [ISI] |
| Aplikasi | PPDB SLB Sana Dharma, commit `70a38d9` |
| Server | Railway (container Docker, PHP 8.2, Apache) |
| Basis Data | MySQL (Railway) |
| Email | Kotak masuk email milik penguji untuk akun uji |
| Source Code | Salinan repository untuk White-box Testing |

### 7. Test Tools

| **Tools** | **Kegunaan** |
|---|---|
| Google Chrome | Menjalankan Manual Testing |
| Visual Studio Code | Membaca source code untuk White-box Testing |
| Snipping Tool / tangkapan layar | Mengambil bukti pengujian |
| Microsoft Excel | Menyusun Test Case dan mencatat hasil eksekusi |
| GitHub | Menyimpan dokumentasi pengujian |

### 8. Test Data

1. Semua pengujian memakai akun uji (dummy) dengan nama yang mudah dikenali, misalnya `QA Kelompok5 01`, dan email milik anggota tim.
2. Aksi admin (Terima, Tolak, dan menetapkan hasil seleksi) hanya dilakukan pada akun uji. Setiap aksi tersebut mengirim email ke pendaftar, sehingga tidak boleh dilakukan pada data pendaftar lain.
3. Berkas uji disiapkan dalam format JPG, PNG, PDF, dan satu format tidak valid (misalnya DOCX), serta berkas dengan ukuran sesuai nilai batas di bagian 5.3.
4. Berkas uji tidak boleh berisi dokumen pribadi asli (akta, KK, KTP). Gunakan dokumen contoh.
5. Setelah pengujian selesai, akun dan data uji dihapus atau dilaporkan ke pengelola website untuk dihapus.

### 9. Test Roles and Responsibilities

| **Pelaksana** | **Tanggung Jawab** |
|---|---|
| Gunawan Wibisono | Test Lead. Menyusun Test Plan, System Overview, dan Flowchart. Menyusun Test Case dan menjalankan Manual Testing untuk fitur Autentikasi (Registrasi, Login & Logout, Lupa Password), beserta bukti pengujian. Menjalankan White-box Testing. |
| Jumigih Andrian | Menyusun Test Case dan menjalankan Manual Testing untuk fitur User bagian pendaftaran (Beranda, Formulir, Upload Berkas, Pengumuman, Daftar Ulang), beserta bukti pengujian. |
| Lintang Nur Hafsari | Menyusun Test Case dan menjalankan Manual Testing untuk fitur Admin (Dashboard, Verifikasi Pendaftar, Kelola Pengumuman), beserta bukti pengujian. Menyusun Bug Report dan Test Report. |

Ketiga anggota berperan sebagai tester. Defect yang ditemukan dilaporkan ke pengelola website melalui Bug Report.

### 10. Test Schedule

| **Tahapan** | **Aktivitas** | **Pelaksanaan** |
| ----------- | ------------- | --------------- |
| 1 | Penyusunan System Overview, Use Case, dan Flowchart | Minggu 1 |
| 2 | Penyusunan Test Plan | Minggu 2 |
| 3 | Penyusunan Test Scenario | Minggu 2 |
| 4 | Penyusunan Test Case (Black-box dan White-box) | Minggu 2 |
| 5 | Pelaksanaan Manual Testing (Black-box) | Minggu 3 |
| 6 | Pelaksanaan White-box Testing | Minggu 3 |
| 7 | Pelaporan defect dan pengujian ulang (retest) | Minggu 3 |
| 8 | Analisis hasil dan penyusunan Test Report | Minggu 4 |


### 11. Entry and Exit Criteria

**11.1 Entry Criteria**

Pengujian dapat dimulai apabila:

1. Website dapat diakses di URL pengujian.
2. Nomor commit versi yang diuji sudah dicatat.
3. Akun uji pendaftar dan akses akun admin sudah tersedia.
4. Data uji dan berkas uji sudah disiapkan.
5. Test Scenario dan Test Case sudah disusun dan ditinjau tim.
6. Source code tersedia untuk White-box Testing.

**11.2 Exit Criteria**

Pengujian dinyatakan selesai apabila:

1. Seluruh test case yang direncanakan telah dieksekusi, atau alasan tidak dieksekusi telah dicatat.
2. Hasil Pass, Fail, dan Blocked telah dicatat beserta bukti.
3. Semua defect telah dilaporkan dengan tingkat severity dan priority.
4. Defect yang sudah diperbaiki telah diuji ulang.
5. Seluruh jalur independen pada unit White-box telah diuji.
6. Test Report telah disusun.

**11.3 Kriteria Penghentian Sementara dan Pelanjutan**

| Kondisi | Tindakan |
|---|---|
| Website tidak dapat diakses atau server error | Pengujian dihentikan sementara, dicatat waktunya, dan dilanjutkan setelah website kembali normal |
| Ditemukan defect Severity 1 yang menghalangi alur utama | Test case yang bergantung pada alur tersebut ditandai Blocked dan dilanjutkan setelah defect diperbaiki |
| Ada perubahan kode di server | Commit baru dicatat dan test case terdampak diuji ulang |

### 12. Defect Management

Setiap defect dicatat dengan ID, judul, langkah reproduksi, hasil yang diharapkan, hasil aktual, bukti, severity, priority, dan status.

**Severity**:

| Tingkat | Arti |
|---|---|
| Critical | Sistem tidak dapat digunakan sama sekali |
| Major | Fitur utama tidak berfungsi |
| Moderate | Fitur tertentu mengalami gangguan, tetapi fungsionalitas inti tetap berjalan |
| Minor | Masalah kecil yang tidak memengaruhi penggunaan utama |
| Trivial | Kesalahan kosmetik, misalnya salah ketik atau warna |

**Priority**: ditentukan dari dampak defect ke pengguna dan urgensi perbaikan, bukan dari severity saja. Dipakai 3 tingkat: **Tinggi** (menghalangi alur utama, harus segera diperbaiki), **Sedang** (mengganggu tetapi masih ada jalan lain), **Rendah** (tidak mendesak). Defect Severity Critical atau Major biasanya berprioritas Tinggi, tapi penguji tetap menilai dampaknya per kasus.

**Status defect** mengikuti Bug Life Cycle: New → Assigned → Open → Fixed → Test → Verified → Closed, atau Reopen kalau masih gagal saat diuji ulang.

### 13. Risks and Mitigation

| **Jenis** | **Risiko** | **Mitigasi** |
|---|---|---|
| Produk | Email (aktivasi, reset password, verifikasi) gagal terkirim sehingga alur tidak bisa dilanjutkan | Catat sebagai defect. Tandai test case lanjutan sebagai Blocked. |
| Produk | Aksi admin mengirim email ke pendaftar sungguhan | Aksi admin hanya dilakukan pada akun uji (bagian 8) |
| Produk | Perbedaan nilai status antara menu Verifikasi dan Pengumuman (lihat catatan di System Overview) | Diuji khusus pada skenario Tolak pendaftar |
| Proyek | Website down saat jadwal pengujian | Jadwalkan ulang dan catat di log pengujian |
| Proyek | Kode berubah di tengah masa pengujian | Catat commit dan lakukan uji ulang pada test case terdampak |
| Proyek | Waktu pengerjaan terbatas | Prioritaskan test case Priority tinggi lebih dulu |

### 14. Test Deliverables

| No | Dokumen | Keterangan |
|---|---|---|
| 1 | Test Plan | Dokumen ini |
| 2 | Test Scenario | Daftar skenario pengujian per role |
| 3 | Test Case (Black-box dan White-box) | Rincian data uji dan prosedur pengujian per skenario |
| 4 | Test Execution Record dan Test Evidence | Hasil eksekusi beserta tangkapan layar |
| 5 | Bug Report | Laporan defect yang ditemukan |
| 6 | Test Report | Ringkasan dan evaluasi hasil pengujian |

Seluruh dokumen dan hasil pengujian disimpan di repository GitHub kelompok.

### 15. Referensi

1. ISO/IEC/IEEE 29119-5:2024. *Software and systems engineering — Software testing — Part 5: Keyword-driven testing*.
2. Modul Testing dan QA Perangkat Lunak, Program Studi Teknik Informatika, Universitas Pamulang (Ahmad Fauzi, S.Kom., M.Kom.).
