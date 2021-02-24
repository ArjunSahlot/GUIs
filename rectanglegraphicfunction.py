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

