// Konfigurasi Playwright. Alamat dan akun uji dibaca dari environment variable.
const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: process.env.BASE_URL || 'https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/',
    screenshot: 'on',
    trace: 'retain-on-failure',
  },
});
