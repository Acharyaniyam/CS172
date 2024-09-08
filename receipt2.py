class Receipt:
    def __init__(self, tax_rate=0.07):
        self.__tax_rate = tax_rate
        self.__purchases = []

    def receiptToString(self):
        total_cost = sum(item.getPrice() + item.getTax(self.__tax_rate) for item in self.__purchases)
        receipt_str = "Receipt:\n"
        
        for item in self.__purchases:
            receipt_str += item.itemToString() + "\n"

        receipt_str += f"Total Cost: ${total_cost:.2f}"
        return receipt_str

    def addItem(self, item):
        if isinstance(item, Item):
            self.__purchases.append(item)
        else:
            raise ValueError("Only Item objects can be added to the receipt.")

