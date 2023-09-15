#RM97824 - Vinicius Oliveira de Barros
print("LOGIN")
user = input("Digite seu user: ")
senha = input("Digite sua senha: ")

arquivo = open("D:/Vini1.txt", "r")

for linha in arquivo:
    parte = linha.split(" ")

nomeDeUsuario = parte[1]
senhaUsuario = parte[2]
arquivo.close()
if user == nomeDeUsuario and senha == senhaUsuario:
    print("Acesso concedido")
elif user != nomeDeUsuario and senha == senhaUsuario:
    print("Usuário inválido")
elif user == nomeDeUsuario and senha != senhaUsuario:
    print("Senha inválida")
else:
    print("Acesso negado")
