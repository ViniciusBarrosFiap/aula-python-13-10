#Vinicius Oliveira de Barros - RM97824
from tkinter.ttk import *
from tkinter import *

#Função que faz o calculo e a mudança de imagens no programa
def fazPedido():
    #Muda imagem da direita
    nova_imagemDireita = "cardapio/" + comboLanches.get() + ".png"
    imagemDireita["file"] = nova_imagemDireita
    #Muda imagem central
    nova_imagemCentral = "cardapio/" + comboPorcao.get() + ".png"
    imagemCentral["file"] = nova_imagemCentral
    #Muda imagem da esquerda
    nova_imagemEsquerda = "cardapio/" + comboBebida.get() + ".png"
    imagemEsquerda["file"] = nova_imagemEsquerda

    #cardapio
    data = {
        "lanche":{
            "escolha": 0,
            "burger": 34.9,
            "noodles": 44.5,
            "pizza": 49
        },
        "porcao":{
            "escolha": 0,
            "fritas":14.9,
            "nuggets": 9.5,
            "milho": 12.3,
        },
        "bebida":{
            "escolha": 0,
            "suco":"14.9",
            "shake":"19.9"
        }
    }
    #Guarda os valores dos itens selecionados
    totalLanche = data["lanche"][comboLanches.get()]
    totalPorcao = data["porcao"][comboPorcao.get()]
    totalBebida = data["bebida"][comboBebida.get()]
    #Faz a soma dos valores armazenados
    totalConta = totalLanche + totalPorcao + float(totalBebida)
    #Muda o texto do resultado
    resultado["text"] = f"R$ {totalConta:.2f}"
#Define a fonte
fonte = ("Cooper Black", "14")
#Define a janela
window = Tk()
#Muda o titulo da janela
window.title("Escolha um combo")
#Define o tamanho inicial da janela
window.geometry("400x500")
#Cria um container para armazrnar o formulario do pedido
container = Frame(window, pady=5, padx=5)
container.pack()
#Rótulo para escolher o lanche
rotulo1 = Label(container, text="Lanche", pady=5, font=fonte)
rotulo1.pack()
comboLanches = Combobox(container)
comboLanches["values"] = ("escolha","burger", "noodles", "pizza")
comboLanches["state"] = "readonly"
comboLanches.current(0)
comboLanches.pack()
rotulo2 = Label(container, text="Porção", pady=5, font=fonte)
rotulo2.pack()
#Rótulo para escolher a porção
comboPorcao = Combobox(container)
comboPorcao["values"] = ("escolha","fritas", "nuggets", "milho")
comboPorcao["state"] = "readonly"
comboPorcao.current(0)
comboPorcao.pack()
#Rótulo para escolher a bebida
rotulo3 = Label(container, text="Bebida", pady=5, font=fonte)
rotulo3.pack()
comboBebida = Combobox(container)
comboBebida["values"] = ("escolha","suco", "shake")
comboBebida["state"] = "readonly"
comboBebida.current(0)
comboBebida.pack()

#Cria um container para organizar as imagens
container2 = Frame(window, pady=5, padx=5)
container2.pack()
#Define a imagem da direita
imagemDireita = PhotoImage(file="./cardapio/escolha.png")
rotuloDireito = Label(container2, image=imagemDireita)
rotuloDireito.pack(side=LEFT)
#Define a imagem central
imagemCentral = PhotoImage(file="./cardapio/escolha.png")
rotuloCentral = Label(container2, image=imagemCentral)
rotuloCentral.pack(side=LEFT)
#Define a imagem da esquerda
imagemEsquerda = PhotoImage(file="./cardapio/escolha.png")
rotuloEsquerdo = Label(container2, image=imagemEsquerda)
rotuloEsquerdo.pack(side=RIGHT)
#Cria o botão que irá chamar a função que faz o pedido
botao = Button(window, text="Terminar pedido", pady=5, padx=10, font=fonte)
botao["command"] = fazPedido #Quando clicado a função "fazPedido" é chamada
botao.pack()#mostra o botão
#Cria label do resultado
resultado = Label(window, font="Arial 20", pady=10)
resultado.pack()#Exibe o resultado
window.mainloop()#Mantem o programa em loop