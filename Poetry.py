from Word import WordList
import random as rand


class Generator:
    class __Group:
        type = 0
        length_1 = []
        length_2 = []
        length_3 = []
        length_4 = []
        length_5 = []
        length_6 = []

        def __init__(self, type):
            self.length_1 = []
            self.length_2 = []
            self.length_3 = []
            self.length_4 = []
            self.length_5 = []
            self.length_6 = []
            self.type = type

        def add(self, word_list):
            for i in word_list:
                if len(i.representation) == 1:
                    self.length_1.append(i.word)
                elif len(i.representation) == 2:
                    self.length_2.append(i.word)
                elif len(i.representation) == 3:
                    self.length_3.append(i.word)
                elif len(i.representation) == 4:
                    self.length_4.append(i.word)
                elif len(i.representation) == 5:
                    self.length_5.append(i.word)
                elif len(i.representation) == 6:
                    self.length_6.append(i.word)

        def has_length(self, length):
            if length == 1:
                if len(self.length_1) > 1:
                    return True
                else:
                    return False
            elif length == 2:
                if len(self.length_2) > 1:
                    return True
                else:
                    return False
            elif length == 3:
                if len(self.length_3) > 1:
                    return True
                else:
                    return False
            elif length == 4:
                if len(self.length_4) > 1:
                    return True
                else:
                    return False
            elif length == 5:
                if len(self.length_5) > 1:
                    return True
                else:
                    return False
            elif length == 6:
                if len(self.length_6) > 1:
                    return True
                else:
                    return False

        def get_word(self, length):
            if length == 1:
                word = self.length_1.pop(rand.randint(0, len(self.length_1) - 1))
                return word
            elif length == 2:
                word = self.length_2.pop(rand.randint(0, len(self.length_2) - 1))
                return word
            elif length == 3:
                word = self.length_3.pop(rand.randint(0, len(self.length_3) - 1))
                return word
            elif length == 4:
                word = self.length_4.pop(rand.randint(0, len(self.length_4) - 1))
                return word
            elif length == 5:
                word = self.length_5.pop(rand.randint(0, len(self.length_5) - 1))
                return word
            elif length == 6:
                word = self.length_6.pop(rand.randint(0, len(self.length_6) - 1))
                return word

    __type1_group = __Group(1)
    __type2_group = __Group(2)
    __groups = []

    def __init__(self, groups):
        self.__groups = groups
        for word_list in self.__groups:
            if word_list.type == 1:
                self.__type1_group.add(word_list.words)
                if word_list.words[0].get_length() == 1:
                    self.__type2_group.add(word_list.words)
            else:
                self.__type2_group.add(word_list.words)
                if word_list.words[0].get_length() == 1:
                    self.__type2_group.add(word_list.words)

    def __get_rhyme(self, word):
        for group in self.__groups:
            for w in group.words:
                if w.word == word:
                    rhyme = group.words[rand.randint(0, len(group.words) - 1)]
                    while rhyme.word == word:
                        rhyme = group.words[rand.randint(0, len(group.words) - 1)]
                    return rhyme

    def __delete_word(self, word, length, type):
        if type == 1:
            if length == 1:
                try:
                    self.__type1_group.length_1.remove(word)
                except:
                    True
                try:
                    self.__type2_group.length_1.remove(word)
                except:
                    True
                return
            elif length == 2:
                self.__type1_group.length_2.remove(word)
                return
            elif length == 3:
                self.__type1_group.length_3.remove(word)
                return
            elif length == 4:
                self.__type1_group.length_4.remove(word)
                return
            elif length == 5:
                self.__type1_group.length_5.remove(word)
                return
            elif length == 6:
                self.__type1_group.length_6.remove(word)
                return
        elif type == 2:
            if length == 1:
                try:
                    self.__type1_group.length_1.remove(word)
                except:
                    1 == 1
                try:
                    self.__type2_group.length_1.remove(word)
                except:
                    1 == 1
                return
            elif length == 2:
                self.__type2_group.length_2.remove(word)
                return
            elif length == 3:
                self.__type2_group.length_3.remove(word)
                return
            elif length == 4:
                self.__type2_group.length_4.remove(word)
                return
            elif length == 5:
                self.__type2_group.length_5.remove(word)
                return
            elif length == 6:
                self.__type2_group.length_6.remove(word)
                return

    def __construct_string(self, type, length, last_word=''):
        end = ''
        if last_word != '':
            w = self.__get_rhyme(last_word)
            end = w.word
            try:
                self.__delete_word(end, w.count_of_syllables, w.type)
            except:
                True
            length -= w.count_of_syllables
        string = ''
        if type == 1:
            first_syllable = 1
        else:
            first_syllable = 0
        last = ''
        while length > 0:
            word_length = rand.randint(1, 6)
            if first_syllable == 1:
                if word_length > length or not self.__type1_group.has_length(word_length):
                    continue
                last = self.__type1_group.get_word(word_length)
            else:
                if word_length > length or not self.__type2_group.has_length(word_length):
                    continue
                last = self.__type2_group.get_word(word_length)
            string += last + ' '
            length -= word_length
            first_syllable = (first_syllable + (word_length % 2)) % 2
        string += end
        return [string, last]

    def generate(self, count_of_syllables, type):
        text = ''
        for i in range(1):
            data = self.__construct_string(type, count_of_syllables)
            text += data[0] + '\n'
            last = data[1]
            data = self.__construct_string(type, count_of_syllables, last)
            text += data[0] + '\n'
            data = self.__construct_string(type, count_of_syllables)
            text += data[0] + '\n'
            last = data[1]
            data = self.__construct_string(type, count_of_syllables, last)
            text += data[0] + '\n'
        return text
