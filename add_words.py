from Word import WordList
from Poetry import Generator


# This function parses the Data File
def init():
    file = open('base1.txt', 'r', encoding='utf-8')
    group_list = []
    line = file.readline()
    while line:
        rep = file.readline()
        rep = rep[:len(rep) - 1]
        line = line[:len(line) - 1]
        l = line.split(sep=', ')
        word_list = WordList(l, rep)
        group_list.append(word_list)
        line = file.readline()
    file.close()
    return group_list


# This function generates a poem with chosen verse size and syllable length
# 1 - trochee
# 2 - iamb
def generate():
    groups = init()
    generator = Generator(groups)
    print(generator.generate(9, 1))


generate()
