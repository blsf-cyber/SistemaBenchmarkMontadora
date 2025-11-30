# CI/CD - Integração e Deploy Contínuo

## Visão Geral

O projeto utiliza GitHub Actions para automatizar o processo de CI/CD. O workflow executa automaticamente a cada push ou pull request nas branches `main` e `develop`.

## Workflow CI/CD

### Arquivo de Configuração
- Localização: `.github/workflows/ci.yml`
- Triggers: Push e Pull Request nas branches `main` e `develop`

### Job: Build e Testes

O workflow possui um único job que executa os seguintes passos:

1. Checkout do código
2. Configura Node.js v20
3. Instala dependências com `npm ci`
4. Executa testes automatizados com `npm test`

## Testes Automatizados

### Framework
- Jest para testes JavaScript
- html-validate para validação de HTML

### Cobertura de Testes

Os testes validam:
- Estrutura HTML das páginas (index, cadastro, lista)
- Existência de elementos essenciais (formulários, botões, campos)
- Funcionalidades de exclusão e navegação
- Presença de arquivos críticos
- Configuração do Dockerfile

Threshold mínimo: 50% de cobertura. Relatórios gerados em `frontend/coverage/`.

## Como Executar Localmente

```bash
cd frontend
npm install
npm test
```

## Verificar Status no GitHub

1. Acesse a aba Actions no GitHub
2. Selecione o workflow CI/CD Pipeline
3. Visualize execuções por branch/commit

Status:
- Verde: todos os testes passaram
- Vermelho: falha detectada
- Amarelo: execução em andamento

## Configuração

Nenhuma variável de ambiente ou secret é necessária. O workflow requer apenas permissões padrão de leitura do repositório.

## Manutenção

Para atualizar dependências:
```bash
cd frontend
npm update
npm audit fix
```

Para modificar o workflow, edite `.github/workflows/ci.yml`.

Para adicionar testes, crie arquivos `*.test.js` em `frontend/tests/`.

## Troubleshooting

Testes falhando:
- Execute `npm test` localmente
- Verifique logs do Jest
- Confirme estrutura HTML

Build Docker falhando:
- Valide Dockerfile localmente
- Confirme presença de arquivos public/
- Teste: `docker build -t test ./frontend`
