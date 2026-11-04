const { chromium } = require('playwright');
(async () => {
  const [src, outCurta, outFull] = process.argv.slice(2);
  const b = await chromium.launch();
  for (const [mode, out] of [['curta', outCurta], ['completa', outFull]]) {
    const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
    await pg.goto('file://' + src + '#' + mode + '-1', { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    await pg.pdf({ path: out, width: '1920px', height: '1080px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await pg.close();
  }
  await b.close();
})();
