import re
erro = ""
try:
    nome = input("Digite seu nome:")
    if re.search("\d", nome):
        erro = "Erro: Não é permitido números no nome"
        raise ValueError
    print(nome)

    placa = input("Informe sua placa: ").upper()

    if re.search(r"^\(\D{3}\) \d{1} \D{1} \D{2}$", placa):
        print("Sucesso meu amigo, vc foi genio vini")
    else:
        erro = "A placa é inválida"
        raise ValueError
except ValueError:
    print(erro)