import tkinter as tk





def D2():
    global c,couleurs
    for i in range(int(200/c)):
        demo2.create_rectangle(0,c*i,500,c+(c*i), fill=couleurs[i], outline="black")

def D3():
    global coul_v_2
    c = 20
    for i in range(int(200/c)):    
        for j in range(int(500/c)):
            demo3.create_rectangle(0+(i*c),0+(j*c),50+(i*c),50+(j*c), fill=coul_v_2[i%2 if  j%2 else not i%2], outline="Black")
            
def D4():
    global coul_v_2,coul_v_6
    c = 20
    for i in range(int(200/c)):    
        for j in range(int(200/c)):
            demo4.create_rectangle(0+(i*c),0+(j*c),50+(i*c),50+(j*c), fill=coul_v_6[(i + j) if i + j < len(coul_v_6) else (i + j - len(coul_v_6)) if (i + j - len(coul_v_6) < len(coul_v_6)) else (i + j - len(coul_v_6) - len(coul_v_6))], outline="Black")
def D5():
    c = 10
    global coul_v_2
    for i in range(12):    
        demo5.create_rectangle(0+(i*c),0+(i*c),200-(i*c),200-(i*c), fill=coul_v_2[i%2])
def D6():
    c = 10
    global couleurs
    for i in range(12):    
        demo6.create_rectangle(0+(i*c),0+(i*c),200-(i*c),200-(i*c), fill=couleurs[i])

c = 20
coul_v_2 = ["white","black"]
couleurs = [
    "red", "green", "blue", "yellow", "orange", "pink", "purple", "brown",
    "cyan", "magenta", "gold", "lime", "indigo", "violet", "teal", "olive",
    "maroon", "navy", "gray", "black", "white", "silver", "aqua", "fuchsia", "orchid"
]
coul_v_6 = ["red", "green", "blue", "yellow", "orange", "pink","black","white"]



fen1 = tk.Tk()
fen1.title("Ma Fenêtre")

cadre = tk.Frame(fen1)
cadre.pack()  

demo1 = tk.Canvas(cadre, width=200, height=200)
demo2 = tk.Canvas(cadre, width=200, height=200)
demo3 = tk.Canvas(cadre, width=200, height=200)
demo4 = tk.Canvas(cadre, width=200, height=200)
demo5 = tk.Canvas(cadre, width=200, height=200)
demo6 = tk.Canvas(cadre, width=200, height=200)
demo1.grid(column=0, row=0)
demo2.grid(column=1, row=0)
demo3.grid(column=0, row=1)
demo4.grid(column=1, row=1)
demo5.grid(column=0, row=2)
demo6.grid(column=1, row=2)

desein1 = tk.Button(fen1, text="first drawing", command=D1)
desein1.pack(side=tk.LEFT)
desein2 = tk.Button(fen1, text="Second drawing", command=D2)
desein2.pack(side=tk.LEFT)
desein3 = tk.Button(fen1, text="Third drawing", command=D3)
desein3.pack(side=tk.LEFT)
desein4 = tk.Button(fen1, text="Fourth drawing", command=D4)
desein4.pack(side=tk.LEFT)
desein5 = tk.Button(fen1, text="Fifth drawing", command=D5)
desein5.pack(side=tk.LEFT)
desein6 = tk.Button(fen1, text="Sixth drawing", command=D6)
desein6.pack(side=tk.LEFT)

fen1.mainloop()
