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