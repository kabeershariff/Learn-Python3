#Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "mango", "orange", "grapes", "strawberry"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in the_count:  #For loop through a list of numbers
    print(f"This is count {i}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}") #For loop through a list of strings

for coin in change: #For loop through a mixed list
    print(f"I got {coin}") 

#Building a list from a empty one

elements = []

for i in range(0, 9):
    print(f"Lets add {i} to the list")
    elements.append(i)

print(elements)

#print from list using loop
for i in elements:
    print(f"The Element was: {i}")

#Study Drill
#In python2 range() gives a direct list , in Python 3 it is a iterator so use list function
another_list = list(range(0, 9))
print(another_list)
