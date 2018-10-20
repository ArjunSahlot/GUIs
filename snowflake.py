import tkinter as tk
import turtle

root = tk.Tk()

turtle.speed("slow")
turtle.pencolor("white")
turtle.penize(10)

turtle.Screen().bgcolor("red")

def vsnow():
    turtle.right(30)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(60)

    turtle.forward(60)
    
vsnow()

def snowarm():
    for i in range(0,4):
        turtle.forward(30)
        vsnow()
    turtle.backward(120)

def snow():
    for x in range (0,6):
        snowarm()
        turtle.right(60)


snow()