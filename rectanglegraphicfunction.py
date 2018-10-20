import tkinter as tk
import turtle

root = tk.Tk()

def rect (horiz,vert,color):
    turtle.pendown()
    turtle.pensize(2)

    turtle.color(color)
    turtle.begin_fill()

    for i in range(1,3):
        turtle.forward(horiz)
        turtle.right(90)
        turtle.forward(vert)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.speed("slowest")

rect(50,25,'red')

