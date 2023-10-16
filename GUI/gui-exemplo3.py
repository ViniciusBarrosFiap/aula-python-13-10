from tkinter import *
def muda_texto():
    rotulo["text"] = "Kawabunga"

window = Tk()
window.title("Titulo da janela")
window.geometry("550x350+400+200")
window.configure(background="moccasin")
rotulo = Label(window)
rotulo["text"] = "Hello World!"
rotulo["font"] = ("Impact", "20")
rotulo["fg"] = "black"
rotulo["bg"] = "moccasin"
rotulo["pady"] = 5
rotulo["padx"] = 10
rotulo["width"] = 20
rotulo.pack()
botao = Button(window, text="Click ME", pady=10, padx=10, border=5)
botao["font"] = ("Times New Roman", "16", "bold")
botao["fg"]= "white"
botao["bg"] = "black"
botao["command"] = muda_texto
botao.pack()
window.mainloop()