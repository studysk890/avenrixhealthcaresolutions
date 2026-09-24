const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

console.log('=== SVG ACCESSIBILITY AUDIT ===');
const svgMatches = [...html.matchAll(/<svg([^>]*)>/g)];
console.log('Total SVGs found:', svgMatches.length);

let missingAria = 0;
svgMatches.forEach((m, i) => {
  const attrs = m[1];
  const hasAriaHidden = attrs.includes('aria-hidden="true"');
  const hasRoleImg = attrs.includes('role="img"');
  const hasAriaLabel = attrs.includes('aria-label=');
  if (!hasAriaHidden && !hasRoleImg && !hasAriaLabel) {
    console.log(`SVG #${i + 1} missing aria: ${m[0]}`);
    missingAria++;
  }
});
console.log('SVGs missing aria attributes:', missingAria);

console.log('\n=== FORM ACCESSIBILITY AUDIT ===');
const inputs = [...html.matchAll(/<(input|select|textarea)([^>]*)>/g)];
console.log('Total Form Controls:', inputs.length);
inputs.forEach((inp, i) => {
  const tag = inp[1];
  const attrs = inp[2];
  const idMatch = attrs.match(/id="([^"]+)"/);
  const id = idMatch ? idMatch[1] : 'NO_ID';
  const hasAria = attrs.includes('aria-');
  console.log(`Control #${i + 1} <${tag} id="${id}"> - hasAria: ${hasAria}`);
});

console.log('\n=== BUTTON ACCESSIBILITY AUDIT ===');
const buttons = [...html.matchAll(/<button([^>]*)>/g)];
console.log('Total Buttons:', buttons.length);
buttons.forEach((btn, i) => {
  const attrs = btn[1];
  console.log(`Button #${i + 1}: ${attrs}`);
});
