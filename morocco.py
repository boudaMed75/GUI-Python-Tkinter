import turtle

# Initialisation de la fenêtre Turtle
fenetre = turtle.Screen()
fenetre.title("Drapeau du Maroc")
fenetre.bgcolor("white")

# Création du drapeau
drapeau = turtle.Turtle()
drapeau.speed(0)

# Dessiner le fond rouge du drapeau
drapeau.color("#E12828")
drapeau.begin_fill()
drapeau.goto(200, 0)
drapeau.goto(200, 100)
drapeau.goto(0, 100)
drapeau.goto(0, 0)
drapeau.end_fill()

# Dessiner l'étoile verte
drapeau.penup()
drapeau.color("green")
drapeau.goto(75, 50)
drapeau.begin_fill()
for _ in range(5):
    drapeau.forward(40)
    drapeau.right(144)
drapeau.end_fill()

# Cacher la tortue
drapeau.hideturtle()

# Fermer la fenêtre en cliquant dessus
fenetre.exitonclick()
