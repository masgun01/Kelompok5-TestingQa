# Pemetaan Materi

Tabel ini menunjukkan di mana setiap topik materi kuliah Testing dan QA diterapkan di proyek ini. Kolom Status diisi menurut kenyataan: *Dirancang* berarti dokumen atau skrip sudah ada, *Dijalankan* berarti sudah ada hasil aktual dan bukti di repository.

| No | Topik | Penerapan di proyek | Lokasi | PIC | Status |
|---|---|---|---|---|---|
| 1 | Pengantar Testing dan QA | Tujuan, ruang lingkup, dan prinsip pengujian | README, Test Plan bagian 1 sampai 3 | Seluruh tim | Dijalankan |
| 2 | Proses Testing | Perencanaan, desain, eksekusi, pelaporan, penutupan | Test Plan, Test Scenario, Test Case, Test Report | Seluruh tim | Dijalankan |
| 3 | Strategi Pengujian (black-box dan white-box) | EP, BVA, Decision Table, State Transition, Use Case, Basis Path, Statement, Branch, Condition, Loop, Data Flow | Test Case (4 berkas), Decision Table, White-box Testing, Teknik Tambahan | Gunawan, Jumigih, Lintang | Dijalankan |
| 4 | Strategi Pengujian lanjutan (gray-box, smoke, sanity, eksploratori) | Gray-box lewat DevTools, Smoke, Sanity, Exploratory | White-box Testing (jalur DevTools), TC-SM, TC-EX, TC-SC-03 | Gunawan, Jumigih, Lintang | Dijalankan |
| 5 | Unit Testing | Pengujian unit lewat jalur white-box tiap unit kode dan fungsi JavaScript | White-box Testing WB-01 sampai WB-05 (29/32 jalur), Decision Table DT-02 | Gunawan | Dijalankan |
| 6 | Integration Testing | Alur lintas fitur dan lintas role secara bertahap | TC-IN-01 sampai TC-IN-06 | Jumigih, Lintang | Dijalankan |
| 7 | Pengujian Fungsional dan Non-Fungsional | Fungsional (11 fitur), kegunaan, kompatibilitas, aksesibilitas | Test Case Autentikasi, User, Admin; TC-NF-01 sampai TC-NF-05 | Seluruh tim | Dijalankan |
| 8 | System Testing | Pengujian end-to-end seluruh alur sistem | TC-IN-01, TC-IN-02, TC-IN-03, TC-SM-01 | Jumigih, Lintang | Dijalankan |
| 9 | User Acceptance Testing | Alpha oleh tim (dijalankan), beta oleh responden luar (dirancang) | UAT Plan dan Hasil, TC-UA-01 sampai TC-UA-03 | Jumigih | Dirancang (Alpha selesai, Beta menunggu responden) |
| 10 | Automation Testing | Otomasi uji berulang dengan Playwright (11 test) | Automation Testing, AT-01 sampai AT-07 | Gunawan | Dijalankan |
| 11 | Regression Testing | Regresi berdasarkan prioritas (Run 1 & Run 2) dan retest defect | Regression Record, TC-RG-01, TC-RG-02 | Lintang | Dijalankan |
| 12 | API Testing | Endpoint AJAX JSON verifikasi dokumen, terima, tolak | TC-AP-01 sampai TC-AP-06, koleksi Postman | Lintang | Dijalankan |
| 13 | Performance Testing | Waktu muat (TC-PF-01), waktu upload 2MB (TC-PF-02), rancangan k6 (TC-PF-03) | TC-PF-01 sampai TC-PF-03, skrip k6 | Lintang | Dijalankan (TC-PF-01 & 02; TC-PF-03 bersyarat) |
| 14 | Security Testing | Pemeriksaan pasif dan peninjauan kode, tanpa penetration testing | TC-SC-01 sampai TC-SC-08, temuan W-1 sampai W-7 | Gunawan | Dijalankan |
| 15 | Manajemen Bug dan Pemeliharaan Kualitas | Severity, priority, siklus status, GitHub Issues (BUG-001 s/d BUG-010) | Bug Report, templat issue | Lintang | Dijalankan |
| 16 | Dokumentasi Pengujian dan Tren QA | Dokumen standar pengujian dan rujukan standar | Test Plan, Test Report, ISO/IEC/IEEE 29119-5:2024 | Seluruh tim | Dijalankan |

## Acuan standar

Penulisan Prosedur Pengujian mengikuti ISO/IEC/IEEE 29119-5:2024 (keyword-driven testing). Daftar aksi bernama ada di [Daftar Keyword](Test%20Case/Daftar%20Keyword.md). Jenis pengujian lain berasal dari materi kuliah, bukan dari standar itu.

## Batasan yang disengaja
- Performance: stress, spike, endurance, dan volume hanya dirancang di Test Plan 5.7 dan tidak dijalankan di website yang hidup. Load testing 10 pengguna virtual (`TC-PF-03`) hanya dijalankan dengan izin pemilik website.
- Security: hanya pemeriksaan pasif dan peninjauan kode. Tidak ada penetration testing dan tidak ada pengujian aktif terhadap kredensial orang lain.
- Automation, API, dan performa (`TC-PF-01`, `TC-PF-02`): skrip Playwright (`AT-01` s/d `AT-07`), `cek-header.sh`, dan pengujian endpoint API (`TC-AP-01` s/d `TC-AP-06`) telah dijalankan dan diverifikasi terhadap website yang berjalan.
- Unit testing: dilakukan lewat jalur white-box dari UI dan DevTools, bukan kerangka unit test internal, karena tim tidak mengubah kode sistem.
