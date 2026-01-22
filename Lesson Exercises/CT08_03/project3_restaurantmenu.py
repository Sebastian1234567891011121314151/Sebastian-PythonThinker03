Menu = {
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

Order={}
print("Welcome to Mcds. Heres our Menu ") 


for food,price in Menu.items():
    print(f"{food}:${price:.2f}")



def ask_for_food():

    Cost=0
    
    while True:
        question=input("What would you like to order? ")
        
        if question in Menu:
            print("The "+question+" is $"+str(Menu[question]))
            question2=input("Do you want to add it to your order? (y/n)")
            if question2 =="y":
                # check for whether the key is already in the dict
                if question in Order:
                    Order[question]+=Menu[question]
                else:
                    Order[question]=Menu[question]
                print(question+" has been added to ur order")
                continue
            elif question2== "n":
                print(question+" has not been added to ur order")
                continue
            Cost=Cost+Order[question]
        elif question == "no more":
            print("Ok, Thank you for your order!") 
            print("---Order Summary---")
            for food2,price2 in Order.items():
                print(f"{food2}:${price2:.2f}")
            print("-------------------")
            print("Total: "+Cost)
            print("Your total bill is $"+Cost+" Enjoy your meal!")

                
            break
        else:
            print("We don't have that item")
            continue
ask_for_food()
