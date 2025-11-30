import pytest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, salvar_ideias, carregar_ideias
from src.db_utils import carregar_ideias, salvar_ideias, DB_PATH

# Define o caminho do arquivo JSON de TESTE, diferente do DB_PATH original
TEST_DB_PATH = 'backend/data/test_ideias.json'

@pytest.fixture
def client():
    """Configura o cliente de teste do Flask para cada teste."""
    app.config['TESTING'] = True
    
    # Sobrescreve o caminho do DB para o teste
    original_db_path = DB_PATH
    
    # Altera a variável global no módulo db_utils
    # Uso do atributo de módulo para garantir que a alteração seja temporária
    import src.db_utils
    src.db_utils.DB_PATH = TEST_DB_PATH
    
    with app.test_client() as client:
        if not os.path.exists('backend/data'):
            os.makedirs('backend/data')
            
        # Limpeza antes de cada teste
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)
        
        yield client # Executa teste

    # Limpeza e restauração após o teste
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    # Restaura o caminho do DB para o valor original após o teste
    src.db_utils.DB_PATH = original_db_path


def test_salvar_e_carregar_ideias(client):
    """Verifica se as ideias são salvas no JSON e carregadas corretamente."""
    
    ideias_iniciais = carregar_ideias()
    assert len(ideias_iniciais) == 0

    dados_teste = [{"id": 1, "ideia": "Teste SCM"}]
    salvar_ideias(dados_teste)
    
    ideias_carregadas = carregar_ideias()
    assert len(ideias_carregadas) == 1
    assert ideias_carregadas[0]['ideia'] == "Teste SCM"


def test_cadastro_ideia_sucesso(client):
    """Testa o cadastro de uma ideia válida via endpoint POST."""
    dados_validos = {
        "sistema": "Transmissao",
        "componente": "Sensor",
        "ideia": "Reduzir peso"
    }
    
    response = client.post('/api/ideias/cadastro', 
                           data=json.dumps(dados_validos),
                           content_type='application/json')
    
    # Testa o código de retorno HTTP
    assert response.status_code == 200 
    
    # Testa a mensagem de sucesso
    assert b"Ideia cadastrada com sucesso!" in response.data
    
    # Verifica se a ideia foi salva
    ideias = carregar_ideias()
    assert len(ideias) == 1
    assert ideias[0]['componente'] == "Sensor"
    assert ideias[0]['status'] == "Aguardando Aprovação" # Verifica o campo de rastreabilidade


def test_cadastro_ideia_falha_inputs(client):
    """Testa a falha de validação (Lógica de Rever Inputs - Requisito)."""
    # Dados com componente vazio (falha esperada)
    dados_invalidos = {
        "sistema": "Transmissao",
        "componente": "", 
        "ideia": "Reduzir peso"
    }
    
    response = client.post('/api/ideias/cadastro', 
                           data=json.dumps(dados_invalidos),
                           content_type='application/json')
    
    # Testa o código de retorno HTTP (400 Bad Request para falha de validação)
    assert response.status_code == 400 
    
    # Testa a mensagem de erro
    response_json = response.get_json()
    assert "Todos os campos são obrigatórios." in response_json['message']

    # Verifica que NENHUMA ideia foi salva
    ideias = carregar_ideias()
    assert len(ideias) == 0