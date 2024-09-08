#Programmer and userId = Niyam Acharya nka42(14510667)
#Program date = 10/25/2023
#Description = Main application script for the shopping cart program.
#              Instantiates a shopping cart and interacts with it.
#              Adds and removes products, calculates the total price, and displays the shopping cart's contents.
#              Demonstrates the functionality of the implemented classes.
from products import ClothingProduct, ElectronicProduct, Product
from shopping import ShoppingCart


cart = ShoppingCart()


product1 = ElectronicProduct("Laptop","Dell",True, 1200.0)
product2 = ClothingProduct("T-shirt", "Blue", "Large", 25.0)
product3 = ClothingProduct("Jeans", "Black", "Medium", 65.0)
product4 = ElectronicProduct("Smartphone", "Samsung", True, 800.0)
product5 = ClothingProduct("Sweater", "Small", "Red", 45.0)
product6 = ElectronicProduct("Tablet", "Apple", False ,300.0)

cart.addProduct(product1)
cart.addProduct(product2)
cart.addProduct(product3)
cart.addProduct(product4)
cart.addProduct(product5)
cart.addProduct(product6)


cart.removeProduct(product2.getProductID())
cart.removeProduct(product4.getProductID())

cart.changeSaleStatus(True)
print(f"There are {len(cart.getProducts())} items in your shopping cart.")
if cart.getSaleStatus():
    print("We are having a sale. Discounts have been applied.")
print(f"Total price: ${cart.calculateTotalPrice():.2f}")

cart.changeSaleStatus(False)
print(f"There are {len(cart.getProducts())} items in your shopping cart.")
print(f"Total price: ${cart.calculateTotalPrice():.2f}")
