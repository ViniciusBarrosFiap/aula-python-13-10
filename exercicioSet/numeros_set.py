#RM97824 - Vinicius Oliveira de Barros
numeros = {0}
tipo_numero_usuario = input('''Escolha um tipo de número para digitar\n
"R" para numeros REAIS
"I" para números INTEIROS\n''').upper()

if tipo_numero_usuario == "R":
    tipo_numero_usuario = "REAL"

elif tipo_numero_usuario == "I":
    tipo_numero_usuario = "INTEIRO"

else:
    print("Escolha um tipo de número válido")

maior_numero = 0
numeros.remove(0)
print(numeros)
while len(numeros) < 10:
    try:
        if tipo_numero_usuario == "REAL":
            numeros_usuario = float(input("DIgite um número REAL: "))
            numeros.add(numeros_usuario)
            for i in numeros:
               if i >= maior_numero:
                   maior_numero = i

        elif tipo_numero_usuario == "INTEIRO":
            numeros_usuario = int(input("Digite um numero INTEIRO: "))
            numeros.add(numeros_usuario)
            for i in numeros:
               if i >= maior_numero:
                   maior_numero = i
        else:
            raise ValueError
    except ValueError:
        print("Digite um valor válido")

print(f"Você escolheu digitar números do tipo: {tipo_numero_usuario}")
print(f"O maior número digitado foi: {maior_numero}")
