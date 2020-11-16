#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

#Make a procedure to make the text show line by line
def arrangeText(text):
    for i in text:
        print(i)

#define variables and ask for an input
text = input("input a text:> ")
arrangeText(text)