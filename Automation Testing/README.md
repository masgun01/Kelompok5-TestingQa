# Automation Testing

Skrip otomasi untuk bagian pengujian yang berulang. Ruang lingkup dan alasannya ada di [Test Plan](../Test%20Plan/Test%20Plan.md) bagian 5.9.

**Status: Sudah dijalankan dan diverifikasi terhadap website live (25 November 2026).** Seluruh 11 pengujian pada Playwright (`AT-01` s/d `AT-07`), skrip pemeriksaan header keamanan (`cek-header.sh`), serta pengujian endpoint API (`TC-AP-01` s/d `TC-AP-06`) telah dieksekusi dan lulus.

| ID | Skrip | Test Case | Alat | Hasil Eksekusi |
|---|---|---|---|---|
| AT-01 | playwright/tests/ppdb.spec.js | TC-AU-19 login password salah | Playwright | Pass |
| AT-02 | playwright/tests/ppdb.spec.js | TC-AU-21 login kolom kosong | Playwright | Pass |
| AT-03 | playwright/tests/ppdb.spec.js | TC-AU-26 dan TC-AU-25 akses tanpa login, logout | Playwright | Pass |
| AT-04 | playwright/tests/ppdb.spec.js | DT-02 tombol Daftar Sekarang (R1–R5) | Playwright | Pass |
| AT-05 | playwright/tests/ppdb.spec.js | TC-AU-29 lupa password email tidak terdaftar | Playwright | Pass |
| AT-06 | playwright/tests/ppdb.spec.js | TC-SM-01 smoke halaman publik (4 halaman) | Playwright | Pass (4/4) |
| AT-07 | playwright/tests/ppdb.spec.js | TC-PF-01 waktu muat (`login.php`: ~634 ms, `register.php`: ~561 ms) | Playwright | Pass (2/2) |
| API | postman/ppdb-api.postman_collection.json | TC-AP-01 sampai TC-AP-06 | Postman / Playwright API | Pass (6/6) |
| LD | k6/load-login.js | TC-PF-03 (10 VU, 60s — hanya dengan izin pemilik) | k6 | Dirancang (bersyarat) |
| HD | scripts/cek-header.sh | TC-SC-01 (Pass), TC-SC-02 (Fail — BUG-002) | curl | Dijalankan |

## Menjalankan

```bash
cd playwright
npm install
npx playwright install chromium
# akun uji tim, jangan ditulis di file
export TEST_USER_EMAIL="akun.uji@contoh.com"
export TEST_USER_PASSWORD="isi-di-terminal"
npx playwright test
```

Di PowerShell: `$env:TEST_USER_EMAIL="..."`.

## Aturan

- Akun, password, dan cookie sesi tidak boleh masuk repo. Skrip hanya membaca environment variable.
- Hanya akun uji milik tim.
- k6 hanya setelah pemilik website mengizinkan: 10 pengguna virtual, 60 detik, halaman publik. Tidak ada stress, spike, endurance, atau volume.
- Postman: tempel cookie sesi admin di header Cookie saat run, hapus setelahnya. Ganti `ISI_ID_AKUN_UJI_*` dengan ID akun uji tim.
