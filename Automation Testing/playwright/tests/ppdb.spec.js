// AT-01 sampai AT-07. Sudah diverifikasi dengan Chromium (Playwright) terhadap website live.
// Akun uji dibaca dari environment variable, jangan ditulis di file ini:
//   TEST_USER_EMAIL, TEST_USER_PASSWORD
const { test, expect } = require('@playwright/test');

const EMAIL = process.env.TEST_USER_EMAIL;
const PASS = process.env.TEST_USER_PASSWORD;

async function isiLogin(page, email, pw) {
  await page.goto('auth/login.php');
  await page.fill('input[name="email"]', email);
  await page.fill('input[name="password"]', pw);
  await page.click('button[type="submit"]');
}

// AT-01 -> TC-AU-19 : login password salah
test('AT-01 login dengan password salah', async ({ page }) => {
  test.skip(!EMAIL, 'TEST_USER_EMAIL belum di-set');
  await isiLogin(page, EMAIL, 'salah-password-123');
  await expect(page.getByText('Email atau password salah!')).toBeVisible();
});

// AT-02 -> TC-AU-21 : login kolom kosong
test('AT-02 login dengan kolom kosong', async ({ page }) => {
  await page.goto('auth/login.php');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/login\.php/);
  await expect(page.locator('input[name="email"]')).toBeVisible();
});

// AT-03 -> TC-AU-26 / TC-AU-25 : halaman admin & user tanpa login dialihkan, logout mengakhiri sesi
test('AT-03 akses tanpa login dan logout', async ({ page }) => {
  await page.goto('user/dashboard.php');
  await expect(page).toHaveURL(/login\.php/);
  await page.goto('admin/dashboard.php');
  await expect(page).toHaveURL(/login\.php/);
  test.skip(!EMAIL, 'TEST_USER_EMAIL belum di-set untuk bagian logout');
  await isiLogin(page, EMAIL, PASS);
  await page.goto('auth/logout.php');
  await page.goto('user/dashboard.php');
  await expect(page).toHaveURL(/login\.php/);
});

// AT-04 -> DT-02 : status tombol Daftar Sekarang (R1 sampai R5 tanpa mengirim form)
test('AT-04 tombol Daftar Sekarang mengikuti syarat DT-02', async ({ page }) => {
  await page.goto('auth/register.php');
  const btn = page.locator('#submitBtn');
  // Kondisi awal kosong -> Nonaktif
  await expect(btn).toBeDisabled();

  // R1: Semua field terisi valid, password >= 6, konfirmasi cocok, S&K dicentang -> Aktif
  await page.fill('input[name="nama_lengkap"]', 'QA Kelompok 5');
  await page.fill('input[name="email"]', 'qa.dt02@example.com');
  await page.fill('input[name="no_hp"]', '081234567890');
  await page.fill('input[name="password"]', '123456');
  await page.fill('input[name="confirm_password"]', '123456');
  await page.check('#terms');
  await expect(btn).toBeEnabled();

  // R2: S&K tidak dicentang -> Nonaktif
  await page.uncheck('#terms');
  await expect(btn).toBeDisabled();
  await page.check('#terms');
  await expect(btn).toBeEnabled();

  // R3: Salah satu field kosong (nama_lengkap) -> Nonaktif
  await page.fill('input[name="nama_lengkap"]', '');
  await expect(btn).toBeDisabled();
  await page.fill('input[name="nama_lengkap"]', 'QA Kelompok 5');

  // R4: Password kurang dari 6 karakter (5 karakter) -> Nonaktif
  await page.fill('input[name="password"]', '12345');
  await page.fill('input[name="confirm_password"]', '12345');
  await expect(btn).toBeDisabled();

  // R5: Konfirmasi tidak sama dengan password -> Nonaktif
  await page.fill('input[name="password"]', '123456');
  await page.fill('input[name="confirm_password"]', '123457');
  await expect(btn).toBeDisabled();
});

// AT-05 -> TC-AU-29 : lupa password dengan email tidak terdaftar
test('AT-05 lupa password email tidak terdaftar', async ({ page }) => {
  await page.goto('auth/forgot-password.php');
  await page.fill('input[name="email"]', 'tidak.ada.' + Date.now() + '@example.com');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/forgot-password\.php/);
  await expect(page.locator('body')).toContainText(/tidak terdaftar|tidak ditemukan/i);
});

// AT-06 -> TC-SM-01 : smoke halaman publik
for (const p of ['', 'auth/login.php', 'auth/register.php', 'auth/forgot-password.php']) {
  test(`AT-06 smoke ${p || 'landing'}`, async ({ page }) => {
    const res = await page.goto(p);
    expect(res.status()).toBeLessThan(400);
    await expect(page.locator('body')).not.toContainText(/Fatal error|Warning:|Parse error/);
  });
}

// AT-07 -> TC-PF-01 : waktu muat halaman publik, batas tim 3 detik
for (const p of ['auth/login.php', 'auth/register.php']) {
  test(`AT-07 waktu muat ${p}`, async ({ page }) => {
    const t0 = Date.now();
    await page.goto(p, { waitUntil: 'load' });
    const ms = Date.now() - t0;
    console.log(`${p}: ${ms} ms`);
    expect(ms).toBeLessThan(3000);
  });
}
