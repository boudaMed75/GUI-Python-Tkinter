import tkinter as tk
import random

# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Jeu de Football")

# Créer un canevas pour le terrain (gazon)
canvas = tk.Canvas(window, width=400, height=300, bg="green")
canvas.pack()

# Créer un joueur (cercle) sur le terrain
player = canvas.create_oval(190, 130, 210, 150, fill="red")

# Créer le ballon (cercle) sur le terrain
ball = canvas.create_oval(195, 145, 205, 155, fill="black")

# Fonction pour déplacer le ballon aléatoirement
def move_ball():
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    canvas.move(ball, x, y)
    window.after(100, move_ball)

# Lancer la fonction pour déplacer le ballon
move_ball()

# Lancer la boucle principale de l'application
window.mainloop()
