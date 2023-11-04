
from tkinter import *
from random import randrange


def dominer():
    global c,coul,add
    for i in range(int(500/c)):    
        for j in range(int(500/c)):
            if(j%2):
                demo.create_rectangle(0+(i*c),0+(j*c),50+(i*c),50+(j*c), fill=coul[i%2==0], outline="Black")
            else:
                demo.create_rectangle(0+(i*c),0+(j*c),50+(i*c),50+(j*c), fill=coul[not i%2==0], outline="Black")
    point = Button(fen1,text="panier",command=add)
    point.pack(side=RIGHT)

def add():
    global suprimer
    i = randrange(10) 
    j = randrange(10) 
    # demo.create_oval(50*i,50*j,50,50, fill="blue", outline="red", width=2)
    demo.create_oval(0+(i*c),0+(j*c),50+(i*c),50+(j*c), fill="red" )
        

def suprimer():
    global supprimer_button
    for objet in demo.find_all():
        if demo.type(objet) == "oval":
            demo.delete(objet)
fen1 = Tk()


demo = Canvas(fen1,width=500,height=510)
demo.pack()

x1,y1,x2,y2 = 0,0,50,50
ntf = True
coul = ["Blue","White"]
c = 50

deminer = Button(fen1,text="deminee",command=dominer)
deminer.pack(side=LEFT)

supprimer_button = Button(fen1, text="RESTART", command=suprimer)
supprimer_button.pack(side=LEFT)







fen1.mainloop()