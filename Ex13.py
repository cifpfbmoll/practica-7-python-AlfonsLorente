#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, 
#por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), 
#o de otra (con while). Ambas funciones devolverá true (si es primo) o false (si no es primo). 
#El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la 
#solución de una manera u otra. Comentario: aprovecha el código que tienes ya creado
#ask for the number and set variables
import sys
import time

#See if its prime with the for loop
def forPrime(num):
    counter = 0
    if num < 1:
        sys.exit("The number must be more than 0") 
    #make greater the counter if there is a number divisible by num that is not himself and 1
    for i in range(2, num):
        if num % i == 0:
            counter+=1
        
    #return if its prime number or not
    if counter == 0:
        return True
    else:
        return False


#See if its prime with the while loop
def whilePrime(num):
    #ask for the number and set variables
    counter = 0
    divisor = 2
    #the number must be greater than 0
    if num < 1:
        sys.exit("The number must be more than 0") 
    #Look if its prime
    while counter == 0 and divisor < num:
        if num % divisor == 0:
            counter += 1
        divisor += 1

    #return if its prime number or not
    if counter == 0:
        return True
    else:
        return False

#decalre the variables and ask the user for an input
num = int(input("Insert an integuer:> "))
prime = (bool)
print("The operation can be done with a for loop or with a while loop, what do you prefire?")
print("1. for")
print("2. while")
ans = int(input("Insert 1 or 2:> "))
#the answer must be 1 or 2
while ans == 1 and ans == 2:
    ans = int(input("The answer must be between 1 or 2:> "))

#start the timer so we can see which loop is faster
startTime = time.time()

#call the function
if ans == 1:
    prime = forPrime(num)
elif ans == 2:
    prime = whilePrime(num)

#print if its a prime number or not
if prime:
    print("The number %d IS a prime number" % num)
else:
    print("The number %d is NOT a prime number" % num)

#print the seconds the loop took
endTime = time.time()
totalTime = endTime - startTime
print(f"------ {totalTime} seconds ------")