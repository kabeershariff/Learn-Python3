def add(a, b):
    print(f"Adding {a} and {b}")
    return a+b

def subtract(a, b):
    print(f"Subtracting {a} and {b}")
    return a-b

def multiply(a, b):
    print(f"Multiply {a} and {b}")
    return a*b

def divide(a, b):
    print(f"Dividing {a} and {b}")
    return a/b

print("Lets do math")

age = add(20, 12)
height = subtract(300, 200)
weight = multiply(20, 3)
iq = divide(1000,7.5)

print(f"Age is {age}, Height is {height}, Weight is {weight} and IQ is {iq}")

#A equation to solve

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("The answer is ", what)
