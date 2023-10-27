from tkinter import *
import random
def muda_imagem():
    nova_imagem = "jogo_img/" + escolha.get() + ".png"
    imagemEsquerda["file"] = nova_imagem
def verificaJogadas():
    jogadas = ["pedra", "papel", "tesoura"]
    jogadaPc = jogadas[random.randint(0, 2)]
    jogadaUser = escolha.get()
    print(jogadaPc)
    #Empates
    if jogadaUser == "pedra" and jogadaPc == "pedra":
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Empate!"
        rotuloResultado["fg"] = "white"

    elif jogadaUser == "papel" and jogadaPc == "papel":
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Empate!"
        rotuloResultado["fg"] = "white"

    elif jogadaUser == "pedra" and jogadaPc == "pedra": 
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Empate!"
        rotuloResultado["fg"] = "white"

    #vitorias user
    elif jogadaUser == "pedra" and jogadaPc == "tesoura":
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Vitória!"
        rotuloResultado["fg"] = "green"

    elif jogadaUser == "papel" and jogadaPc == "pedra":
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Vitória!"
        rotuloResultado["fg"] = "green"

    elif jogadaUser == "tesoura" and jogadaPc == "papel":
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Vitória!"
        rotuloResultado["fg"] = "green"
    #vitoria pc
    elif jogadaPc == "pedra" and jogadaUser == "tesoura" :#tesoura
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Derrota!"
        rotuloResultado["fg"] = "red"

    elif jogadaPc == "papel" and jogadaUser == "papel": #papel
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Derrota!"
        rotuloResultado["fg"] = "red"

    elif jogadaPc == "tesoura" and jogadaUser == "pedra": #pedra
        imagemDireita["file"] = "jogo_img/" + jogadaPc + ".png"
        rotuloResultado["text"] = "Derrota!"
        rotuloResultado["fg"] = "red"

fonte = ("Arial", "12", "bold")

window = Tk()
window.title("Jokempo")
window.geometry("500x600")
window.configure(bg="goldenrod")
escolha = StringVar()
escolha.set("tesoura")
container1 = Frame(window, padx=10, bg="goldenrod")
container1.pack(side=LEFT)

container2 = Frame(window, width=5, bg="goldenrod")
container2.pack(side=LEFT)

container3 = Frame(window, padx=20, bg="goldenrod")
container3.pack(side=RIGHT)

texto = ["Pedra", "Papel", "Tesoura"]
valor = ["pedra", "papel", "tesoura"]

for i in range(0, 3, 1):
    Radiobutton(container1, text=texto[i],indicatoron=False, value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem).pack()

rotuloJogador = Label(container2, text="Jogador", bg="goldenrod", font=fonte)
rotuloJogador.pack(side=TOP)
btnJogar = Button(container2, text="Jogar", padx=10,height=3, width=20, command=verificaJogadas)
btnJogar.pack(side=BOTTOM)
imagemEsquerda = PhotoImage(file="jogo_img/pedra.png")
rotulo1 = Label(container2, padx=10, image=imagemEsquerda, bg="goldenrod")
rotulo1.pack()

rotuloComputador = Label(container3, text="Computador", bg="goldenrod", font=fonte)
rotuloComputador.pack(side=TOP)
rotuloResultado = Label(container3, text="", font=fonte,fg="black",bg="goldenrod",padx=10,height=3, width=20)
rotuloResultado.pack(side=BOTTOM)
imagemDireita = PhotoImage(file="jogo_img/vazio.png")
rotulo2 = Label(container3, image=imagemDireita, bg="goldenrod")
rotulo2.pack()

window.mainloop()