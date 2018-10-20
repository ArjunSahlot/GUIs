import tkinter as tk

window=tk.Tk()

window.title("Hello random person")

tk.Label(window,text="Enter text: ").grid(row=0, column=0)

tk.Entry(window, width=20, bg="light blue").grid(row=1, column=0)

tk.Checkbutton(window,text="Hi, this is Checkbutton 1. So you can click me!").grid(row=3,column=0)

tk.Checkbutton(window,text="Hi, this is Checkbutton 2. So you can click me!").grid(row=4,column=0)

tk.Scale(window,from_=0, to=100,orient=tk.HORIZONTAL).grid(row=1,column=1)

tk.Canvas(window,bg="light blue", width=150, height= 100).grid(row=6, column=0)

window.mainloop()