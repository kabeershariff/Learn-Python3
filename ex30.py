#Else and If

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")

if trucks > cars:
    print("Too many trucks")
elif trucks < cars:
    print("Too many cars")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, lets take trucks")
else:
    print("Just stay at home LOL")
