# Pemetaan Materi

Tabel ini menunjukkan di mana setiap topik materi kuliah Testing dan QA diterapkan di proyek ini. Kolom Status diisi menurut kenyataan: *Dirancang* berarti dokumen atau skrip sudah ada, *Dijalankan* berarti sudah ada hasil aktual dan bukti.

| No | Topik | Penerapan di proyek | Lokasi | PIC | Status |
|---|---|---|---|---|---|
| 1 | Pengantar Testing dan QA | Tujuan, ruang lingkup, dan prinsip pengujian | README, Test Plan bagian 1 sampai 3 | Seluruh tim | Dirancang |
| 2 | Proses Testing | Perencanaan, desain, eksekusi, pelaporan, penutupan | Test Plan, Test Scenario, Test Case, Test Report | Seluruh tim | Dirancang |
| 3 | Strategi Pengujian (black-box dan white-box) | EP, BVA, Decision Table, State Transition, Use Case, Basis Path, Statement, Branch, Condition, Loop, Data Flow | Test Case (3 berkas), Decision Table, White-box Testing, Teknik Tambahan | Gunawan, Jumigih, Lintang | Dirancang |
| 4 | Strategi Pengujian lanjutan (gray-box, smoke, sanity, eksploratori) | Gray-box lewat DevTools, Smoke, Sanity, Exploratory | White-box Testing (jalur DevTools), TC-SM, TC-EX, TC-SC-03 | Gunawan, Jumigih, Lintang | Dirancang |
| 5 | Unit Testing | Pengujian unit lewat jalur white-box tiap unit kode dan fungsi JavaScript | White-box Testing WB-01 sampai WB-05, Decision Table DT-02 | Gunawan | Dirancang |
| 6 | Integration Testing | Alur lintas fitur dan lintas role secara bertahap | TC-IN-01 sampai TC-IN-06 | Jumigih, Lintang | Dirancang |
| 7 | Pengujian Fungsional dan Non-Fungsional | Fungsional (11 fitur), kegunaan, kompatibilitas, aksesibilitas | Test Case Autentikasi, User, Admin; TC-NF-01 sampai TC-NF-05 | Seluruh tim | Dirancang |
| 8 | System Testing | Pengujian end-to-end seluruh alur sistem | TC-IN-01, TC-IN-02, TC-IN-03, TC-SM-01 | Jumigih, Lintang | Dirancang |
| 9 | User Acceptance Testing | Alpha oleh tim, beta oleh responden | UAT Plan dan Hasil, TC-UA-01 sampai TC-UA-03 | Jumigih | Dirancang |
| 10 | Automation Testing | Otomasi uji berulang dengan Playwright | Automation Testing, AT-01 sampai AT-07 | Gunawan | Dirancang |
| 11 | Regression Testing | Regresi berdasarkan prioritas dan retest defect | Regression Record, TC-RG-01, TC-RG-02 | Lintang | Dirancang |
| 12 | API Testing | Endpoint AJAX JSON verifikasi dokumen, terima, tolak | TC-AP-01 sampai TC-AP-06, koleksi Postman | Lintang | Dirancang |
| 13 | Performance Testing | Waktu muat, waktu upload, load testing kecil | TC-PF-01 sampai TC-PF-03, skrip k6 | Lintang | Dirancang |
| 14 | Security Testing | Pemeriksaan pasif dan peninjauan kode, tanpa penetration testing | TC-SC-01 sampai TC-SC-08, temuan W-1 sampai W-7 | Gunawan | Dirancang |
| 15 | Manajemen Bug dan Pemeliharaan Kualitas | Severity, priority, siklus status, GitHub Issues | Bug Report, templat issue | Lintang | Dirancang |
| 16 | Dokumentasi Pengujian dan Tren QA | Dokumen standar pengujian dan rujukan standar | Test Plan, Test Report, ISO/IEC/IEEE 29119-5:2024 | Seluruh tim | Dirancang |

## Acuan standar

Penulisan Prosedur Pengujian mengikuti ISO/IEC/IEEE 29119-5:2024 (keyword-driven testing). Daftar aksi bernama ada di [Daftar Keyword](Test%20Case/Daftar%20Keyword.md). Jenis pengujian lain berasal dari materi kuliah, bukan dari standar itu.

## Batasan yang disengaja
- Performance: stress, spike, endurance, dan volume hanya dirancang di Test Plan 5.7 dan tidak dijalankan di website yang hidup. Load testing 10 pengguna virtual hanya dengan izin pemilik website.
- Security: hanya pemeriksaan pasif dan peninjauan kode. Tidak ada penetration testing dan tidak ada pengujian aktif terhadap kredensial orang lain.
- Automation, API, dan performa: skrip sudah ditulis tetapi belum dijalankan, dan selector perlu dicek dengan DevTools pada run pertama.
- Unit testing: dilakukan lewat jalur white-box dari UI, bukan kerangka unit test, karena tim tidak mengubah kode sistem.

Kolom Status diperbarui menjadi Dijalankan setelah hasil aktual dan bukti ada di repository.
