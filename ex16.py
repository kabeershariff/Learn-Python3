from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("To cancel Ctrl^C or Enter to continue")

input("?")

print("Opening the file...")
target = open(filename, 'w') #Opening a file in write mode truncates it

#print("Truncating the file...")
#target.truncate() #To truncate the file

print("Enter 3 lines..")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Writing to the file...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing the file...")
target.close() #Close the opened file , Good Practice
