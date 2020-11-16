#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, 
#y ésta te diga si es o no palíndroma o capicúa.

#Make a function to comprove if its a palindrome
def palindrome(text):
    revers = text[::-1]
    return revers == text 


#Ask to the user for a word or a number
text = input("Introduce a text or a number:> ")
#call the function
palindrome = palindrome(text)
#print if its a palindrome or not
if palindrome:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")