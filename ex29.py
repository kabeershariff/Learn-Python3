#What if

people = 20
cars = 4
bikes = 11

if people > cars * 4:
    print("Not enough cars.")

if people < cars * 4:
    print("Enough cars.")

if people > bikes * 2:
    print("Not enough bikes.")

if people < bikes * 2:
    print("Enough bikes.")

bikes += 9

if people <= bikes:
    print("We have less or equal number of people than bikes.")

if people >= bikes:
    print("We have more or equal number of people than bikes.")

if people == bikes:
    print("We have equal number of people and bikes.")
