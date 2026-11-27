# Test Report

Status: **Dijalankan (Putaran 1 & 2 — 24–25 November 2026)**. Seluruh angka di bawah berasal dari hasil eksekusi aktual pada berkas Excel Test Case, White-box Testing, Automation Testing, dan Bug Report.

## 1. Identitas

| Hal | Isi |
|---|---|
| Aplikasi | PPDB SLB Sana Dharma ([https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/](https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/)) |
| Versi | Commit `70a38d9` |
| Periode pengujian | 24 – 25 November 2026 |
| Penguji | Gunawan Wibisono, Jumigih Andrian, Lintang Nur Hafsari |

## 2. Cakupan yang dijalankan

| Jenis pengujian | Direncanakan | Dijalankan | Tidak dijalankan dan alasannya |
|---|---|---|---|
| Black-box Fungsional (Autentikasi: 34, User: 17, Admin: 12) | 63 | 54 | 9 TC Autentikasi (`TC-AU-10, 11, 14, 15, 23, 30, 31, 32, 34`) tidak diulang agar tidak membanjiri database produksi dengan akun baru dan karena token email bersifat sekali pakai |
| White-box Basis Path (49 jalur formal; 32 jalur dapat dijalankan) | 49 (32 dapat dijalankan) | 29 | 10 jalur tidak mungkin secara logika (*infeasible path*); 7 jalur butuh kegagalan DB/SMTP/server atau perubahan DB produksi; 3 jalur (`WB-04-J2, J6`, `WB-05-J4`) butuh akun pendaftar yang belum punya baris di tabel `pengumuman` |
| Integrasi (`TC-IN-01` s/d `TC-IN-06`) | 6 | 6 | 0 (seluruhnya dijalankan) |
| Non-fungsional (`TC-NF`: 5, `TC-PF`: 3, `TC-SC`: 8) | 16 | 14 | 2 TC: `TC-NF-03` (uji manual browser desktop Edge/Firefox di lokal) dan `TC-PF-03` (Load test k6 10 VU — sesuai Test Plan 5.7 hanya dijalankan dengan izin pemilik website) |
| API (`TC-AP-01` s/d `TC-AP-06`) | 6 | 6 | 0 (seluruhnya dijalankan) |
| Smoke & Sanity (`TC-SM-01`, `TC-SM-02`) | 2 | 1 | 1 TC: `TC-SM-02` (Sanity Test menunggu perbaikan defect dari pemilik website) |
| UAT (`TC-UA-01` s/d `TC-UA-03`) | 3 | 0 (Alpha selesai) | 3 TC Beta UAT menunggu jadwal dengan responden luar (orang tua/wali & petugas sekolah) |
| Regresi (`TC-RG-01`, `TC-RG-02`) | 2 | 1 | 1 TC: `TC-RG-02` (Retest defect menunggu pemilik website memperbarui commit) |
| Eksploratori (`TC-EX-01` s/d `TC-EX-03`) | 3 | 3 | 0 (seluruhnya dijalankan) |
| Otomasi Playwright (`AT-01` s/d `AT-07` — 11 test) | 7 skenario (11 test) | 7 skenario (11 test) | 0 (seluruhnya dijalankan dan Pass) |

## 3. Rekap hasil

### A. Rekap Test Case Black-box & Sistem (4 Berkas Excel)

| Berkas Test Case | Total TC | Dijalankan | Pass | Fail | Blocked | Belum Dijalankan |
|---|---:|---:|---:|---:|---:|---:|
| [Test Case Autentikasi.xlsx](../Test%20Case/Test%20Case%20Autentikasi.xlsx) | 34 | 25 | 25 | 0 | 0 | 9 |
| [Test Case User.xlsx](../Test%20Case/Test%20Case%20User.xlsx) | 17 | 17 | 15 | 2 | 0 | 0 |
| [Test Case Admin.xlsx](../Test%20Case/Test%20Case%20Admin.xlsx) | 12 | 12 | 12 | 0 | 0 | 0 |
| [Test Case Sistem.xlsx](../Test%20Case/Test%20Case%20Sistem.xlsx) | 38 | 31 | 26 | 5 | 0 | 7 |
| **Total Black-box & Sistem** | **101** | **85** | **78** | **7** | **0** | **16** |

### B. Rekap White-box Basis Path & Coverage Aktual

Dari [White-box Testing](../White-box%20Testing/White-box%20Testing.md) dan [Teknik Tambahan](../White-box%20Testing/Teknik%20Tambahan.md):
- **Jalur dieksekusi**: **29 dari 32** jalur yang dapat dijalankan (**29 Pass, 0 Fail**).
- **Statement Coverage aktual keseluruhan**: **86,7%** (98 dari 113 simpul; `WB-01`: 95,0%, `WB-02`: 76,2%, `WB-03`: 88,0%, `WB-04`: 92,3%, `WB-05`: 81,0%).
- **Branch Coverage aktual keseluruhan**: **79,5%** (70 dari 88 cabang; `WB-01`: 93,8%, `WB-02`: 68,8%, `WB-03`: 86,4%, `WB-04`: 77,8%, `WB-05`: 68,8%).
- **Data Flow Coverage**: Variabel `$uploadOk` tercakup **100%** (14 dari 14 pasangan def-use); variabel `$password_valid` tercakup **66,7%** (2 dari 3 pasangan).

### C. Rekap Automation Testing (Playwright)

- **Playwright (`AT-01` s/d `AT-07`)**: **11 dari 11 test Pass** (waktu eksekusi total ~37 detik; waktu muat `login.php` rata-rata 167 ms dan `register.php` rata-rata 101 ms, jauh di bawah batas 3.000 ms).

## 4. Rekap defect

Rincian lengkap setiap defect terdapat pada [Bug Report](../Bug%20Report/README.md).

