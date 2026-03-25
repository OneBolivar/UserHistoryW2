import Option2 # Importa el módulo Option2 para poder acceder al inventario global

def calculate_statistics(): # Define la función para calcular y mostrar estadísticas
    total = 0 # Inicializa la variable total en cero para el acumulado de ventas
    total_products = 0
    product_added = {} # Crea un diccionario local vacío
    product_added.update(Option2.Inventory) # Copia el contenido del inventario desde Option2 al diccionario local
    print("---------------------------------------------------------") # Imprime una línea decorativa
    print("Here are your statistics") # Muestra el encabezado de la sección de estadísticas
    for product, details in product_added.items(): # Inicia un bucle para recorrer cada producto y su información
        total += float((details['price'] * details['quantity'])) # Calcula el valor total por producto y lo suma al acumulado
        total_products += details['quantity']
    print("") # Imprime una línea en blanco para mejorar el formato
    print("---------------------------------------------------------") # Imprime una línea divisoria
    print("Total sales: ", total) # Muestra el valor total acumulado de todo el inventario
    print("Total products:", total_products)
    print("---------------------------------------------------------") # Imprime otra línea divisoria
    print("") # Imprime una línea en blanco final
    return # Finaliza la ejecución de la función y regresa al menú principal
