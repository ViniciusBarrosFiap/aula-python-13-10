import random
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

elif jogada_user == 2 and jogada_pc == "Pedra":
    print("Você ganhou")

elif jogada_user == 3 and jogada_pc == "Papel":
    print("Você ganhou")

#vitoria pc

elif jogada_pc == "Pedra" and jogada_user == 3 :#tesoura
    print("Computador ganhou")
elif jogada_pc == "Papel" and jogada_user == 1: #papel
    print("Computador ganhou")
elif jogada_pc == "Tesoura" and jogada_user == 2: #pedra
    print("Computador ganhou")