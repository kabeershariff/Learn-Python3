ten_things = "Apples Oranges Cars Bikes Light Phone"

print("But there are not 10 things above.")

stuff = ten_things.split(' ')
#print(stuff)

more_stuff = ["Day", "Night", "Thunder", "Music", "Truck", "Game", "Mouse", "Keyboard"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding : ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items right now")

print("There we go : ", stuff)

#Lets print the item at index 1
print(stuff[1])

#Lets print the item at index -1
print(stuff[-1])
#pop the item off the list , default value is -1 , indexs can be passed for eg: stuff.pop(1)
print(stuff.pop())

print(' '.join(stuff))  #Essentially reverse of split here 
print('#'.join(stuff[3:5])) #Join the items using '#' from index 3 to 5

