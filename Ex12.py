#!/usr/bin/env python3
#encoding: "UTF-16"
#Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. 
#Debe imprimir el programa principal el resultado.
#Asumir que cada palabra está separada por un solo blanco.
#No se sabe cómo están separadas las palabras. Pueden estar separadas por más de un blanco o por signos de puntuación.

#define a function to count the words
def textDecomposer(text):
    #set a counter
    counter = 1
    #loop around all the letters of a text
    if len(text) == 0:
        return 0
    for i in text:
        if i == " ":
            counter += 1
    if text[-1] == " ":
        counter -= 1
    
    return counter

#decalre the variables and ask the user for an imput
print("Insert a text. Remember that every word must be separated by 1 space")
text = input("> ")
#call the function
words = textDecomposer(text)
#print the amount of words
print(f"There is {words} amount of words in your text")
