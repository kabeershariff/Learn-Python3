#First download the languages.txt file

import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()                     #read a line from the file
    if line:                                            #if line is not empty then
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)    #keep looping and printing lines until if condition becomes false

def print_line(line, encoding, errors):
    next_lang = line.strip()                                    #remove trailing whitespaces
    raw_bytes = next_lang.encode(encoding, errors=errors)       #DBES, Encode Strings to get Raw Bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)   #Decode Bytes to get Strings

    print(raw_bytes, "<====>", cooked_string)

#Open a file with encoding UTF-8
languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)                                
