# function that counts all vowels in a string
def count_vowels(string):
    num_vowels = 0
    vowels = 'aeiou'
    for char in string:
        if char.lower() in vowels:
            num_vowels += 1
    return num_vowels
