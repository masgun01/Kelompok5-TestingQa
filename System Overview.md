# System Overview – PPDB SLB Sana Dharma

## 1. Informasi Sistem

| Informasi | Keterangan |
|---|---|
| Nama Aplikasi | PPDB SLB Sana Dharma |
| Jenis Aplikasi | Sistem Informasi Penerimaan Peserta Didik Baru berbasis web |
| Website | https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/ |
| Versi yang Diuji | Commit `70a38d9` (21 November 2026) |
| Bahasa Pemrograman | PHP 8.2 (tanpa framework) |
| Basis Data | MySQL |
| Web Server | Apache (berjalan di dalam container Docker) |
| Hosting | Railway |
| Tujuan Dokumen | Memberikan gambaran umum sistem sebagai dasar aktivitas Software Testing dan Quality Assurance |

## 2. Pendahuluan

PPDB SLB Sana Dharma adalah website untuk menerima pendaftaran calon peserta didik baru di Sekolah Luar Biasa (SLB) Sana Dharma. Calon pendaftar membuat akun, mengisi formulir pendaftaran, mengunggah berkas, lalu melihat hasil seleksi dan melakukan daftar ulang. Admin sekolah memeriksa data dan berkas pendaftar, memutuskan keabsahan pendaftaran, dan mengumumkan hasil seleksi.

Dokumen ini disusun dari sudut pandang Software Quality Assurance (QA). Isinya dipakai untuk menentukan ruang lingkup pengujian, menyusun strategi pengujian, serta merancang test scenario dan test case. Informasi di dokumen ini diambil dari dua sumber: tampilan website yang sedang berjalan dan source code versi yang diuji.

## 3. Tujuan Aplikasi

Website ini dibuat untuk memindahkan proses pendaftaran siswa baru ke sistem daring. Aktivitas yang didukung:

- Pembuatan dan aktivasi akun pendaftar melalui email.
- Pengisian formulir pendaftaran bertahap (jenjang, data pribadi, surat keterangan, data orang tua).
- Unggah berkas persyaratan.
- Verifikasi data dan berkas oleh admin.
- Pengumuman hasil seleksi kepada pendaftar.
- Informasi daftar ulang bagi pendaftar yang lolos.

## 4. Gambaran Umum Fitur Utama

Fitur di bawah ini adalah fitur utama yang menjadi objek pengujian.

| No | Modul | Fitur | Deskripsi |
|---:|---|---|---|
| 1 | Autentikasi | Login | Masuk dengan email dan password. Sistem mengarahkan pengguna ke halaman sesuai role (admin atau pendaftar). |
| 2 | Autentikasi | Lupa Password | Mengirim link reset password ke email terdaftar. Link berlaku 1 jam. |
| 3 | Autentikasi | Registrasi Akun | Membuat akun pendaftar baru. Akun harus diaktifkan lewat link di email sebelum bisa dipakai login. |
| 4 | Admin | Dashboard | Menampilkan jumlah total pendaftar, menunggu verifikasi, diterima, ditolak, serta daftar pendaftar terbaru. |
| 5 | Admin | Verifikasi Pendaftar | Mencari dan menyaring pendaftar, melihat detail, memverifikasi tiap berkas, lalu menerima atau menolak pendaftar. |
| 6 | Admin | Kelola Pengumuman | Menetapkan hasil seleksi (Lolos, Gagal, atau Pending) beserta catatan untuk tiap pendaftar. |
| 7 | User | Beranda | Menampilkan kelengkapan data, progress pendaftaran, status pendaftaran, dan notifikasi. |
| 8 | User | Formulir Pendaftaran | Formulir 5 langkah: pilih jenjang, data pribadi, surat keterangan, data orang tua, dan menuju upload berkas. |
| 9 | User | Upload Berkas | Mengunggah berkas wajib dan berkas tambahan, serta melihat status verifikasi tiap berkas. |
| 10 | User | Pengumuman | Menampilkan hasil seleksi dan catatan dari sekolah. |
| 11 | User | Daftar Ulang | Menampilkan data pendaftar, berkas yang harus dibawa, dan informasi pembayaran. Hanya untuk pendaftar yang lolos. |

## 5. Pengguna Sistem

| Aktor | Gambaran Peran |
|---|---|
| User | Calon peserta didik (diwakili orang tua/wali). Sebelum login membuka halaman registrasi, login, dan lupa password; setelah login mengisi formulir, mengunggah berkas, melihat pengumuman, dan melakukan daftar ulang. |
| Admin | Panitia PPDB yang memverifikasi pendaftar dan mengumumkan hasil seleksi. |

