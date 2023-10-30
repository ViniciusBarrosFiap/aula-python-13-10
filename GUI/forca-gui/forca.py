from tkinter import *
import random
def jogar():
    valorPalpites = palpites.get()
    if valorPalpites in palavra:
        if valorPalpites == palavra[0]:
            palavra[0] = "@"
            tracos[0] = valorPalpites
            rotuloTracos["text"] = tracos
        elif valorPalpites == palavra[1]:
            palavra[1] = "@"
            tracos[1] = valorPalpites
            rotuloTracos["text"] = tracos

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

container2 = Frame(window, padx=20)
container2.pack(side=RIGHT)
rotuloForca.pack()
rotuloTracos = Label(container2, text=tracos, font="Arial, 20")
rotuloTracos.pack()

rotuloInput = Label(container2, text="Palpite:", font=fonte, pady=10)
rotuloInput.pack()
palpites = Entry(container2, font=fonte)
palpites.pack()

botaoFazPalpite = Button(container2, text="fazer palpite", command=jogar)
botaoFazPalpite.pack()

window.mainloop()