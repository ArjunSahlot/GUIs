from tkinter import *

tk=Tk()

canvas = Canvas(tk, width=500, height=500, bg="light blue")

canvas.pack()

canvas.create_rectangle(20,20,100,300)

mainloop()