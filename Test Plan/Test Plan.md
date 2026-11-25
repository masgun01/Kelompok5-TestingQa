# TEST PLAN

## PPDB SLB Sana Dharma

| Informasi | Keterangan |
|---|---|
| ID Dokumen | TP-PPDB-01 |
| Versi | 0.2 (draft) |
| Disusun oleh | Kelompok 5 – 07TPLE002 |

### 1. Pendahuluan

Dokumen Test Plan ini menjadi pedoman pelaksanaan pengujian pada website PPDB SLB Sana Dharma. Pengujian dilakukan untuk memastikan fitur utama berjalan sesuai fungsinya, mulai dari pembuatan akun sampai daftar ulang di sisi user, serta verifikasi dan pengumuman hasil seleksi di sisi admin.

Pengujian mengikuti seluruh materi mata kuliah Testing dan QA Perangkat Lunak: strategi White-box dan Black-box (termasuk Gray-box), pengujian unit, integrasi, fungsional dan non-fungsional, sistem, User Acceptance Testing (UAT), otomatisasi, regresi, API, performa, dan keamanan, ditutup dengan manajemen bug dan dokumentasi. Pengujian yang berisiko mengganggu website yang sedang berjalan dilakukan dalam skala kecil dan tidak merusak, batasannya dijelaskan pada bagian 3.3 dan 5.5 sampai 5.13.

Standar acuan yang dipakai adalah ISO/IEC/IEEE 29119-5:2024
yaitu bagian kelima dari rangkaian standar pengujian perangkat lunak ISO/IEC/IEEE 29119 yang membahas *keyword-driven testing*.
Inti pendekatannya ada pada cara menulis test case: aksi pengujian yang berulang diberi nama baku beserta parameternya, lalu test case disusun dari rangkaian nama aksi itu.
Nama yang dipilih mengikuti istilah pengguna sistem, bukan nama elemen halaman, sehingga prosedurnya tidak perlu ditulis ulang setiap kali tata letak halaman berubah. Pasal 5.1 standar tersebut menyatakan pendekatan ini tetap dapat dipakai walaupun automasi tidak direncanakan, dan hal itulah yang menjadi dasar pelaksanaan pengujian manual pada proyek ini. Penyebutan standar di sini bersifat acuan penyusunan dokumen, bukan klaim pemenuhan persyaratan kesesuaian (*conformance*) pada Pasal 7 yang memang ditujukan bagi penyedia kerangka kerja pengujian. Automation yang dipakai (bagian 5.9) terbatas pada skenario terpilih dan tidak mengubah sifat acuan ini.

### 2. Test Objectives

Tujuan pengujian adalah:

1. Memastikan 11 fitur utama berjalan sesuai fungsi yang ditampilkan di website dan yang tertulis di source code.
2. Memastikan setiap role (User dan Admin) hanya dapat mengakses fitur sesuai haknya.
3. Memastikan validasi input menolak data yang tidak valid dan menerima data yang valid, termasuk pada nilai batas.
4. Memeriksa alur logika program pada fungsi inti fitur utama melalui Basis Path Testing.
5. Mengidentifikasi dan mendokumentasikan kesalahan (defect) beserta bukti.
6. Mendokumentasikan hasil pengujian sebagai dasar evaluasi kualitas sistem.
7. Memastikan modul-modul yang saling terhubung bekerja benar sebagai satu alur dari pendaftaran sampai daftar ulang (Integration Testing).
8. Memeriksa aspek non-fungsional yang relevan: kegunaan, kompatibilitas, performa dasar, dan keamanan dasar.
9. Memastikan website dapat diterima calon pengguna dan pengelola lewat User Acceptance Testing.
10. Memastikan perbaikan defect tidak merusak fitur lain lewat Regression Testing, dan menjalankan sebagian skenario secara otomatis.

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
- Pengujian alur logika pada fungsi inti fitur utama berdasarkan source code (daftar unit ada di bagian 5.4), ditambah Statement, Branch, dan Condition Coverage, Loop Testing, serta Data Flow Testing.

