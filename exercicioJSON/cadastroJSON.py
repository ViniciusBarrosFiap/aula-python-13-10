#Rm97824 - Vinicius Barros
import json
continuar = "sim"
usuario = {}
while continuar == "sim":
    nome = input("Digite seu nome: ")
    login = input("Digite um nome de login: ")
    senha = input("Digite sua senha: ")
    usuario[f"{login}"] = {
        "nome": nome,
        "login": login,
        "senha":senha
    }
    with open("d:/usuariosCadastrados.json", "w") as arquivo:
        json.dump(usuario, arquivo)
    continuar = input("Deseja continuar cadastrando usuários ?\n")