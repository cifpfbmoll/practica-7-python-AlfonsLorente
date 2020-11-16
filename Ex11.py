#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. 
#Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:

#Make a function to comprove if its a palindrome
def palindrome(text):
    #replace all the spaces of the text
    text = text.replace(" ", "")
    #reverse the text
    revers = text[::-1]
    #return if the text and the reversed text are palindromes.
    return revers == text 


#Ask to the user for a word or a number
text = input("Introduce a text:> ")
#call the function
palindrome = palindrome(text)
#print if its a palindrome or not
if palindrome:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")