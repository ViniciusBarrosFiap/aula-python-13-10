from tkinter import *
def verificaCombinacoes():
    if ballistamon.get() and shoutmon.get() and dorulumon.get():
        rotulo1["image"] = imgShoutmon5
    elif dorulumon.get() and ballistamon.get():
        rotulo1["image"] = imgShoutmon4
    elif dorulumon.get() and shoutmon.get():
        rotulo1["image"] = imgShoutmon3
    elif ballistamon.get() and shoutmon.get():
        rotulo1["image"] = imgShoutmon2
    elif ballistamon.get():
        rotulo1["image"] = imgBallistamon
    elif dorulumon.get():
        rotulo1["image"] = imgDorulumon

    elif shoutmon.get():
        rotulo1["image"] = imgShoutmon

    else:
        rotulo1["image"] = desconhecido
fonte = ("Arial", "12")
window = Tk()
window.title("Digimon")
window.geometry("400x200")

ballistamon = BooleanVar()
dorulumon = BooleanVar()
shoutmon = BooleanVar()

container1 = Frame(window)
container2 = Frame(window)
container1.pack(side=LEFT)
container2.pack(side=TOP)

desconhecido = PhotoImage(file="digimon/desconhecido.png")
imgBallistamon = PhotoImage(file="digimon/ballistamon.png")
imgDorulumon = PhotoImage(file="digimon/dorulumon.png")
imgShoutmon = PhotoImage(file="digimon/shoutmon.png")
imgShoutmon2 = PhotoImage(file="digimon/shoutmonX2.png")
imgShoutmon3 = PhotoImage(file="digimon/shoutmonX3.png")
imgShoutmon4 = PhotoImage(file="digimon/shoutmonX4.png")
imgShoutmon5 = PhotoImage(file="digimon/shoutmonX5.png")


checkTv = Checkbutton(container1, text="ballistamon",
                        font=fonte, variable=ballistamon, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)
checkPc = Checkbutton(container1, text="dorulumon",
                        font=fonte, variable=dorulumon, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)
checkVg = Checkbutton(container1, text="shoutmon",
                        font=fonte, variable=shoutmon, width=15, 
                        padx=10, pady=5, anchor="w", 
                        command=verificaCombinacoes)

checkTv.grid(row=0, column=0)
checkPc.grid(row=1, column=0)
checkVg.grid(row=2, column=0)

rotulo1 = Label(container2, image=desconhecido)
rotulo1.grid(row=0, column=1)

window.mainloop()