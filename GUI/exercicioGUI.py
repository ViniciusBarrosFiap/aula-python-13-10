from tkinter import *
def soma():
    resultado["text"] = int(texto.get()) + int(texto2.get())
window = Tk()
window.title("Boas Vindas")
window.geometry("450x350+400+200")
rotulo1 = Label(window, text="Seja bem vindo!", font="Impact 20 bold", pady=10)
rotulo1.pack()
container = Frame(window, pady=1, padx=10)
container.pack()
rotulo2 = Label(container, text="1N°:", font="Impact 16", pady=10)
rotulo2.pack(side=LEFT)
texto = Entry(container, font=("Times New Roman", "16"))
texto.pack(side=LEFT)

container = Frame(window, pady=1, padx=10)
container.pack()
rotulo2 = Label(container, text="2N°:", font="Impact 16", pady=10)
rotulo2.pack(side=LEFT)
texto2 = Entry(container, font=("Times New Roman", "16"))
texto2.pack(side=RIGHT)

botao = Button(window, text="Click aqui", padx=10, pady=5, bg="black", fg="white")
botao["font"] = ("Courier New", "16", "bold")
botao["command"] = soma
botao.pack()
texto.focus()

rotulo3 = Label(window, text="resultado:", font="Arial 20", pady=10)
rotulo3.pack()

resultado = Label(window, font="Arial 20", pady=10)
resultado.pack()
window.mainloop()