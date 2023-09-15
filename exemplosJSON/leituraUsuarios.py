import json
import os
try:
    usuarios = {}
    if os.path.exists("d:/usuarios.json"):
        with open('d:/usuarios.json', 'r') as f:
            usuarios = json.loads(f.read())
    print(usuarios)
except FileNotFoundError:
    print("Caminho e/ou arquivo inexistente!")