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
        arquivo = open(f"D:/usuarios/{credenciais[1]}.txt", "a")
        arquivo.write(f"{credenciais[0]}\n{credenciais[1]}\n{credenciais[2]}")
        arquivo.close()
        continuar = input("Deseja continuar ?").lower()
main()