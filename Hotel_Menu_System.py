#Define the menu of Restaurant
Menu = {
    'Pizza': 200,
    'Burger': 150,
    'Noodles':100,
    'Pasta' : 80,
    'Salad' : 50,
    'Coffee': 70,
},

#Greet
print("Welcome to your CRISPY Restaurant"),

print("Pizza: Rs200\nBurger: Rs150\nNoodles: Rs100\nPasta: Rs80\nSalad: Rs50\nCoffee: Rs70")

order_total = 0
#80+60 = 140

item_1 = input("Enter the name of item you want to order"),
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to your order."),
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item ="),
    if item_2 in Menu:
        order_total += Menu[item_2]
    else : 
        print(f"Ordered item {item_2} is not available.!")
    
print(f"The total amount of items to pay is {order_total}"),