**C. Pengujian lain sesuai materi** (rincian di bagian 5.5 sampai 5.13)
- Integration Testing: alur antar modul dari registrasi sampai daftar ulang.
- Non-functional Testing: kegunaan, kompatibilitas browser dan ukuran layar, aksesibilitas dasar.
- Performance Testing terbatas: waktu muat halaman dan Load Testing skala kecil.
- Security Testing terbatas: pemeriksaan pasif, peninjauan kode, dan uji hak akses.
- API Testing pada endpoint yang mengembalikan JSON.
- Automation Testing pada tujuh skenario terpilih.
- Regression Testing, Smoke dan Sanity Testing, serta Exploratory Testing.
- User Acceptance Testing (UAT) oleh calon pengguna di luar tim.

#### 3.3 Out of Scope

Pengujian tidak mencakup:

| No | Bagian | Alasan |
|---|---|---|
| 1 | Menu Laporan, Data User, dan ekspor data (admin) | Bukan fitur utama yang disepakati tim |
| 2 | Halaman landing (beranda publik, info, alur, FAQ) | Hanya berisi informasi statis |
| 3 | Stress, Spike, Endurance, dan Volume Testing pada website yang berjalan | Memberi beban buatan besar berisiko mengganggu layanan. Rancangannya ditulis di bagian 5.7 tetapi tidak dijalankan. Load Testing hanya skala kecil. |
| 4 | Penetration Testing aktif (eksploitasi kerentanan, scanner aktif, serangan menebak password skala besar) | Berisiko merusak data atau layanan dan memerlukan izin tertulis. Yang dilakukan hanya pemeriksaan pasif dan peninjauan kode (bagian 5.8). |
| 5 | Compatibility Testing di semua browser dan perangkat | Dibatasi pada tiga browser dan tiga ukuran layar (bagian 5.6) |
| 6 | Isi dan tampilan email secara detail | Yang diperiksa hanya apakah email terkirim dan link di dalamnya berfungsi |
| 7 | Automation untuk seluruh test case | Hanya tujuh skenario terpilih yang diotomasi (bagian 5.9). Test case lain tetap dijalankan manual karena pengujian ini dilakukan sekali untuk tugas |

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
| Test level | Unit (white-box pada lima unit kode), Integration, System, dan Acceptance (UAT) | Keempat level pada hierarki pengujian dipakai. Unit diuji lewat Basis Path karena logika kode bercampur dalam satu berkas, tanpa fungsi terpisah yang bisa dipanggil sendiri. Integration, System, dan Acceptance dijalankan pada website yang sudah berjalan |
| Test type | Functional dan Non-functional (kegunaan, kompatibilitas, performa, keamanan), Regression, Smoke dan Sanity, Exploratory, API | Fitur utama diuji lebih dulu secara fungsional, lalu aspek non-fungsional dan jenis pengujian lain |
| Pelaksanaan | Manual terskrip, dan otomatis untuk tujuh skenario terpilih | Test case ditulis sebelum dijalankan. Sebagian besar dieksekusi lewat browser, sebagian kecil lewat skrip (bagian 5.9) |

#### 5.2 Teknik Perancangan Pengujian

Ada lima teknik Black Box Testing yang diajarkan: Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, State Transition Testing, dan Use Case Testing. Kelimanya dipakai pada fitur utama PPDB SLB Sana Dharma, ditambah Basis Path untuk White-box dan pengujian Gray-box:

