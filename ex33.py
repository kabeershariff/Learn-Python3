#While Loops

i = 0
numbers = []

#While check for this condition , Keep looping until condition is False
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1 #increment value or infinite loop
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers are : ")
for num in numbers:
    print(num)
