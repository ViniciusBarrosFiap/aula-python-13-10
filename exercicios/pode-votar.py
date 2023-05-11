idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Obrigátorio ir votar")

elif idade >= 16 and idade < 18:
    print ("Você pode votar, mas não obrigátorio")

else:
    print("Não pode votar")