#RM97824 - Vinicius Oliveira de Barros

try:
    fraseNova = input("Digite outro ditado popular: ")
    f = open("exercicioManipulaArquivo/exercicio1.txt", "a", encoding="utf-8")
    f.write(f"\n{fraseNova}")
    f.close()
    f = open("exercicioManipulaArquivo/exercicio1.txt", "r", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("O arquivo não existe")
