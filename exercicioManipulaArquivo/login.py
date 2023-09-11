#RM97824 - Vinicius Oliveira de Barros
print("LOGIN")
user = input("Digite seu user: ")
senha = input("Digite sua senha: ")
usuario = "D:/usuarios/Vini1.txt"
arquivo = open(f"{usuario}", "r")
primeira_linha = arquivo.readline()
if user and senha in arquivo.read():
    print(f"Bem vindo {primeira_linha}")
else:
    print("Acesso inválido")
