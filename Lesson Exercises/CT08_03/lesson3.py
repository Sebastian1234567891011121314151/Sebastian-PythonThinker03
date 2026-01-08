price = {
    "Apple": 1.2,
    "Orange": 1.8,
    "Pineapple": 2.2,
}

question= input("What fruit?")
if question == price:
    print("i dont have that")
else:
    print(price[question])