# HEADER COMMENT HERE
#Programmer = Niyam Acharya
#Program details = Represents an item with a name, price, and taxability
#Attributes:
# __name (str): The name of the item.  
# __price (float): The price of the item in dollars.
# __taxable (bool): True if the item is taxable, False otherwise.


# ADD BOTH LAB PARTNERS NAMES AND USER-ID
#Programmer User-ID = nka42 (14510667)

class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    def itemToString(self):
        return "Item: {}, Price: ${}, Taxable: {}".format(self.__name, self.__price, self.__taxable)

    def getPrice(self):
        return self.__price

    def getTax(self, tax_rate):
        if self.__taxable:
            tax = self.__price * tax_rate
            return tax
        else:
            return 0.0
