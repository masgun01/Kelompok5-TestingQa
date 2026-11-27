# Bug Report

Daftar defect yang ditemukan dan telah dibuktikan selama pengujian pada website **PPDB SLB Sana Dharma** (commit `70a38d9`), dikelola oleh Lintang Nur Hafsari bersama tim penguji.

## Pelaporan

Defect dicatat menggunakan templat [`.github/ISSUE_TEMPLATE/bug_report.md`](../.github/ISSUE_TEMPLATE/bug_report.md) dan direkap pada tabel di bawah. Bukti tangkapan layar disimpan di [Test Evidence](../Test%20Evidence/) dan [White-box Testing/Bukti](../White-box%20Testing/Bukti/).

Kolom: ID, Judul, Test Case Terkait, Langkah Reproduksi Ringkas, Hasil Diharapkan, Hasil Aktual, Bukti, Severity, Priority, Status.

## Severity

| Level | Arti |
|---|---|
| Critical | Fitur utama tidak bisa dipakai, atau data rusak atau bocor |
| Major | Fitur penting berjalan salah, ada celah validasi atau jalan pintas |
| Minor | Fungsi berjalan tetapi ada kekeliruan kecil |
| Trivial | Kosmetik, salah ketik, atau label kurang tepat |

Priority: High, Medium, Low (urutan perbaikan).

## Siklus status

New, Assigned, Open, Fixed, Retest, Verified, Closed. Jika perbaikan gagal: Reopen. Jika bukan defect: Rejected. Jika sama dengan yang sudah ada: Duplicate. Perbaikan dilakukan pemilik website, sehingga tim penguji menjalankan Retest dan Verified.

## Daftar Defect

