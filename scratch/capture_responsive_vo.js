const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8119;
const ROOT = 'C:\\Users\\SK\\Documents\\avenrixhealthcaresolutions';
const ARTIFACT_DIR = 'C:\\Users\\SK\\.gemini\\antigravity\\brain\\c1b884bb-af26-47d8-b057-656fb701cda0';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.otf': 'font/otf',
  '.ttf': 'font/ttf'
};

const server = http.createServer((req, res) => {
  let reqPath = decodeURIComponent(req.url.split('?')[0]);
  if (reqPath === '/') reqPath = '/index.html';
  if (reqPath === '/favicon.ico') reqPath = '/images/Avenrix Logo Vertical.png';
  const filePath = path.join(ROOT, reqPath.replace(/\//g, path.sep));
  if (fs.existsSync(filePath)) {
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end();
  }
});

server.listen(PORT, async () => {
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const userDataDir = path.join(ARTIFACT_DIR, 'scratch', 'chrome_profile_resp_' + Date.now());
  const cdpPort = 9269;

  const chrome = spawn(chromePath, [
    '--headless=new',
    `--remote-debugging-port=${cdpPort}`,
    `--user-data-dir=${userDataDir}`,
    '--no-first-run',
    '--no-default-browser-check',
    '--disable-gpu',
    '--window-size=1920,1080'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch(`http://127.0.0.1:${cdpPort}/json/list`);
    const targets = await listRes.json();
    const pageTarget = targets.find(t => t.type === 'page') || targets[0];
    const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
    await new Promise(r => ws.onopen = r);

    let id = 1;
    const pending = new Map();
    ws.onmessage = (evt) => {
      const msg = JSON.parse(evt.data);
      if (msg.id && pending.has(msg.id)) {
        const { resolve, reject } = pending.get(msg.id);
        pending.delete(msg.id);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };

    function send(method, params = {}) {
      return new Promise((resolve, reject) => {
        const callId = id++;
        pending.set(callId, { resolve, reject });
        ws.send(JSON.stringify({ id: callId, method, params }));
      });
    }

    await send('Page.enable');
    await send('Page.navigate', { url: `http://127.0.0.1:${PORT}/index.html` });
    await new Promise(r => setTimeout(r, 2000));

    async function screenshotElement(selector, filename, width, height, dsf, mobile) {
      await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: dsf, mobile });
      await new Promise(r => setTimeout(r, 300));

      const evalRes = await send('Runtime.evaluate', {
        expression: `(() => {
          const el = document.querySelector('${selector}');
          if (!el) return null;
          el.scrollIntoView({ behavior: 'instant', block: 'start' });
          const rect = el.getBoundingClientRect();
          return { x: rect.left + window.scrollX, y: rect.top + window.scrollY, width: rect.width, height: rect.height };
        })()`,
        returnByValue: true
      });

      await new Promise(r => setTimeout(r, 800));
      const box = evalRes.result.value;
      if (!box) return;

      const capture = await send('Page.captureScreenshot', {
        format: 'png',
        clip: {
          x: Math.max(0, box.x),
          y: Math.max(0, box.y),
          width: Math.min(width, box.width),
          height: box.height,
          scale: 1
        }
      });

      const filePath = path.join(ARTIFACT_DIR, filename);
      fs.writeFileSync(filePath, Buffer.from(capture.data, 'base64'));
      console.log(`Saved screenshot: ${filename}`);
    }

    // Tablet 768x1024
    await screenshotElement('#home', 'vo_tablet_hero.png', 768, 1024, 2, true);
    await screenshotElement('#values', 'vo_tablet_values.png', 768, 1024, 2, true);
    await screenshotElement('#contact', 'vo_tablet_contact.png', 768, 1024, 2, true);

    // Mobile 390x844
    await screenshotElement('#home', 'vo_mobile_hero.png', 390, 844, 3, true);
    await screenshotElement('#values', 'vo_mobile_values.png', 390, 844, 3, true);
    await screenshotElement('#contact', 'vo_mobile_contact.png', 390, 844, 3, true);

    console.log('Responsive captures complete.');
    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    server.close();
    process.exit(0);
  }
});
