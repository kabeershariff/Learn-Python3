#Python Dictionaries

#create a mapping of state to abbv

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
}

#set of states and cities in them

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

cities['NY'] =  'New York'
cities['OR'] =  'Portland'

print("-" * 30)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print("-" * 30)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print("-" * 30)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#printing every state's abbreviation
print("-" * 30)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#print every city in state
print("-" * 30)
for abbrev, city in list(states.items()): #items() returns tuples of all key-value pairs of a dictionary
    #list() --> convert to list
    print(f"{abbrev} has the city {city}")

print(f"-" * 30)

#Printing both the above results
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    print(f"and has a city {cities[abbrev]}")

print(f"-" * 30)

#get abbreviation which might not exist
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

# get city with default value
# get() method can handle missing keys, while passing key directly raises error if not found
city = cities.get('TX', 'Does not Exist') #get() gives default value of None if not defined
print(f"The city for the state 'TX' is: {city}")
