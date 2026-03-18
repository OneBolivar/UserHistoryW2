def OptionNumber1(Options): # Define la función que recibe la opción elegida
    Inventory= {} # Crea un diccionario vacío para almacenar los datos del nuevo producto
    if Options == 1: 
        VALIDATOR_NAME = True 
        while VALIDATOR_NAME: 
                product_name = input("Enter the product name: ").strip() # Pide el nombre y elimina espacios extras
                if product_name == "": # Valida si el nombre está vacío
                    print("ERROR! Name cannot be empty. ") # Muestra error si no se escribió nada
                else:
                    VALIDATOR_NAME = False 
    #------------------------------------------------------------
        VALIDATOR_PRICE = True # Variable de control para el bucle de validación del precio
        while VALIDATOR_PRICE: # Inicia bucle para asegurar que el precio sea correcto
                try: # Bloque para intentar ejecutar código que puede fallar
                    product_price = float(input("Enter the product price: ")) # Convierte la entrada a número decimal
                    if product_price < 0: # Verifica si el precio es un número negativo
                        int("Force Error") # Fuerza un error manual para saltar al except
                    else:
                        VALIDATOR_PRICE = False # Cambia el estado para salir del bucle del precio
                except ValueError: # Captura errores de tipo de dato o errores forzados
                    print("ERROR! Invalid price (must be a positive number). Try again.") # Mensaje de error
    #------------------------------------------------------------
        VALIDATOR_QUANTITY = True # Variable de control para el bucle de la cantidad
        while VALIDATOR_QUANTITY: # Inicia bucle para validar la cantidad de productos
                try: # Bloque para capturar errores al ingresar la cantidad
                    product_quantity = int(input("How many products do you want to buy?: ")) # Convierte la entrada a entero
                    if product_quantity < 0: # Verifica si la cantidad es negativa
                        int("Force Error") # Fuerza un error manual
                    else:
                        print("Product successfully registered") # Confirma el registro del producto
                        print("  ") # Imprime un espacio en blanco para orden visual
                        VALIDATOR_QUANTITY = False # Cambia el estado para salir del bucle de cantidad
                except ValueError: # Captura errores si no es un entero positivo
                    print("ERROR! Invalid quantity (must be a positive integer). Try again.") # Mensaje de error
        #total = product_price * product_quantity
        Inventory[product_name]={ # Agrega el nombre del producto como clave en el diccionario
            "price" : product_price, # Guarda el precio dentro del sub-diccionario del producto
            "quantity" : product_quantity, # Guarda la cantidad dentro del sub-diccionario del producto
        }
        return(Inventory) # Devuelve el diccionario con la información registrada
