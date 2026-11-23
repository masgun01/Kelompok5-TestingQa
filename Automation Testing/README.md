# Automation Testing

Skrip otomasi untuk bagian pengujian yang berulang. Ruang lingkup dan alasannya ada di [Test Plan](../Test%20Plan/Test%20Plan.md) bagian 5.9.

**Status: skrip sudah ditulis, belum dijalankan.** Website tidak bisa dijangkau dari tempat skrip ditulis, jadi selector dan hasil belum terverifikasi. Jalankan di laptop tim, cek selector dengan DevTools, lalu isi hasilnya di Test Execution Record.

| ID | Skrip | Test Case | Alat |
|---|---|---|---|
| AT-01 | playwright/tests/ppdb.spec.js | TC-AU-19 login password salah | Playwright |
| AT-02 | playwright/tests/ppdb.spec.js | TC-AU-21 login kolom kosong | Playwright |
| AT-03 | playwright/tests/ppdb.spec.js | TC-AU-26 dan TC-AU-25 akses tanpa login, logout | Playwright |
| AT-04 | playwright/tests/ppdb.spec.js | DT-02 tombol Daftar Sekarang | Playwright |
| AT-05 | playwright/tests/ppdb.spec.js | TC-AU-29 lupa password email tidak terdaftar | Playwright |
| AT-06 | playwright/tests/ppdb.spec.js | TC-SM-01 smoke halaman publik | Playwright |
| AT-07 | playwright/tests/ppdb.spec.js | TC-PF-01 waktu muat | Playwright |
| API | postman/ppdb-api.postman_collection.json | TC-AP-01 sampai TC-AP-05 | Postman |
| LD | k6/load-login.js | TC-PF-03 | k6 |
| HD | scripts/cek-header.sh | TC-SC-01, TC-SC-02 | curl |

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
