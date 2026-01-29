menu = {
    "notebook" : {"amount":0,"price":2.50},
    "pencil" : {"amount":0,"price":0.50},
    "pen" : {"amount":0,"price":1.20},
    "ruler" : {"amount":0,"price":1.50},
    "eraser" : {"amount":0,"price":0.50},
    "writing pad" : {"amount":0,"price":2.50},
    "glue" : {"amount":0,"price":3.00},
    "calculator" : {"amount":0,"price":35.00}
}
order = {

}

wallet = 50
cost = 0

print("Welcome to the Bookshop")
print("Ordering System (BOS)!")

print("\nHere's our menu")
for item , inner in menu.items():
    print(f"{item}: ${inner["price"]:.2f}")

def ask_for_order():
    global wallet
    global cost
    while True:
        item = input("What would you like to buy?").lower().strip()
        if item == "no more":
            print("----------------------")
            for item , inner in order.items():
                print(f"{item}: {inner["amount"]}, ${inner["price"]:.2f}")
            print(f"Your total is ${cost:.2f}")
            print("----------------------")
            print(f"You have ${wallet} left.")
            break
        if item in menu:# the code that didnt work below
            print(f"{item.title()} costs ${menu[item]:.2f}")
            confirm_order = input(f"Do you want to add {item} to your order?(y/n)")
            if confirm_order == "y":
                if wallet >= menu[item]:
                    if item in order:
                        menu[item] += {"amount"+ 1}
                        order[item] += menu[item["amount" and "price"]]
                        cost += menu[item]
                        wallet -= menu[item]
                    else:
                        order[item] = menu[item]
                        wallet -= menu[item]
                        print(f"You have ${wallet:.2f} remaining.")
                        cost += order[item]
                else:
                    print("You do not have enough money")
                    print(f"You have ${wallet:.2f}.")
            elif confirm_order =="n":
                print(f"{item} was not added to you order.")

        else:
            print(f"Sorry we don't have {item} in our store")
            continue



        
ask_for_order()








# What would you like to buy? Notebook
# Notebook costs $2.50.

# What would you like to buy? Chopsticks
# Sorry, we don’t have Chopsticks in our store.

# Do you want to add Notebook to your order? (y/n): y
# Notebook has been added to your order.

# Do you want to add Pencil to your order? (y/n): n
# Pencil was not added to your order.