#cars.py: This is is a simple example of a loop 
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())   

car = 'audi'
car == 'audi'
#The single equality is used for equating a variable to another value
#whereas the double equality is used to ask whether the value of it is true or not

car = 'Audi'
car.lower() == 'audi'
#This method is used to check whether every username is unique or not

#toppings.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
else:
    print("Give me them goddamn side dishes, you punk!")

#here != is an inequality sign

#magic_numbers.py
#testing the conditionalities on numbers is pretty clear. Here,

age = 18
if age != 17:
    print("Goddamn, henry. Get a hold on yourself. \nYou're too young for this.")


banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users: 
    print(f"{user.title()}, you can post a reponse if you wish.")

age = 14
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")

age = 80
if age < 4:
    price = 0
elif age < 18: 
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}")

#you can omit the else block at the end of an if-elif statement and put a spcific elif instead. else is basically a round about
#that says if you don't match any of the conditions above then you fall under me. It is better to put an elif block instead

#When you want two conditions to be met use multiple if or an if chain

#toppings.py

requested_topping = ["Mushrooms", "Mozerella"]

if "Mushrooms" in requested_topping:
    print("Adding Mushrooms, mon amie")
if "Mozerella" in requested_topping:
    print("Adding your favorite cheese")
if "Pineapples" in requested_topping:
    print("Eh, you're a pineapple on pizza guy?")
print("\nHere is your pizza, monsieur!")

requested_toppings = ["mushrooms", "garlic", "olives", "pepparoni", "cheese"]

#if-else statement in a for loop
for requested_topping in requested_toppings:
    if requested_topping == "garlic":
        print("We ain't got no garlics, mate!")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making pizza!")

#for loop in an if else statement
requested_toppings = ["Mushrooms"]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nAdding them damn {requested_topping}!")
        print("\nFinished making your pizza. Here it is, mate!")
else:
    print("Are you sure you don't want a pizza?")

#Using multiple lists 
available_toppings = ["mushrooms", "cheese", "olvies", "bell peppers"]

requested_toppings = ["cheese", "pepperoni"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping} to pizza.")
    else:
        print(f"we don't have {requested_topping}")
print("Enjoy your pizza!")

#hello_
user_names = ["admin", "Rosa", "Allen"]

if user_names:
    for user_name in user_names:
        if user_name == "admin":
            print("Hello, admin. Would you like to do a weekly checkup?")
    else:
        print(f"Hello, {user_name}. How are you today?")
else:
    print("We need to find some users!")
    





