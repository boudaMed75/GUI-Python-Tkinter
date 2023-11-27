import tkinter as tk


fenetre = tk.Tk()
fenetre.title("Logo WhatsApp")

# Créer un canevas pour dessiner le logo
canvas = tk.Canvas(fenetre, width=200, height=200, bg="green")
canvas.pack()



# Dessiner l'icône de téléphone blanc
canvas.create_rectangle(40, 60, 160, 150, fill="white")



# Fonction pour fermer la fenêtre en cliquant sur le bouton "Fermer"
def fermer_fenetre():
    fenetre.destroy()


bouton_fermer = tk.Button(fenetre, text="Fermer", command=fermer_fenetre)
bouton_fermer.pack()

# Lancer la boucle principale de l'application
fenetre.mainloop()
