carta = {
    "ki": 7400,
    "tecnicas": 6000,
    "velocidade": 66,
    "transformcao": 3
}
print("Caracteristicas:")
for i in carta.keys():
    print(i)

novaCaracteristica = input("Digite o nome da nova caracteristica: ")
novoValor = int(input("Digite o novo valor da caracteristica: "))

carta.update({f"{novaCaracteristica}": f"{novoValor}"})
print(carta)

print("Caracteristicas:")
for i in carta.keys():
    print(i)

escolhaCaracteristica = input("Escolha uma caracteristica: ").lower()

if escolhaCaracteristica in carta.keys():
    print(f"Você escolheu a caracteristica:{escolhaCaracteristica}")
    print(f"Valor da caracteristica:{carta[escolhaCaracteristica]}")
else:
    print("Digite uma caracteristica válida")