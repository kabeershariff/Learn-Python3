def scan(sentence):
    words = sentence.split(" ")
    items = []
    directions = ['north', 'south', 'east', 'west']
    verbs = ['go', 'eat', 'kill']
    stops = ['the', 'in', 'of']
    nouns = ['bear', 'princess']
    
    for i in words:
        if i in directions:
            kind = 'direction'
        elif i in verbs:
            kind = 'verb'
        elif i in stops:
            kind = 'stop'
        elif i in nouns:
            kind = 'noun'
        elif i.isdigit():
            kind = 'number'
            i = int(i)
        else:
            kind = 'error'
        tuple1 = (kind, i)
        items.append(tuple1)
    return items

    
    
