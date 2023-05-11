import re
erro = ""
formato_telefone = ""
try:
    nome = input("Digite seu nome: ")

    if re.search("\d", nome):
        erro = "O nome não pode conter dígitos"
        raise ValueError
    
    celular = input("Digite seu numero de celular: ")

    if re.search("\D", celular):
        erro = "Não é permitido letras no numero"
        raise ValueError
        
    if len(celular) > 11:
        erro = "O numero ultrapassa a quantidade permitida"
        raise ValueError
            
    else:
        formato_telefone = re.sub(r"^(\d{2})(\d{5})(\d{4})$", r"(\1) \2-\3", celular)

    print(f"Nome: {nome} Numero: {formato_telefone}")
    

except ValueError:
    print(erro)
finally:
    print("Fim do programa")