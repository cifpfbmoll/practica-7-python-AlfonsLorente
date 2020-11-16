#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los
#espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.


#Make a function that erase the spaces
def modText(text):
    return(text.replace(" ", ""))


#Ask to the user for the text
text = input("Introduce a text:> ")

#call the function
text = modText(text)

#print the function
print(text)