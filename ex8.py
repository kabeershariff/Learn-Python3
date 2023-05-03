formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

name = "Omar Shariff"
age = 23
height = 175
weight = 60

print(formatter.format(name, age, height, weight))
