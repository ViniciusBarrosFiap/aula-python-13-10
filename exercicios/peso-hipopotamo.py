peso = 1
soma = 0
gordao = 0
while soma != 100000:
    peso = float(input("Digite o peso do hipopotamo: "))
    soma += peso

    if peso > gordao:
        gordao = peso
    
print(f"O hipopotamo mais gordo é o {gordao}")

print(f"A soma dos pesos é: {soma}")
        