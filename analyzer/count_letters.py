# function that returns count of alphabetical characters in a string
def count_letters(string):
    # count number of alphabetical letters
    num_letters = 0
    for char in string:
        if char.isalpha():
            num_letters += 1
    return num_letters
