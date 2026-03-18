from Option1 import OptionNumber1 # Importa la función OptionNumber1 del módulo Option1
from Option2 import inventory_print # Importa la función para imprimir el inventario de Option2
import Option2 # Importa el módulo Option2 completo para acceder a sus variables
from Option3 import calculate_statistics # Importa la función de estadísticas del módulo Option3

def MenuOptions(): 
    VALIDATOR = True 
    while VALIDATOR: # Inicia el bucle que repetirá el menú hasta que se decida salir
        print("                   Welcome") 
        print("=" * 50) 
        print("=" * 50) 
        print("1. Add product") 
        print("2. Show inventory") 
        print("3. Calculates statistics") 
        print("4. Exit") 
        
        #---------------------------------------------------------
        VALIDATOR_OPTIONS = True # Variable para validar la entrada del usuario
        try: # Inicia bloque para manejo de errores (por si el usuario ingresa letras)
            while VALIDATOR_OPTIONS: 
                Options = float(input("What do you want to do?: "))
                print("      ") 
                if (Options <= 0) or (Options > 4): 
                    int("Force Error") # Si el número es inválido, fuerza un error para ir al except
                elif Options == 1: 
                    Option2.Inventory.update(OptionNumber1(Options)) # Actualiza el inventario con lo que retorne OptionNumber1
                    
                elif Options == 2: 
                    inventory_print() # Llama a la función que muestra los productos en pantalla
                elif Options == 3:
                    calculate_statistics() # Ejecuta la función que procesa los datos numéricos
                elif Options == 4: 
                    print("Muchas gracias por usar nuestro sistema, tenga un bonito dia") 
                    VALIDATOR_OPTIONS = False
                    VALIDATOR = False
         
        #------------------------------------------------------------        
        except ValueError: # Se ejecuta si el usuario ingresa algo que no es un número o una opción inválida
            print("---------------------------------------") 
            print("Error only shows the displayed options") # Mensaje de error al usuario
            print("---------------------------------------") 
            print("     ") 