| Severity | Jumlah | Open | Closed |
|---|---:|---:|---:|
| Critical | 0 | 0 | 0 |
| Major | 6 | 6 | 0 |
| Minor | 3 | 3 | 0 |
| Trivial | 1 | 1 | 0 |
| **Total** | **10** | **10** | **0** |

**Fitur dengan defect terbanyak**:
1. **Autentikasi & Keamanan Sesi** (`BUG-001` hash MD5 tanpa salt, `BUG-002` cookie `PHPSESSID` tanpa `HttpOnly`/`Secure`/`SameSite`, `BUG-004` tidak ada pembatasan brute-force login, `BUG-005` validasi server `register.php` meloloskan password kosong `md5('')` dan < 6 karakter, `BUG-008` banner kontradiktif pada `login.php?registered=success`, `BUG-009` tidak ada pesan pada `logout=success` dan `error=invalid_token`).
2. **Upload Berkas** (`BUG-003` berkas unggahan di `assets/uploads/` dapat diakses tanpa login, `BUG-006` fungsi `uploadFile()` membuang pesan sukses/error server karena `location.reload()` dan drag-drop tidak mengisi `#fileType`, `BUG-010` indikator kelengkapan berkas wajib tetap `4 / 4` saat berkas ditolak).
3. **Verifikasi & Pengumuman** (`BUG-007` perbedaan nilai `hasil_seleksi = 'tidak_lulus'` saat Tolak Verifikasi vs `'gagal'` di Kelola Pengumuman yang menyebabkan halaman Pengumuman pendaftar menampilkan *"Belum Ada Pengumuman"* dan kartu ringkasan admin tidak menjumlahkan pendaftar tersebut).

## 5. Hasil UAT dan regresi

- **Regression Testing** ([Regression Record](../Regression/Regression%20Record.md)): Run 1 (24 Nov 2026) dan Run 2 (25 Nov 2026) termasuk suite otomatis Playwright (`AT-01` s/d `AT-07`) dan suite API (`TC-AP-01` s/d `TC-AP-06`) menunjukkan **0 regresi** (tidak ada test case yang berubah dari Pass menjadi Fail).
- **UAT** ([UAT Plan dan Hasil](../UAT/UAT%20Plan%20dan%20Hasil.md)): Alpha Testing oleh tim penguji telah selesai sepenuhnya; Beta Testing dengan responden luar disiapkan pada dokumen formulir UAT.

## 6. Kriteria penutupan

| Kriteria | Terpenuhi |
|---|---|
| Seluruh test case direncanakan sudah dijalankan atau alasannya dicatat | **Ya** (85/101 TC Black-box/Sistem dijalankan, 29/32 jalur White-box dijalankan, seluruh sisanya memiliki alasan tertulis) |
| Tidak ada defect Critical yang terbuka tanpa keputusan | **Ya** (0 defect Critical; 6 defect Major telah didokumentasikan beserta rekomendasi perbaikan) |
| Kriteria UAT terpenuhi | **Sebagian** (Alpha Testing terpenuhi; Beta Testing menunggu responden luar & perbaikan defect Major oleh pemilik website) |
| Regresi tidak menemukan kegagalan baru | **Ya** (0 regresi pada Run 2) |

## 7. Risiko yang tersisa

1. **Keamanan Data & Kredensial (`BUG-001`, `BUG-002`, `BUG-003`, `BUG-004`)**: Penggunaan `md5()` tanpa salt, absennya flag `HttpOnly`/`Secure`/`SameSite` pada cookie `PHPSESSID`, tidak adanya *rate limiting* login, serta dapat diaksesnya URL langsung berkas di `assets/uploads/` tanpa login berisiko terhadap privasi dokumen calon siswa apabila aplikasi digunakan secara publik.
2. **Pengalaman Pengguna pada Upload Berkas & Penolakan Verifikasi (`BUG-006`, `BUG-007`)**: Pendaftar yang mengunggah format berkas salah tidak melihat pesan error karena `location.reload()`, dan pendaftar yang ditolak pada menu Verifikasi melihat status *"Belum Ada Pengumuman"* alih-alih status tidak lolos.

## 8. Kesimpulan dan rekomendasi

Alur utama fungsional website **PPDB SLB Sana Dharma** (mulai dari registrasi, login, pengisian formulir 4 langkah, unggah berkas, verifikasi dokumen oleh admin, penetapan pengumuman Lolos/Gagal, hingga informasi Daftar Ulang) serta performa dasar halaman (waktu muat rata-rata 101–167 ms dan unggah 2 MB rata-rata 762 ms) telah berjalan dengan baik.

**Rekomendasi perbaikan prioritas utama bagi pengembang sistem**:
1. Ganti `md5()` dengan `password_hash(..., PASSWORD_BCRYPT)` dan validasi `$_POST['password']` (minimal 6 karakter, tidak kosong) di sisi server sebelum hashing (`BUG-001`, `BUG-005`).
2. Aktifkan atribut `session.cookie_httponly = 1`, `session.cookie_secure = 1`, dan `session.cookie_samesite = Lax` pada konfigurasi sesi PHP (`BUG-002`) serta batasi akses langsung ke `assets/uploads/` melalui skrip PHP pemeriksa sesi (`BUG-003`).
3. Simpan pesan hasil unggah berkas di `$_SESSION` sebelum `location.reload()` pada `user/upload-berkas.php` agar pesan sukses maupun error format berkas tampil kepada pendaftar (`BUG-006`).
4. Samakan nilai `hasil_seleksi` pada aksi Tolak di `admin/verifikasi.php` menjadi `'gagal'` (bukan `'tidak_lulus'`) agar sinkron dengan `admin/pengumuman.php` dan `user/pengumuman.php` (`BUG-007`).
