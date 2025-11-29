from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder='frontend/public')
DB_PATH = 'data/ideias.json'

def carregar_ideias():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        # Tenta carregar, senão retorna lista vazia
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_ideias(ideias):
    with open(DB_PATH, 'w') as f:
        json.dump(ideias, f, indent=4)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro_ideia():
    return render_template('cadastroIdeias.html')

@app.route('/ideias')
def ideias_page():
    return render_template('listaIdeias.html')

@app.route('/api/ideias/cadastro', methods=['POST'])
def cadastrar_ideia():
    dados = request.get_json()

    # Validação (Lógica de Rever Inputs)
    if not dados or not dados.get('sistema') or not dados.get('componente') or not dados.get('ideia'):
        return jsonify({"message": "Todos os campos são obrigatórios."}), 400

    ideias = carregar_ideias()
    
    # Gera um ID simples
    novo_id = max([i.get('id', 0) for i in ideias] or [0]) + 1
    
    nova_ideia = {
        "id": novo_id,
        "sistema": dados['sistema'],
        "componente": dados['componente'],
        "ideia": dados['ideia'],
        "status": "Aguardando Aprovação"
    }

    ideias.append(nova_ideia)
    salvar_ideias(ideias)

    return jsonify({"message": "Ideia cadastrada com sucesso!", "id": novo_id}), 200


@app.route('/api/ideias', methods=['GET'])
def listar_ideias():
    return jsonify(carregar_ideias()), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)