menu = {
    "notebook" : 2.50,
    "pencil" : 0.50,
    "pen" : 1.20,
    "ruler" : 1.50,
    "eraser" : 0.50,
    "writing pad" : 2.50,
    "glue" : 3.00,
    "calculator" : 35.00
}


print("Welcome to the Bookshop")
print("Ordering System (BOS)!")

print("\nHere's our menu")
for item , price in menu.items():
    print(f"{item}: ${price:.2f}")

def ask_for_order():
    while True:
        item = input("What would you like to buy?").lower().strip()
    # exit the loop
        if item == "no more":
            break
# What would you like to buy? Notebook
# Notebook costs $2.50.

# What would you like to buy? Chopsticks
# Sorry, we don’t have Chopsticks in our store.

        if item in menu:
            print(f"{item.title()} costs ${menu[item]:.2f}")
            confirm_order = input("Do ")
        else:
            print(f"Sorry we don't have {item} in our store")
            continue
        
# Do you want to add Notebook to your order? (y/n): y
# Notebook has been added to your order.

# Do you want to add Pencil to your order? (y/n): n
# Pencil was not added to your order.
ask_for_order()