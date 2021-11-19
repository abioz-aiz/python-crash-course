#This is a for loop that basically states the elements in the list one by one
things = ["pens", "eraser", "scale", "pouch"]
for thing in things:
    print(thing)

magicians = ["Alice", "Charles", "Nancy", "Alex"]
for magician in magicians: 
    print(f"I attended a show in which a magician named {magician.title()} performed this amazing trick.")
    print(f"I can't wait to see {magician.title()}'s next trick!\n")

#the range() function prints out no. in th range given
for value in range(1,10):
    print(value)

#this creates a list of the series of numbers
numbers = list(range(1,7))
print(numbers)

#this is a stepper
odd_numbers = list(range(2,11,2))
print(odd_numbers)

#squares.py
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#cubes.py
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#Simple Statistics with list of numbers
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

list_of_numbers = list(range(1,9))
print(sum(list_of_numbers))
print(min(list_of_numbers))
print(max(list_of_numbers))

#list comprehensions

squares = [value**2 for value in range(1,9)]
print(squares)

#player.py: Slicing a list. You use the index of the elements to print them. Here's an example:
players = ["Charles", "Boyl", "Jake", "Holt", "Gina"]
print(players[:4])
#You can either use [0:3] an initial and end index. when you don't specify an initial index python asummes it as 0.
#It's the same when you don't specify an end index. 

#Looping through a list
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())

#Using slice function to copy a list
my_pizza = ["Beef", "Barbeque", "Vegan Cheese", "Olives"]
your_pizza = my_pizza[:]
my_pizza.append("Chicken Salami")
your_pizza.insert(0, "Pineapple")
print(my_pizza)
print(your_pizza)
print(f"My favorite pizzas are: {my_pizza}")
print(f"His favorite pizzas are: {your_pizza}")
her_pizza = ["Parmesan Cheese", "Momomia", "Roasted Chicken"]
for value in her_pizza:
    print(f" I have {value} favorite pizzas at the moment")

#Tuples
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
#tuples are usually signified by a trailing comma eg: my_t = (3,)

#DIY: Buffet
menu = ("Glazed Bread", "Chai", "Ice Cream", "Rusk", "Nan Khatai")
for items in menu:
    print(items)

new_menu = ("Cheese Sticks", "Aglio O lio", "Chicken 65", "Rumali Roti")
menu = new_menu
for items in menu:
    print(items)