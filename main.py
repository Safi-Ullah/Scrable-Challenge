from scrable_cheater import ScrableCheater
from operator import itemgetter
from collections import OrderedDict

if __name__ == '__main__':
    scrable_cheater = ScrableCheater()
    words = scrable_cheater.retrieve_word_list('./sowpods.txt')
    rack = scrable_cheater.retrieve_rack()

    valid_words = scrable_cheater.find_valid_words(words)

    words_score = scrable_cheater.get_word_score(valid_words)

    if len(words_score) == 0:
        print ("No valid words could be formed with " + rack)

    # Printing the words in the reverse order of their scores
    for word in OrderedDict(sorted(words_score.items(),
                           key=itemgetter(1), reverse=True)):
        print (str(words_score[word]) + "\t" + word)
