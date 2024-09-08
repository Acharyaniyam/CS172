#Programmer and userId = Niyam Acharya nka42(14510667)
#Program date = 10/25/2023
#Description = Represents a generic product.
#              Contains information about its name, price, and product ID.
#              Serves as the base class for other product types.

from abc import ABC, abstractmethod

class Product(ABC):
    
    __nextIdNumber = 1000
    
    @staticmethod
    def getNextIdNumber():
        _num = Product.__nextIdNumber
        Product.__nextIdNumber += 1
        return _num
    
    def __init__(self, name, price = 0):
        self.__name = name
        self.__price = price
        self.__productID = self.getNextIdNumber()
        
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getProductID(self):
        return self.__productID
    
    def setPrice(self, price):
        self.__price = price
    
    def __eq__(self,other):
        return self.__productID == other.__productID
    
    def __str__(self):
        return f"Product ID Number: {self.__productID}\nProduct Name: {self.__name}\nProduct Price: ${self.__price:.2f}"
    
    @abstractmethod
    def calculateDiscountedPrice(self):
        return

class ClothingProduct(Product):
    def __init__(self, name, color, size, price = 0):
        Product.__init__(self, name, price)
        self.__color = color
        self.__size = size

    def getColor(self):
        return self.__color

    def getSize(self):
        return self.__size

    def calculateDiscountedPrice(self):
        if self.getPrice() <= 25.00:
            return self.getPrice() - 5.0
        elif 25.00 < self.getPrice() <= 50.00:
            return self.getPrice() - 10.0
        else:
            return self.getPrice() - 15.0

    def __str__(self):
        return "Product ID Number: " + str(self.getProductID()) + "\nProduct Name: " + self.getName() + "\nProduct Price: $" + "{:.2f}".format(self.getPrice()) + "\nColor: " + self.getColor() + "\nSize: " + self.getSize()
    
#Product ID Number: product's ID number here
#Product Name: product's name here
#Product Price: $dollars.cents (with 2 decimal places after the decimal point)
#Color: clothing product's color here
#Size: clothing product's size here
    
class ElectronicProduct(Product):
    def __init__(self, name, brand, availability, price = 0):
        Product.__init__(self, name, price)
        super().setPrice(price)
        self.__brand = brand
        self.__availability = availability

    def getBrand(self):
        return self.__brand

    def getAvailability(self):
        return self.__availability

    def changeAvailability(self):
        self.__availability = not self.__availability

    def calculateDiscountedPrice(self):
        return float(self.getPrice()) * float(0.80)
    
    def __str__(self):
        if self.__availability == True:
            availability_str = "Currently in stock" 
        else:
            availability_str = "Currently out of stock"
        return f"{super().__str__()}\nBrand: {self.__brand}\n{availability_str}"
        
