#
#  Guis
#  Some GUIs to learn from
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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