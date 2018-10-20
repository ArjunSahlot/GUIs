import tkinter as tk
import turtle

root = tk.Tk()

turtle.speed("slow")

turtle.color("red")
turtle.shape("turtle")

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

root.mainloop()
