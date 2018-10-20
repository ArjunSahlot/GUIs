import tkinter as tk
import turtle as t

root = tk.Tk()

#t.penup()

t.color("blue")
t.shape("turtle")

for i in range(36):
    t.forward(10)
    t.left(10)
    for i in range(36):
        t.forward(10)
        t.right(10)

t.speed("fastest")

root.mainloop()