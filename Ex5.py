#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se encargará de cambiar todas las 
#vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá:
#Tengo una hormiga, a = tanga ana harmaga

#Modify all the vocals of a text for a single vocal
def modText(text, vocal):
    text = text.replace("a", vocal)
    text = text.replace("e", vocal)
    text = text.replace("i", vocal)
    text = text.replace("o", vocal)
    text = text.replace("u", vocal)
    return text


#Declare variables and ask the user for inputs
text = input("Insert a text:> ") 
vocal = input("Insert a vocal:> ")
text = modText(text, vocal) #call the variable to modify the text 
#print the text modified
print(text)
