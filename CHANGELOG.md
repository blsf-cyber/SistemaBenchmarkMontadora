# CHANGELOG

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.
O projeto adota o Versionamento Semântico.

## [v1.1.0] - 2025-11-30

Marca o **Release Minor** com a introdução do **ciclo de vida completo da ideia** (implementando a funcionalidade de **Aprovação/Rejeição**) e uma importante **refatoração de arquitetura**. A refatoração exigiu a **validação dos testes** para garantir que a cobertura de qualidade do *backend* fosse mantida.

### Adicionado
- **Funcionalidade:** Implementação da lógica de Aprovação/Exclusão de Ideias (Backend).
- **Funcionalidade:** Implementação email de login para acesso.
- **Documentação:** Criação do `relatorio.md` detalhando.

### Modificado
- **Arquitetura:** Refatoração estrutural (refactor/arch) movendo todo o código Python/Flask e seus artefatos (tests/, src/, data/) para a pasta **`backend/`**.
- **Setup:** Atualização do Docker e `docker-compose.yml` para suportar a nova arquitetura de pastas.

### Corrigido
- Correção de caminhos relativos de importação pós-refatoração (resolução de conflitos no CI).

## [v1.0.0] - 2025-11-29

Marca o Primeiro Release Funcional da Aplicação (Versão Base).

### Adicionado
- **Funcionalidade:** Implementação do Cadastro de Ideias e persistência em arquivo JSON.
- **Qualidade:** Adição de **Testes Unitários (Pytest)** para validação de *inputs* e persistência de dados.
- **Estrutura:** Configuração inicial da aplicação Flask e Front-end (HTML/JS).
- **SCM:** Configuração inicial dos *pipelines* de CI (GitHub Actions).

## [v0.1.0] - 2025-11-28

Marca a versão de Configuração Inicial do Projeto.

### Adicionado
- Criação do Repositório GitHub e definição das branches (`main`, `develop-main`).
- Criação e aprovação do `README.md` com o Escopo do Projeto.
- Configuração do ambiente virtual (`venv`) e `.gitignore`.