import tkinter as tk

fen1 = tk.Tk()
fen1.title("Ma Fenêtre")

def change_color():
    global ovaux
    for i in ovaux :
        if demo1.itemcget(i,"fill") == "green":
            demo1.itemconfig(i,fill="blue")
        else :
            demo1.itemconfig(i,fill="green")



cadre = tk.Frame(fen1)
 
demo1 = tk.Canvas(fen1, width=600, height=500)
demo1.pack()

change_color = tk.Button(fen1,text="Changer le color",command=change_color)
change_color.pack(side=tk.LEFT)
coul = ["green","blue"]
ovaux = []

demo1.create_rectangle(100,0,500,500,fill="dark gray")
oval = demo1.create_oval(25,100,75,150,fill=coul[0])
ovaux.append(oval)
oval = demo1.create_oval(25,400,75,350,fill=coul[1])
ovaux.append(oval)
oval = demo1.create_oval(525,100,575,150,fill=coul[1])
ovaux.append(oval)
oval = demo1.create_oval(525,400,575,350,fill=coul[0])
ovaux.append(oval)

coul_1 = ["red","dark gray"]

for i in range(int(390/30)):
    demo1.create_rectangle(105+i*30,100,135+i*30,400,fill=coul_1[i%2])


fen1.mainloop()
