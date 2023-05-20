#Names, Variables, Code , Functions

#define a function with keyword def
#takes any number of argument -> *args
def print_two(*args):
    arg1, arg2 = args #arguments from args
    print(f"arg1: {arg1} , arg2: {arg2}")

#*args seems pointless we can also do 
#simplified
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#Only one argument for this function
def print_one(arg1): #takes only one argument
    print(f"arg1: {arg1}")

#This function takes no arguments

def print_none():
    print("None")

#Calling functions with required arguments
print_two("Omar", "Shariff")
print_two_again("Omar", "Shariff")
print_one("Hello")
print_none()
