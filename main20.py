# HEADER COMMENT HERE
#Programmer = Niyam Acharya

# ADD BOTH LAB PARTNERS NAMES AND USER-ID
#Programmer User-ID = nka42 (14510667)


from receipt import Receipt
from item import Item
import datetime

#Main Program
    
def main():
    print("Welcome to Receipt Creator")
    
    r = Receipt()
    total_price = 0.0
    total_tax = 0.0
    items_display = []

    # Gather item details from the user
    while True:
        item_name = input("Enter Item name: ")
        item_price = float(input("Enter Item Price: "))
        item_taxable = input("Is the item taxable (yes/no): ").lower() 
        item = Item(item_name, item_price, item_taxable)
        r.addItem(item)

        total_price += item.getPrice()
        total_tax += item.getTax(0.07)
        
        items_display.append((item.getPrice()))


        add_another_item = input("Add another item (yes/no): ").lower()
        if add_another_item != "yes":
            break
    
    current_datetime = datetime.datetime.now()    
    print("----- Receipt", current_datetime, "-----")
    for item_price in items_display:
        print(f"{item_name:<30}{item_price:.2f}")
    
    print(f"{'Sub Total':<30}{'_'*10}{total_price:.2f}")
    print(f"{'Tax':<30}{'_'*10}{total_tax:.2f}")
    print(f"{'Total':<30}{'_'*10}{total_price + total_tax:.2f}")



if __name__=="__main__":
    main()