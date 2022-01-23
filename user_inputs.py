message = input("Tell me something, and I will repeat it back to you:")
print(message)

#another example of clear prompts
name = input("Please enter your name:")
print(f"\nHello, {name}!")

#greeter.py
prompt = "If you tell us who you are, we can personalize the music you listen to"
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")
#The above code is really special. Read it to understand why.

#rollercoaster.py
height = input("How tall are you, in inches?")#
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride the giant rollercoaster!")
else:
    print("\nYou'll be able to ride when you're a little older, honey")

#the modulus operator
#We use % to divide a no. by another no. and for it to return the remainder
7 % 3

#even_or_odd.py
number = input("Enter a number, and I'll tell you whether it is odd or even:")
number= int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"\nThe number {number} is odd")


    

    
