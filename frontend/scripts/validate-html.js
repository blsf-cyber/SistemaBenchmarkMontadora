
const { HtmlValidate } = require('html-validate');
const fs = require('fs');
const path = require('path');

const htmlvalidate = new HtmlValidate({
  extends: ['html-validate:recommended'],
  rules: {
    'no-inline-style': 'off',
    'require-sri': 'off',
    'no-trailing-whitespace': 'off'
  }
});

const publicDir = path.join(__dirname, '../public');
const htmlFiles = [
  'index.html',
  'cadastroIdeias.html',
  'listaIdeias.html'
];

let hasErrors = false;

console.log('🔍 Validando arquivos HTML...\n');

htmlFiles.forEach(file => {
  const filePath = path.join(publicDir, file);
  
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Arquivo não encontrado: ${file}`);
    hasErrors = true;
    return;
  }
  
  const content = fs.readFileSync(filePath, 'utf-8');
  const report = htmlvalidate.validateString(content);
  
  if (report.valid) {
    console.log(`✅ ${file} - Válido`);
  } else {
    console.log(`⚠️  ${file} - Avisos encontrados:`);
    report.results.forEach(result => {
      result.messages.forEach(msg => {
        console.log(`   Linha ${msg.line}: ${msg.message}`);
      });
    });
  }
});

console.log('\n✓ Validação HTML concluída\n');

if (hasErrors) {
  process.exit(1);
}
