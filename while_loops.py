#WHILE LOOPS
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#parrot.py
#before
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
#after
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


#citites.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#counting.py
x = 1
while x <= 5:
    print(x)
    x+= 1

#confiremed_user.py
#Start with users that need to be verified 
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Verify each user until there are no more uncomfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#using the while loop here removes 'cat' from the list
while 'cat' in pets:
    pets.remove('cat')

print(pets)

#mountain_poll.py
responses = {}

#Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    #Store the response in the dictionary.

    responses[name] = response
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

