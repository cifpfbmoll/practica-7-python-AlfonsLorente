#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. 
#El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

#Make a procedure that look at the vowels and then print how many there are:
def countVowels(text):
    #count each vocal
    a = text.count("a")
    e = text.count("e")
    i = text.count("i")
    o = text.count("o")
    u = text.count("u")
    #sum them up
    total = a + e + i + o + u
    #print the total
    print(f"there is {total} vowels in you text")

#ask the user a text
text = input("insert a text:> ")
#Pass the variable to a procedure
countVowels(text)