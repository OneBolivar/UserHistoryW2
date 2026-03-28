# Imports the Option2 module to access the global inventory

def product_search (product_name, Inventory):
    return Inventory.get(product_name, {})
