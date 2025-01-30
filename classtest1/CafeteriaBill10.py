print("available item \nSandwich: ₹50\nCoffee: ₹30\nFries: ₹40")
order = "yes"
totalprice = 0
while(order == "yes"):
    item_name = str(input("enter a item name :- "))
    item_quantity = int(input("enter a item quantity :- "))
    if(item_name == "sandwich"):
        price = 50 * item_quantity
    elif(item_name == "coffee"):
        price = 30 * item_quantity
    elif(item_name == "fries"):
        price = 40 * item_quantity
    totalprice += price
    order = str(input("you want a order is repeat yes/no :- "))
if(totalprice >= 200):
    discount = int((totalprice/100)*10)
    print("you got 10%","discount your total price is :-",totalprice - discount)
else:
    print("your total price is :- ",totalprice)