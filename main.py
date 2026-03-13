# Declare a variable called VALIDATOR as True
VALIDADOR = True
# Ask for the product name via input
NameProduct = input("Enter the product name: ")
# Create a while loop with VALIDATOR so the process repeats until valid input is provided
while VALIDADOR:
    # Start a try block to handle potential input errors
    try:
        # Ask for the product price and convert it to float
        ProductPrice = float(input("Enter the product price: "))
        # Ask for the quantity and convert it to int
        ProuctQuantity = int(input("How many products do you want to buy?: "))
        # Calculate total as price times quantity
        Total = ProductPrice * ProuctQuantity
        # Print the product, unit price, quantity, and total to pay
        print("Product:", NameProduct, "| Unit Price:", ProductPrice, "| Quantity:", ProuctQuantity, "| Total to pay:", Total)
        # Set the validator to False to end the loop once the process completes successfully
        VALIDADOR = False
    except ValueError:
        # Show an error message when incorrect numeric input is entered
        print("ERROR! You must enter a number")



   