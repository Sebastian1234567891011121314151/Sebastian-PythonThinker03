# price = {
#     "Apple": 1.2,
#     "Orange": 1.8,
#     "Pineapple": 2.2,
# }

# question= input("What fruit?")

# if question in price:
#     print(price[question])
            
# else:
#     print("i dont have that")



students ={
    "Alice":85,      
    "Bob":37,
    "Charlie":68,
    "John":59,
    "Elias":100,
    "Kok Seng":67}

students["Hello"] = 75  # add into dictionary

del students["Alice"]   # del from dictionary

if "Hello" in students:
    print("Hello is in the list")
else:
    print("Hello is not in the list")


for name,grade in students.items():
    print(name,grade)
