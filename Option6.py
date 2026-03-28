

def calculate_statistics(Inventory):
    # STATISTICS MODULE: Calculate key inventory metrics and insights
    # Computes: total units, total value, most expensive item, highest stock item
    
    # 1. COPY INVENTORY: Create local version to work with
    product_added = {}
    product_added.update(Inventory)

    if not product_added:
        print("\n The inventory is empty.")
        return

    # 2. LAMBDA FUNCTION: Calculate subtotal (price × quantity) for any product
    # Usage: calculate_subtotal(product_data)
    # Lambda is a concise way to define simple calculation functions
    calculate_subtotal = lambda d: d['price'] * d['quantity']

    # 3. AGGREGATE CALCULATIONS: Sum all quantities and total inventory value
    # Using generator expressions for memory efficiency
    total_units = sum(d['quantity'] for d in product_added.values())
    total_value = sum(calculate_subtotal(d) for d in product_added.values())

    # 4. FIND MAX VALUES: Identify most expensive and highest stock items
    # max() with lambda key function finds the maximum based on specific criteria
    # This demonstrates advanced Python techniques for data analysis
    expensive_name, expensive_data = max(product_added.items(), key=lambda item: item[1]['price'])
    stock_name, stock_data = max(product_added.items(), key=lambda item: item[1]['quantity'])

    # 5. Display statistics in a readable format
    print("\n---------------------------------------------------------")
    print("                INVENTORY STATISTICS")
    print("---------------------------------------------------------")
    print(f"Total units:          {total_units}")
    print(f"Total value:          ${total_value:,.2f}")
    print(f"Most expensive:       {expensive_name} (${expensive_data['price']})")
    print(f"Highest stock:        {stock_name} ({stock_data['quantity']} units)")
    print("---------------------------------------------------------")
