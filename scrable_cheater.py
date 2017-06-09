import sys

class ScrableCheater:

    def __init__(self):
        self.__scores = {
                "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                "x": 8, "z": 10
                }

    def retrieve_word_list(self, file_name):
        words = []
        with open(file_name) as words_list:
            word = words_list.readline().split('\r')[0]
            while word:
                words.append(word)
                word = words_list.readline().split('\r')[0]
        return words

    def init_rack_letters_count(self):
        rack_letters_count = {}
        for letter in self.rack:
            rack_letters_count[letter] = 0
        return rack_letters_count

    def update_rack_letters_count(self):
        rack_letters_count = self.init_rack_letters_count()
        for letter in self.rack:
            rack_letters_count[letter] += 1
        return rack_letters_count

    def retrieve_rack(self):
        if len(sys.argv) != 2:
            print ("Compile program as : python main.py <RACK(no spaces)>")
            sys.exit(2)
        else:
            self.rack = sys.argv[1].upper()
            return self.rack

    def is_valid(self, word):
        rack_letters_count = self.update_rack_letters_count()
        for letter in word:
            if letter not in rack_letters_count:
                return False
            else:
                rack_letters_count[letter] -= 1

        for key in rack_letters_count:
            if rack_letters_count[key] < 0:
                return False

        return True

    def find_valid_words(self, words):
        valid_words = []
        for word in words:
            if self.is_valid(word):
                valid_words.append(word)

        return valid_words

    def calculate_score(self, word):
        word_score = 0
        for letter in word:
            word_score += self.__scores[letter.lower()]

        return word_score

    def get_words_score(self, valid_words):
        words_score = {}
        for word in valid_words:
            words_score[word] = self.calculate_score(word)

        return words_score
