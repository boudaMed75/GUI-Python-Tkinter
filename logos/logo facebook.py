import tkinter as tk

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Logo Facebook")

# Créer un canevas pour dessiner le logo
canvas = tk.Canvas(fenetre, width=200, height=200, bg="white")
canvas.pack()

# Tracer le logo de Facebook
# Dessiner le fond bleu
canvas.create_rectangle(10, 10, 190, 190, fill="#1877F2")

# Dessiner le "f" blanc
canvas.create_text(100, 100, text="f", fill="white", font=("Helvetica", 100, "bold"))

# Fonction pour fermer la fenêtre en cliquant sur le bouton "Fermer"
def fermer_fenetre():
    fenetre.destroy()

# Créer un bouton pour fermer la fenêtre
bouton_fermer = tk.Button(fenetre, text="Fermer", command=fermer_fenetre)
bouton_fermer.pack()

# Lancer la boucle principale de l'application
fenetre.mainloop()
