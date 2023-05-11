soma = 0
for i in range(1, 31):
    notas = float(input("Digite a nota do aluno: "))

    soma += notas

media = soma / 30
print(media)