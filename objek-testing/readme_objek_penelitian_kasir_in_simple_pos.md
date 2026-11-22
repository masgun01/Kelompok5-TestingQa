# Pengujian dan Jaminan Kualitas Perangkat Lunak (QA) pada Aplikasi Mobile *Kasir-in Simple POS* (Versi 1.1.4) Berbasis Standar ISO/IEC/IEEE 29119 dan ISO/IEC 25010

> **Direktori:** `objek-testing/`  
> **Repositori:** `Kelompok-5---Testing-Qa-Perangkat`  
> **Mata Kuliah:** Testing dan QA Perangkat Lunak — Program Studi Teknik Informatika, Fakultas Ilmu Komputer, Universitas Pamulang  
> **Dosen Pengampu:** Ahmad Fauzi, S.Kom., M.Kom.

---

## Tim Peneliti / Penguji (Kelompok 5)

| No | Nama Anggota | Peran dalam Pengujian |
| :---: | :--- | :--- |
| 1 | **Gunawan Wibisono** | Test Lead & QA Tester 1 (*Test Plan*, Pemodelan *White-Box Flow*, Modul Kasir & Integrasi) |
| 2 | **Jumingih Andrian** | QA Tester 2 (Modul Kelola Stok, Fitur *Scan Nota AI* & Observasi Performa) |
| 3 | **Lintang Nur Hafsari** | QA Tester 3 (Modul Dashboard, Laporan, Pengaturan, UI/UX, *Bug Report* & UAT) |

---

## 1. Profil Objek Penelitian (*Test Item*)

Objek penelitian yang diuji pada proyek ini adalah aplikasi kasir mobile komersial berbasis Android yang tersedia secara publik di Google Play Store.

| Atribut | Detail Informasi |
| :--- | :--- |
| **Nama Aplikasi** | Kasir-in Simple POS |
| **Pengembang (*Developer*)** | Install-in |
| **Versi Terkunci (*Test Build*)** | `1.1.4` |
| **Tanggal Rilis Awal** | 5 Juni 2026 |
| **Pembaruan Terakhir** | 15 Oktober 2026 |
| **Platform & OS Minimum** | Android 8.0 dan yang lebih tinggi |
| **Ukuran Unduhan** | 18 MB |
| **Jumlah Unduhan** | 100+ unduhan |
| **Rating Konten** | Rating 3+ |
| **Model Monetisasi** | Gratis (*Freemium*), berisi iklan (*banner* & *interstitial*), serta pembelian dalam aplikasi (*Kasirin Pro*: `Rp39.900/bulan` atau `Rp349.000/tahun`) |
| **Target Pengguna** | UMKM, toko retail, warung, cafe, restoran, usaha laundry, dan penyedia jasa |
| **Sifat Objek Uji** | Aplikasi rilis publik Google Play Store (tanpa akses *source code* maupun *endpoint* API) |

---

## 2. Alasan Pemilihan Objek Penelitian

Aplikasi **Kasir-in Simple POS v1.1.4** dipilih sebagai objek pengujian berdasarkan beberapa pertimbangan utama dalam bidang *Software Quality Assurance*:

1. **Tahap Pengembangan Awal (*Early-Stage Application*):** Dengan jumlah unduhan pada kisaran 100+, aplikasi masih berada pada tahap pertumbuhan awal sehingga sangat potensial untuk dievaluasi kestabilan fungsional, konsistensi antarmuka (UI/UX), dan kualitas rilisnya.
2. **Kompleksitas Logika Bisnis Kasir (POS):** Sistem kasir melibatkan perhitungan transaksi finansial, kembalian, omset, modal, keuntungan, dan sinkronisasi stok secara *real-time* yang memiliki tingkat risiko kesalahan tinggi jika tidak diuji secara sistematis.
3. **Adopsi Fitur Berbasis Kecerdasan Buatan (AI):** Aplikasi menawarkan fitur baru **`Scan Nota Belanja (AI)`** untuk pembaruan stok otomatis, yang relevan dengan tren pengujian modern dan analisis risiko perilaku *black-box* pada sistem AI (sesuai Modul Pertemuan 15 & 16).
4. **Kesesuaian dengan Standar Pengujian:** Struktur aplikasi memungkinkan penerapan langsung standar **ISO/IEC/IEEE 29119**, **ISO/IEC 25010**, **IEEE Std 829-2008**, serta seluruh metode pengujian *Black-Box*, *Functional Integration*, pemodelan *White-Box* (*Basis Path Testing*), *Usability*, dan *User Acceptance Testing* (UAT).

---

## 3. Klaim Fitur Google Play Store (*Test Basis*)

Karena tidak tersedia dokumen *Software Requirement Specification* (SRS) resmi dari pengembang, deskripsi resmi aplikasi pada halaman Google Play Store digunakan sebagai acuan pengujian (*Test Basis*). Berikut 12 fitur utama yang diklaim pengembang:

1. Sistem kasir POS sederhana dan modern
2. Proses transaksi penjualan yang cepat
3. Manajemen produk dan stok barang
4. Scan nota / struk untuk *update* stok otomatis *(Fitur Baru — AI)*
5. Laporan penjualan dan keuntungan
6. Multi-metode pembayaran (*Cash*, QRIS, Transfer)
7. Dukungan *barcode scanner*
8. Riwayat transaksi lengkap
9. Manajemen pelanggan
10. Sinkronisasi *cloud* & *backup* otomatis
11. Multi-perangkat *(akses fitur Pro)*
12. Sistem akun yang aman

