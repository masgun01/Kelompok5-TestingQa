# Decision Table

Decision Table Testing dipakai untuk bagian yang hasilnya ditentukan oleh kombinasi beberapa kondisi. Setiap aturan (kolom R) menjadi satu test case. Y = ya, T = tidak, - = tidak berpengaruh.

## DT-01 Hasil login

Sumber: `auth/login.php`. Test case: [Test Case Autentikasi](Test%20Case%20Autentikasi.xlsx).

| Kondisi | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| Email terdaftar | T | Y | Y | Y | Y |
| Password benar | - | T | Y | Y | Y |
| Akun aktif | - | - | T | Y | Y |
| Role admin | - | - | - | T | Y |
| **Hasil** | Pesan 'Email atau password salah!' | Pesan 'Email atau password salah!' | Pesan 'Akun belum diaktifasi...' | Masuk Beranda user | Masuk Dashboard Admin |
| Test case | TC-AU-20 | TC-AU-19 | TC-AU-22 | TC-AU-17 | TC-AU-18 |

## DT-02 Tombol Daftar Sekarang

Sumber: `auth/register.php` (fungsi `updateButtonState`). Tombol aktif hanya jika semua kondisi Y.

| Kondisi | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| Syarat dan Ketentuan dicentang | Y | T | Y | Y | Y |
| Nama, email, no HP terisi | Y | Y | T | Y | Y |
| Password minimal 6 karakter | Y | Y | Y | T | Y |
| Konfirmasi sama dengan password | Y | Y | Y | Y | T |
| **Tombol** | Aktif | Nonaktif | Nonaktif | Nonaktif | Nonaktif |
| Test case | TC-AU-04 | TC-AU-08 | TC-AU-07 | TC-AU-03 | TC-AU-06 |

Fungsi `updateButtonState` juga bisa diuji langsung dari Console DevTools (unit test sederhana pada kode JavaScript): isi kolom lewat kode, lalu cek nilai `document.getElementById('submitBtn').disabled` untuk tiap aturan.

## DT-03 Aksi Terima pada Verifikasi Pendaftar

Sumber: `admin/verifikasi.php` baris 28 sampai 72. Test case: [White-box Testing](../White-box%20Testing/White-box%20Testing.md) bagian WB-04.

| Kondisi | R1 | R2 | R3 |
|---|---|---|---|
| Semua berkas wajib terverifikasi | T | Y | Y |
| Sudah ada baris pengumuman | - | T | Y |
| **Hasil** | Ditolak: pesan berkas belum diverifikasi | Diterima, baris pengumuman baru dibuat (pending) | Diterima, hasil seleksi lama tidak diubah |
| Test case | WB-04-J3 | WB-04-J2 | WB-04-J4 |

