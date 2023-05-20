from sys import argv

script, filename = argv

txt = open(filename)

print(f"Your file name is {filename}")

#printing content of the file
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