| ID | Judul | Test Case | Langkah Reproduksi & Hasil Aktual | Hasil Diharapkan | Bukti | Severity | Priority | Status |
|---|---|---|---|---|---|---|---|---|
| **BUG-001** | Password disimpan dengan `md5()` tanpa salt | `TC-SC-04` | Pada `auth/register.php` baris 25, `auth/login.php` baris 23, dan `auth/reset-password.php` baris 42, password di-hash memakai `md5()` tanpa salt (`password_verify` hanya cadangan di `login.php`). | Password disimpan memakai `password_hash()` (bcrypt/argon2) bersalt. | `Test Evidence/Sistem/TC-SC-04.png`, `TC-SC-04-b-register.png`, `TC-SC-04-c-login.png` | Major | High | Open |
| **BUG-002** | Cookie sesi `PHPSESSID` tidak memiliki atribut `HttpOnly`, `Secure`, dan `SameSite` | `TC-SC-02` | Periksa header `Set-Cookie` pada respons HTTPS `auth/login.php`: `set-cookie: PHPSESSID=...; path=/` tanpa flag `HttpOnly`, `Secure`, maupun `SameSite`, serta tidak ada security header (`HSTS`, `X-Frame-Options`, `CSP`, `X-Content-Type-Options`). | Cookie sesi dilengkapi `HttpOnly`, `Secure`, dan `SameSite=Lax/Strict`. | `Test Evidence/Sistem/TC-SC-02.png` | Major | High | Open |
| **BUG-003** | Berkas unggahan di `assets/uploads/` dapat diakses langsung tanpa login | `TC-SC-06` | Meskipun akses ke daftar direktori `assets/uploads/` ditolak (`403 Forbidden`), URL langsung berkas unggahan (mis. `assets/uploads/28_foto_siswa_*.jpg`) dapat dibuka di jendela Incognito tanpa sesi login (`HTTP 200`). | Berkas dokumen pendaftar dilindungi pemeriksaan sesi login sebelum disajikan. | `Test Evidence/Sistem/TC-SC-06.png`, `TC-SC-06-a-berkas-tanpa-login.png` | Major | High | Open |
| **BUG-004** | Tidak ada pembatasan percobaan login gagal beruntun (*brute-force protection*) | `TC-SC-08` | Melakukan login dengan password salah 5 kali berturut-turut pada akun uji, lalu login ke-6 dengan password benar langsung berhasil masuk tanpa jeda, captcha, atau penguncian sementara. | Sistem menerapkan *rate limiting* atau jeda setelah beberapa kali gagal login beruntun. | `Test Evidence/Sistem/TC-SC-08.png` | Major | Medium | Open |
| **BUG-005** | Validasi server `auth/register.php` meloloskan password kosong (`md5('')`) dan password < 6 karakter (`W-1`, `W-2`) | `WB-02-J3`, `TC-AU-03` | `register.php` baris 25 melakukan `$password = md5($_POST['password'])` sebelum `empty($password)` pada baris 30. Karena `md5('')` menghasilkan string 32 karakter, password kosong lolos pemeriksaan field kosong di server. Selain itu batas minimal 6 karakter dan persetujuan S&K hanya diperiksa di JavaScript browser. | Server memvalidasi `$_POST['password']` sebelum di-hash, menolak password < 6 karakter, memeriksa kecocokan konfirmasi, dan memvalidasi checkbox S&K di sisi server. | `White-box Testing/Bukti/WB-02-W2-password-kosong.png` | Major | High | Open |
| **BUG-006** | Fungsi `uploadFile()` di `user/upload-berkas.php` membuang pesan sukses/error server karena `location.reload()` & drag-drop tidak mengisi `#fileType` (`T-6`) | `WB-03-J3`, `WB-03-J7`, `TC-PD-10` | `uploadFile()` mengirim POST via `fetch()`, mengabaikan HTML respons yang berisi `$message` / `$error` PHP, lalu memanggil `location.reload()` (GET). Akibatnya pesan `'File berhasil diupload.'` maupun pesan error `'Hanya file JPG, JPEG, PNG & PDF yang diperbolehkan.'` tidak pernah tampil di layar. Selain itu event `drop` tidak mengisi `#fileType`. | Pesan sukses/error disimpan di `$_SESSION` (flash message) atau dirender dari respons `fetch()`, dan event `drop` mengisi `#fileType` sesuai kartu dokumen. | `White-box Testing/Bukti/WB-03-J3.png`, `WB-03-J7.png` | Major | High | Open |
| **BUG-007** | Inkonsistensi nilai `hasil_seleksi = 'tidak_lulus'` saat Tolak Verifikasi vs `'gagal'` di Kelola Pengumuman (`W-4`, `T-2`) | `WB-04-J7`, `TC-PD-14B`, `TC-IN-03` | Aksi Tolak di `admin/verifikasi.php` menyimpan `hasil_seleksi = 'tidak_lulus'`, sedangkan `admin/pengumuman.php` hanya mengenal `'lolos'`, `'gagal'`, dan `'pending'`. Akibatnya di tabel Kelola Pengumuman tampil `--` dan pendaftar yang ditolak tidak masuk ke kartu ringkasan mana pun (total kartu 28 dari 29 pendaftar). | Gunakan nilai enum/status yang seragam (`'gagal'`) di kedua modul sehingga statistik kartu ringkasan konsisten. | `White-box Testing/Bukti/WB-04-J7-b-pengumuman-admin.png`, `WB-04-J7-c-kartu-ringkasan.png` | Minor | Medium | Open |
| **BUG-008** | Banner hijau `'Registrasi berhasil!'` dan alert merah `'Akun belum diaktifasi'` tampil bersamaan (`T-1`) | `TC-AU-22`, `WB-01-J6` | Saat user gagal login karena akun belum aktif pada URL `login.php?registered=success`, banner hijau `'Registrasi berhasil!'` dari parameter GET tetap tampil bersamaan dengan pesan merah `'Akun belum diaktifasi.'`. | Sembunyikan banner `registered=success` ketika form login sudah di-submit (POST) dan menghasilkan pesan error. | `Test Evidence/Autentikasi/TC-AU-22.png`, `White-box Testing/Bukti/WB-01-J6.png` | Minor | Low | Open |
| **BUG-009** | Halaman login tidak menampilkan pesan untuk parameter `logout=success` maupun `error=invalid_token` (`T-4`, `W-6`) | `TC-AU-16`, `TC-AU-24`, `WB-01` | Setelah logout (`login.php?logout=success`) atau saat membuka link aktivasi dengan token salah (`login.php?error=invalid_token`), halaman login tidak menampilkan pesan informasi/error apa pun kepada pengguna. | Tampilkan alert informasi saat `logout=success` dan alert peringatan saat `error=invalid_token`. | `Test Evidence/Autentikasi/TC-AU-24.png`, `TC-AU-16.png`, `White-box Testing/Bukti/WB-01-T4-logout-tanpa-pesan.png` | Minor | Low | Open |
| **BUG-010** | Indikator `'Kelengkapan Berkas Wajib 4 / 4'` tetap penuh saat berkas ditolak (`T-5`) & banner `'Siap diverifikasi'` tetap muncul setelah diterima (`T-3`) | `WB-04-J4`, `WB-04-J7` | (1) Di `user/upload-berkas.php`, indikator menghitung jumlah berkas yang pernah diunggah (`4 / 4`) walaupun ada berkas wajib yang berstatus `Ditolak`. (2) Di `admin/detail-pendaftar.php`, banner `'Siap diverifikasi di Halaman Verifikasi'` masih tampil walaupun pendaftar sudah berstatus `DITERIMA`. | Sesuaikan label indikator berkas dengan status verifikasi, dan sembunyikan banner ajakan verifikasi jika status pendaftar sudah `DITERIMA`. | `White-box Testing/Bukti/WB-04-J7-d-sisi-user-berkas-ditolak.png`, `WB-04-J4-c-status-diterima.png` | Trivial | Low | Open |

## Rekapitulasi Defect Berdasarkan Severity

| Severity | Jumlah | Open | Fixed / Closed |
|---|---|---|---|
| Critical | 0 | 0 | 0 |
| Major | 6 | 6 | 0 |
| Minor | 3 | 3 | 0 |
| Trivial | 1 | 1 | 0 |
| **Total** | **10** | **10** | **0** |

## Catatan Keamanan

Temuan keamanan dari peninjauan kode (`TC-SC-07`: potensi tampilan pesan `mysqli_error` pada beberapa halaman saat query gagal; `W-7`: parameter token pada `activate.php` dan `reset-password.php` belum memakai *prepared statement*) ditulis singkat sebatas lokasi dan dampak perbaikan tanpa langkah eksploitasi sesuai aturan pada Test Plan bagian 5.8.
