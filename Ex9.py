#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no. 
#Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden solo las dos últimas tiene que 
#decir que riman un poco y si no, que no riman.

#Make a procedure to see if the two words rhyme
def rhyme(word1, word2):
    #declare some variables
    letter3_1 = ""
    letter3_2 = ""
    letter2_1 = ""
    letter2_2 = ""
    
    #take the 3 last letters with a for loop    
    for i in range(-3, 0):
        letter3_1 += word1[i]
    for i in range(-3, 0):
        letter3_2 += word2[i]
    
    #lower the text
    letter3_1.lower()
    letter3_2.lower()
    #copy the 2 last letters to other variables
    letter2_1 = letter3_1[1] + letter3_1[2]
    letter2_2 = letter3_2[1] + letter3_2[2]

    #print if they rhyme or not
    if letter3_1 == letter3_2:
        print("%s and %s does rhyme" % (word1, word2))
    elif letter2_1 == letter2_2:
        print("%s and %s does just rhyme a little bit" % (word1, word2))
    else:
        print("they dont rhyme")


#ask the usr for 2 words
word1 = input("input a word:> ")
word2 = input("input another word:> ")
while len(word1) < 3 or len(word2) < 3:
    print("Both words have to be longer than 2 words")
    word1 = input("input a word:> ")
    word2 = input("input another word:> ")
rhyme(word1, word2)
