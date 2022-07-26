

class Menu_Usuario:
    

        
 
        def int_input(prompt):
                while True:
                    try:
                        coordinate = int(input(prompt))
                        return coordinate
                    except ValueError as e:
                        print('El valor debe de ser numerico, por favor intenta ingresar otro valor')

        def main_usuario():
            
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
            
            
            print("****** Bienvenido a Cartelera de cines Doña Pelos *****")
            print("[1] Menu Administador")
            print("[2] Menu Usuario")