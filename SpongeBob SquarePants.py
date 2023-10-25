import turtle as t

# Configurations de la fenêtre Turtle
t.bgcolor("sky blue")
t.title("SpongeBob SquarePants")

# Définition de la fonction pour dessiner un carré
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Définir la taille du pinceau et la vitesse
t.pensize(2)
t.speed(1)

# Dessiner le visage de SpongeBob (un carré jaune)
t.fillcolor("yellow")
t.begin_fill()
draw_square()
t.end_fill()

# Dessiner les yeux
t.penup()
t.goto(30, 170)
t.pendown()
t.fillcolor("white")
t.begin_fill()
draw_square()
t.end_fill()

t.penup()
t.goto(50, 190)
t.pendown()
t.fillcolor("black")
t.begin_fill()
draw_square()
t.end_fill()

t.penup()
t.goto(90, 170)
t.pendown()
t.fillcolor("white")
t.begin_fill()
draw_square()
t.end_fill()

t.penup()
t.goto(110, 190)
t.pendown()
t.fillcolor("black")
t.begin_fill()
draw_square()
t.end_fill()

# Dessiner la bouche
t.penup()
t.goto(60, 120)
t.pendown()
t.right(90)
t.circle(50, 180)

# Cacher le dessin quand il est terminé
t.hideturtle()

# Afficher le dessin
t.done()
