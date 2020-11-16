#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará 
#si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.

#find if in the text is there the character choosed
def tryChar(text, char):
    text = text.lower()
    char = char.lower()
    return(text.find(char))

#declare variables and ask the user for an input
name = input("insert your name:> ")
char = input("insert a character:> ")
while len(char) != 1: #There only can be one caracter in the char variable
    print("You can only insert one character")
    char = input("insert only one character:> ")
if (tryChar(name, char) != -1): #If the character is in the text then:
    print("There is the character %s in your name" % (char))

else:#If the character is not in the text then:
    print("There is not the character %s in your name" % (char))


