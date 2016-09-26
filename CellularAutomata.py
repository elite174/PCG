import Constants as C
import random as rand
from PIL import Image, ImageDraw


class CellAutomata:
    __matrix = []
    __new_matrix = []
    __generations = 0

    def __init__(self, generations):
        self.__generations = generations
        self.__matrix = [0] * C.matrix_size
        self.__new_matrix = [0] * C.matrix_size
        for i in range(C.matrix_size):
            self.__matrix[i] = ['#'] * C.matrix_size
            self.__new_matrix[i] = ['#'] * C.matrix_size
        self.__fill_random()

    def __init_new_matrix(self):
        self.__new_matrix = [0] * C.matrix_size
        for i in range(C.matrix_size):
            self.__new_matrix[i] = ['#'] * C.matrix_size

    def __fill_random(self):
        for i in range(1, C.matrix_size - 1):
            for j in range(1, C.matrix_size - 1):
                number = rand.randint(0, 100)
                if number > 45:
                    self.__matrix[i][j] = '.'

    def __make(self):
        for i in range(1, C.matrix_size - 1):
            for j in range(1, C.matrix_size - 1):
                self.__new_matrix[i][j] = self.__place_wall(i, j)
        self.__matrix = self.__new_matrix
        self.__init_new_matrix()

    def __count_walls(self, i, j):
        count = 0
        for n in range(i - 1, i + 2):
            for m in range(j - 1, j + 2):
                if self.__matrix[n][m] == '#' and (n != i or m != i):
                    count += 1
        return count

    def __place_wall(self, i, j):
        count = self.__count_walls(i, j)
        if self.__matrix == '#':
            if count < 4:
                return '.'
            else:
                return '#'
        else:
            if count > 4:
                return '#'
            else:
                return '.'

    def print_matrix(self):
        for i in range(C.matrix_size):
            print(''.join([x for x in self.__matrix[i]]))

    def generate_cave(self):
        for i in range(self.__generations):
            self.__make()
        self.__show_matrix()

    def __show_matrix(self):
        img = Image.new('RGB', (C.matrix_size * C.pixel_size, C.matrix_size * C.pixel_size), (0, 0, 0))
        color = (255, 255, 255)
        y = 0
        draw = ImageDraw.Draw(img)
        for i in range(C.matrix_size):
            x = 0
            for j in range(C.matrix_size):
                if self.__matrix[i][j] == '#':
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], (0, 0, 0))
                else:
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], color)
                x += C.pixel_size
            y += C.pixel_size
        img.save('cave.jpg', 'JPEG')
        del draw
