#greeter.py
def greet_user(username):
    """ Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

#pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
#assigning key arguments will make sure that there's no mistake in positioning
#you can do it this way as well minding the positional arguments
describe_pet('cat', 'julia')

def describe_pet(pet_name, animal_type= 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet('henry')
describe_pet(pet_name= 'Tom')

#formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

artist = get_formatted_name("harry", "styles")
print(artist)
#this helps in storing names in larger programs where many names need to be saved

#Sometimes, some parameters are optional, in those cases:
def formatted_name(first_name, last_name, middle_name =''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('harry','styles','edward')
print(musician)

#person.py
def build_person (first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def create_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age: 
        person['age'] = age
    return person

#here the age argument is optional. that's why the function would work without
#assigning a parameter to it

scientist = create_person('albert', 'einstein', age=40)
print(scientist)

#greeter.py
def get_form_name(firstname, lastname):
    """Return a full name, neatly formatted"""
    fullname = f"{firstname} {lastname}"
    return fullname

while :
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("first name:")
    if f_name == 'q':
        break

    l_name = input("last name:")
    if l_name == 'q':
        break

    form_name = get_form_name(f_name, l_name)
    print(f"\nHello, {form_name}!")

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)    




