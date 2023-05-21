#More Practice

print("Practice Everything so far")

print('You\'d need to know \'bout escape characters like \\')
print('\n newline and \t tabs')

multiline = """
\tLine 1 
Line 2 ...
Line 3 ...
Line 4 ...
Line 5 ...
Line 6 ...
Line 7 ... \nLine 8 ...
\n\t\tThe End
"""

print("----------------")
print(multiline)
print("----------------")

answer = 10 - 2 + 5 * 3
print(f"The answer seems to be {answer}")

def recipe_func(num):
    jelly_beans = 19 * num
    jars = jelly_beans/20
    crates = jars/5
    return jelly_beans, jars, crates

members = 4
beans, jars, crates = recipe_func(members) #three variables to hold 3 returning values from function

#Another way to format a string
print("We have {} members for dinner".format(members))
#F strings seem easiers
print(f"We seem to have  {beans} beans, {jars} jars, and {crates} crates")

print("We can also do it this way")
food_list = recipe_func(members) #A single variable to hold returning values , creates a tuple for us
print(food_list) #Not a list but a tuple

#easy way to apply a list to format strings
print("We seem to have {} beans, {} jars and {} crates.".format(*food_list))



