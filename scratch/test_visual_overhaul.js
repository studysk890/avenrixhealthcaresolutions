const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8117;
const ROOT = 'C:\\Users\\SK\\Documents\\avenrixhealthcaresolutions';
const ARTIFACT_DIR = 'C:\\Users\\SK\\.gemini\\antigravity\\brain\\c1b884bb-af26-47d8-b057-656fb701cda0';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.otf': 'font/otf',
  '.ttf': 'font/ttf',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2'
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
  console.log(`[Visual Overhaul QA Server] Listening on http://127.0.0.1:${PORT}`);
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const userDataDir = path.join(ARTIFACT_DIR, 'scratch', 'chrome_profile_vo_' + Date.now());
  const cdpPort = 9267;

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
    const networkFailures = [];
    const consoleEntries = [];

    ws.onmessage = (evt) => {
      const msg = JSON.parse(evt.data);
      if (msg.id && pending.has(msg.id)) {
        const { resolve, reject } = pending.get(msg.id);
        pending.delete(msg.id);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      } else if (msg.method === 'Console.messageAdded') {
        consoleEntries.push(msg.params.message);
      } else if (msg.method === 'Runtime.consoleAPICalled') {
        consoleEntries.push({
          type: msg.params.type,
          text: msg.params.args.map(a => a.value || a.description).join(' ')
        });
      } else if (msg.method === 'Network.responseReceived') {
        const { response } = msg.params;
        if (response.status >= 400) {
          networkFailures.push({ url: response.url, status: response.status });
        }
      } else if (msg.method === 'Network.loadingFailed') {
        networkFailures.push({ url: msg.params.requestId, error: msg.params.errorText });
      }
    };

    function send(method, params = {}) {
      return new Promise((resolve, reject) => {
        const callId = id++;
        pending.set(callId, { resolve, reject });
        ws.send(JSON.stringify({ id: callId, method, params }));
      });
    }

    // Enable domains
    await send('Network.enable');
    await send('Console.enable');
    await send('Runtime.enable');
    await send('Page.enable');

    console.log('\n--- 1. LOADING PAGE ---');
    await send('Page.navigate', { url: `http://127.0.0.1:${PORT}/index.html` });
    await new Promise(r => setTimeout(r, 2000));

    console.log(`Network Failures: ${networkFailures.length}`);
    console.log(`Console Entries: ${consoleEntries.length}`);

    // Helper: Take screenshot of selector
    async function screenshotElement(selector, filename) {
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

      await new Promise(r => setTimeout(r, 1000));
      const box = evalRes.result.value;
      if (!box) {
        console.error(`Element not found: ${selector}`);
        return;
      }

      const capture = await send('Page.captureScreenshot', {
        format: 'png',
        clip: {
          x: Math.max(0, box.x),
          y: Math.max(0, box.y),
          width: Math.min(1920, box.width),
          height: box.height,
          scale: 1
        }
      });

      const filePath = path.join(ARTIFACT_DIR, filename);
      fs.writeFileSync(filePath, Buffer.from(capture.data, 'base64'));
      console.log(`Saved screenshot: ${filename} (${box.width}x${box.height})`);
    }

    // Take Desktop Screenshots
    console.log('\n--- CAPTURING DESKTOP SCREENSHOTS ---');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await new Promise(r => setTimeout(r, 400));
    await screenshotElement('#home', 'vo_desktop_hero.png');
    await screenshotElement('#values', 'vo_desktop_values.png');
    await screenshotElement('#contact', 'vo_desktop_contact.png');

    // 2. Viewport Overflow Check across 8 Key Viewports
    console.log('\n--- 2. VIEWPORT OVERFLOW AUDIT ---');
    const viewports = [
      { name: 'Desktop 1920x1080', width: 1920, height: 1080, dsf: 1 },
      { name: 'Desktop 1440x900', width: 1440, height: 900, dsf: 1 },
      { name: 'Desktop 1366x768', width: 1366, height: 768, dsf: 1 },
      { name: 'Desktop 1024x768', width: 1024, height: 768, dsf: 1 },
      { name: 'Tablet 768x1024', width: 768, height: 1024, dsf: 2 },
      { name: 'Mobile 390x844', width: 390, height: 844, dsf: 3 },
      { name: 'Mobile 375x812', width: 375, height: 812, dsf: 3 },
      { name: 'Mobile Landscape 844x390', width: 844, height: 390, dsf: 3 }
    ];

    for (const vp of viewports) {
      await send('Emulation.setDeviceMetricsOverride', {
        width: vp.width,
        height: vp.height,
        deviceScaleFactor: vp.dsf,
        mobile: vp.width < 992
      });
      await new Promise(r => setTimeout(r, 350));

      const evalRes = await send('Runtime.evaluate', {
        expression: `({
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          innerWidth: window.innerWidth,
          hasOverflow: document.documentElement.scrollWidth > window.innerWidth
        })`,
        returnByValue: true
      });

      const { scrollWidth, innerWidth, hasOverflow } = evalRes.result.value;
      console.log(`[${vp.name}]: innerWidth=${innerWidth}px, scrollWidth=${scrollWidth}px -> ${hasOverflow ? 'FAIL: Overflow detected!' : 'PASS: 0px overflow'}`);
    }

    // 3. Contact Form Test (Validation + Submission + Reset)
    console.log('\n--- 3. FORM VALIDATION & SUBMISSION TEST ---');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await new Promise(r => setTimeout(r, 300));

    const formAudit = await send('Runtime.evaluate', {
      expression: `(() => {
        const form = document.getElementById('avxContactForm');
        const successBlock = document.getElementById('avxContactSuccess');
        const nameInput = document.getElementById('avxContactName');
        const emailInput = document.getElementById('avxContactEmail');
        const phoneInput = document.getElementById('avxContactPhone');
        const submitBtn = document.getElementById('avxContactSubmit');
        const resetBtn = document.getElementById('avxContactReset');

        // Test empty submit
        submitBtn.click();
        const nameErrorBefore = document.getElementById('avxNameError').textContent;
        const isNameInvalid = nameInput.getAttribute('aria-invalid') === 'true';

        // Fill valid credentials
        nameInput.value = 'Dr. Sarah Chen';
        emailInput.value = 's.chen@apexhealth.com';
        phoneInput.value = '+1 555 892 4110';
        
        // Submit valid form
        submitBtn.click();
        const isFormHidden = form.classList.contains('is-hidden');
        const isSuccessVisible = successBlock.classList.contains('is-visible');

        // Reset
        resetBtn.click();
        const isFormRestored = !form.classList.contains('is-hidden');
        const isSuccessHidden = !successBlock.classList.contains('is-visible');

        return {
          validationTriggered: isNameInvalid && !!nameErrorBefore,
          formSubmittedSuccessfully: isFormHidden && isSuccessVisible,
          formRestoredCleanly: isFormRestored && isSuccessHidden
        };
      })()`,
      returnByValue: true
    });
    console.log('Form Flow Results:', JSON.stringify(formAudit.result.value, null, 2));
    console.log(`Console Entries after form interactions: ${consoleEntries.length}`);

    console.log('\n--- QA COMPLETE ---');
    ws.close();
  } catch (err) {
    console.error('QA Test Error:', err);
  } finally {
    chrome.kill();
    server.close();
    process.exit(0);
  }
});
