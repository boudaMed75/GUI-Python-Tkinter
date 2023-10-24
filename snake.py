import tkinter as tk
import random

# dans ce jeu je vais ecrire un jeu de snake c'est la premier base en suite elle possible de developer ensuite

# Paramètres du jeu
GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15
SNAKE_SPEED = 100

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Snake Game")

        # Crée un canvas pour le jeu
        self.canvas = tk.Canvas(window, width=GRID_WIDTH * GRID_SIZE, height=GRID_HEIGHT * GRID_SIZE)
        self.canvas.pack()

        # Initialisation du serpent
        self.snake = [(2, 3), (2, 2), (2, 1)]
        self.direction = "Right"

        # Initialisation de la nourriture
        self.food = self.generate_food()

        # Crée un chronomètre
        self.timer = None

        # Configure les touches du clavier
        self.window.bind("<Key>", self.on_key_event)

    def start(self):
        self.update()
        self.window.mainloop()

    def on_key_event(self, event):
        key = event.keysym
        if key in ["Left", "Right", "Up", "Down"]:
            self.direction = key

    def update(self):
        self.move()
        self.check_collision()
        self.draw()

        if self.is_game_over():
            self.game_over()
        else:
            self.timer = self.window.after(SNAKE_SPEED, self.update)

    def move(self):
        head = self.snake[0]
        if self.direction == "Left":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 1, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 1)

        self.snake.insert(0, new_head)

        # Si le serpent a mangé de la nourriture, génère un nouvel emplacement pour la nourriture
        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def generate_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            self.game_over()
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            self.game_over()

    def is_game_over(self):
        return False

    def game_over(self):
        self.window.after_cancel(self.timer)
        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE / 2,
            GRID_HEIGHT * GRID_SIZE / 2,
            text="Game Over",
            fill="red",
            font=("Helvetica", 24),
            anchor="center"
        )

    def draw(self):
        # Efface le canvas
        self.canvas.delete("all")

        # Dessine le serpent
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * GRID_SIZE, y * GRID_SIZE,
                (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
                fill="green")

        # Dessine la nourriture
        x, y = self.food
        self.canvas.create_oval(
            x * GRID_SIZE, y * GRID_SIZE,
            (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
            fill="red")

# Crée la fenêtre principale
root = tk.Tk()
game = SnakeGame(root)
game.start()
