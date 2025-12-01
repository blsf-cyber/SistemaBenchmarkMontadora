# Sistema de Benchmark de Montadora de Veículo

## Descrição Geral

O sistema tem como objetivo gerenciar e organizar ideias de redução de custos e melhorias relacionadas a sistemas automotivos de outras montadoras. A proposta é centralizar o processo de submissão, avaliação e acompanhamento de iniciativas identificadas através de benchmarking, permitindo que as equipes mantenham um fluxo estruturado de análise e possível implementação dessas oportunidades.
## Tecnologias Utilizadas

Para este projeto, com foco em práticas de SCM e rastreabilidade, utilizaremos as seguintes tecnologias:
* **Linguagem:** Python 3.12
* **Framework Web:** Flask
* **Banco de Dados:** JSON para simulação 
* **Versionamento:** Git e GitHub.
* **Ambiente:** Docker para ambiente replicável.


## Funcionalidades

### Cadastro de Ideias

Os usuários poderão registrar ideias de redução de custos ou melhorias identificadas em veículos de outras montadoras. Durante o cadastro, será necessário informar:

- Sistema do veículo (Powertrain, Infotainment, Carroceria, entre outros)
- Componentes específicos (ECU, Sensor, Atuador, Display, etc.)
- Descrição da oportunidade de redução de custo ou melhoria identificada

### Aprovação

As ideias submetidas passarão por validação de outro usuário, geralmente um responsável pela área técnica correspondente. Esse processo vai garantir que apenas propostas viáveis e alinhadas aos objetivos do departamento avancem no fluxo.

### Atribuição de Responsável

Após aprovação, cada ideia receberá um responsável designado. Esse profissional ficará encarregado de acompanhar o desenvolvimento, análise de viabilidade ou implementação da iniciativa.

## Configuração e Setup

### Pré-requisitos
Certifique-se de que possui o docker instalado e acesso a internet.

1. **Preparação do container**
```bash
docker compose up --build -d
```

2. **Verificação do estado do container**

```bash
docker ps
```
O container nomeado "mateuscin/sistema_benchmark_montadoras_frontend" e "mateuscin/sistema_benchmark_montadoras_backend" deverão estar no estatus "up * minutes"

```bash
CONTAINER ID   IMAGE                                                    COMMAND                  CREATED         STATUS         PORTS                                         NAMES
96f05908490d   mateuscin/sistema_benchmark_montadoras_frontend:V1.0.0   "/docker-entrypoint.…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp       frontend
8752d387503d   mateuscin/sistema_benchmark_montadoras_backend:V1.0.0    "python app.py"          9 minutes ago   Up 9 minutes   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   backend
```