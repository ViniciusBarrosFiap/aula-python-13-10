i = int(input("Digite um numero inteiro entre 1 e 3: "))
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))

if i == 1:
    trocou = True
    while trocou:
        trocou = False
        if a > b:
            a, b = b, a
            trocou = True
        if b > c:
            b, c = c, b
            trocou = True
    print(f"Crescente {a}, {b}, {c}")
elif i == 2: 
    trocou = True
    while trocou:
        trocou = False
        if a > b:
            a, b = b, a
            trocou = True
        if b > c:
            b, c = c, b
            trocou = True
    print(f"Decrecente {a}, {b}, {c}")
elif i == 3:
    while True:
        if a >= b and a >= c:
            if b>= c:
                print(f"maior valor no meio {b}, {a}, {c}")
            else:
                print(f"maior valor no meio {c}, {a}, {b}")
            break

        elif b >= a and b >= c:
            if a >= c:
                print(f"maior valor no meio {a}, {b}, {c}")
            else:
                print(f"maior valor no meio {c}, {b}, {a}")
            break
        elif c >= a and c >= b:
            if a >= b: 
                print(f"maior valor no meio {a}, {c}, {b}")
            else:
                print(f"maior valor no meio {b}, {c}, {a}")
else:
    print("Valor de I é inválido")