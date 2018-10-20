from tkinter import *
import random

tk=Tk()

canvas = Canvas(tk, width=500, height=500, bg="light blue")

canvas.pack()

def generalrect(width, height):
    x1=random.randrange(width)
    y1=random.randrange(height)

    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)

    canvas.create_rectangle(x1,y1,x2,y2)

for i in range(5):
    generalrect(350,350)

mainloop()