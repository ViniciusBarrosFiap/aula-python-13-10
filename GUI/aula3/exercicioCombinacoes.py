from tkinter import *
def verificaCombinacoes():
    imagem = ""
    if tv.get() and not pc.get() and not vg.get() :
        imagem = "./digimon/shoutmon.png"
        imagem = PhotoImage(file=imagem)
        rotulo1["image"] = imagem
    if pc.get():
        mensagem += '\n' + checkPc["text"]
    if vg.get():
        mensagem += '\n' + checkVg["text"]
    return imagem
fonte = ("Arial", "12")
window = Tk()
window.title("Pesquisa")
window.geometry("400x200")

tv = BooleanVar()
pc = BooleanVar()
vg = BooleanVar()
container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT)
container2.pack(side=TOP)
checkTv = Checkbutton(container1, text="ballistamon",
                        font=fonte, variable=tv, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)
checkPc = Checkbutton(container1, text="dorulumon",
                        font=fonte, variable=pc, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)
checkVg = Checkbutton(container1, text="shoutmon",
                        font=fonte, variable=vg, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)


imagemDigimon = PhotoImage(file=f"./digimon/desconhecido.png")
checkTv.grid(row=0, column=0)
checkPc.grid(row=1, column=0)
checkVg.grid(row=2, column=0)

rotulo1 = Label(container2, image=imagemDigimon)
rotulo1.grid(row=0, column=1)
window.mainloop()