cinquenta, vinte, dez, cinco, um = 0, 0, 0, 0, 0
preco = float(input("Valor a ser pago: "))
valor_pago = float(input("Valor efetivamente pago: "))

troco = valor_pago - preco

if valor_pago < preco:
    print("Valor pago é inferior ao preço")

else:
    while troco > 0:

        if troco >= 50:
            cinquenta = int(troco // 50)
            troco -= (cinquenta * 50)
        
        elif troco >= 20:
            vinte = int(troco // 20)
            troco -= (vinte * 20)
        
        elif troco >= 10:
            dez = int(troco // 10)
            troco -= (dez * 10)
        
        elif troco >= 5:
            cinco = int(troco // 5)
            troco -= (cinco * 5)
        
        elif troco >= 1:
            um = int(troco // 1)
            troco -= (um * 1)


    print(f"Foi usado {cinquenta} notas de 50")
    print(f"Foi usado {vinte} notas de 20")
    print(f"Foi usado {dez} notas de 10")
    print(f"Foi usado {cinco} notas de 5")
    print(f"Foi usado {um} moedas de 1")