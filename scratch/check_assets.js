const fs = require('fs');
const path = require('path');

const html = fs.readFileSync('index.html', 'utf8');

// Check all src attributes
const srcMatches = [...html.matchAll(/src="([^"]+)"/g)];
console.log('--- SRC ATTRIBUTES ---');
for (const match of srcMatches) {
  const file = match[1];
  const exists = fs.existsSync(file);
  console.log(`${exists ? 'EXISTS' : 'MISSING'}: ${file}`);
}

// Check all href attributes for css/fonts
const hrefMatches = [...html.matchAll(/href="([^"]+)"/g)];
console.log('\n--- HREF ATTRIBUTES ---');
for (const match of hrefMatches) {
  const file = match[1];
  if (file.startsWith('#') || file.startsWith('http') || file.startsWith('mailto:')) {
    console.log(`LINK: ${file}`);
  } else {
    const exists = fs.existsSync(file);
    console.log(`${exists ? 'EXISTS' : 'MISSING'}: ${file}`);
  }
}
