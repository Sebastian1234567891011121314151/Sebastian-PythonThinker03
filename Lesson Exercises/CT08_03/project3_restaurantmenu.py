menu = {
    "Big Mac": 6.00,
    "McChicken": 2.50,
    "Fries": 3.30,
    "Chicken McNuggets": 4.50,
    "Cheeseburger": 2.30,
    "Coke": 2.00,
    "Vanilla Cone": 1.50,
    "McFlurry": 3.90,
    "Hot Fudge Sundae": 3.20,
    "Apple Pie": 1.80,
    "McSpicy": 4.00,
}

order={}
print("Welcome to Mcds. Heres our Menu ") 


for food,price in menu.items():
    print(f"{food}:${price:.2f}")



def ask_for_food():

    cost=0
    wallet=10
    while True:
        question=input("What would you like to order? ")
        
        if question in menu:
            # print("The "+question+" is $"+str(Menu[question]))
            print(f"The {question} is ${menu[question]:.2f}")
            question2=input("Do you want to add it to your order? (y/n)")
            if question2 =="y":
                if wallet >= menu[question]:
                    if question in order:
                        order[question]+=menu[question]
                        # print(f"{question} has been added to your order.")
                        # wallet-=menu[question]
                        # print(f"Remaining wallet balance : ${wallet:.2f}")
                    else:
                        order[question]=menu[question]
                    print(f"{question} has been added to your order.")
                    wallet-=menu[question]
                    print(f"Remaining wallet balance : ${wallet:.2f}")
                    cost=cost+menu[question]
                    continue
                else:
                    print(f"{question} cost ${order[question]:.2f}. You only have{wallet:.2f} in your wallet.")
                    print(f"{question} not added")
                # check for whether the key is already in the dict
                # if question in Order:
                #     Order[question]+=Menu[question]
            #     else:
            #         Order[question]=Menu[question]
            #     print(question+" has been added to ur order")
            #     Cost=Cost+Menu[question]
            #     # print(Cost)
            #     continue
            # elif question2== "n":
            #     print(question+" has not been added to ur order")
            #     continue

        elif question == "no more":
            print("Ok, Thank you for your order!") 
            print("---Order Summary---")
            for food2,price2 in order.items():
                print(f"{food2}:${price2:.2f}")
            print("-------------------")
            # print("Total: "+str(Cost))
            print(f"Total: ${cost:.2f}")
            # print("Your total bill is "+f"${Cost:.2f}"+" Enjoy your meal!")
            print(f"Your total bill is ${cost:.2f} Enjoy your meal!")

                
            break
        else:
            print("We don't have that item")
            continue
ask_for_food()
