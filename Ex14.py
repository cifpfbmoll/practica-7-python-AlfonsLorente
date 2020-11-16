#!/usr/bin/env python3
#encoding: "UTF-16"

#Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, 
#que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes. 
#Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 

#procedure to print the month in words
def monthText(date):
    #Split the date
    day = date[0] + date[1]
    month = date[3] + date[4]
    year = date[6] + date[7] + date[8] + date[9]
    #make the dictionary of the months 
    monthDict = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December"
    }
    #printing the date
    print("The introduced date is:", day, monthDict[month], year )

#ask for the date to the user
date = input("Input a date (dd/mm/year):> ")
#pass the date to the procedure
monthText(date)