## 6. Gambaran Teknologi dan Struktur Aplikasi

Struktur folder pada source code:

| Komponen | Lokasi | Fungsi Umum |
|---|---|---|
| Autentikasi | `auth/` | Login, registrasi, aktivasi akun, lupa password, reset password, logout |
| Halaman Admin | `admin/` | Dashboard, verifikasi, detail pendaftar, pengumuman, laporan, data user, ekspor |
| Halaman User | `user/` | Beranda, formulir, upload berkas, pengumuman, daftar ulang |
| Konfigurasi | `config/` | Koneksi basis data, pengiriman email, websocket |
| Komponen Bersama | `includes/` | Header, footer, navbar, notifikasi |
| Halaman Publik | `landing/` | Beranda publik, info, alur, FAQ |
| Aset | `assets/` | CSS, JavaScript, berkas unggahan |

Library pihak ketiga (dari `composer.json`): PHPMailer (pengiriman email), TCPDF (PDF), PhpSpreadsheet (ekspor Excel), dan Ratchet (websocket). Saat berjalan di Railway, email dikirim melalui API Brevo karena koneksi SMTP keluar diblokir oleh layanan hosting.

Tabel basis data utama:

| Tabel | Isi |
|---|---|
| `users` | Akun admin dan pendaftar |
| `profil_siswa` | Jenjang, data pribadi, dan status verifikasi pendaftar |
| `surat_keterangan` | Jenis surat keterangan dokter yang dimiliki |
| `data_ortu` | Data ayah, ibu, dan wali |
| `berkas` | Nama berkas yang diunggah dan status berkas keseluruhan |
| `berkas_verifikasi` | Status verifikasi tiap dokumen |
| `pengumuman` | Hasil seleksi dan catatan |

## 7. Alur Proses Program

Uraian di bawah ini adalah alur tingkat tinggi tiap fitur utama. Aturan validasi yang disebutkan sudah dicocokkan dengan source code versi yang diuji.

### 7.1 Proses Registrasi dan Aktivasi Akun

1. User membuka halaman Buat Akun Baru.
2. User mengisi nama lengkap, email, nomor HP, password, dan konfirmasi password.
3. Tombol Daftar Sekarang baru aktif jika semua field terisi, password minimal 6 karakter, konfirmasi password sama, dan kotak persetujuan Syarat dan Ketentuan dicentang.
4. Sistem memeriksa apakah email sudah terdaftar. Jika sudah, muncul pesan "Email sudah terdaftar!".
5. Jika email belum terdaftar, sistem menyimpan akun dengan status belum aktif dan mengirim link aktivasi ke email.
6. Pendaftar membuka link aktivasi. Sistem mengaktifkan akun dan mengarahkan ke halaman login.

### 7.2 Proses Login dan Logout

1. Pengguna membuka halaman login, lalu memasukkan email dan password.
2. Sistem mencari akun berdasarkan email dan mencocokkan password.
3. Jika email tidak ditemukan atau password salah, muncul pesan "Email atau password salah!".
4. Jika password benar tetapi akun belum diaktivasi, muncul pesan bahwa akun belum diaktivasi.
5. Jika berhasil, admin diarahkan ke Dashboard Admin dan pendaftar diarahkan ke Beranda.
6. Saat memilih Logout, sesi diakhiri dan pengguna kembali ke halaman login.

Halaman admin memeriksa sesi login dan role admin. Halaman pendaftar memeriksa sesi login. Pengguna yang tidak memenuhi syarat tersebut diarahkan ke halaman login.

### 7.3 Proses Lupa Password dan Reset Password

1. Pengguna membuka halaman Lupa Password dan memasukkan email.
2. Jika email tidak terdaftar, sistem menampilkan pesan bahwa email tidak terdaftar.
3. Jika email terdaftar, sistem membuat token reset yang berlaku 1 jam dan mengirim link reset ke email.
4. Pengguna membuka link, lalu mengisi password baru dan konfirmasinya.
5. Sistem menolak jika token tidak valid atau kedaluwarsa, password kurang dari 6 karakter, atau konfirmasi tidak cocok.
6. Jika valid, password diperbarui dan pengguna bisa login dengan password baru.

### 7.4 Proses Pengisian Formulir Pendaftaran

