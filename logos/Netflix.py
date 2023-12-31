import tkinter as tk


fenetre = tk.Tk()
fenetre.title("Logo Netflix")

# Créer un canevas pour afficher le texte
canvas = tk.Canvas(fenetre, width=300, height=100, bg="black")
canvas.pack()

# Afficher le nom "Netflix" en rouge avec une police personnalisée
canvas.create_text(150, 50, text="Netflix", fill="red", font=("Helvetica", 30, "bold"))

def fermer_fenetre():
    fenetre.destroy()


bouton_fermer = tk.Button(fenetre, text="Fermer", command=fermer_fenetre)
bouton_fermer.pack()

# Lancer la boucle principale de l'application
fenetre.mainloop()
