# function that returns counts of consonants in a string
def count_consonants(string):
    num_consonants = 0
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for char in string:
        if char.lower() in consonants:
            num_consonants += 1
    return num_consonants