| Teknik | Jenis | Dipakai Untuk |
|---|---|---|
| Equivalence Partitioning (EP) | Black Box Testing | Membagi input (email, password, jenis berkas, jenjang) ke kelas valid dan tidak valid |
| Boundary Value Analysis (BVA) | Black Box Testing | Menguji nilai batas, yaitu panjang password (5, 6, 7 karakter) dan ukuran berkas (sekitar batas 2 MB) |
| State Transition Testing | Black Box Testing | Menguji perubahan status akun (belum aktif ↔ aktif), status berkas (menunggu, terverifikasi, ditolak), dan hasil seleksi (Pending, Lolos, Gagal) |
| Use Case Testing | Black Box Testing | Menguji alur utama dan alur alternatif setiap use case pada [Matriks dan Use Case](../Matriks%20dan%20Use%20Case/Matriks%20dan%20Use%20Case.md), dari awal sampai akhir per role |
| Decision Table Testing | Black Box Testing | Menguji kombinasi kondisi yang menentukan hasil: hasil login, aktif tidaknya tombol Daftar Sekarang, dan syarat Terima pada Verifikasi (lihat [Decision Table](../Test%20Case/Decision%20Table.md)) |
| Basis Path Testing | White Box Testing | Menguji setiap jalur independen pada fungsi inti fitur utama |
| Gray Box Testing | Gray Box Testing | Menguji lewat tampilan website dengan memanfaatkan pengetahuan sebagian tentang kode, misalnya mengubah nilai input lewat DevTools untuk menguji pemeriksaan di server |

EP biasanya perlu dilengkapi teknik lain seperti BVA, supaya nilai batas tidak terlewat.

#### 5.3 Black-box Testing

Langkah perancangan dan pelaksanaan:

1. Turunkan Test Scenario dari use case tiap role (Use Case Testing) dan dari flowchart fitur utama.
2. Untuk setiap skenario, tentukan kelas ekuivalensi dan nilai batas input (EP dan BVA), serta perubahan status yang terlibat (State Transition Testing).
3. Tulis test case dengan kolom: ID Pengujian, Deskripsi Pengujian, Lingkup Pengujian, Teknik Pengujian, Input Data, Type (Positif/Negatif), Prosedur Pengujian, Hasil yang Diharapkan, Kriteria Penerimaan, Prioritas, Lingkungan, Hasil Pengujian Aktual, Status, Bukti, dan Catatan. Mengikuti pendekatan pada bagian 1, Prosedur Pengujian ditulis sebagai urutan aksi bernama beserta datanya, bukan kalimat bebas. Skenario login dengan password salah, misalnya, cukup ditulis dua langkah: Login memakai email terdaftar dan password yang salah, lalu periksa apakah pesan "Email atau password salah!" muncul.
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

Selain Basis Path, dipakai teknik white-box lain: Statement Coverage, Branch Coverage, Condition Coverage, Loop Testing, dan Data Flow Testing. Hitungan dan data ujinya ada di [Teknik Tambahan](../White-box%20Testing/Teknik%20Tambahan.md). Statement Coverage dan Branch Coverage dihitung dari jalur yang bisa dijalankan, dan angkanya dilaporkan di Test Report.

#### 5.5 Integration Testing

Pendekatan yang dipakai adalah incremental, bukan Big Bang. Modul diuji bersama modul sebelumnya mengikuti alur data: Autentikasi, lalu Formulir dan Upload Berkas, lalu Verifikasi Admin, lalu Pengumuman, lalu Daftar Ulang. Semua modul sudah ada dan berjalan, sehingga tidak perlu stub atau driver. Yang diuji adalah serah terima data dan status antarmodul: akun dari registrasi dipakai login, berkas dari Upload muncul di Verifikasi, aksi Terima dan Tolak mengubah Pengumuman dan Dashboard, dan hasil Pengumuman menentukan akses ke Daftar Ulang. Skenarionya TS-IN-01 sampai TS-IN-06.

#### 5.6 Non-functional Testing