1. Pendaftar membuka menu Formulir.
2. Langkah 1: memilih jenjang TKLB, SDLB, atau SMPLB. Menurut keterangan di halaman, jenjang bisa diubah sebelum pendaftaran diverifikasi admin.
3. Langkah 2: mengisi data pribadi calon siswa.
4. Langkah 3: memilih surat keterangan yang dimiliki (psikolog, psikiater, dokter THT, dokter mata, pediatri).
5. Langkah 4: mengisi data ayah, ibu, dan wali.
6. Langkah 5: diarahkan ke halaman Upload Berkas.

### 7.5 Proses Upload Berkas

1. Pendaftar membuka menu Upload Berkas.
2. Berkas wajib: foto siswa, akta kelahiran, kartu keluarga, dan KTP orang tua. Berkas tambahan (opsional): ijazah atau surat pindah, dan surat dokter.
3. Sistem menolak berkas yang lebih dari 2 MB dan berkas selain JPG, JPEG, PNG, atau PDF.
4. Berkas yang sudah diverifikasi admin tidak bisa diganti lagi.
5. Pendaftar melihat status tiap berkas (menunggu, terverifikasi, atau ditolak).

### 7.6 Proses Verifikasi Pendaftar oleh Admin

1. Admin membuka menu Verifikasi. Sistem menampilkan statistik dan daftar pendaftar.
2. Admin dapat mencari pendaftar (nama, email, nomor HP) dan menyaring berdasarkan status.
3. Admin membuka detail pendaftar, memeriksa data, lalu menandai setiap berkas sebagai terverifikasi atau ditolak.
4. Admin memilih Terima atau Tolak.
5. Terima hanya bisa dilakukan jika semua berkas wajib sudah terverifikasi. Jika belum, sistem menolak dan menampilkan pesan.
6. Setelah Terima, status pendaftar menjadi diterima, data pengumuman dibuat dengan hasil seleksi Pending, dan email konfirmasi dikirim.
7. Setelah Tolak, status pendaftar menjadi ditolak dan email pemberitahuan dikirim.

### 7.7 Proses Kelola Pengumuman

1. Admin membuka menu Pengumuman. Sistem menampilkan statistik dan daftar pendaftar beserta hasil seleksinya.
2. Admin memilih Edit pada seorang pendaftar.
3. Admin memilih hasil seleksi (Lolos, Gagal, atau Pending) dan mengisi catatan.
4. Sistem hanya menerima nilai Lolos, Gagal, atau Pending, lalu menyimpan hasilnya.
5. Untuk hasil Lolos atau Gagal, sistem mengirim email hasil seleksi ke pendaftar.

### 7.8 Proses Melihat Pengumuman dan Daftar Ulang

1. Pendaftar membuka menu Pengumuman.
2. Sistem menampilkan hasil seleksi: Sedang Diproses (Pending), Lolos, atau tidak lolos, beserta catatan dari sekolah.
3. Pendaftar yang lolos dapat membuka menu Daftar Ulang. Sistem menampilkan data pendaftar, berkas yang harus dibawa, dan informasi pembayaran.
4. Pendaftar yang belum atau tidak lolos diarahkan kembali ke halaman Pengumuman jika membuka Daftar Ulang.

### 7.9 Proses Melihat Beranda dan Dashboard

1. Setelah login, pendaftar melihat Beranda berisi kelengkapan data, progress pendaftaran, status, dan notifikasi.
2. Setelah login, admin melihat Dashboard berisi jumlah pendaftar per status dan daftar pendaftar terbaru.

## 8. Konteks Pengujian QA

Fitur utama di atas akan diuji dengan:

- **Black-box Testing (manual):** Equivalence Partitioning, Boundary Value Analysis, State Transition Testing, dan Use Case Testing untuk menilai perilaku sistem dari sisi pengguna.
- **White-box Testing (Basis Path):** analisis alur logika program pada fungsi-fungsi inti fitur utama berdasarkan source code.

Rincian strategi, jadwal, dan kriteria ada di [Test Plan](Test%20Plan/Test%20Plan.md).

---

**Status Dokumen:** Draft – perlu ditinjau tim.

**Catatan QA:** Beberapa hal dari pembacaan source code perlu dibuktikan saat eksekusi pengujian, misalnya:
- Aksi Tolak di menu Verifikasi menyimpan hasil seleksi dengan nilai `tidak_lulus`, sedangkan menu Pengumuman hanya mengenal nilai `lolos`, `gagal`, dan `pending`. Tampilan yang diterima pendaftar setelah ditolak perlu diperiksa.
- Aturan password minimal 6 karakter pada registrasi diperiksa di sisi browser (JavaScript). Pemeriksaan yang sama tidak ditemukan di sisi server.

Hal-hal ini belum dianggap sebagai defect sampai dibuktikan melalui pengujian.
