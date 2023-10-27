from tkinter import *
def muda_imagem():
    nova_imagem = "jogo_img/" + escolha.get() + ".png"
    imagemEsquerda["file"] = nova_imagem
fonte = ("Arial", "12")
window = Tk()
window.title("Jokempo")
window.geometry("500x500")
window.configure(bg="goldenrod")
escolha = StringVar()
container1 = Frame(window, padx=10, bg="goldenrod")
container1.pack(side=LEFT)

container2 = Frame(window, padx=20, bg="goldenrod")
container2.pack()

container3 = Frame(window, padx=20, bg="goldenrod")
container3.pack(side=RIGHT)

texto = ["Pedra", "Papel", "Tesoura"]
valor = ["pedra", "papel", "tesoura"]

for i in range(0, 3, 1):
    Radiobutton(container1, text=texto[i],indicatoron=False, value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem).pack()
rotuloJogador = Label(text="Jogador", bg="goldenrod", font=fonte)
rotuloJogador.pack()
imagemEsquerda = PhotoImage(file="jogo_img/tesoura.png")
rotulo1 = Label(container2, padx=10, image=imagemEsquerda, bg="goldenrod")
rotulo1.pack()

imagemDireita = PhotoImage(file="jogo_img/vazio.png")
rotulo2 = Label(container3, image=imagemDireita, bg="goldenrod")
rotulo2.pack()

window.mainloop()