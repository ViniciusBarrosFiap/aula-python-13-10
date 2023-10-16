from tkinter import *

window = Tk()
window.title("Titulo da janela")
window.geometry("550x350+400+200")
window.configure(background="moccasin")
rotulo = Label(window)
rotulo["text"] = "Hello World!"
rotulo["font"] = ("Impact", "20")
rotulo["fg"] = "brown"
rotulo["bg"] = "moccasin"
rotulo["pady"] = 5
rotulo["padx"] = 10
rotulo["width"] = 20
rotulo["anchor"] =  "w"
rotulo.pack()
botao = Button(window, text="Click ME", pady=10, padx=10)
botao["font"] = ("Times New Roman", "16", "bold")
botao["fg"]= "white"
botao["bg"] = "black"
botao["command"] = window.destroy
botao.pack()
window.mainloop()