# function that counts the top words from a dictionary
def count_top_words_count(word_count_dictionary, top_count):
    # sort word_count_dictionary by count, largest to smallest
    top_words = sorted(word_count_dictionary.items(), key=lambda x: x[1], reverse=True)[:top_count]
    return top_words
