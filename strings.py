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