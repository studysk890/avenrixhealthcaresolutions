const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8118;
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
  const userDataDir = path.join(ARTIFACT_DIR, 'scratch', 'chrome_profile_dbg_' + Date.now());
  const cdpPort = 9268;

  const chrome = spawn(chromePath, [
    '--headless=new',
    `--remote-debugging-port=${cdpPort}`,
    `--user-data-dir=${userDataDir}`,
    '--no-first-run',
    '--no-default-browser-check',
    '--disable-gpu',
    '--window-size=1440,900'
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

    // Scroll directly to bottom
    await send('Runtime.evaluate', { expression: `window.scrollTo(0, document.body.scrollHeight);` });
    await new Promise(r => setTimeout(r, 1000));

    const checkRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const form = document.getElementById('avxContactForm');
        const rows = document.querySelectorAll('.avx-contact__row');
        const inputs = document.querySelectorAll('.avx-contact__input');
        const submitWrap = document.querySelector('.avx-contact__submit-wrap');
        const success = document.getElementById('avxContactSuccess');
        
        return {
          formClass: form ? form.className : null,
          formComputedStyle: form ? {
            display: window.getComputedStyle(form).display,
            opacity: window.getComputedStyle(form).opacity,
            height: window.getComputedStyle(form).height,
            visibility: window.getComputedStyle(form).visibility
          } : null,
          rowsCount: rows.length,
          inputsCount: inputs.length,
          submitWrapOpacity: submitWrap ? window.getComputedStyle(submitWrap).opacity : null,
          successVisible: success ? success.classList.contains('is-visible') : false
        };
      })()`,
      returnByValue: true
    });

    console.log('FORM DEBUG CHECK:', JSON.stringify(checkRes.result.value, null, 2));

    ws.close();
  } catch (err) {
    console.error('Debug error:', err);
  } finally {
    chrome.kill();
    server.close();
    process.exit(0);
  }
});
