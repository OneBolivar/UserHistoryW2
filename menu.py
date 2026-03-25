from Option1 import OptionNumber1 # Importa la función OptionNumber1 del módulo Option1
from Option2 import inventory_print # Importa la función para imprimir el inventario de Option2
import Option2 # Importa el módulo Option2 completo para acceder a sus variables
from Option3 import product_search # Importa la función de búsqueda del módulo Option4
import Option4 # Importa el módulo Option4 completo para acceder a sus variables
import Option5 # Importa el módulo Option5 completo para acceder a sus variables    
from Option6 import calculate_statistics # Importa la función de estadísticas del módulo Option3


def MenuOptions(): 
    VALIDATOR = True 
    while VALIDATOR: # Inicia el bucle que repetirá el menú hasta que se decida salir
        print("                   Welcome") 
        print("=" * 50) 
        print("=" * 50) 
        print("1. Add product") 
        print("2. Show inventory") 
        print("3. Search product") 
        print("4. Update product") 
        print("5. Delete product") 
        print("6. Calculates statistics") 
        print("7. Exit") 
        
        #---------------------------------------------------------
        VALIDATOR_OPTIONS = True # Variable para validar la entrada del usuario
        try: # Inicia bloque para manejo de errores (por si el usuario ingresa letras)
            while VALIDATOR_OPTIONS: 
                Options = float(input("What do you want to do?: "))
                print("      ") 
                if (Options <= 0) or (Options > 7): 
                    int("Force Error") # Si el número es inválido, fuerza un error para ir al except
                elif Options == 1: 
                    Option2.Inventory.update(OptionNumber1(Options)) # Actualiza el inventario con lo que retorne OptionNumber1
                elif Options == 2: 
                    inventory_print() # Llama a la función que muestra los productos en pantalla
                elif Options == 3:
                    product_name = input("Enter the name of the product you wish to search for: ")
                    resultado = product_search(product_name)
                    if resultado != {}:
                        print(f"Product Found: {resultado}")
                    else:
                        print("The product doesn't exist in the inventory")
                elif Options == 4:
                    name = input("What product do you want to update?: ")
                    Option4.product_update(name)
                elif Options == 5:
                    Option5.product_delete()
                elif Options == 6:
                    calculate_statistics() # Ejecuta la función que procesa los datos numéricos
                elif Options == 7: 
                    print("Thank you so much for using our system, have a nice day") 
                    VALIDATOR_OPTIONS = False
                    VALIDATOR = False
         
        #------------------------------------------------------------        
        except ValueError: # Se ejecuta si el usuario ingresa algo que no es un número o una opción inválida
            print("---------------------------------------") 
            print("Error only shows the displayed options") # Mensaje de error al usuario
            print("---------------------------------------") 
            print("    ") 
