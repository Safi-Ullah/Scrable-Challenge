

def get_word_list():
    words = []
    with open("./snowpods.txt") as words_list:
        word = words_list.readline().split('\n')[0]
        words.append(word)
        while word:
            word = words_list.readline().split('\n')[0]
            words.append(word)

    return words


    if __name__ == '__main__':
        print "Hello"
        words = get_word_list()
        print words
