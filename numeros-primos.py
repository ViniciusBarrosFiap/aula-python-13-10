print("Os numeros primos de 1 a 100")

for i in range (1, 101, 1):
    div1 = i % 2
    div2 = i % 3
    div3 = i % 5
    div4 = i % 7
    if i != 2 and i != 3 and i != 5 and i != 7:
        if div1 and div2 and div3 and div4 != 0:
            print(i)
    else:
        print(i)