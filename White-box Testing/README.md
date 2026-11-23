# White-box Testing

Pengujian Basis Path pada lima unit kode. Penanggung jawab: Gunawan Wibisono.

Dokumen lengkap: [White-box Testing.md](White-box%20Testing.md)

Teknik white-box lain (Statement, Branch, Condition Coverage, Loop, Data Flow): [Teknik Tambahan.md](Teknik%20Tambahan.md)

| Unit | Yang diuji | Berkas sumber | V(G) |
|---|---|---|---|
| WB-01 | Pemeriksaan login | `auth/login.php` | 9 |
| WB-02 | Pemeriksaan registrasi | `auth/register.php` | 9 |
| WB-03 | Pemeriksaan upload berkas | `user/upload-berkas.php` | 12 |
| WB-04 | Aksi Terima dan Tolak | `admin/verifikasi.php` | 10 |
| WB-05 | Penyimpanan hasil seleksi | `admin/pengumuman.php` | 9 |

Tiap unit berisi flow graph, perhitungan Cyclomatic Complexity V(G) dengan tiga cara, daftar jalur independen, dan test case per jalur beserta hasilnya.

| Folder | Isi |
|---|---|
| images | Gambar flow graph tiap unit |
| Bukti | Tangkapan layar hasil uji, nama berkas sama dengan ID jalur, misalnya `WB-01-J3.png` |
