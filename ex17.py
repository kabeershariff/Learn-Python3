from sys import argv            #To pass arguments 
from os.path import exists      #Used to check if a file exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)   #Opening the source file
in_data = in_file.read()    #Reading the source file

print(f"The input file {len(in_data)} bytes long")  #len() returns length of the string

print(f"Does the output file exists ? {exists(to_file)}")   #Checking if destination file exists
print("Ctrl^C to exit , Enter to continue")
input()

out_file = open(to_file, 'w')   #Opening the destination file in Write mode
out_file.write(in_data)         #Writing to the destination file

print("Done")

out_file.close()    #Closing Opened files , Good Practice
in_file.close()
