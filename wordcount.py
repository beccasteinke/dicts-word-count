
'''poem = open('test.txt')   
word_counts = {}
    
for line in poem:
    words = line.rstrip().split(" ")
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)'''

import sys

def split_poem(the_file):
    file = open(the_file)
    all_words = []
    
    for line in file:
        words = line.rstrip().split(" ")
        all_words.extend(words)

    return all_words

def word_count(words):

    word_counts = {}
    import string
    

    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def print_word_dictionary(word_counts):

    for word, count in word_counts.items():
        print(word, count)



words = split_poem("test.txt")
word_counts = word_count(words)
print_word_dictionary(word_counts)

