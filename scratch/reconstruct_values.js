const fs = require('fs');

const logPath = 'C:\\Users\\SK\\.gemini\\antigravity\\brain\\c1b884bb-af26-47d8-b057-656fb701cda0\\.system_generated\\logs\\transcript_full.jsonl';
const lines = fs.readFileSync(logPath, 'utf8').split('\n');

// 1. Get base from step 347
let baseObj = JSON.parse(lines[347]);
let code = baseObj.tool_calls[0].args.CodeContent;
console.log('Step 347 base code length:', code.length, 'lines:', code.split('\n').length);

const editSteps = [376, 382, 384, 397, 594, 1026, 1030];
for (const step of editSteps) {
  const obj = JSON.parse(lines[step]);
  const args = obj.tool_calls[0].args;
  console.log(`Applying step ${step}: ${args.Description || args.Instruction}`);
  if (code.includes(args.TargetContent)) {
    code = code.replace(args.TargetContent, args.ReplacementContent);
    console.log(`  -> Applied successfully. New lines: ${code.split('\n').length}`);
  } else {
    console.error(`  -> ERROR: TargetContent not found for step ${step}!`);
  }
}

console.log('Final reconstructed lines:', code.split('\n').length, 'bytes:', Buffer.byteLength(code, 'utf8'));
fs.writeFileSync('scratch/reconstructed_values.css', code, 'utf8');
