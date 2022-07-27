#!/usr/bin/python3
class Menu_user:
    def user_main_menu():
        
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num

    def show_menu():

        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Buscar peliculas por nombre")
            print ("2. Buscar peliculas por clasificacion") 
            print("3 Buscar peliculas por genero")         
            print ("4. Ordernar cartelera( A Y D) ")
            print ("5. Consultar cartelera")
            print ("6. Salir")
            
            print ("choose one option ")
        
            opcion = Menu_user.user_main_menu()
        
            if opcion == 1:
                print ("4. Exit")
            elif opcion == 2:
                print ("4. Exit")
            elif opcion == 3:
                print ("4. Exit")
            elif opcion == 4:
                print ("4. Exit")
            elif opcion == 5:
                print ("4. Exit")
            elif opcion == 6:
                print ("4. Exit")
                salir = True
                
            else:
                print ("Choose the option beetween 1 and 3")
        