| Aspek | Cara | Batas |
|---|---|---|
| Kegunaan (usability) | Penguji menilai kejelasan pesan, label, dan alur memakai daftar periksa | Halaman Registrasi, Login, Formulir, Upload Berkas, dan Verifikasi |
| Kompatibilitas | Menjalankan halaman kunci di tiga browser: Chrome, Edge, Firefox | Tiga browser dan tiga lebar layar (360, 768, 1366 piksel, memakai mode perangkat di DevTools) |
| Aksesibilitas dasar | Mengisi form hanya dengan keyboard, memeriksa label dan kontras | Karena pengguna website ini keluarga peserta didik berkebutuhan khusus |

Skenarionya TS-NF-01 sampai TS-NF-05.

#### 5.7 Performance Testing

Website berjalan di server yang dipakai pengguna, sehingga pengujian performa dibatasi. Kriteria di bawah ditetapkan tim karena website tidak punya dokumen SLA.

| Jenis | Rancangan | Status |
|---|---|---|
| Waktu muat halaman | Ukur waktu muat Login, Registrasi, Beranda User, dan Dashboard Admin dengan Lighthouse dan tab Network. Kriteria tim: selesai dimuat dalam 3 detik pada koneksi normal | Dijalankan |
| Waktu proses upload | Unggah berkas 2.000.000 byte dan catat waktu sampai pesan hasil muncul. Kriteria tim: 10 detik | Dijalankan |
| Load Testing skala kecil | 10 pengguna virtual membuka halaman publik (Login dan Registrasi, hanya GET) selama 60 detik dengan k6. Catat waktu respons p95 dan jumlah error. Kriteria tim: tidak ada error, p95 di bawah 3 detik. Dijalankan hanya setelah pemilik website mengizinkan, di luar jam pendaftaran ramai, dan dihentikan jika error muncul | Dijalankan bersyarat |
| Stress Testing | Menaikkan beban bertahap sampai sistem gagal untuk mencari batas kapasitas | Dirancang, tidak dijalankan |
| Spike Testing | Lonjakan pengguna mendadak, misalnya saat pengumuman hasil dibuka | Dirancang, tidak dijalankan |
| Endurance Testing | Beban sedang selama berjam-jam untuk melihat kebocoran memori | Dirancang, tidak dijalankan |
| Volume Testing | Basis data diisi data dalam jumlah besar | Dirancang, tidak dijalankan |

Empat jenis terakhir akan dijalankan pada lingkungan uji terpisah (staging), bukan pada website yang dipakai. Skenario yang dijalankan: TS-PF-01 sampai TS-PF-03.

#### 5.8 Security Testing

Strategi yang diambil dari materi dan relevan: identifikasi kerentanan secara pasif, peninjauan kode (code review), peninjauan konfigurasi, dan penilaian risiko. Penetration Testing tidak dilakukan.

Aturan pelaksanaan:
1. Hanya memakai akun uji milik tim.
2. Tidak mengeksploitasi kerentanan yang ditemukan dan tidak membuka data pendaftar lain.
3. Input yang dipakai hanya karakter khusus biasa (misalnya tanda kutip dan tag HTML sederhana), bukan muatan serangan.
4. Temuan keamanan dilaporkan ke pengelola website secara pribadi. Di repository publik hanya ditulis ringkas, tanpa langkah eksploitasi dan tanpa kredensial.

Skenarionya TS-SC-01 sampai TS-SC-08.

#### 5.9 Automation Testing

Alat: Playwright. Skrip disimpan di folder [Automation Testing](../Automation%20Testing/). Skenario dipilih karena berulang, tidak membuat data baru, dan tidak mengirim email, sehingga aman dijalankan berkali-kali:

