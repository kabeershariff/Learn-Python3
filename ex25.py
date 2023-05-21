#Even More Practice

def break_words(stuff):
    """This function will break words for us."""
    words = stuff.split(' ')    #split the passed string whenever a space is encountered
    return words

def sort_words(words):
    """Sorting the words"""     
    return sorted(words)        #returns a list of elements in a sorted order

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)         #pop the element at index 0
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)        #pop the element at index -1
    print(word)

def sort_sentence(sentence):
    """Takes a full sentence and returns sorted words."""
    words = break_words(sentence)   #calling a function within a function
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort then print first and last words of a sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


