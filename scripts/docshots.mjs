// Erzeugt die Screenshots für die Anton-Benutzerdokumentation.
// Voraussetzung: DDEV läuft, kr-Testarchiv unter kr.anton.ddev.site, Testuser `editor`.
// Aufruf:  node docshots.mjs
import { chromium } from '/Users/ak/Sites/anton.test/node_modules/playwright/index.mjs';

const BASE = process.env.BASE || 'https://kr.anton.ddev.site';
const OUT = process.env.OUT || '/Users/ak/Sites/anton-documentation/docs/user/images';

const browser = await chromium.launch();
const ctx = await browser.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1280, height: 900 }, locale: 'de-CH' });
const page = await ctx.newPage();

const clean = async () => {
  await page.waitForTimeout(1500);
  await page.addStyleTag({ content: '.phpdebugbar { display: none !important; }' });
};

// Anmelden
await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded' });
const form = page.locator('form').filter({ has: page.locator('input[name="username"]:visible') }).first();
await form.locator('input[name="username"]').fill('editor');
await form.locator('input[name="password"]').fill('editor');
await Promise.all([page.waitForLoadState('networkidle'), form.locator('input[type="submit"], button[type="submit"]').first().click()]);

// Bearbeitungsmaske einer Verzeichnungseinheit (KRA 1/1, Einzelstück)
await page.goto(`${BASE}/objects/20/edit`, { waitUntil: 'domcontentloaded' });
await clean();
await page.screenshot({ path: `${OUT}/erschliessen-edit.png`, fullPage: true });
console.log('✓ erschliessen-edit.png');

// Fenster "Neue Datensätze erstellen"
await page.goto(`${BASE}/objects/20`, { waitUntil: 'domcontentloaded' });
await clean();
const neu = page.locator('a,button').filter({ hasText: /^\s*Neu\s*$/ }).first();
if (await neu.count()) {
  await neu.click();
  await page.waitForTimeout(800);
  const modal = page.locator('.modal.show .modal-dialog').first();
  if (await modal.count()) {
    await modal.screenshot({ path: `${OUT}/erschliessen-neu.png` });
    console.log('✓ erschliessen-neu.png');
  } else {
    console.log('! Modal "Neu" nicht sichtbar geworden');
  }
} else {
  console.log('! Taste "Neu" nicht gefunden');
}

await browser.close();
