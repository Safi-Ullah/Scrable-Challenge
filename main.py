from scrable_cheater import ScrableCheater

if __name__ == '__main__':
    scrable_cheater = ScrableCheater()
    words = scrable_cheater.retrieve_word_list('./sowpods.txt')
    rack = scrable_cheater.retrieve_rack()
    print scrable_cheater.rack
    # print scrable_cheater.rack_letters_count
    valid_words = scrable_cheater.find_valid_words(words)
    # words_score = scrable_cheater.get_word_score(valid_words)

    # for key in words_score:
    #     print (key, "\t", words_score[key])
