#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase.
#La función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver 
#el resultado para que el programa principal la imprima por pantalla.

#Make a function that replace all the spaces and replace them with an "*"
def modText(text):
    return(text.replace(" ", "*"))


#Ask to the user for the text
text = input("Introduce a text:> ")

#call the function
text = modText(text)

#print the function
print(text)