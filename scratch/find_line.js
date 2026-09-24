const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
lines.forEach((l, i) => {
  if (l.includes('<svg') && l.includes('width="24"')) {
    console.log(`Line ${i + 1}: ${l}`);
  }
});
