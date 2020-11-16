#!/usr/bin/env python3
#encoding: "UTF-16"

#Desarrolla un programa que nos sirva para gestionar nuestros contactos (la información a gestionar será el teléfono, nombre,
#apellido1, apellido2 y correo electrónico. El programa tendrá un menú, con las siguientes opciones: añadir contacto, 
#consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido 
#hasta el momento (diccionarios, funciones, procedimientos…).

def menu():
    print("Menu:")
    print("1. Add contact")
    print("2. View contact")
    print("3. View all contacts")
    print("4. Erase contact")
    print("5. Close the program")
    option = int(input("Input the desired option (1, 2, 3 or 4):> "))
    while option > 5 or option < 1:
        print("You have to choose between the options given (1, 2, 3, 4)")
        option = int(input("Input a valid option:> "))
    return option

def addContact(diary):
    number = int(input("Number: "))
    name = input("Name: ")
    midname = input("midname: ")
    lastname = input("lastname: ")
    email = input("email: ")
    contact = {
        "number":number,
        "name":name,
        "midname":midname,
        "lastname":lastname,
        "email":email
    }
    fullname = name +" "+ midname + " " + lastname
    diary.update({fullname:contact})
    return diary

def viewContact(diary):
    print("your viable contacts are: ")
    print(diary.keys())
    print("Name of the contact you want to see")
    name = input("> ")
        



if __name__ == "__main__":
    diary = {}
    option = int
    while option != 5:
        option = menu()
        if option == 1:
            diary = addContact(diary)
        
        elif option == 2:
            viewContact(diary)

    else:
        print("The program has finished")
    