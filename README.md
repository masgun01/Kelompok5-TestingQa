# Software Testing & Quality Assurance

## Tentang Proyek

Repository ini berisi dokumentasi, perencanaan, pelaksanaan, dan hasil pengujian perangkat lunak pada website **PPDB SLB Sana Dharma** (Penerimaan Peserta Didik Baru Sekolah Luar Biasa Sana Dharma) sebagai tugas kelompok mata kuliah Testing dan QA Perangkat Lunak.

Pengujian difokuskan pada **fitur utama** website, yaitu alur pendaftaran calon peserta didik dari pembuatan akun sampai daftar ulang, serta alur kerja admin dalam memverifikasi pendaftar dan mengumumkan hasil seleksi.

## Tujuan Proyek

- Memahami dan mengevaluasi fungsionalitas fitur utama website PPDB SLB Sana Dharma.
- Menyusun Test Scenario dan Test Case secara terstruktur sebagai dasar pengujian.
- Mengidentifikasi kesalahan (*defect*) dan potensi masalah pada sistem.
- Melakukan pengujian Black-box secara manual berdasarkan Test Scenario dan Test Case.
- Melakukan pengujian White-box (Basis Path) pada logika program yang menjadi inti fitur utama.
- Mendokumentasikan hasil pengujian beserta bukti dan rekomendasi perbaikan.

## Ruang Lingkup Pengujian

Pengujian hanya mencakup 11 fitur utama berikut:

| No | Kelompok | Fitur |
|---|---|---|
| 1 | Autentikasi | Login |
| 2 | Autentikasi | Lupa Password |
| 3 | Autentikasi | Registrasi Akun |
| 4 | Admin | Dashboard |
| 5 | Admin | Verifikasi Pendaftar |
| 6 | Admin | Kelola Pengumuman |
| 7 | User | Beranda |
| 8 | User | Formulir Pendaftaran |
| 9 | User | Upload Berkas |
| 10 | User | Pengumuman |
| 11 | User | Daftar Ulang |

Jenis pengujian yang dilakukan:

- **Manual Testing (Black-box Testing)**: pengujian langsung melalui website berdasarkan Test Scenario dan Test Case, memakai teknik Equivalence Partitioning, Boundary Value Analysis, State Transition Testing, dan Use Case Testing.
- **White-box Testing**: Basis Path Testing pada lima unit kode (flow graph, Cyclomatic Complexity, jalur independen), ditambah Statement, Branch, Condition Coverage, Loop, dan Data Flow Testing.
- **Pengujian tingkat sistem**: Smoke, Sanity, Integrasi, Eksploratori, UAT, dan Regresi.
- **Non-fungsional**: kegunaan, kompatibilitas, aksesibilitas, performa (skala kecil), dan keamanan (pemeriksaan pasif dan peninjauan kode).
- **API Testing** pada endpoint AJAX admin dan **Automation Testing** (Playwright) pada alur yang berulang.

Menu Laporan, Data User, ekspor data, dan halaman landing tidak termasuk ruang lingkup. Rinciannya ada di [Test Plan](Test%20Plan/Test%20Plan.md).

## Standar dan Referensi

Proyek ini mengacu pada standar internasional berikut:

- ISO/IEC/IEEE 29119-5:2024 – Software and systems engineering — Software testing — Part 5: Keyword-driven testing

ISO/IEC/IEEE 29119 adalah rangkaian standar internasional untuk pengujian perangkat lunak, dan bagian kelimanya khusus membahas *keyword-driven testing*. Pendekatan ini menyusun test case sebagai urutan aksi bernama beserta datanya, bukan sebagai kalimat panjang yang ditulis bebas tiap kali. Nama aksinya diambil dari istilah yang dipakai pengguna sistem, misalnya Login dan Upload Berkas, sehingga test case tetap terbaca walaupun susunan tombol atau tampilan halamannya nanti berubah. Pada pasal 5.1 disebutkan bahwa pendekatan ini memang lazim dipakai untuk mendukung automasi, tetapi masih dapat diterapkan jika automasi tidak direncanakan. Karena itu pengujian di proyek ini dijalankan manual, sedangkan prosedur pengujiannya tetap disusun dengan pola tersebut.

Standar ini dipakai sebagai acuan penyusunan dokumen dan prosedur pengujian. Proyek ini bukan proses sertifikasi ISO.

Materi kuliah yang jadi dasar: Modul Testing dan QA Perangkat Lunak, Program Studi Teknik Informatika, Universitas Pamulang.

## Aplikasi yang Diuji

| Informasi | Keterangan |
|---|---|
| Nama Aplikasi | PPDB SLB Sana Dharma |
| Website | [https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/](https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/) |
| Jenis Aplikasi | Sistem Informasi Penerimaan Peserta Didik Baru berbasis web |
| Platform | Web Application |
| Versi yang Diuji | Commit `70a38d9` (21 November 2026) |

## Tim Penguji

Proyek ini disusun oleh Kelompok 5, kelas 07TPLE002:

1. Gunawan Wibisono - 231011400057
2. Jumigih Andrian - 231011401426
3. Lintang Nur Hafsari - 231011400071

Dosen Pengampu: Asep Erlan Maulana, S.Kom., M.Kom.

## Susunan Repository

| Folder / Berkas | Isi |
|---|---|
| [System Overview.md](System%20Overview.md) | Gambaran umum sistem yang diuji |
| [Matriks dan Use Case](Matriks%20dan%20Use%20Case/Matriks%20dan%20Use%20Case.md) | Hak akses fitur per role dan diagram use case |
| [System Flowchart](System%20Flowchart/) | Flowchart alur proses per role |
| [Test Plan](Test%20Plan/Test%20Plan.md) | Rencana pengujian |
| [Test Scenario](Test%20Scenario/Test%20Scenario.md) | Daftar skenario pengujian per role |
| [Test Case](Test%20Case/) | Test case per role (4 berkas Excel) beserta Daftar Keyword dan Decision Table |
| [White-box Testing](White-box%20Testing/) | Basis Path Testing pada lima unit kode (29/32 jalur dijalankan) |
| [Automation Testing](Automation%20Testing/README.md) | Skrip Playwright, Postman, k6, dan cek-header.sh (sudah dijalankan) |
| [UAT](UAT/UAT%20Plan%20dan%20Hasil.md) | Rencana dan hasil User Acceptance Testing |
| [Regression](Regression/Regression%20Record.md) | Strategi dan catatan regresi (Run 1 & Run 2) |
| [Pemetaan Materi](Pemetaan%20Materi.md) | Peta topik materi kuliah ke bagian proyek |
| [Test Evidence](Test%20Evidence/) | Tangkapan layar bukti pengujian |
| [Bug Report](Bug%20Report/) | Daftar defect yang ditemukan (`BUG-001` s/d `BUG-010`) |
| [Test Report](Test%20Report/Test%20Report.md) | Ringkasan dan evaluasi hasil pengujian |

## Kontribusi dan Dokumentasi

Seluruh dokumentasi, test scenario, test case, test execution, test result, serta test report dikelola dalam repository ini agar proses pengujian dapat dilakukan secara terstruktur, terdokumentasi, dan dapat ditelusuri.

---

*Repository ini digunakan sebagai pusat dokumentasi seluruh aktivitas pengujian dan penjaminan kualitas perangkat lunak pada website PPDB SLB Sana Dharma.*
