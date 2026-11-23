# Regression Record

Regression Testing memastikan perbaikan atau perubahan tidak merusak fungsi yang sebelumnya benar. Test case: TC-RG-01 dan TC-RG-02. Penanggung jawab: Lintang Nur Hafsari.

## Strategi

| Hal | Isi |
|---|---|
| Pendekatan | Berdasarkan prioritas: semua test case Prioritas High diulang |
| Retest | Setiap defect berstatus Fixed diuji ulang dengan langkah reproduksi aslinya |
| Selektif | Jika perbaikan hanya menyentuh satu fitur, tambahkan test case fitur terkait yang berprioritas Medium |
| Otomasi | Skrip di [Automation Testing](../Automation%20Testing/README.md) dijalankan ulang untuk bagian yang tercakup |
| Pemicu | Commit baru pada website, atau defect berstatus Fixed |

Catatan: tim penguji tidak mengubah kode. Perbaikan dilakukan pemilik website. Regresi dijalankan ketika ada commit baru atau ketika website diperbarui.

## Catatan Run

| Run | Tanggal | Commit | Pemicu | Jumlah dijalankan | Pass | Fail | Test case yang berubah dari Pass ke Fail |
|---|---|---|---|---|---|---|---|
| Run 1 | | 70a38d9 | Pengujian awal | | | | - |
| Run 2 | | | | | | | |

## Retest Defect

| ID Defect | Status sebelum | Hasil retest | Status sesudah | Tanggal |
|---|---|---|---|---|
| | Fixed | | Verified/Closed/Reopen | |

Tabel diisi setelah pengujian dijalankan.