---

## 4. Pemetaan Struktur Menu Aktual (`v1.1.4`)

Berdasarkan hasil observasi langsung terhadap aplikasi yang terinstal pada perangkat Android, struktur antarmuka aktual terdiri atas 3 tab navigasi utama dan 1 menu pengaturan:

* **Tab Kasir (`Transaksi`):**
  * Pencarian nama barang, input jumlah & harga, tombol `Tambah ke Keranjang`, dan fitur `Item Manual` (`Nama Item *`, `Harga Jual *`, `Modal (opsional)`, `Jumlah`).
  * Daftar produk `Terlaris` dengan tombol pintas `+ Pcs` dan `+ Pack`.
  * Modal pembayaran **`BAYAR`** (`Cash`, status konfigurasi `QRIS` & `Transfer ATM`, kolom `Uang Diterima`, tombol nominal cepat, perhitungan `Kembalian`, dan aksi `Selesaikan Transaksi`).
* **Tab Dashboard:**
  * Kartu ringkasan `Omset Hari Ini`, jumlah `Transaksi`, `Keuntungan`, indikator status stok, dan daftar `Barang Terlaris`.
  * Menu opsi pojok kanan atas (`⋮`): `Riwayat Transaksi`, `Laporan` (detail keuntungan per produk & grafik `Rata-rata per Transaksi`), `Hubungkan ke Web/PC`, `Pengaturan`, `Tentang Aplikasi`, dan `Kebijakan Privasi`.
* **Tab Stok (`Kelola Stok`):**
  * Kolom `Cari barang...`, fitur **`Scan Nota Belanja` (AI)**, filter `Hanya stok rendah`, daftar inventori (kuota versi gratis: maks. 50 item), tombol `Hapus`, dan tombol melayang `+ Tambah Produk/Stok`.
* **Menu Pengaturan:**
  * Akun & Langganan: `Sinkronisasi Cloud`, `Kasir-in Web`, `Langganan Pro`, dan `Keluar`.
  * Toko & Pembayaran: `Informasi Toko` (batas karakter `Nama Toko 0/50`, `Alamat 0/200`, `Nomor Telepon 0/15`, `Ucapan Terima Kasih 0/150`, dan `Logo Usaha`), `Pembayaran — QRIS` (`JPEG/PNG, maks 2 MB`), `Pembayaran — Rekening Bank`, `Pengaturan Printer` (`58 mm` / `80 mm`), dan `Bahasa`.

---

## 5. Batasan Akses & Pengendalian Objek Uji

Untuk menjaga validitas dan etika pengujian perangkat lunak pada aplikasi publik, diterapkan ketentuan berikut:

* **Penguncian Versi (*Version Locking*):** Fitur *auto-update* Google Play Store dinonaktifkan selama periode pengujian agar seluruh pengujian terkunci pada versi `1.1.4`.
* **Penggunaan Data Uji (*Dummy Data*):** Seluruh transaksi dan produk yang diuji menggunakan akun dan data simulasi, bukan data transaksi bisnis nyata.
* **Keterbatasan Akses Kode & Server:** Karena aplikasi merupakan rilis publik tanpa *source code* dan dokumentasi API, pengujian difokuskan pada *Black-Box Testing*, *Black-Box Functional Integration Testing*, *Usability/UI*, UAT, serta pemodelan alur kontrol konseptual *White-Box* (*Basis Path Testing*). *Unit Testing* kode sumber, *API Testing*, *Load/Stress Testing* server, dan *Penetration Testing* aktif dikecualikan secara eksplisit di dalam *Test Plan*.

---

## 6. Navigasi Artefak Pengujian Terkait

Seluruh dokumen hasil pengujian terhadap objek penelitian ini tersimpan secara terstruktur pada repositori:

* **Standar Acuan Internasional:** [`ISO Standar IEEE 2026/29119-1-2022.pdf`](../ISO%20Standar%20IEEE%202026/29119-1-2022.pdf)
* **Dokumen Perencanaan Uji:** [`Hasil-Dokumentasi testing/01_Test_Plan.md`](../Hasil-Dokumentasi%20testing/01_Test_Plan.md)
* **Pemodelan Alur White-Box:** [`Hasil-Dokumentasi testing/02_WhiteBox_Flow_Analysis.md`](../Hasil-Dokumentasi%20testing/02_WhiteBox_Flow_Analysis.md)
* **Daftar Kasus Uji (*Test Cases*):** [`Hasil-Dokumentasi testing/03_Test_Cases.md`](../Hasil-Dokumentasi%20testing/03_Test_Cases.md)
* **Laporan Temuan Bug:** [`Hasil-Dokumentasi testing/04_Bug_Report.md`](../Hasil-Dokumentasi%20testing/04_Bug_Report.md)
* **Laporan Akhir (*Test Report*):** [`Hasil-Dokumentasi testing/05_Test_Report.md`](../Hasil-Dokumentasi%20testing/05_Test_Report.md)
* **Bukti Tangkapan Layar (19 *Screenshots*):** [`Hasil-Dokumentasi testing/screenshots/`](../Hasil-Dokumentasi%20testing/screenshots/)
* **Log Konsultasi Dosen:** [`Konsultasi Testing/log_konsultasi.md`](../Konsultasi%20Testing/log_konsultasi.md)