import Constants as C
import itertools
import random as rand
from PIL import Image, ImageDraw


class Digger:
    __matrix = []
    __sizes = []
    __length = []
    __stack = []
    __corridor_stack = []

    # Constructor of the class
    # It initializes the variables
    def __init__(self):
        self.__matrix = [0] * C.matrix_size
        for i in range(C.matrix_size):
            self.__matrix[i] = ['\''] * C.matrix_size
        size = [x for x in range(C.min_room_size, C.max_room_size + 1, 2)]
        self.__sizes = list(itertools.product(size, size))
        for i in range(C.min_length, C.max_length + 1):
            self.__length.append(i)

    # This function checks whether it possible to place a room
    # with given height and width at coordinate (i,j)
    def __can_place_room(self, i, j, height, width):
        if (i - int(height / 2)) < 1 or (j - int(width / 2) < 1) or (
                        i + int(height / 2) >= C.matrix_size - 1) or (j + int(width / 2) >= C.matrix_size - 1):
            return False
        flag = True
        for y in range(i - int(height / 2) - 1, i + int(height / 2) + 2):
            for x in range(j - int(width / 2) - 1, j + int(width / 2) + 2):
                if self.__matrix[y][x] == '#':
                    return False
        return flag

    # This function checks whether it possible to place a corridor
    # with given length and direction at coordinate (i,j)
    def __can_place_corridor(self, i, j, length, direction):
        if direction == 'U':
            while self.__matrix[i][j] == '#':
                i -= 1
            if i - length < 1:
                return False
            k = 0
            while k < length:
                if self.__matrix[i][j] == '#' or self.__matrix[i][j] == '0':
                    return False
                i -= 1
                k += 1
            return True
        elif direction == 'D':
            while self.__matrix[i][j] == '#':
                i += 1
            if i + length > C.matrix_size - 2:
                return False
            k = 0
            while k < length:
                if self.__matrix[i][j] == '#' or self.__matrix[i][j] == '0':
                    return False
                i += 1
                k += 1
            return True
        elif direction == 'L':
            while self.__matrix[i][j] == '#':
                j -= 1
            if j - length < 1:
                return False
            k = 0
            while k < length:
                if self.__matrix[i][j] == '#' or self.__matrix[i][j] == '0':
                    return False
                j -= 1
                k += 1
            return True
        elif direction == 'R':
            while self.__matrix[i][j] == '#':
                j += 1
            if j + length > C.matrix_size - 2:
                return False
            k = 0
            while k < length:
                if self.__matrix[i][j] == '#' or self.__matrix[i][j] == '0':
                    return False
                j += 1
                k += 1
            return True

    # This function places (or deletes) a corridor
    # with given length and direction at coordinate (i,j)
    def __place_corridor(self, i, j, length, direction, delete=False):
        if direction == 'U':
            while self.__matrix[i][j] == '#':
                i -= 1
            k = 0
            while k < length:
                if delete:
                    self.__matrix[i][j] = '\''
                else:
                    self.__matrix[i][j] = '0'
                i -= 1
                k += 1
            return [i, j]
        elif direction == 'D':
            while self.__matrix[i][j] == '#':
                i += 1
            k = 0
            while k < length:
                if delete:
                    self.__matrix[i][j] = '\''
                else:
                    self.__matrix[i][j] = '0'
                i += 1
                k += 1
            return [i, j]
        elif direction == 'L':
            while self.__matrix[i][j] == '#':
                j -= 1
            k = 0
            while k < length:
                if delete:
                    self.__matrix[i][j] = '\''
                else:
                    self.__matrix[i][j] = '0'
                j -= 1
                k += 1
            return [i, j]
        elif direction == 'R':
            while self.__matrix[i][j] == '#':
                j += 1
            k = 0
            while k < length:
                if delete:
                    self.__matrix[i][j] = '\''
                else:
                    self.__matrix[i][j] = '0'
                j += 1
                k += 1
            return [i, j]

    # This function changes the matrix by replacing '0' to '#'
    def __correct_matrix(self):
        for item in self.__corridor_stack:
            self.__place_corridor(item[0], item[1], item[2], item[3], delete=True)
        for i in range(C.matrix_size):
            for j in range(C.matrix_size):
                if self.__matrix[i][j] == '0':
                    self.__matrix[i][j] = '#'

    # This function starts to generate the maze from the given position (i,j)
    def dig(self, i, j):
        flag1 = False
        flag2 = False
        while not (flag1 and flag2):
            local_sizes = self.__sizes.copy()
            flag1 = True
            while len(local_sizes) != 0:
                item = local_sizes.pop(rand.randint(0, len(local_sizes) - 1))
                if self.__can_place_room(i, j, item[0], item[1]):
                    self.__corridor_stack = []
                    self.__placeRoom(i, j, item[0], item[1])
                    self.__stack.append((i, j))
                    flag1 = False
                    break
            flag2 = True
            local_directions = C.directions.copy()
            while len(local_directions) != 0:
                direction = local_directions.pop(rand.randint(0, len(local_directions) - 1))
                local_length = self.__length.copy()
                done = False
                while len(local_length) != 0:
                    length = local_length.pop(rand.randint(0, len(local_length) - 1))
                    if self.__can_place_corridor(i, j, length, direction):
                        self.__corridor_stack.append((i, j, length, direction))
                        item = self.__place_corridor(i, j, length, direction)
                        i = item[0]
                        j = item[1]
                        done = True
                        flag2 = False
                        break
                if done:
                    break
                if len(local_directions) == 0:
                    if len(self.__stack) == 0:
                        break
                    local_directions = C.directions.copy()
                    for item in self.__corridor_stack:
                        self.__place_corridor(item[0], item[1], item[2], item[3], delete=True)
                    self.__corridor_stack = []
                    item = self.__stack.pop()
                    i = item[0]
                    j = item[1]
        self.__correct_matrix()
        # self.print_matrix()
        self.__show_maze()

    # This function places a room
    # with given height and width at coordinate (i,j)
    def __placeRoom(self, i, j, height, width):
        for y in range(i - int(height / 2), i + int(height / 2) + 1):
            for x in range(j - int(width / 2), j + int(width / 2) + 1):
                self.__matrix[y][x] = '#'

    # This is auxiliary function
    # It prints the matrix to the screen
    def print_matrix(self):
        for i in range(C.matrix_size):
            print(''.join([x for x in self.__matrix[i]]))

    # This function generates a picture (map) that based on the output matrix
    def __show_maze(self):
        img = Image.new('RGB', (C.matrix_size * C.pixel_size, C.matrix_size * C.pixel_size), (0, 0, 0))
        color = (255, 255, 255)
        x = 0
        y = 0
        draw = ImageDraw.Draw(img)
        for i in range(C.matrix_size):
            x = 0
            for j in range(C.matrix_size):
                if self.__matrix[i][j] == '#':
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], color)
                else:
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], (0, 0, 0))
                x += C.pixel_size
            y += C.pixel_size
        img.save('maze.jpg', 'JPEG')
        del draw
