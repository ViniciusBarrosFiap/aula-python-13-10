import json
import os
try:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    usuarios = {}
    if os.path.exists("d:/usuariosCadastrados.json"):
        with open("d:/usuariosCadastrados.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.loads(arquivo.read())
    if login in usuarios:
        print("Login encontrado")
        if senha == usuarios[login]["senha"]:
            print("Acesso concedido")
        else:
            print("Senha inválida")
except FileNotFoundError:
    print("Caminho o/ou arquivo não existe!")