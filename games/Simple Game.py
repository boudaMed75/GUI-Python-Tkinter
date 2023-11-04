import tkinter as tk

def move_square(event):
    if event.keysym == 'Right':
        canvas.move(square, 10, 0)
    elif event.keysym == 'Left':
        canvas.move(square, -10, 0)

window = tk.Tk()
window.title("Simple Game")


canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

square = canvas.create_rectangle(100, 100, 150, 150, fill="red")


window.bind("<Left>", move_square)
window.bind("<Right>", move_square)


window.focus_set()


window.mainloop()
