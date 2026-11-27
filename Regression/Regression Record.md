# Regression Record

Regression Testing memastikan perbaikan atau perubahan tidak merusak fungsi yang sebelumnya benar. Test case: `TC-RG-01` dan `TC-RG-02`. Penanggung jawab: Lintang Nur Hafsari.

## Strategi

| Hal | Isi |
|---|---|
| Pendekatan | Berdasarkan prioritas: semua test case Prioritas High dan suite otomasi diulang |
| Retest | Setiap defect berstatus Fixed diuji ulang dengan langkah reproduksi aslinya |
| Selektif | Jika perbaikan hanya menyentuh satu fitur, tambahkan test case fitur terkait yang berprioritas Medium |
| Otomasi | Skrip di [Automation Testing](../Automation%20Testing/README.md) (`AT-01` s/d `AT-07`) dan suite API (`TC-AP-01` s/d `TC-AP-06`) dijalankan ulang |
| Pemicu | Commit baru pada website, defect berstatus Fixed, atau verifikasi konsistensi lintas putaran pengujian |

Catatan: tim penguji tidak mengubah kode aplikasi. Perbaikan dilakukan pemilik website. Sesuai [Test Plan](../Test%20Plan/Test%20Plan.md) bagian 5.10 butir 3, apabila belum ada perubahan commit dari pemilik website selama masa pengujian, Run 2 dijalankan menggunakan suite otomatis dan skenario High untuk memastikan tidak ada regresi fungsi.

## Catatan Run

| Run | Tanggal | Commit | Pemicu | Jumlah dijalankan | Pass | Fail | Test case yang berubah dari Pass ke Fail |
|---|---|---|---|---|---|---|---|
| Run 1 | 24 November 2026 | `70a38d9` | Pengujian awal (Baseline Putaran 1) | 28 (9 TC-AU + 1 TC-SC + 18 WB) | 27 | 1 (`TC-SC-04`) | - |
| Run 2 | 25 November 2026 | `70a38d9` | Eksekusi penuh Putaran 2 + Suite Otomasi (`AT-01`..`AT-07` & `TC-AP-01`..`06`) | 46 TC Prioritas High + 11 Automation Test | 41 TC High + 11 AT | 5 TC High (`TC-PD-10`, `TC-PD-14B`, `TC-IN-03`, `TC-SC-04`, `TC-SC-06`) | Tidak ada (0 regresi dari Pass ke Fail) |

## Retest Defect

| ID Defect | Status sebelum | Hasil retest | Status sesudah | Tanggal |
|---|---|---|---|---|
| `BUG-001` s/d `BUG-010` | Open | Belum ada perubahan commit dari pemilik website (masih pada commit `70a38d9`) | Open | 25 November 2026 |
