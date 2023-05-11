import re
from types import CellType
erro = ""
try:
    nome = input("Digite seu nome: ")
    if re.search("\d", nome):
        erro = "Nomes não podem conter números"
        raise ValueError
    cep = input("Digite seu CEP: ")
    if not re.search("\d{8}", cep) or len(cep) > 8:
        erro = "CEP deve conter 8 dígitos"
        raise ValueError
    print(f"Nome: {nome}\nCEP: {cep}")
except ValueError:
    print(erro)
finally:
    print("Fim do programa")