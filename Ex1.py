#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, 
#y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

#create a variable that print the text cappitalized and lower
def modText(text):
    text = text.upper()
    print(text)
    text = text.lower()
    print(text)

#create the variables and ask the user for an imput
print("Insert a text:")
text = input("> ")
#call the procedure
modText(text)
