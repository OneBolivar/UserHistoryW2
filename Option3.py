import Option2 # Importa el módulo Option2 para poder acceder al inventario global

def product_search (product_name):
    
    return Option2.Inventory.get(product_name, {})