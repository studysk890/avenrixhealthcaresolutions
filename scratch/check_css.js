const fs = require('fs');
const path = require('path');

const cssFiles = [
  'css/fonts.css',
  'css/design-system.css',
  'css/header.css',
  'css/hero.css',
  'css/about.css',
  'css/products.css',
  'css/values.css',
  'css/contact.css',
  'css/footer.css'
];

console.log('=== CSS FILES AUDIT ===');
cssFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  console.log(`${file}: ${content.length} bytes, ${content.split('\n').length} lines`);

  // Check matching braces
  const opens = (content.match(/{/g) || []).length;
  const closes = (content.match(/}/g) || []).length;
  if (opens !== closes) {
    console.error(`ERROR in ${file}: Mismatched braces! { = ${opens}, } = ${closes}`);
  }
});
console.log('Brace check complete.');
