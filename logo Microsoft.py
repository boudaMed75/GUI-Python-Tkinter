
import tkinter as tk

def draw_logo():
    
    x, y = 10, 10
    x2, y2 = 90, 90
    width, height = 100, 100

    # Create a new tkinter window
    root = tk.Tk()
    root.title("Microsoft Logo")
    canvas = tk.Canvas(root, width=width+x, height=height+y)
    canvas.pack()

    # Draw the main part of the logo
    for i in range(1, 5):
        x += 10
        y += 10
        canvas.create_rectangle(x, y, x+80, y+80, fill='blue')
        canvas.create_oval(x, y, x+80, y+80, fill='white')
        canvas.create_oval(x+5, y+5, x+75, y+75, fill='blue')
        canvas.create_oval(x+15, y+15, x+65, y+65, fill='white')
        canvas.create_oval(x+25, y+25, x+55, y+55, fill='blue')

    # Draw the two additional lines on the bottom
    for i in range(2):
        x += 10
        y += 10
        canvas.create_rectangle(x, y, x+80, y+80, fill='blue')
        canvas.create_oval(x, y, x+80, y+80, fill='white')
        canvas.create_oval(x+5, y+5, x+75, y+75, fill='blue')
        canvas.create_oval(x+15, y+15, x+65, y+65, fill='white')
        canvas.create_oval(x+25, y+25, x+55, y+55, fill='blue')
        x -= 90
        y -= 90
        x += 10

    # Run the tkinter window's main loop
    root.mainloop()

draw_logo()
