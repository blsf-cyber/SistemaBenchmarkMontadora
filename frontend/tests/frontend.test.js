/**
 * Testes Automatizados - Sistema de Benchmarking
 * 
 * Valida a estrutura e funcionalidades do frontend:
 * - Estrutura HTML das páginas
 * - Elementos de navegação e formulários
 * - Funcionalidades de cadastro e listagem
 * - Integridade de arquivos essenciais
 */

describe('Testes de Frontend - Sistema de Benchmarking', () => {
  
  describe('Página Index', () => {
    let indexContent;
    
    beforeAll(() => {
      const fs = require('fs');
      const path = require('path');
      indexContent = fs.readFileSync(
        path.join(__dirname, '../public/index.html'),
        'utf-8'
      );
    });
    
    test('deve conter título relacionado ao sistema', () => {
      expect(indexContent.toLowerCase()).toMatch(/benchmark|innova|sistema/);
    });
    
    test('deve ter links de navegação', () => {
      expect(indexContent).toContain('cadastroIdeias.html');
      expect(indexContent).toContain('listaIdeias.html');
    });
    
    test('deve ser HTML válido', () => {
      expect(indexContent).toContain('<!DOCTYPE html>');
      expect(indexContent).toContain('<html');
      expect(indexContent).toContain('</html>');
    });
  });
  
  describe('Página de Cadastro de Ideias', () => {
    let cadastroContent;
    
    beforeAll(() => {
      const fs = require('fs');
      const path = require('path');
      cadastroContent = fs.readFileSync(
        path.join(__dirname, '../public/cadastroIdeias.html'),
        'utf-8'
      );
    });
    
    test('deve conter formulário de cadastro', () => {
      expect(cadastroContent).toContain('<form');
    });
    
    test('deve ter campos do formulário', () => {
      expect(cadastroContent.toLowerCase()).toMatch(/sistema|select|input/);
    });
    
    test('deve ter campo para entrada de texto', () => {
      expect(cadastroContent.toLowerCase()).toMatch(/textarea|input/);
    });
    
    test('deve ter botão de envio', () => {
      expect(cadastroContent.toLowerCase()).toMatch(/button|submit|cadastrar|enviar/);
    });
  });
  
  describe('Página de Lista de Ideias', () => {
    let listaContent;
    
    beforeAll(() => {
      const fs = require('fs');
      const path = require('path');
      listaContent = fs.readFileSync(
        path.join(__dirname, '../public/listaIdeias.html'),
        'utf-8'
      );
    });
    
    test('deve conter área para listar ideias', () => {
      expect(listaContent).toContain('<');
      expect(listaContent.toLowerCase()).toMatch(/lista|ideias|div/);
    });
    
    test('deve ter funcionalidade de exclusão', () => {
      expect(listaContent.toLowerCase()).toMatch(/excluir/);
    });
    
    test('deve ter botão de voltar', () => {
      expect(listaContent.toLowerCase()).toMatch(/voltar/);
    });
    
    test('deve ter container de lista', () => {
      expect(listaContent.toLowerCase()).toMatch(/id=\"lista\"|id='lista'/);
    });
  });
  
  describe('Validação de Estrutura de Arquivos', () => {
    test('deve existir index.html', () => {
      const fs = require('fs');
      const path = require('path');
      const exists = fs.existsSync(
        path.join(__dirname, '../public/index.html')
      );
      expect(exists).toBe(true);
    });
    
    test('deve existir cadastroIdeias.html', () => {
      const fs = require('fs');
      const path = require('path');
      const exists = fs.existsSync(
        path.join(__dirname, '../public/cadastroIdeias.html')
      );
      expect(exists).toBe(true);
    });
    
    test('deve existir listaIdeias.html', () => {
      const fs = require('fs');
      const path = require('path');
      const exists = fs.existsSync(
        path.join(__dirname, '../public/listaIdeias.html')
      );
      expect(exists).toBe(true);
    });
    
    test('deve existir Dockerfile', () => {
      const fs = require('fs');
      const path = require('path');
      const exists = fs.existsSync(
        path.join(__dirname, '../Dockerfile')
      );
      expect(exists).toBe(true);
    });
  });
  
  describe('Validação do Dockerfile', () => {
    let dockerfileContent;
    
    beforeAll(() => {
      const fs = require('fs');
      const path = require('path');
      dockerfileContent = fs.readFileSync(
        path.join(__dirname, '../Dockerfile'),
        'utf-8'
      );
    });
    
    test('deve usar imagem nginx', () => {
      expect(dockerfileContent).toContain('nginx');
    });
    
    test('deve copiar arquivos públicos', () => {
      expect(dockerfileContent).toContain('COPY public/');
    });
    
    test('deve expor porta 80', () => {
      expect(dockerfileContent).toContain('EXPOSE 80');
    });
  });
});
