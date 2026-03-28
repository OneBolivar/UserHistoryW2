import csv

def upload_inventory_csv(inventory, route="new_inventory.csv"):
    # CSV IMPORT MODULE: Load and validate inventory data from external CSV file
    # Strict validation ensures data integrity before updating main inventory
    invalid_rows = 0
    csv_data = {} # We use a temporary dict for the new data
    
    try:
        with open(route, 'r', encoding='utf-8') as csvfile:
            result = csv.reader(csvfile)
            try:
                header = next(result)
            except StopIteration:
                print("The file is empty.")
                return

            # CRITICAL VALIDATION: Header must match exact format
            if header != ['name', 'price', 'quantity']:
                print("The CSV header is invalid. Expected: name, price, quantity")
                return

            for fila in result:
                # MULTI-LEVEL VALIDATION: Check structure, types, and values
                # Validate that the 3 columns exist and are not empty
                if len(fila) == 3 and all(item.strip() for item in fila):
                    try:
                        # TYPE CONVERSION: Convert to correct data types and validate
                        name = fila[0].strip()
                        price = float(fila[1])
                        quantity = int(fila[2])

                        # VALUE VALIDATION: Ensure positive values only
                        if price > 0 and quantity > 0:
                            csv_data[name] = {'price': price, 'quantity': quantity}
                        else:
                            invalid_rows += 1
                    except ValueError:  # Catches conversion errors
                        invalid_rows += 1
                else:
                    invalid_rows += 1
                    
        if not csv_data:
            print("No valid data was found to load.")
            return

        # MERGE STRATEGY: Ask user how to handle existing inventory
        while True:
            option = input("\nDo you want to overwrite the entire current inventory? (Y/N): ").strip().upper()
            if option in ["Y", "N"]:
                break
            print("Please input: Y o N.")

        # APPLY CHANGES: Two merge strategies available
        if option == "Y":
            # OPTION 1: Complete Replacement - Clear all and load CSV data
            inventory.clear()
            inventory.update(csv_data)
        else:
            # OPTION 2: Merge Mode - Keep existing, add/update from CSV
            # Updates the existing and adds the new without deleting the rest
            for name, data in csv_data.items():
                inventory[name] = data

        print("\nData successfully loaded.")
        print(f"Invalid rows omitted: {invalid_rows}\n")

    except FileNotFoundError:
        print("File no found.")
