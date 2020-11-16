#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes),
#los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.

#make the function to bind the words
def bindName(word1, word2, word3):
    text = word1 + " " + word2 + " " + word3
    return text
    

if __name__ == "__main__":
    #declare variables and ask the user for an input
    firstName = input("Write the name:> ")
    midName = input("Write the middle name:> ")
    lastName = input("Writhe the last name:> ")
    #call the function
    fullName = bindName(firstName, midName, lastName)
    #print the full name
    print("your full name is: ", fullName)
    
    