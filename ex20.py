from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) #read the file passed to the function

def print_a_line(line_count, f):
    print(line_count, f.readline()) #get the line number and read the line of the file

def rewind(f):
    f.seek(0)  #rewind the cursor to the start of the file

current_file = open(input_file)  #opening the passed file to a variable

print("Printing the whole file\n")
print_all(current_file) #pass the file contents to the function

print("Let's rewind")
rewind(current_file)

print("Lets print 3 lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