| ID | Skenario | Mengotomasi |
|---|---|---|
| AT-01 | Login dengan password salah menampilkan pesan penolakan | TC-AU-19 |
| AT-02 | Login dengan form kosong ditolak | TC-AU-21 |
| AT-03 | Halaman admin dan user tanpa login diarahkan ke login | TC-AU-26 dan TC-AU-25 |
| AT-04 | Tombol Daftar Sekarang aktif atau nonaktif sesuai kombinasi kondisi (tidak mengirim form) | DT-02 |
| AT-05 | Lupa password dengan email tidak terdaftar menampilkan pesan | TC-AU-29 |
| AT-06 | Halaman publik dan halaman autentikasi termuat tanpa error | TC-SM-01 |
| AT-07 | Waktu muat halaman publik dicatat dan dibandingkan dengan kriteria | TC-PF-01 |

Hasil skrip dicatat di Test Execution Record bersama hasil manual, lalu dibandingkan: waktu eksekusi, konsistensi hasil, dan kesulitan perawatan skrip.

#### 5.10 Regression Testing

Jenis yang dipakai: Priority-based dan Selective Regression. Regression Suite berisi semua test case berprioritas High, ditambah test case pada fitur yang terkait defect yang diperbaiki.

1. Run 1 (baseline) dijalankan saat eksekusi pertama.
2. Setiap defect yang diperbaiki di-retest, lalu Regression Suite dijalankan lagi (Run 2).
3. Jika tidak ada perubahan kode selama pengujian, Run 2 memakai skrip otomatis (bagian 5.9) dan dicatat bahwa tidak ada perubahan.
4. Hasil Run 1 dan Run 2 dibandingkan di [Regression Record](../Regression/Regression%20Record.md).

Skenarionya TS-RG-01 dan TS-RG-02.

#### 5.11 User Acceptance Testing (UAT)

| Unsur | Isi |
|---|---|
| Tujuan | Memastikan website dapat dipakai calon pengguna dan pengelola untuk menyelesaikan tugas utamanya |
| Jenis | Alpha Testing oleh tim (seluruh pengujian di dokumen ini), Beta Testing oleh responden di luar tim |
| Responden | Tiga orang yang berperan sebagai calon orang tua atau wali, dan satu orang yang berperan sebagai petugas admin (pengelola sekolah jika bersedia) |
| Ruang lingkup | Tugas user: buat akun, aktivasi, isi formulir, unggah berkas, lihat pengumuman. Tugas admin: verifikasi satu pendaftar uji, Terima, tetapkan hasil seleksi |
| Kriteria penerimaan | Disepakati tim, karena tidak ada dokumen kebutuhan: (1) kelima tugas user selesai tanpa bantuan oleh minimal dua dari tiga responden, (2) tugas admin selesai tanpa bantuan, (3) tidak ada defect Critical atau Major yang masih terbuka, (4) skor kepuasan rata-rata minimal 4 dari 5 |
| Lingkungan | Website yang berjalan, akun uji, berkas contoh |
| Pelaporan | Formulir UAT diisi responden dan ditandatangani, hasilnya dirangkum di [UAT](../UAT/UAT%20Plan%20dan%20Hasil.md) |
| Kriteria kelulusan | Keempat kriteria penerimaan terpenuhi. Jika tidak, alasannya ditulis dan menjadi rekomendasi |

Skenarionya TS-UA-01 sampai TS-UA-03.

#### 5.12 Smoke, Sanity, dan Exploratory Testing

- **Smoke Testing**: pemeriksaan cepat bahwa 11 fitur utama bisa dibuka tanpa error. Dijalankan di awal setiap sesi pengujian dan setiap kali commit berubah (TS-SM-01).
- **Sanity Testing**: pemeriksaan terarah pada fitur yang baru diperbaiki, sebelum Regression Suite dijalankan (TS-SM-02).
- **Exploratory Testing**: tiga sesi masing-masing 30 menit dengan piagam (charter) tertulis. Tiap sesi dijalankan oleh anggota yang bukan pemilik fitur tersebut, supaya sudut pandangnya berbeda (TS-EX-01 sampai TS-EX-03).

#### 5.13 API Testing

