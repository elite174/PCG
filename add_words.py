from Word import WordList
from Poetry import Generator


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


def generate():
    groups = init()
    generator = Generator(groups)
    print(generator.generate(8, 2))


def check():
    groups = init()
    for i in groups:
        print('type = ' + str(i.type))
        for w in i.words:
            print(w.word)
            print(w.representation)

generate()

