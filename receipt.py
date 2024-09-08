# HEADER COMMENT HERE
#Programmer = Niyam Acharya
#Program details = Represents a receipt with a tax rate and a list of purchased items.
#Attributes:
#     __tax_rate (float): The tax rate for items on the receipt.
#     __purchases (list): A list of Item objects representing purchased items.

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
        
class Receipt:
    def __init__(self, tax_rate=7.0):
        self.__tax_rate = tax_rate
        self.__purchases = []

    def receiptToString(self):
        receipt_str = "Receipt:\n"
        total_price = 0.0
        total_tax = 0.0

        for item in self.__purchases:
            receipt_str += item.itemToString() + "\n"
            total_price += item.getPrice()
            total_tax += item.getTax(self.__tax_rate)

        total_amount = total_price + total_tax
        receipt_str += f"Subtotal: ${total_price:.2f}\nTax ({self.__tax_rate}%): ${total_tax:.2f}\nTotal: ${total_amount:.2f}\n"
        
        return receipt_str

    def addItem(self, item):
        self.__purchases.append(item)
        
        
        