#bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[1])

#using the append function adds elements to a list
bicycles.append('master')

#del function removes specified elements using the index given
del bicycles[-1]

#inset function helps you insert a particular element in a specific place
#Note: you cannot use .append() function instead of insert function 'cause the former takes exactly one argument
bicycles.insert(0, 'hero')

#this reverses the order of the list
bicycles.reverse()

#When you use pop function, it removes the last element of the list by default
last_bicycle = bicycles.pop()

print(f"I used to ride a {last_bicycle.title()} when I was in highschool.")

print(bicycles.sort())

nations = ["United Kingdom", "USA", "India", "Japan"]

#length of the list

len(nations)
print(sorted(nations))

print(nations.sort(reverse=True))



