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