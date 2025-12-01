# Relatório de Gerenciamento de Configuração de Software (SCM)

## 1. Estratégia de Branching
Adotamos o modelo GitFlow para garantir estabilidade, isolamento e rastreabilidade:
- **`main`:** Branch estável e imutável. Reflete a versão de produção (Tags de Release, ex: ```v1.1.0```). Recebe merges da develop-main.
- **`develop-main`:** Branch de integração contínua (CI). Todo o desenvolvimento de features é mesclado aqui, onde os testes de integração são executados antes de ir para a ```main```.
- **`feature/*`:** Branches de trabalho para o desenvolvimento de novas funcionalidades (ex: `feature/implementa-cadastro-ideias`).
- **Revisão de Código:** Todos os merges de ```feature/*``` para develop-main foram realizados via Pull Request
e exigiram ao menos uma aprovação de um revisor.

## 2. Versionamento Semântico
Utilizamos o seguinte padrão para releases:
- **v0.1.0:** Versão de setup inicial.
- **v1.0.0:** Marca a primeira entrega funcional (Cadastro e Arquitetura Base).
- **v1.1.0:** Marca a inclusão de novas funcionalidades (Aprovação/Exclusão).

## 3. Convenção de Commits
A rastreabilidade foi garantida pela vinculação de Commits/PRs com as Issues correspondentes (ex: ```closes #5```).
Utilizamos a convenção `tipo(escopo): mensagem` para um histórico limpo:
- **`feat:`:** Nova funcionalidade (ex: `feat: implementa api de cadastro`).
- **`fix:`:** Correção de bug ou de merge (ex: `fix: corrige conflito no gitignore`).
- **`refactor:`:** Mudança na estrutura do código sem alterar o comportamento externo (ex: `refactor(arch): move codigo para backend/`).
- **`docs:`:** Alterações em arquivos de documentação (ex: `docs: atualiza CHANGELOG`).

## 4. Procedimentos de Build e CI/CD
O projeto utiliza GitHub Actions para automação e validação contínua (conforme detalhado no ```docs/CI-CD.md```).
* **Validação em PR:** O workflow é executado a cada Pull Request na branch ```develop-main```.
* **Testes:** O pipeline executa o Pytest para validar o código Python (```backend/```) e o Jest para testes de frontend.

## 5. Lições Aprendidas e Reflexões Individuais
Esta seção resume os desafios encontrados e como a equipe aplicou as práticas de SCM para superá-los.

### Bruna Fortes
**Pápeis principais:** ```Gerente de Configuração``` e ```Resp. por Build/CI```
**Reflexões:** 

### Diego Silva
**Pápeis principais** ```Desenvolvedor``` e ```Testador```
**Reflexões:** O projeto representou um desafio significativo na curva de aprendizado e adaptação. No início, senti uma dificuldade de entender e seguir o processo de SCM, cometendo alguns erros ainda. No entanto, ao longo do projeto fui realizando pesquisas e esclarecendo melhor os conceitos para poder aplicar de forma mais assertiva.
Entre os aprendizados estão:
* O aprendizado sobre o uso prático de Flask e a necessidade de estruturar a aplicação.
* O desafio arquitetural de mover o código Python para a pasta ```backend/``` ensinou a importância da separação de responsabilidades e a complexidade de corrigir todos os erros de referência resultantes.
* O entendimento do fluxo hierárquico (```feature``` $\rightarrow$ ```develop-main``` $\rightarrow$ ```main```) se consolidou ao resolver os erros de merge. O problema de duplicação de arquivos na raiz após um merge (que exigiu o uso de ```git rm``` e commits de correção) foi um dos obstáculos práticos.

O processo foi um aprendizado contínuo, onde cada erro nos ajudou a adequar as práticas ao máximo, valorizando a rastreabilidade e a limpeza do histórico acima de tudo e entendendo na prática a importância do SCM.

### Izaac Moraes
**Pápeis principais** ```Testador``` e ```Gerente de Configuração```
**Reflexões:**

### Mateus Lourenço
**Pápeis principais** ```Desenvolvedor``` e ```Resp. por Build/CI```
**Reflexões:** Durante o desenvolvimento deste projeto, pude consolidar diversas competências importantes que ampliaram minha visão sobre a criação e manutenção de aplicações modernas. Trabalhar com interfaces de tela trouxe aprendizados valiosos sobre organização, estruturação e boas práticas de desenvolvimento front-end, enquanto os desafios de integração e deployment aprofundaram meu entendimento sobre ferramentas de versionamento, containerização e automação. Aprendi a construir páginas utilizando HTML, criar e manipular containers para isolar serviços e gerar imagens portáveis, além de versionar e publicar essas imagens na nuvem. Também evoluí na utilização de pipelines de CI/CD e no versionamento de código de forma profissional, garantindo entregas mais ágeis e controladas. Outro ponto marcante foi a experiência de colaboração em equipe, que me proporcionou um contexto real de trabalho e reforçou a importância da comunicação, organização e cooperação para o sucesso coletivo. Esses aprendizados, em conjunto, representam um avanço significativo na minha maturidade técnica e profissional.
