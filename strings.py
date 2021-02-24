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

str1="Hello. I have a dog."
print(str1)
print(type(str1))

str2="8"
print(type(str2))

str3="He is a labradoodle"
print(str1+str3)

#space between strings
print(str1+" "+str3)
 
c=" ".join([str1,str3])
print(c)

#length of string
print(len(str1))

#print(variable.upper()) will convert everythong into upper case
#print(varibale.lower()) will do the opposite

print(str1.split()) # split between spaces

str1a=str1[:] #copy a string

print(str1a.replace('dog', 'black dog'))