const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// For product card images, replace 'loading="lazy"\n              >' with 'loading="lazy"\n                decoding="async"\n              >'
let count = 0;
html = html.replace(/(class="avx-product-card__image"[\s\S]*?loading="lazy")(\s*>)/g, (match, p1, p2) => {
  count++;
  return `${p1}\n                decoding="async"${p2}`;
});

console.log(`Updated ${count} product card images with decoding="async".`);
fs.writeFileSync('index.html', html, 'utf8');
