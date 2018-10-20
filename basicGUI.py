import tkinter

window = tkinter.Tk()

window.title("Hello random person")

button = tkinter.Button(window,text="Click Me!",width=50)
button.pack(padx=20, pady=20)

counter=0

def onClick(event):
    global counter 
    counter = counter+1
    button.configure(text="You Have Clicked Me %d times" % counter)

button.bind("<ButtonRelease>",onClick)

window.mainloop()