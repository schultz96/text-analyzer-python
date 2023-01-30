from analyzer.count_consonants import count_consonants
from analyzer.count_letters import count_letters
from analyzer.count_top_longest_words import count_top_longest_words
from analyzer.count_top_words_count import count_top_words_count
from analyzer.count_vowels import count_vowels
from analyzer.log_output import log_chapter_summary


def analyze_text_file(text_file_path):
    # count paragraphs
    num_paragraphs = 0
    # count number of lines
    num_lines = 0
    # count number of lines that contain characters
    num_lines_with_text = 0
    # count number of words
    num_words = 0
    # count of all letters
    num_letters = 0
    # count of all vowels
    num_vowels = 0
    # count of consonants
    num_consonants = 0
    # word count dictionary
    word_count_dictionary = {}

    # read file lines into a list
    # encoding may need to be changed based on where this file came from (didnt work right away on windows)
    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        lines = text_file.readlines()
        for line in lines:
            # skip first 3 lines (they are title and 2 lines of blank spacing)
            if num_lines < 3:
                num_lines += 1
                continue

            # count number of lines
            num_lines += 1
            # if line is not blank, count it.
            if line.strip():
                num_lines_with_text += 1
                # count words in line
                num_words += len(line.split())
            # else line is blank, count it as a paragraph
            else:
                num_paragraphs += 1

            # count number of alphabetical letters
            num_letters += count_letters(line)

            # count number of vowels
            num_vowels += count_vowels(line)

            # count number of consonants
            num_consonants += count_consonants(line)

            # count unique words and add to dictionary
            for word in line.split():
                if word in word_count_dictionary:
                    word_count_dictionary[word] += 1
                else:
                    word_count_dictionary[word] = 1

    # get top 5 words by count
    top_five_words = count_top_words_count(word_count_dictionary, 5)
    # get top 3 longest words
    top_three_longest_words = count_top_longest_words(word_count_dictionary, 3)

    # log chapter summary
    log_chapter_summary(num_paragraphs, num_lines, num_lines_with_text, num_words, num_letters, num_vowels,
                        num_consonants, top_five_words, top_three_longest_words)
