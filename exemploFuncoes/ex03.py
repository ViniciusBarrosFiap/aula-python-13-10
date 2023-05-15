def situacao(estado):
    if estado.lower() == "solteiro":
        print("Você é solteiro")
    else:
        print("Você é casado")

ecivil = input("Digite seu estado civil: ")
situacao(ecivil)