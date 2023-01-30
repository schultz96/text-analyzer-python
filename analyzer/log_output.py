# function that logs chapter summary
def log_chapter_summary(num_paragraphs,
                        num_lines,
                        num_lines_with_text,
                        num_words,
                        num_letters,
                        num_vowels,
                        num_consonants,
                        top_five_words,
                        top_three_longest_words):
    print('==================================')
    print('Number of paragraphs: {}'.format(num_paragraphs))
    print('Number of lines: {}'.format(num_lines))
    print('Number of lines with text: {}'.format(num_lines_with_text))
    print('Number of words: {}'.format(num_words))
    print('Number of letters: {}'.format(num_letters))
    print('     Number of vowels: {}'.format(num_vowels))
    print('     Number of consonants: {}'.format(num_consonants))
    print('Top 5 words: ')
    for word, count in top_five_words:
        # print numbered list
        print('     {}. "{}" appeared {} times.'.format(top_five_words.index((word, count)) + 1, word, count))
    print('Top 3 longest words: ')
    for word in top_three_longest_words:
        # print numbered list of just the words
        print('     {}. "{}"'.format(top_three_longest_words.index(word) + 1, word[0]))

    print('==================================')