Website tidak memiliki REST API terpisah. Endpoint yang mengembalikan JSON dan dipanggil dari halaman lewat AJAX diuji sebagai API:

| ID | Endpoint | Metode | Fungsi |
|---|---|---|---|
| API-1 | `admin/verifikasi.php?action=terima` dan `action=tolak` | GET dengan header `X-Requested-With: XMLHttpRequest` | Terima atau tolak pendaftar |
| API-2 | `admin/detail-pendaftar.php` dengan parameter `ajax_verifikasi_dokumen` | POST | Simpan status verifikasi satu dokumen |

Alat: Postman, dengan cookie sesi admin akun uji. Yang diperiksa: kode status HTTP, header Content-Type, struktur dan nilai JSON, penanganan error (parameter salah atau kurang), dan hak akses (pemanggilan tanpa sesi admin). Skenarionya TS-AP-01 sampai TS-AP-06.

### 6. Test Environment

| **Komponen** | **Keterangan** |
|---|---|
| Sistem Operasi | Windows 11 |
| Browser | Google Chrome / Chromium versi 131.0.6778.33 (utama), Microsoft Edge dan Mozilla Firefox (untuk Compatibility Testing) |
| Aplikasi | PPDB SLB Sana Dharma, commit `70a38d9` |
| Server | Railway (container Docker, PHP 8.2, Apache) |
| Basis Data | MySQL (Railway) |
| Email | Kotak masuk email milik penguji untuk akun uji |
| Source Code | Salinan repository untuk White-box Testing |
| Alat bantu | Node.js untuk Playwright, Postman, k6 |

### 7. Test Tools

| **Tools** | **Kegunaan** |
|---|---|
| Google Chrome | Menjalankan Manual Testing |
| Visual Studio Code | Membaca source code untuk White-box Testing |
| Snipping Tool / tangkapan layar | Mengambil bukti pengujian |
| Microsoft Excel | Menyusun Test Case dan mencatat hasil eksekusi |
| GitHub | Menyimpan dokumentasi pengujian |
| GitHub Issues | Mengelola bug dan siklus hidupnya |
| Playwright | Automation Testing (bagian 5.9) |
| Postman | API Testing (bagian 5.13) |
| Lighthouse (di Chrome DevTools) | Mengukur waktu muat halaman dan aksesibilitas dasar |
| k6 | Load Testing skala kecil (bagian 5.7) |
| Chrome DevTools | Memeriksa cookie, header, jaringan, dan mengubah nilai input untuk pengujian Gray-box |
| Graphviz | Menggambar flow graph |

### 8. Test Data

1. Semua pengujian memakai akun uji (dummy) dengan nama yang mudah dikenali, misalnya `QA Kelompok5 01`, dan email milik anggota tim.
2. Aksi admin (Terima, Tolak, dan menetapkan hasil seleksi) hanya dilakukan pada akun uji. Setiap aksi tersebut mengirim email ke pendaftar, sehingga tidak boleh dilakukan pada data pendaftar lain.
3. Berkas uji disiapkan dalam format JPG, PNG, PDF, dan satu format tidak valid (misalnya DOCX), serta berkas dengan ukuran sesuai nilai batas di bagian 5.3.
4. Berkas uji tidak boleh berisi dokumen pribadi asli (akta, KK, KTP). Gunakan dokumen contoh.
5. Setelah pengujian selesai, akun dan data uji dihapus atau dilaporkan ke pengelola website untuk dihapus.

### 9. Test Roles and Responsibilities

