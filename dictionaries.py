#alien.py
alien_0 = {'color': 'green', "points": 10}

print(alien_0)
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just won {new_points} points!")

alien_0["size"] = 6 
alien_0["avatar"] = "noob"
print(alien_0)

alien_1 = {}
alien_1["colour"] = "pink"
alien_1["points"] = 7
print(alien_1)
print(f"The alien is {alien_1['colour']}" ) 

alien_1["colour"] = "yellow"
print(f"The alien is now {alien_1['colour']}.")

alien_0 = {"x_position": 0, "y_position": 25, "speed": 'slow'}
print(f"Original position: {alien_0['x_position']}")
#Move the alien to the right.
#Determine how far to move the alien based on its current speed
if alien_0["speed"] == 'slow':
    x_increase = 1
elif alien_0["speed"] == 'medium':
    x_increase = 2
else:
    #This must be a fast alien.
    x_increase = 3
#The new position is the old position plus the increase
alien_0["x_position"] = alien_0["x_position"] + x_increase
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
    "jen": "python",
    "sarah": "java",
    "edward": "C++",
    "phil": "java",
}
print(f"Sarah's favorite programming language is {favorite_languages['sarah'].title()}")

alien_2 = {"color": 'green', "speed": 'fast'}
point_value = alien_2.get("points", "No value assigned yet")
print(point_value)

user_0 = {
    'username': 'efermi',
    'first' : 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items(): 
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")   

if 'phil' in favorite_languages.keys():
    print("Phil, You've done a great job") 

#you can sort or arrange a loop in a particular order 
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#using a .set() attribute will help you get only unique answers when 
#there are repetitive answers
for language in set(favorite_languages.values()):
    print(language.title())

#NESTING: you store a dic in another dic or a dic in another list and vice versa
#aliens.py
alien_3 = {'color': 'green', 'points': 5}
alien_4 = {'color': 'blue', 'points': 7}
alien_5 = {'color': 'pink', 'points': 9}
aliens = [alien_3, alien_4, alien_5]
for alien in aliens:
    print(alien)

#Make an empty list for storing aliens
aliens = []
#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created. 
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

#Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
"\nwith the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n {name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {'aienstein': {
    'first': 'albert', 
    'last': 'einstein',
     'location': 'princeton',},
'mcurie': 
{'first': 'marie',
 'last': 'curie', 
 'location': 'paris',},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()} ")
    print(f"\tLocation: {location.title()}")