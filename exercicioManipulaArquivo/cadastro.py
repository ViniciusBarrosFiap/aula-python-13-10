#RM97824 - Vinicius Oliveira de Barros
def credenciaisUsuario():
    nome = input("Digite seu nome: ")
    user = input("Digite seu nome de usuário: ")
    senha = input("Digite uma senha: ")
    listaCredenciais = [nome, user, senha]
    return listaCredenciais

def main():
    continuar = "sim"
    while continuar == "sim":
        credenciais = credenciaisUsuario()
        arquivo = open(f"D:/{credenciais[1]}.txt", "a")
        arquivo.write(f"{credenciais[0]} ")
        arquivo.write(f"{credenciais[1]} ")
        arquivo.write(f"{credenciais[2]}")
        arquivo.close()
        continuar = input("Deseja continuar ?").lower()
main()