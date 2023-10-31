#RM97824 - Vinicius Barros
from tkinter import *
import random
def jogar():
    valorPalpites = palpites.get().upper()
    global acertos
    if valorPalpites in palavra:
        if valorPalpites == palavra[0]:
            palavra[0] = "@"
            tracos[0] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[1]:
            palavra[1] = "@"
            tracos[1] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[2]:
            palavra[2] = "@"
            tracos[2] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[3]:
            palavra[3] = "@"
            tracos[3] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[4]:
            palavra[4] = "@"
            tracos[4] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[5]:
            palavra[5] = "@"
            tracos[5] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[6]:
            palavra[6] = "@"
            tracos[6] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[7]:
            palavra[7] = "@"
            tracos[7] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
        elif valorPalpites == palavra[8]:
            palavra[8] = "@"
            tracos[8] = valorPalpites
            rotuloTracos["text"] = tracos
            rotuloPalpitesDados["text"] += valorPalpites
            acertos += 1
    else:
        global erro
        erro += 1
        rotuloPalpitesDados["text"] += valorPalpites
        mudaImagem(erro)
    
    if acertos == 9:
        rotuloResultado["text"] = "GANHOU"
    elif erro == 6:
        rotuloResultado["text"] = "PERDEU"
    
    
def mudaImagem(imagem):
    novaImagem = "./imagens/forca" + str(imagem) + ".png"
    imagemForca["file"] = novaImagem
    rotuloForca["image"] = imagemForca
erro = 0
acertos = 0
palavras = ["BATRANGUE", "AEROPORTO", "CONSELHOS"]
tracos = ["_", "_","_","_","_","_","_","_","_",]
#Sorteando a palavra
sorteio = random.randint(0,2)
sorteado = palavras[sorteio]
palavra = []

for i in range(0, 9):
    palavra.append(sorteado[i:i+1])

fonte = ("Arial", "12", "bold")
window = Tk()
window.title("Forca")
window.geometry("600x200")

container1 = Frame(window, padx=10)
container1.pack(side=LEFT)
imagemForca = PhotoImage(file="./imagens/forca.png")
rotuloForca = Label(container1, padx=10, image=imagemForca)
rotuloForca.pack()

container2 = Frame(window, padx=20)
container2.pack(side=RIGHT)

rotuloResultado = Label(container2, text="", font="Arial, 23")
rotuloResultado.pack()

rotuloTracos = Label(container2, text=tracos, font="Arial, 20")
rotuloTracos.pack()

rotuloInput = Label(container2, text="Palpite:", font=fonte, pady=10)
rotuloInput.pack()
palpites = Entry(container2, font=fonte)
palpites.pack()

botaoFazPalpite = Button(container2, text="fazer palpite", command=jogar)
botaoFazPalpite.pack()

rotuloPalpitesDados = Label(container2, text="", font="Arial, 20")
rotuloPalpitesDados.pack()
window.mainloop()