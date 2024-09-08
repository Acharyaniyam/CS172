#Programmer and userId = Niyam Acharya nka42(14510667)
#Program date = 10/25/2023
#Description = Manages a collection of products and handles shopping cart operations.
#              Provides methods to add, remove, and calculate the total price of products in the cart.
#              Tracks whether the store is having a sale or not.
class ShoppingCart:
    def __init__(self):
        self.__products = []
        self.__onSale = False

    def getProducts(self):
        return self.__products

    def getSaleStatus(self):
        return self.__onSale

    def changeSaleStatus(self):
        self.__onSale = not self.__onSale

    def addProduct(self, product):
        self.__products.append(product)

    def removeProduct(self, productID):
        for product in self.__products:
            if product.getProductID() == productID:
                self.__products.remove(product)
                break

    def calculateTotalPrice(self):
        total_price = sum(product.calculateDiscountedPrice() if self.__onSale else product.getPrice() for product in self.__products)
        return total_price
    def calculateTotalPrice(self):
        total_price = sum(product.calculateDiscountedPrice() if self.__onSale else product.getPrice() for product in self.__products)
        return total_price

    def __str__(self):
        num_items = len(self.__products)
        sale_status = "We are having a sale. Discounts have been applied." if self.__onSale else ""
        total_price = self.calculateTotalPrice()
        
        if self.__onSale == True:
            return f"There are {num_items} items in your shopping cart.\n{sale_status}\nTotal price: ${total_price:.2f}"
        else:
            return f"There are {num_items} items in your shopping cart.\nTotal price: ${total_price:.2f}"
        