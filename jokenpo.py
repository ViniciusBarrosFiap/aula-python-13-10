import random
jogada_user = str(input("Digite sua jogada:\n [1] Pedra \n [2] Papel \n [3] Tesoura"))

jogadas = ["Pedra", "Papel", "Tesoura"]

jogada_pc = random.choice(jogadas)

if jogada_user == 1 and jogada_pc == "Papel":
    print("Maquina Ganhou")

elif jogada_user == 2 and jogada_pc == "Tesoura":
    print("Maquina Ganhou")

elif jogada_user == 3 and jogada_pc == "Pedra": 
    print("Maquina Ganhou")

elif jogada_user == 1 and jogada_pc == "Tesoura":
    print("Você ganhou")

elif jogada_user == 2 and jogada_pc == "Pedra":
    print("Você ganhou")

elif jogada_user == 3 and jogada_pc == "Papel":
    print("Você ganhou")