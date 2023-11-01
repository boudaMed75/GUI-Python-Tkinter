import tkinter as tk

# Créez une fenêtre Tkinter
root = tk.Tk()
root.title("Drapeau de l'Algérie")

# Créez un canevas pour dessiner le drapeau
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Dessinez la bande verte à gauche
canvas.create_rectangle(0, 0, 100, 200, fill="green")

# Dessinez la bande blanche à droite
canvas.create_rectangle(100, 0, 300, 200, fill="white")

# Dessinez l'étoile et le croissant rouges
canvas.create_polygon(150, 100, 160, 90, 170, 100, 160, 110, fill="red")  # Étoile
canvas.create_arc(120, 90, 190, 160, start=30, extent=120, style=tk.ARC, outline="red")  # Croissant

# Lancement de la boucle principale de l'application
root.mainloop()