| **Pelaksana** | **Tanggung Jawab** |
|---|---|
| Gunawan Wibisono | Test Lead. Menyusun Test Plan, System Overview, dan Flowchart. Menyusun Test Case dan menjalankan Manual Testing untuk fitur Autentikasi (Registrasi, Login & Logout, Lupa Password), beserta bukti pengujian. Menjalankan White-box Testing (Basis Path, Coverage, Data Flow). Menjalankan Smoke dan Sanity Testing, Security Testing terbatas, dan menyusun serta menjalankan skrip Automation. Menjalankan sesi Exploratory pada fitur pendaftaran. |
| Jumigih Andrian | Menyusun Test Case dan menjalankan Manual Testing untuk fitur User bagian pendaftaran (Beranda, Formulir, Upload Berkas, Pengumuman, Daftar Ulang), beserta bukti pengujian. Menjalankan Integration Testing bersama Lintang, Non-functional Testing (kegunaan, kompatibilitas, aksesibilitas), Loop Testing, mengoordinasikan UAT dengan responden, dan menjalankan sesi Exploratory pada fitur Verifikasi. |
| Lintang Nur Hafsari | Menyusun Test Case dan menjalankan Manual Testing untuk fitur Admin (Dashboard, Verifikasi Pendaftar, Kelola Pengumuman), beserta bukti pengujian. Menyusun Bug Report dan Test Report. Menjalankan API Testing, Performance Testing terbatas, dan Regression Testing, serta sesi Exploratory pada fitur Autentikasi. |

Ketiga anggota berperan sebagai tester. Defect yang ditemukan dilaporkan ke pengelola website melalui Bug Report.

### 10. Test Schedule

| **Tahapan** | **Aktivitas** | **Pelaksanaan** |
| ----------- | ------------- | --------------- |
| 1 | Penyusunan System Overview, Use Case, dan Flowchart | Minggu 1 |
| 2 | Penyusunan Test Plan, Test Scenario, dan Test Case (Black-box dan White-box) | Minggu 2 |
| 3 | Smoke Testing, lalu Manual Testing fungsional (Black-box) dan White-box Testing | Minggu 3 |
| 4 | Integration Testing, Non-functional Testing, API Testing, Security Testing terbatas, dan Exploratory Testing | Minggu 4 |
| 5 | Performance Testing terbatas dan Automation Testing | Minggu 4 |
| 6 | Pelaporan defect, retest, Sanity Testing, dan Regression Testing (Run 1 dan Run 2) | Minggu 5 |
| 7 | UAT oleh responden | Minggu 5 |
| 8 | Analisis hasil, Test Report, dan Test Closure | Minggu 6 |

### 11. Entry and Exit Criteria

**11.1 Entry Criteria**

Pengujian dapat dimulai apabila:

1. Website dapat diakses di URL pengujian.
2. Nomor commit versi yang diuji sudah dicatat.
3. Akun uji pendaftar dan akses akun admin sudah tersedia.
4. Data uji dan berkas uji sudah disiapkan.
5. Test Scenario dan Test Case sudah disusun dan ditinjau tim.
6. Source code tersedia untuk White-box Testing.
7. Izin pemilik website sudah didapat sebelum Load Testing skala kecil dijalankan.
8. Responden UAT sudah dihubungi dan bersedia.

**11.2 Exit Criteria**

Pengujian dinyatakan selesai apabila:

1. Seluruh test case yang direncanakan telah dieksekusi, atau alasan tidak dieksekusi telah dicatat.
2. Hasil Pass, Fail, dan Blocked telah dicatat beserta bukti.
3. Semua defect telah dilaporkan dengan tingkat severity dan priority.
4. Defect yang sudah diperbaiki telah diuji ulang.
5. Seluruh jalur independen pada unit White-box telah diuji.
6. Test Report telah disusun.
7. Statement Coverage dan Branch Coverage aktual sudah dihitung dan dilaporkan.
8. Regression Run 1 dan Run 2 sudah dicatat.
9. Hasil UAT sudah dirangkum dan kriteria penerimaannya dievaluasi.
10. Test Closure sudah dilakukan: hasil diarsipkan di repository, akun dan data uji dihapus atau dilaporkan, dan pelajaran dari pengujian dicatat.

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

