import turtle as t

def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)




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
