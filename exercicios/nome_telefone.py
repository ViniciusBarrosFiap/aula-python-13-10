from mailbox import NotEmptyError
import re
from this import d
erro = ""
try:
    nome = input("Digite seu nome: ")

    if re.search("\d", nome):
        erro = "O nome não pode conter dígitos"
        raise ValueError
    
    celular = input("Digite seu numero de celular: ")

    if re.search("\D", celular) or len(celular) > 14:
        erro = "O numero de celular pode conter apenas números"
        raise ValueError
    print(f"Nome: {nome} Numero: ")
except ValueError:
    print(erro)