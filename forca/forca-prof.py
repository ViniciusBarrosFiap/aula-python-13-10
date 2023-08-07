import random

topo =    "UU=====U"
corda =   "||     |"
cabeca =  "||      "
corpo =   "||      "
pernas =  "||      "
base1 =   "||"
base2 =   "||"

dica = ""

l1 = l2 = l3= l4= l5= l6= l7= l8= l9 = "_"
palpites = ""
erro = acerto = 0
palavras = ["BATRANGUE", "AEROPORTO", "CONSELHOS"]
dicas = ["Morcego que vai e volta",
         "Local onde podemos viajar,"
         "Se fosse bons não eram de graça"]

#Sorteando a palavra
sorteio = random.randint(0,2)
sorteado = palavras[sorteio]
palavra = []
for i in range(0, 9):
    palavra.append(sorteado[i:i+1])
dica = dicas[sorteio]

while (acerto < 9 and erro < 6):
    #exibindo forca
    print()
    print()
    print(dica)
    print(topo)
    print(corda)
    print(cabeca)
    print(corpo)
    print(pernas)
    print(base1)
    print(base2)
    print(" ",l1, l2, l3, l4, l5, l6, l7, l9)
    print()
    print(palpites)
    print()
    print("Digite uma letra: ")
    letra = input().upper()
    print()
    print()
    print()
    palpites += " " + letra
    if letra in palavra:
        if letra  == palavra[0]:
            l1 = letra
            palavra[0] = "@"
            acerto += 1
        elif letra == palavra[1]:
            l2 = letra
            palavra[1] = "@"
            acerto += 1
        elif letra == palavra[2]:
            l3 = letra
            palavra[2] = "@"
            acerto += 1
        elif letra == palavra[3]:
            l4 = letra
            palavra[3] = "@"
            acerto += 1
        elif letra == palavra[4]:
            l5 = letra
            palavra[4] = "@"
            acerto += 1
        elif letra == palavra[5]:
            l6 = letra
            palavra[5] = "@"
            acerto += 1
        elif letra == palavra[6]:
            l7 = letra
            palavra[6] = "@"
            acerto += 1
        elif letra == palavra[7]:
            l8 = letra
            palavra[7] = "@"
            acerto += 1
        elif letra == palavra[8]:
            l9 = letra
            palavra[8] = "@"
            acerto += 1
    else:
        erro += 1
    #arrumando a forca
    if erro == 1:
        cabeca = "||      (Ï)"
    elif erro == 2:
        corpo =  "||      {.}"
    elif erro == 3:
        corpo =  "||      /{.}"
    elif erro == 4:
        corpo =  "||    /{.}\\"
    elif erro == 5:
        pernas = "||         L"
    elif erro == 6:
        pernas = "||        LL"

print()
print()
print(dica)
print(topo)
print(corda)
print(cabeca)
print(corpo)
print(pernas)
print(base1)
print(base2)
print(" ",l1, l2, l3, l4, l5, l6, l7, l9)
print()
print(palpites)
print()

if acerto >= 9:
    print("GANHOU")
else:
    print("PERDEU")

