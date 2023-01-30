# function that counts longest top words from a dictionary's keys
def count_top_longest_words(word_count_dictionary, top_count):
    # sort word_count_dictionary by word length, largest to smallest
    top_words = sorted(word_count_dictionary.items(), key=lambda x: len(x[0]), reverse=True)

    # remove words that contain non-alphabetical characters
    top_words = [word for word in top_words if word[0].isalpha()]

    return top_words[:top_count]
