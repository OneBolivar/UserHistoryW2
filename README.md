# 📦 Inventory Management System (UserHistoryW3)

A Python-based command-line inventory management application that allows users to perform complete CRUD operations (Create, Read, Update, Delete) on product inventory, calculate statistics, and import/export data via CSV files.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [System Architecture](#system-architecture)
- [File Descriptions](#file-descriptions)
- [Data Structures](#data-structures)
- [Installation & Usage](#installation--usage)
- [How Each Feature Works](#how-each-feature-works)
- [Key Technical Concepts](#key-technical-concepts)
- [Error Handling](#error-handling)
- [Usage Examples](#usage-examples)

---

## 🎯 Project Overview

**Purpose:** This inventory management system is a full-featured application designed to:
- Add and manage product inventory with validation
- Track product prices and quantities
- Search for specific products
- Update product information
- Delete products with confirmation
- Generate automated statistics and analytics
- Save inventory data to CSV format
- Import inventory data from CSV files with strict validation

**Language:** Python 3  
**Data Storage:** In-memory dictionary + CSV file persistence  
**Interface:** Interactive command-line menu  
**Validation:** Comprehensive input validation for all user inputs

---

## 📁 Project Structure

```
UserHistoryW3/
├── main.py                 # Application entry point
├── menu.py                 # Main menu controller (central hub)
├── Option1.py              # Add product functionality
├── Option2.py              # Show/display inventory
├── Option3.py              # Search for products
├── Option4.py              # Update product information
├── Option5.py              # Delete products
├── Option6.py              # Calculate statistics and analytics
├── Option7.py              # Export inventory to CSV
├── Option8.py              # Import inventory from CSV
├── inventory.csv           # Saved inventory data
├── new_inventory.csv       # Template for importing products
└── README.md              # This documentation file
```

---

## ✨ Features

### 1. **Add Product** (Option 1)
   - Validate product name (non-empty)
   - Validate price (positive float)
   - Validate quantity (positive integer)
   - Store in both memory and CSV export list

### 2. **Show Inventory** (Option 2)
   - Display all products with prices and quantities
   - Professional formatted output
   - Shows price per unit and current stock

### 3. **Search Product** (Option 3)
   - Find specific products by name
   - Returns product details if found
   - Returns "not found" if product doesn't exist

### 4. **Update Product** (Option 4)
   - Modify product prices
   - Modify product quantities
   - Update both price and quantity simultaneously
   - Shows current values before update

### 5. **Delete Product** (Option 5)
   - Remove products from inventory
   - Requires user confirmation (safety feature)
   - Prevents accidental deletions

### 6. **Calculate Statistics** (Option 6)
   - Total units in inventory
   - Total inventory value (sum of all subtotals)
   - Most expensive product
   - Product with highest stock quantity
   - Uses advanced lambda functions and aggregation

### 7. **Save to CSV** (Option 7)
   - Export inventory to `inventory.csv`
   - UTF-8 encoding for international characters
   - CSV format: Product, Price, Quantity
   - Overwrites existing file

### 8. **Import from CSV** (Option 8)
   - Load inventory from `new_inventory.csv`
   - Strict validation of all data
   - Two merge strategies: Overwrite or Merge
   - Counts and reports invalid rows

### 9. **Exit** (Option 9)
   - Clean application shutdown
   - Displays farewell message

---

## 🏗️ System Architecture

### Data Flow Diagram

```
main.py → menu.py → [User Input]
              ↓
         Route to Option
              ↓
    [Option1-8] → Modify Inventory Dictionary
              ↓
         Return to Menu Loop
              ↓
         Exit (Option 9)
```

### Global Data Structures

**`Inventory` Dictionary:**
```python
{
    "Product_Name": {
        "price": 100.50,    # Unit price (float)
        "quantity": 25      # Stock quantity (integer)
    },
    "Another_Product": {
        "price": 50.00,
        "quantity": 100
    }
}
```

**`Inventory_to_csv` List:**
```python
[
    {"Product": "Laptop", "Price": 500.0, "Quantity": 10},
    {"Product": "Mouse", "Price": 25.0, "Quantity": 50}
]
```

---

## 📄 File Descriptions

### `main.py` (Entry Point)
**Purpose:** Application launcher  
**What it does:**
- Imports `MenuOptions` from menu.py
- Calls `MenuOptions()` to start the application
- Simple 2-line initialization script

**Key Code:**
```python
# Entry point comment: This is where the application starts
from menu import MenuOptions
MenuOptions()    # Launches the main menu loop
```

---

### `menu.py` (Central Controller) ⭐ **MOST IMPORTANT**
**Purpose:** Main menu system that controls the entire application flow  
**Key Responsibilities:**
- Initializes global `Inventory` dictionary (stores all products in memory)
- Initializes `Inventory_to_csv` list (for CSV export)
- Displays 9-option menu in infinite loop
- Routes user selections to appropriate Option modules
- Validates menu input (must be 1-9)

**Critical Features:**
```python
# INPUT VALIDATION: Ensures option is between 1-9
if (Options <= 0) or (Options > 9):
    int("Force Error")  # Triggers ValueError to show error message

# ERROR HANDLING: Catches non-numeric input
try:
    Options = float(input("What do you want to do?: "))
except ValueError:
    print("Error only shows the displayed options")
```

**Menu Loop Workflow:**
1. Display menu options (1-9)
2. Get user input for menu option
3. Validate input (1-9 numeric only)
4. Route to selected Option module
5. Execute option function
6. Loop back to step 1 (until Exit selected)

---

### `Option1.py` (Add Product) ⭐ **DEMONSTRATES VALIDATION**
**Purpose:** Add new products to inventory  
**Validation Steps (3-level):**

**Step 1: Name Validation**
```python
while VALIDATOR_NAME:
    product_name = input("Enter the product name: ").strip()
    if product_name == "":
        print("ERROR! Name cannot be empty.")
    else:
        VALIDATOR_NAME = False  # Exit loop only if valid
```

**Step 2: Price Validation**
```python
while VALIDATOR_PRICE:
    try:
        product_price = float(input("Enter the product price: "))
        if product_price < 0:
            int("Force Error")  # Trigger exception
        else:
            VALIDATOR_PRICE = False
    except ValueError:
        print("ERROR! Invalid price (must be a positive number)")
```

**Step 3: Quantity Validation**
```python
while VALIDATOR_QUANTITY:
    try:
        product_quantity = int(input("How many products: "))
        if product_quantity < 0:
            int("Force Error")
        else:
            VALIDATOR_QUANTITY = False
    except ValueError:
        print("ERROR! Invalid quantity (must be positive integer)")
```

**Data Storage:**
```python
# Add to main inventory dictionary
Inventory[product_name] = {
    "price": product_price,      # Store as float
    "quantity": product_quantity  # Store as integer
}

# Also add to CSV export list
Inventory_to_csv.append({
    "Product": product_name,
    "Price": product_price,
    "Quantity": product_quantity
})
```

---

### `Option2.py` (Show Inventory)
**Purpose:** Display all products in formatted list  
**Output Format:**
```
---------------------------------------------------------
Here are your inventory
Product: Laptop
  Price: 500.0 by unit
  Quantity: 10
Product: Mouse
  Price: 25.0 by unit
  Quantity: 50
---------------------------------------------------------
```

**Key Code:**
```python
def inventory_print(Inventory):
    product_added = {}
    product_added.update(Inventory)  # Create local copy
    
    for product, details in product_added.items():
        print(f"Product: {product}")
        print(f"  Price: {details['price']} by unit")
        print(f"  Quantity: {details['quantity']}")
```

---

### `Option3.py` (Search Product)
**Purpose:** Find specific products by name  
**Logic:**
- Uses dictionary `.get()` method for safe searching
- Returns product data if found
- Returns empty dictionary `{}` if not found

**Code:**
```python
def product_search(product_name, Inventory):
    return Inventory.get(product_name, {})
    # .get() returns the value if found, {} (empty dict) if not
```

**Example:**
```python
# Looking for "Laptop" that exists:
result = product_search("Laptop", Inventory)
# Returns: {"price": 500.0, "quantity": 10}

# Looking for "Pen" that doesn't exist:
result = product_search("Pen", Inventory)
# Returns: {} (empty dictionary)
```

---

### `Option4.py` (Update Product) ⭐ **DEMONSTRATES UPDATE LOGIC**
**Purpose:** Modify existing product prices and/or quantities  
**Features:**
- Cannot update if product doesn't exist
- Shows current values before update
- Three update options available

**Critical Validation:**
```python
# CRITICAL CHECK: Verify product exists first
producto = Inventory.get(name)
if not producto:
    print(f"Product '{name}' not found.")
    return False
```

**Update Options:**
```python
# OPTION 1: Update price only
if option == "1":
    producto["price"] = float(input("New price: "))

# OPTION 2: Update quantity only
elif option == "2":
    producto["quantity"] = int(input("New stock: "))

# OPTION 3: Update both
elif option == "3":
    producto["price"] = float(input("New price: "))
    producto["quantity"] = int(input("New stock: "))
```

**Note:** Updates happen directly in the dictionary (reference modification). The `Inventory_to_csv` list is not updated (potential design improvement).

---

### `Option5.py` (Delete Product)
**Purpose:** Remove products from inventory with confirmation  
**Safety Feature:** Requires user confirmation to prevent accidents

**Delete Logic:**
```python
name = input("Enter the product name to delete: ")

# Check if product exists
if name in Inventory:
    # Ask for confirmation
    confirmar = input(f"Delete '{name}'? (Yes/No): ").lower()
    
    if confirmar == 'yes':
        del Inventory[name]  # Remove from dictionary
        print(f"Product '{name}' successfully deleted.")
    else:
        print("Operation cancelled")
else:
    print(f"Error: Product '{name}' not found")
```

---

### `Option6.py` (Calculate Statistics) ⭐ **DEMONSTRATES ADVANCED PYTHON**
**Purpose:** Generate inventory analytics and insights  
**Metrics Calculated:**
1. **Total Units:** Sum of all quantities
2. **Total Value:** Sum of (price × quantity) for all products
3. **Most Expensive:** Product with highest unit price
4. **Highest Stock:** Product with most quantity

**Key Technical Concepts:**

**Lambda Functions:**
```python
# Lambda: Anonymous function for quick calculations
calculate_subtotal = lambda d: d['price'] * d['quantity']
# Usage: calculate_subtotal(product_dict) returns result
```

**Generator Expressions (Memory Efficient):**
```python
# Calculate total units: sum of all quantities
total_units = sum(d['quantity'] for d in product_added.values())

# Calculate total value: sum of all subtotals
total_value = sum(calculate_subtotal(d) for d in product_added.values())
```

**Finding Maximum Values:**
```python
# Find most expensive product using max() with lambda key
expensive_name, expensive_data = max(
    product_added.items(),
    key=lambda item: item[1]['price']  # Compare by price
)

# Find highest stock using max() with lambda key
stock_name, stock_data = max(
    product_added.items(),
    key=lambda item: item[1]['quantity']  # Compare by quantity
)
```

**Output Example:**
```
---------INVENTORY STATISTICS--------
Total units:          75
Total value:          $12,750.50
Most expensive:       Laptop ($500.00)
Highest stock:        Mouse (50 units)
```

---

### `Option7.py` (Export to CSV)
**Purpose:** Save inventory to CSV file  
**Features:**
- Uses Python's `csv` module with `DictWriter`
- UTF-8 encoding for international characters
- Overwrites existing file
- Headers: Product, Price, Quantity

**Export Logic:**
```python
def save_csv(Inventory_to_csv, route='inventory.csv'):
    if not Inventory_to_csv:
        print("No information has been saved")
        return
    
    try:
        with open(route, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product', 'Price', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header row
            writer.writerows(Inventory_to_csv)  # Write data rows
        return f"Inventory stored in: {route}"
    except FileExistsError:
        print("The csv file could not be saved")
```

**CSV Output Format:**
```
Product,Price,Quantity
Laptop,500.0,10
Mouse,25.0,50
Keyboard,75.0,15
```

---

### `Option8.py` (Import from CSV) ⭐ **DEMONSTRATES STRICT VALIDATION**
**Purpose:** Load inventory from CSV file with comprehensive validation  
**Validation Levels:**
1. **File existence check**
2. **Header format validation** (must be: name, price, quantity)
3. **Row structure validation** (exactly 3 columns, no empty cells)
4. **Data type validation** (name=string, price=float, quantity=int)
5. **Value validation** (price > 0, quantity > 0)

**Multi-Level Validation:**
```python
# LEVEL 1: File validation
try:
    with open(route, 'r', encoding='utf-8') as csvfile:
        result = csv.reader(csvfile)
        header = next(result)
        
        # LEVEL 2: Header validation (CRITICAL)
        if header != ['name', 'price', 'quantity']:
            print("CSV header is invalid")
            return
        
        # LEVEL 3-5: Row validation
        for fila in result:
            # Check structure: 3 columns, no empty fields
            if len(fila) == 3 and all(item.strip() for item in fila):
                try:
                    # Type conversion with validation
                    name = fila[0].strip()
                    price = float(fila[1])
                    quantity = int(fila[2])
                    
                    # Value validation: positive only
                    if price > 0 and quantity > 0:
                        csv_data[name] = {
                            'price': price,
                            'quantity': quantity
                        }
                    else:
                        invalid_rows += 1
                except ValueError:  # Conversion failed
                    invalid_rows += 1
            else:
                invalid_rows += 1

except FileNotFoundError:
    print("File not found")
```

**Merge Strategies:**
```python
# OPTION 1: Overwrite entire inventory (Y)
if option == "Y":
    inventory.clear()  # Delete all existing
    inventory.update(csv_data)  # Add CSV data

# OPTION 2: Merge mode (N)
else:
    for name, data in csv_data.items():
        inventory[name] = data  # Add/update from CSV, keep rest
```

**Example Invalid Rows (from new_inventory.csv):**
```
name,price,quantity
,50.0,3              # ← Empty product name
mesa,-20.0,2         # ← Negative price
lapiz,abc,10         # ← Invalid price (not a number)
silla,30.0,-5        # ← Negative quantity
monitor,40.0         # ← Missing quantity (only 2 columns)
teclado," ",4        # ← Empty quantity value
mouse,25.0,2,extra   # ← Extra column (4 instead of 3)
```

---

## 📊 Data Structures

### Inventory Dictionary (In-Memory Storage)
```python
Inventory = {
    "Laptop": {
        "price": 500.0,      # Unit price as float
        "quantity": 10       # Stock count as integer
    },
    "Mouse": {
        "price": 25.0,
        "quantity": 50
    },
    "Keyboard": {
        "price": 75.0,
        "quantity": 15
    }
}
```

**Access Pattern:**
```python
Inventory["Laptop"]["price"]      # Returns: 500.0
Inventory["Mouse"]["quantity"]    # Returns: 50
```

### Inventory_to_csv List (CSV Export Buffer)
```python
Inventory_to_csv = [
    {"Product": "Laptop", "Price": 500.0, "Quantity": 10},
    {"Product": "Mouse", "Price": 25.0, "Quantity": 50},
    {"Product": "Keyboard", "Price": 75.0, "Quantity": 15}
]
```

### CSV File Format (inventory.csv)
```
Product,Price,Quantity
Laptop,500.0,10
Mouse,25.0,50
Keyboard,75.0,15
```

### CSV Import Format (new_inventory.csv)
```
name,price,quantity
item_name,50.00,10
another_item,100.00,5
```

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No external packages required (uses only built-in modules)

### Running the Application

**Step 1: Navigate to project directory**
```bash
cd c:\Users\SULEIMA\Desktop\UserHistoryW3\UserHistoryW3
```

**Step 2: Run main.py**
```bash
python main.py
```

**Step 3: Follow the menu prompts**
```
                   Welcome
==================================================
==================================================
1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Calculates statistics
7. Save CSV
8. Upload CSV
9. Exit

What do you want to do?: [Enter your choice]
```

---

## 💡 How Each Feature Works

### Adding a Product
```
1. Select option 1
2. Enter product name (e.g., "Laptop")
3. Enter price (e.g., 500.0)
4. Enter quantity (e.g., 10)
5. Product is stored and ready to use

Data stored as:
Inventory["Laptop"] = {"price": 500.0, "quantity": 10}
```

### Viewing Inventory
```
2. Select option 2
→ Application displays all products with prices and quantities
→ Shows formatted output with decorative borders
```

### Searching for a Product
```
3. Select option 3
4. Enter product name (e.g., "Laptop")
→ Returns product details if found
→ Returns "not found" message if product doesn't exist
```

### Updating a Product
```
4. Select option 4
5. Enter product name
6. Choose update type:
   - 1: Change price only
   - 2: Change quantity only  
   - 3: Change both
7. Enter new value(s)
→ Product updated in inventory
```

### Deleting a Product
```
5. Select option 5
6. Enter product name
7. Confirm deletion (Yes/No)
→ If confirmed: Product removed from inventory
→ If declined: Operation cancelled
```

### Calculating Statistics
```
6. Select option 6
→ Displays:
  - Total units in stock
  - Total inventory value
  - Most expensive product
  - Product with highest quantity
```

### Saving to CSV
```
7. Select option 7
→ Exports all products to inventory.csv
→ File saved in same directory as Python files
→ Can be opened in Excel or any spreadsheet application
```

### Loading from CSV
```
8. Select option 8
→ Reads new_inventory.csv
→ Validates all data (very strict)
→ Asks: Overwrite or Merge?
  - Y: Replace entire inventory with CSV data
  - N: Keep current items + add/update from CSV
→ Reports number of invalid rows encountered
```

---

## 🔧 Key Technical Concepts

### 1. **Dictionary (Hash Map)**
Python dictionaries store key-value pairs for O(1) lookup:
```python
# Storing products by name as dictionary keys
Inventory = {
    "Laptop": {"price": 500.0, "quantity": 10},
    "Mouse": {"price": 25.0, "quantity": 50}
}

# Fast lookup: O(1) time complexity
product = Inventory["Laptop"]  # Instant access
```

### 2. **Input Validation (Try/Except)**
Prevents crashes from invalid user input:
```python
try:
    price = float(input("Enter price: "))
    if price < 0:
        int("Force Error")  # Manually trigger exception
except ValueError:
    print("Error: Must be positive number")
```

### 3. **Lambda Functions**
Concise anonymous functions for quick calculations:
```python
# Lambda syntax: lambda [parameters]: [expression]
calculate_subtotal = lambda d: d['price'] * d['quantity']

# Usage:
total = calculate_subtotal({"price": 50, "quantity": 3})  # 150
```

### 4. **Generator Expressions**
Memory-efficient iteration:
```python
# Calculate sum efficiently without creating intermediate list
total = sum(d['quantity'] for d in Inventory.values())
```

### 5. **max() with Custom Key Function**
Find maximum based on specific criteria:
```python
# Find product with highest price
expensive = max(
    inventory.items(),
    key=lambda item: item[1]['price']
)
```

### 6. **CSV Module**
Import/export data with proper formatting:
```python
import csv
from csv import DictWriter, DictReader  # High-level interface
```

### 7. **Context Managers (with statement)**
Ensures files are properly opened and closed:
```python
with open('file.csv', 'w') as f:
    # File automatically closes at end of block
    # Even if error occurs
```

### 8. **String Methods**
Data cleaning and validation:
```python
product_name = input("Enter name: ").strip()  # Remove whitespace
if product_name == "":  # Check if empty
    print("Cannot be empty")
```

---

## ⚠️ Error Handling

The application includes comprehensive error handling:

| Error Type | Where | Handling |
|-----------|-------|----------|
| Non-numeric menu input | menu.py | ValueError caught, error message shown |
| Menu option out of range (< 1 or > 9) | menu.py | Forced error, error message shown |
| Empty product name | Option1.py | While loop continues until valid |
| Negative/non-numeric price | Option1.py | ValueError caught, retry loop |
| Negative/non-numeric quantity | Option1.py | ValueError caught, retry loop |
| Product not found (search) | Option3.py | Returns empty dict, "not found" message |
| Product not found (update) | Option4.py | Returns error, exits function |
| Product not found (delete) | Option5.py | Returns error message |
| Empty inventory (stats) | Option6.py | Returns early with "empty" message |
| No data to save (CSV export) | Option7.py | Shows "No information saved" |
| CSV file not found | Option8.py | FileNotFoundError caught |
| Invalid CSV header | Option8.py | Format validation, error shown |
| Invalid CSV rows | Option8.py | Row skipped, count incremented |
| Invalid data types in CSV | Option8.py | ValueError caught, row skipped |
| Negative values in CSV | Option8.py | Value validation fails, row skipped |

---

## 📝 Usage Examples

### Example 1: Adding Products and Viewing Inventory
```
Welcome
==================================================
1. Add product
2. Show inventory
...

What do you want to do?: 1

Enter the product name: Laptop
Enter the product price: 500.0
How many products do you want to buy?: 10
Product successfully registered

What do you want to do?: 1

Enter the product name: Mouse
Enter the product price: 25.0
How many products do you want to buy?: 50
Product successfully registered

What do you want to do?: 2

---------------------------------------------------------
Here are your inventory
Product: Laptop
  Price: 500.0 by unit
  Quantity: 10
Product: Mouse
  Price: 25.0 by unit
  Quantity: 50
---------------------------------------------------------
```

### Example 2: Updating Product Information
```
What do you want to do?: 4

What product do you want to update?: Laptop

Update: Laptop (Price: 500.0, Stock: 10)
1. Change Price
2. Change Stock
3. Change Both

Choose an option: 2

New stock: 7
Update successful.
```

### Example 3: Calculating Statistics
```
What do you want to do?: 6

---------INVENTORY STATISTICS--------
Total units:          57
Total value:          $13,687.50
Most expensive:       Laptop ($500.00)
Highest stock:        Mouse (50 units)
```

### Example 4: Save and Export
```
What do you want to do?: 7

Inventory stored in: inventory.csv

[File content - inventory.csv:]
Product,Price,Quantity
Laptop,500.0,10
Mouse,25.0,50
```

### Example 5: Import with Merge
```
What do you want to do?: 8

Do you want to overwrite the entire current inventory? (Y/N): N

Data successfully loaded.
Invalid rows omitted: 3
```

---

## 🔍 Important Code Sections to Review

### Most Important #1: data Structure
**File:** `menu.py`  
**Why:** Central storage for all inventory data
```python
Inventory = {}  # All products stored here
Inventory_to_csv = []  # Export buffer
```

### Most Important #2: Input Validation Pattern
**File:** `Option1.py`  
**Why:** Shows how to validate user input safely
```python
while VALIDATOR:
    try:
        value = type(input(...))
        if value < minimum:
            int("Force Error")
        else:
            VALIDATOR = False
    except ValueError:
        print("Error message")
```

### Most Important #3: Product Access Pattern
**File:** `Option3.py`, `Option4.py`, `Option5.py`  
**Why:** Safe way to access dictionary values
```python
product = Inventory.get(name, {})  # Returns {} if not found
if product:
    # Safe to use
```

### Most Important #4: Lambda & max() for Analytics
**File:** `Option6.py`  
**Why:** Advanced Python for data analysis
```python
expensive = max(inventory.items(), key=lambda item: item[1]['price'])
```

### Most Important #5: CSV Validation Layer
**File:** `Option8.py`  
**Why:** Multi-level validation prevents corrupt data
```python
# Check: format, types, values, ranges
```

---

## 🎓 Learning Value

This project demonstrates:
✅ Dictionary data structures and operations  
✅ Input validation and error handling  
✅ File I/O (CSV reading/writing)  
✅ Lambda functions and advanced iteration  
✅ Try/except exception handling  
✅ Control flow (loops, conditionals)  
✅ String manipulation  
✅ Program architecture (modular design)  
✅ User interface design (menu system)  
✅ Data validation best practices  

---

## 📞 Support & Notes

- All files must be in the same directory for imports to work
- Ensure Python 3.6+ is installed
- CSV files should use standard format (comma-separated, UTF-8 encoding)
- The application stores data in memory; use "Save CSV" to persist data

---

**Last Updated:** 2026-03-27  
**Version:** 1.0  
**Status:** Complete and Functional
