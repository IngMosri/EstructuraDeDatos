#!/usr/bin/python3
import sqlite3
import os

class Admin_menu:
    def main_admin_menu():
        
        if os.path.exists("accounts.db"):
            conn = sqlite3.connect("accounts.db")
            c = conn.cursor()
            
        uname = input("Enter username: ")
        pwd = input("Enter password: ")

        c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [uname, pwd])
        
        if c.fetchone() == None:
            print("Incorrect credentials")
        else:
            print("Logged in!") 
            
            correcto=False
            num=0
            while(not correcto):
                try:
                    num = int(input("choose the following option : "))
                    correcto=True
                except ValueError:
                    print('Error, choose a valid option ')
            
            return num
    
    def show_admin_menu():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Alta de pelicula ")
            print ("2. Alta de horario")
            print ("3. Baja de pelicula")
            print ("4. baja de horario")
            print ("5. Modificar pelicula")
            print ("6. consultar pelicula")
            print ("7. Consultar Cartelera")
            print ("8 . exit ")
            
            
            print ("choose one option ")
        
            opcion = Admin_menu.main_admin_menu()
        
            if opcion == 1:
                
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
                
            elif opcion == 3:
             
                print("Option 3")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")