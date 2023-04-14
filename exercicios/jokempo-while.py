import random
jogada_user = 1
vitorias_pc = 0
vitorias_user = 0
while jogada_user != 0:
    print("Digite sua jogada:\n [1] Pedra \n [2] Papel \n [3] Tesoura")
    jogada_user = int(input())

    jogadas = ["Pedra", "Papel", "Tesoura"]

    jogada_pc = random.choice(jogadas)

    print(f"Você jogou {jogada_user}")
    print(f"O computador jogou {jogada_pc}")

    #Empates
    if jogada_user == 1 and jogada_pc == "Pedra":
        print("Empate")

    elif jogada_user == 2 and jogada_pc == "Papel":
        print("Empate")

    elif jogada_user == 3 and jogada_pc == "Pedra": 
        print("Empate")

    #vitoria usuario
    elif jogada_user == 1 and jogada_pc == "Tesoura":
        print("Você ganhou")
        vitorias_user += 1

    elif jogada_user == 2 and jogada_pc == "Pedra":
        print("Você ganhou")
        vitorias_user += 1

    elif jogada_user == 3 and jogada_pc == "Papel":
        print("Você ganhou")
        vitorias_user += 1

    #vitoria pc

    elif jogada_pc == "Pedra" and jogada_user == 3 :#tesoura
        print("Computador ganhou")
        vitorias_pc += 1
    elif jogada_pc == "Papel" and jogada_user == 1: #papel
        print("Computador ganhou")
        vitorias_pc += 1
    elif jogada_pc == "Tesoura" and jogada_user == 2: #pedra
        print("Computador ganhou")
        vitorias_pc += 1

print(f"O usuario ganhou {vitorias_user} partidas")
print(f"O computador ganhou {vitorias_pc} partidas")