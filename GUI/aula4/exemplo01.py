from tkinter import *

def muda_imagem():
    nova_imagem = "imagens/" + escolha.get() + ".png"
    imagem["file"] = nova_imagem

fonte = ("Arial", "12")
window = Tk()
window.title("Escolha seu avatar")
window.geometry("400x200")
window.configure(bg="moccasin")
escolha = StringVar()
escolha.set("chaplin")
conatiner1 = Frame(window, padx=10, bg="moccasin")
conatiner2 = Frame(window, padx=10, bg="moccasin")
conatiner1.pack(side=LEFT)
conatiner2.pack(side=TOP)
radio_chaplin = Radiobutton(conatiner1, text="Charles Chaplin", value="chaplin", variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem)
radio_arlequina = Radiobutton(conatiner1, text="Harley Quinn", value="arlequina", variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem)
radio_ninja = Radiobutton(conatiner1, text="Ninja do deserto", value="ninja", variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem)
radio_zorro = Radiobutton(conatiner1, text="Copo do Zorro", value="zorro", variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", font=fonte, command=muda_imagem)

radio_chaplin.pack()
radio_arlequina.pack()
radio_ninja.pack()
radio_zorro.pack()
imagem = PhotoImage(file="imagens/chaplin.png")
rotulo = Label(conatiner2, image=imagem, bg="moccasin")
rotulo.pack()
window.mainloop() 