# Sistema de Benchmark de Montadora de Veículo

## Descrição Geral

O sistema tem como objetivo gerenciar e organizar ideias de redução de custos e melhorias relacionadas a sistemas automotivos de outras montadoras. A proposta é centralizar o processo de submissão, avaliação e acompanhamento de iniciativas identificadas através de benchmarking, permitindo que as equipes mantenham um fluxo estruturado de análise e possível implementação dessas oportunidades.

## Tecnologias Utilizadas
Para este projeto, com foco em práticas de SCM e rastreabilidade, utilizaremos as seguintes tecnologias:
* **Linguagem:** Python 3.x
* **Framework Web:** Flask
* **Banco de Dados:** 
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
Certifique-se de ter o Python 3.x e o Git instalados.

1. **Preparação do Ambiente Virtual**
Recomendamos o uso de um ambiente virtual para isolar as dependências:
```bash
# Crie o ambiente virtual (venv)
python3 -m venv venv

# Ative o ambiente virtual em macOS/Linux
source venv/bin/activate  # macOS/Linux

# Ative o ambiente virtual em Windows
venv\Scripts\activate
```

2. **Instalação de Dependências**
Todas as dependências estão listadas no arquivo requirements.txt.
```bash
pip install -r requirements.txt
```
3. **Execução da Aplicação**
Após a instalação, a aplicação pode ser iniciada usando o comando:
```bash
python app.py
```
