class WordList:
    words = []
    type = 0

    # This class contains a word and necessary information about it
    class Word:
        word = ''
        representation = ''
        count_of_syllables = 0
        type = 0

        # Constructor for the class
        # It receives the word and representation of the word
        def __init__(self, word, representation):
            self.word = word
            self.representation = representation
            self.count_of_syllables = len(representation)
            if self.representation[0] == '0':
                self.type = 2
            else:
                self.type = 1

        def get_length(self):
            return self.count_of_syllables

    # Constructor for the class
    # It receives the list of Word objects and representation of the words in this list
    def __init__(self, words, representation):
        self.words = []
        for i in words:
            self.words.append(self.Word(i, representation))
        self.__get_type()

    # This function sets the type (iamb or trochee) for the WordList object
    def __get_type(self):
        self.type = self.words[0].type
