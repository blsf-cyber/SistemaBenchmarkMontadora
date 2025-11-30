import json
import os

# Caminho global que será usado pelo app.py e sobrescrito pelos testes
DB_PATH = 'backend/data/ideias.json'

def carregar_ideias():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_ideias(ideias):
    with open(DB_PATH, 'w') as f:
        json.dump(ideias, f, indent=4)