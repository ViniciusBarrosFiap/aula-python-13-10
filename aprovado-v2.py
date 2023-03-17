media = float(input("Digite sua média final: "))
if media >= 6:
    print("Aprovado")
elif media <= 5.9 and media >= 5:
    print("Recuperação")

elif media < 5:
    print("Reprovado")