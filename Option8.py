import csv

def upload_inventory_csv(inventory, route="new_inventory.csv"):
    invalid_rows = 0
    csv_data = {} # Usamos un dict temporal para los nuevos datos
    
    try:
        with open(route, 'r', encoding='utf-8') as csvfile:
            result = csv.reader(csvfile)
            try:
                header = next(result)
            except StopIteration:
                print("The file is empty.")
                return

            if header != ['name', 'price', 'quantity']:
                print("The CSV header is invalid. Expected: name, price, quantity")
                return

            for fila in result:
                # Validar que existan las 3 columnas y no estén vacías
                if len(fila) == 3 and all(item.strip() for item in fila):
                    try:
                        name = fila[0].strip()
                        price = float(fila[1])
                        quantity = int(fila[2])

                        if price > 0 and quantity > 0:
                            csv_data[name] = {'price': price, 'quantity': quantity}
                        else:
                            invalid_rows += 1
                    except ValueError:
                        invalid_rows += 1
                else:
                    invalid_rows += 1
                    
        if not csv_data:
            print("No valid data was found to load.")
            return

        while True:
            option = input("\nDo you want to overwrite the entire current inventory? (Y/N): ").strip().upper()
            if option in ["Y", "N"]:
                break
            print("Please input: Y o N.")

        if option == "Y":
            inventory.clear()
            inventory.update(csv_data)
        else:
            # Actualiza lo existente y agrega lo nuevo sin borrar el resto
            for name, data in csv_data.items():
                inventory[name] = data

        print("\nData successfully loaded.")
        print(f"Invalid rows omitted: {invalid_rows}\n")

    except FileNotFoundError:
        print("File no found.")