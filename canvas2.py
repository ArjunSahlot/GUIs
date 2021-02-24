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