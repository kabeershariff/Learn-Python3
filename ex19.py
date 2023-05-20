def garage(cars, bikes):
    print(f"You have {cars} cars and {bikes} bikes")

print("We can pass values to functions directly")
garage(10, 20)

print("\nWe can also pass values to functions from variables")
total_cars = 20
total_bikes = 30

#calling function with variables
garage(total_cars, total_bikes)

print("\nWe can do math too") #Don't know where to use this Lmao
garage(20+20, 50+10)

print("\nAlso we can combine variables and math")
garage(total_cars + 10, total_bikes - 3)

