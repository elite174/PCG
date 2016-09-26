import Constants as C
import random as rand
from NodeClass import Node
from PIL import Image, ImageDraw


class BSP:
    # Fields of the class


    __root = None
    __leaf_nodes = []
    __matrix = []

    # Constructor of the class
    def __init__(self):
        self.__root = Node(0, 0, C.matrix_size - 1, C.matrix_size - 1)
        self.__leaf_nodes = []
        self.__leaf_nodes.append(self.__root)
        self.__matrix = ['\''] * C.matrix_size
        for i in range(C.matrix_size):
            self.__matrix[i] = ['\''] * C.matrix_size

    # This function splits the space into two parts
    def __split_part(self, node, horizontal=True):
        if horizontal:
            low = C.part_size
            high = node.roomHeight() - 1 - low
            border = node.iStart + rand.randint(low, high)
            node.leftNode = Node(node.iStart, node.jStart, border, node.jEnd, parent=node)
            node.rightNode = Node(border + 1, node.jStart, node.iEnd, node.jEnd, parent=node)
            self.__leaf_nodes.remove(node)
            self.__leaf_nodes.append(node.leftNode)
            self.__leaf_nodes.append(node.rightNode)
        else:
            low = C.part_size
            high = node.roomWidth() - 1 - low
            border = node.jStart + rand.randint(low, high)
            node.leftNode = Node(node.iStart, node.jStart, node.iEnd, border, parent=node)
            node.rightNode = Node(node.iStart, border + 1, node.iEnd, node.jEnd, parent=node)
            self.__leaf_nodes.remove(node)
            self.__leaf_nodes.append(node.leftNode)
            self.__leaf_nodes.append(node.rightNode)

    # This function recursively splits the space and forms the tree of spaces
    def __generate_partitions(self, node):
        # How to split: horizontal or vertical
        choice = rand.randint(0, 1)
        # Horizontal slice
        if choice == 0:
            # try horizontal
            if node.roomHeight() / 2 > C.part_size:
                self.__split_part(node, horizontal=True)
                self.__generate_partitions(node.leftNode)
                self.__generate_partitions(node.rightNode)
            # try vertical
            elif node.roomWidth() / 2 > C.part_size:
                self.__split_part(node, horizontal=False)
                self.__generate_partitions(node.leftNode)
                self.__generate_partitions(node.rightNode)
        # Vertical slice
        elif (choice == 1):
            # try vertical
            if node.roomWidth() / 2 > C.part_size:
                self.__split_part(node, horizontal=False)
                self.__generate_partitions(node.leftNode)
                self.__generate_partitions(node.rightNode)
            # try horizontal
            elif node.roomHeight() / 2 > C.part_size:
                self.__split_part(node, horizontal=True)
                self.__generate_partitions(node.leftNode)
                self.__generate_partitions(node.rightNode)

    # This function places rooms with random size into a space
    def __generate_rooms(self):
        for node in self.__leaf_nodes:
            height = rand.randint(C.min_room_size, node.roomHeight() - 2)
            width = rand.randint(C.min_room_size, node.roomWidth() - 2)
            iPos = rand.randint(node.iStart + 1, node.iEnd - height)
            jPos = rand.randint(node.jStart + 1, node.jEnd - width)
            node.room(iPos, jPos, iPos + height - 1, jPos + width - 1)
            for i in range(iPos, iPos + height):
                for j in range(jPos, jPos + width):
                    self.__matrix[i][j] = '#'

    # This is auxiliary function
    # It connects "holes" and uncompleted corridors
    def __go(self, i, j, height, width):
        self.__matrix[i][j] = '#'
        if height:
            back = j
            forward = j
            while (True):
                if self.__matrix[i][back - 1] == '\'' and self.__matrix[i][forward + 1] == '\'':
                    self.__matrix[i][back - 1] = '#'
                    self.__matrix[i][forward + 1] = '#'
                    back -= 1
                    forward += 1
                elif self.__matrix[i][back - 1] == '#' and self.__matrix[i][forward + 1] == '\'':
                    self.__matrix[i][forward + 1] = '#'
                    forward += 1
                elif self.__matrix[i][back - 1] == '\'' and self.__matrix[i][forward + 1] == '#':
                    self.__matrix[i][back - 1] = '#'
                    back -= 1
                elif self.__matrix[i][back - 1] == '#' and self.__matrix[i][forward + 1] == '#':
                    break
        elif width:
            back = i
            forward = i
            while (True):
                if self.__matrix[back - 1][j] == '\'' and self.__matrix[forward + 1][j] == '\'':
                    self.__matrix[back - 1][j] = '#'
                    self.__matrix[forward + 1][j] = '#'
                    back -= 1
                    forward += 1
                elif self.__matrix[back - 1][j] == '#' and self.__matrix[forward + 1][j] == '\'':
                    self.__matrix[forward + 1][j] = '#'
                    forward += 1
                elif self.__matrix[back - 1][j] == '\'' and self.__matrix[forward + 1][j] == '#':
                    self.__matrix[back - 1][j] = '#'
                    back -= 1
                elif self.__matrix[back - 1][j] == '#' and self.__matrix[forward + 1][j] == '#':
                    break

    # This function connects two rooms via corridor
    def __connect(self, leftNode, rightNode):
        room1heightS = leftNode.roomiStart
        room1heightE = leftNode.roomiEnd
        room2heightS = rightNode.roomiStart
        room2heightE = rightNode.roomiEnd
        room1widthS = leftNode.roomjStart
        room1widthE = leftNode.roomjEnd
        room2widthS = rightNode.roomjStart
        room2widthE = rightNode.roomjEnd
        commonHeight = list(set([x for x in range(room1heightS, room1heightE + 1)]) & set(
            [x for x in range(room2heightS, room2heightE + 1)]))
        commonWidth = list(set([x for x in range(room1widthS, room1widthE + 1)]) & set(
            [x for x in range(room2widthS, room2widthE + 1)]))
        commonHeight.sort()
        commonWidth.sort()
        if commonHeight != []:
            height = rand.randint(commonHeight[0], commonHeight[len(commonHeight) - 1])
            if room1widthE < room2widthS:
                self.__go(height, room1widthE, height=True, width=False)
            else:
                self.__go(height, room2widthE, height=True, width=False)
            return
        if commonWidth != []:
            width = rand.randint(commonWidth[0], commonWidth[len(commonWidth) - 1])
            if room1heightE < room2heightS:
                self.__go(room1heightE, width, height=False, width=True)
            else:
                self.__go(room2heightE, width, height=False, width=True)
            return

    # This function connects all the rooms via corridors
    def __generate_corridors(self, node):
        while node != None:
            if node.connected == True:
                node = node.parent
            elif node.leftNode == None and node.rightNode == None:
                node.connected = True
            elif node.leftNode.connected == False:
                node = node.leftNode
            elif node.rightNode.connected == False:
                node = node.rightNode
            elif node.leftNode.connected and node.rightNode.connected:
                self.__connect(node.leftNode, node.rightNode)
                node.roomiStart = min(node.leftNode.roomiStart, node.rightNode.roomiStart)
                node.roomjStart = min(node.leftNode.roomjStart, node.rightNode.roomjStart)
                node.roomiEnd = max(node.leftNode.roomiEnd, node.rightNode.roomiEnd)
                node.roomjEnd = max(node.leftNode.roomjEnd, node.rightNode.roomjEnd)
                node.connected = True

    # This is auxiliary function
    # It prints the matrix for checking if it is needed
    def __print_matrix(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                print(self.__matrix[i][j], end='')
            print()

    # This function generates a picture (map) that based on the output matrix
    def __show_matrix(self):
        img = Image.new('RGB', (C.matrix_size * C.pixel_size, C.matrix_size * C.pixel_size), (0, 0, 0))
        color = (0, 0, 0)
        y = 0
        draw = ImageDraw.Draw(img)
        for i in range(C.matrix_size):
            x = 0
            for j in range(C.matrix_size):
                if self.__matrix[i][j] == '#':
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], (255, 255, 255))
                else:
                    draw.rectangle([x, y, x + C.pixel_size, y + C.pixel_size], color)
                x += C.pixel_size
            y += C.pixel_size
        img.save('bsp.jpg', 'JPEG')
        del draw

    # This is the main function that creates a maze
    def generate(self):
        self.__generate_partitions(self.__root)
        self.__generate_rooms()
        self.__generate_corridors(self.__root)
        self.__show_matrix()
