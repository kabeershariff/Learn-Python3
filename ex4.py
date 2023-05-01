# Variables and Names

cars = 100
car_space = 4.0

drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * car_space
average_passengers_per_car = passengers / cars_driven

print("We have ", cars , "cars.")
print("Each car has a capacity for ", car_space , "passengers")
print("We have ", drivers , "drivers")
print("We have ", passengers, "passengers")

print("We have a total carpool capacity of ", carpool_capacity )
print("Average passengers per car is ", average_passengers_per_car)
