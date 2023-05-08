import re
erro = ""
try:
    nome = input("Digite seu nome:")
    if re.search("\d", nome):
        erro = "Erro: Não é permitido números no nome"
        raise ValueError
    print(nome)

    placa = input("Informe sua placa: ").upper()

    if re.match(r"^[A-Z]{3}\d{1}[A-Z]{1}\d{2}$", placa):
        formato_placa = re.sub(r"^([A-Z]{3})(\d{1})([A-Z]{1})(\d{2})$", r"\1-\2\3\4" ,placa)
    else:
        erro = "A placa é inválida"
        raise ValueError
    print(f"Nome {nome} Placa {formato_placa}")
except ValueError:
    print(erro)