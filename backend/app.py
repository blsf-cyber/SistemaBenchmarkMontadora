from flask import Flask, request, jsonify, render_template
import os
from src.db_utils import carregar_ideias, salvar_ideias, DB_PATH

from flask_cors import CORS, cross_origin

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend', 'public')
app = Flask(__name__, template_folder=template_dir)
CORS(app)

@app.route('/')

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


@app.route('/api/ideias/status', methods=['PUT', 'OPTIONS'])
@cross_origin()
def alterarStatusIdeia():
    """Altera apenas o status de uma ideia (Aprovar/Cancelar aprovação)"""
    dados = request.get_json()

    # Validação
    if not dados or 'id' not in dados or 'status' not in dados:
        return jsonify({"message": "ID e status são obrigatórios."}), 400

    ideias = carregar_ideias()
    ideia_id = dados['id']
    novo_status = dados['status']

    # Busca a ideia pelo ID
    ideia_encontrada = None
    for ideia in ideias:
        if ideia['id'] == ideia_id:
            ideia_encontrada = ideia
            break

    if not ideia_encontrada:
        return jsonify({"message": "Ideia não encontrada."}), 404

    # Atualiza o status
    ideia_encontrada['status'] = novo_status
    salvar_ideias(ideias)

    return jsonify({"message": f"Status alterado para: {novo_status}", "ideia": ideia_encontrada}), 200


@app.route('/api/ideias/<int:ideia_id>', methods=['DELETE', 'OPTIONS'])
@cross_origin()
def removerIdeia(ideia_id):
    """Remove uma ideia completamente"""
    ideias = carregar_ideias()

    # Busca a ideia pelo ID
    ideia_encontrada = None
    for ideia in ideias:
        if ideia['id'] == ideia_id:
            ideia_encontrada = ideia
            break

    if not ideia_encontrada:
        return jsonify({"message": "Ideia não encontrada."}), 404

    # Remove a ideia
    ideias = [ideia for ideia in ideias if ideia['id'] != ideia_id]
    salvar_ideias(ideias)

    return jsonify({"message": "Ideia removida com sucesso!"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)