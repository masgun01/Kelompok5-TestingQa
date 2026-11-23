// AT-01 sampai AT-07. Belum dijalankan. Selector (name atribut) berasal dari bacaan source code
// dan harus dicek dengan DevTools sebelum run pertama.
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

// AT-02 -> TC-AU-21 : login kolom kosong (form memakai novalidate, jadi diperiksa server)
test('AT-02 login dengan kolom kosong', async ({ page }) => {
  await page.goto('auth/login.php');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/login\.php/);
});

// AT-03 -> TC-AU-26 / TC-AU-25 : halaman user tanpa login dialihkan, logout mengakhiri sesi
test('AT-03 akses tanpa login dan logout', async ({ page }) => {
  await page.goto('user/dashboard.php');
  await expect(page).toHaveURL(/login\.php/);
  test.skip(!EMAIL, 'TEST_USER_EMAIL belum di-set untuk bagian logout');
  await isiLogin(page, EMAIL, PASS);
  await page.goto('auth/logout.php');
  await page.goto('user/dashboard.php');
  await expect(page).toHaveURL(/login\.php/);
});

// AT-04 -> DT-02 : status tombol Daftar Sekarang
test('AT-04 tombol Daftar Sekarang mengikuti syarat', async ({ page }) => {
  await page.goto('auth/register.php');
  const btn = page.locator('#submitBtn');
  await expect(btn).toBeDisabled();
});

// AT-05 -> TC-AU-29 : lupa password dengan email tidak terdaftar
test('AT-05 lupa password email tidak terdaftar', async ({ page }) => {
  await page.goto('auth/forgot-password.php');
  await page.fill('input[name="email"]', 'tidak.ada.' + Date.now() + '@example.com');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/forgot-password\.php/);
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