**Status defect** mengikuti Bug Life Cycle: New → Assigned → Open → Fixed → Test → Verified → Closed, atau Reopen kalau masih gagal saat diuji ulang. Status lain yang dipakai bila perlu: Duplicate, Deferred, Rejected, Not a Defect, Not Reproducible, dan Need More Information.

**Jenis bug** yang dicatat: Functional, Performance, UI/UX, Security, Compatibility, Regression, Logical, dan Data.

**Alat**: bug dikelola di GitHub Issues pada repository kelompok, memakai template di `.github/ISSUE_TEMPLATE/bug_report.md`. Severity, jenis bug, dan status dicatat sebagai label. Ringkasannya disalin ke folder [Bug Report](../Bug%20Report/).

### 13. Risks and Mitigation

| **Jenis** | **Risiko** | **Mitigasi** |
|---|---|---|
| Produk | Email (aktivasi, reset password, verifikasi) gagal terkirim sehingga alur tidak bisa dilanjutkan | Catat sebagai defect. Tandai test case lanjutan sebagai Blocked. |
| Produk | Aksi admin mengirim email ke pendaftar sungguhan | Aksi admin hanya dilakukan pada akun uji (bagian 8) |
| Produk | Perbedaan nilai status antara menu Verifikasi dan Pengumuman (lihat catatan di System Overview) | Diuji khusus pada skenario Tolak pendaftar |
| Proyek | Website down saat jadwal pengujian | Jadwalkan ulang dan catat di log pengujian |
| Proyek | Kode berubah di tengah masa pengujian | Catat commit dan lakukan uji ulang pada test case terdampak |
| Proyek | Waktu pengerjaan terbatas | Prioritaskan test case Priority tinggi lebih dulu |
| Produk | Load Testing mengganggu layanan | Hanya setelah izin pemilik, skala 10 pengguna virtual, di luar jam ramai, dihentikan jika ada error |
| Produk | Pemeriksaan keamanan mengubah atau membuka data pendaftar lain | Hanya akun uji, tanpa eksploitasi, temuan dilaporkan pribadi |
| Proyek | Responden UAT sulit ditemukan | Dihubungi sejak Minggu 4. Jika kurang dari tiga, jumlah responden dicatat apa adanya di laporan UAT |
| Proyek | Skrip otomatis gagal karena tampilan halaman berubah | Skrip memakai teks dan label yang terlihat pengguna, bukan nama elemen. Perbaikan skrip dicatat |

### 14. Test Deliverables

| No | Dokumen | Keterangan |
|---|---|---|
| 1 | Test Plan | Dokumen ini |
| 2 | Test Scenario | Daftar skenario pengujian |
| 3 | Test Case | Black-box, White-box, dan Decision Table, rincian data uji dan prosedur |
| 4 | Automation Test Script | Skrip Playwright, koleksi Postman, dan skrip k6 |
| 5 | Test Execution Record | Hasil eksekusi manual dan otomatis |
| 6 | Test Evidence | Tangkapan layar dan keluaran skrip |
| 7 | UAT Result and Report | Rencana, formulir, dan rangkuman hasil UAT |
| 8 | Regression Testing Record | Perbandingan Run 1 dan Run 2 |
| 9 | Bug Report | Laporan defect yang ditemukan |
| 10 | Test Report | Ringkasan, evaluasi, dan Test Closure |

Seluruh dokumen dan hasil pengujian disimpan di repository GitHub kelompok.

### 15. Referensi

1. ISO/IEC/IEEE 29119-5:2024. *Software and systems engineering — Software testing — Part 5: Keyword-driven testing*.
2. Modul Testing dan QA Perangkat Lunak, Program Studi Teknik Informatika, Universitas Pamulang (Ahmad Fauzi, S.Kom., M.Kom.).
3. Pemetaan seluruh materi ke dokumen pengujian ada di [Pemetaan Materi](../Pemetaan%20Materi.md).
