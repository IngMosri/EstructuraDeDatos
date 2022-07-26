import admin_menu
import menu_user
class Main_menu:

    def int_input(prompt):
        while True:
            try:
                coordinate = int(input(prompt))
                return coordinate
            except ValueError as e:
                print('El valor debe de ser numerico, por favor intenta ingresar otro valor')

    def menuSelection():
     
        correcto = False
        num = 0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto = True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
     
    salir = False
    opcion = 0
     
    while not salir:
     
        
        print("************Bienvenido a Cinema Deluxe de Doña Pelos**************")
        print("[1] Menu Administador")
        print("[2] Menu Usuario")
        print("[3] Salir")
                
        opcion = menuSelection()
        
        if opcion == 1:
            admin_menu.Admin_menu.show_admin_menu()
                
           

        elif opcion == 2:

            menu_user.Menu_user.show_menu()    
            print ("Option 2")
            
           
        elif opcion == 3:
            print("Salir")
            salir = True
        else:
            print ("Choose the option beetween 1 and 3")
        
        print ("End")