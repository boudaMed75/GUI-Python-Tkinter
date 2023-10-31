import tkinter as tk

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Logo WhatsApp")

# Créer un canevas pour dessiner le logo
canvas = tk.Canvas(fenetre, width=200, height=200, bg="green")
canvas.pack()

# Tracer le logo de WhatsApp
# Dessiner l'arrière-plan vert
canvas.create_oval(10, 10, 190, 190, fill="green")

# Dessiner l'icône de téléphone blanc
canvas.create_rectangle(40, 60, 160, 150, fill="white")

# Dessiner le récepteur du téléphone vert
canvas.create_polygon(40, 60, 20, 80, 40, 100, 160, 100, 180, 80, 160, 60, fill="green")

# Fonction pour fermer la fenêtre en cliquant sur le bouton "Fermer"
def fermer_fenetre():
    fenetre.destroy()

# Créer un bouton pour fermer la fenêtre
bouton_fermer = tk.Button(fenetre, text="Fermer", command=fermer_fenetre)
bouton_fermer.pack()

# Lancer la boucle principale de l'application
fenetre.mainloop()
