class Node:
    # Coordinates of the space
    iStart = 0
    jStart = 0
    iEnd = 0
    jEnd = 0

    leftNode = None
    rightNode = None
    parent = None

    # Flag that shows the room is connected
    connected = False

    # Coordinates of the room inside the space
    roomiStart = 0
    roomjStart = 0
    roomiEnd = 0
    roomjEnd = 0

    # Constructor of the class
    # It receives coordinates of a space (iStart, jStart, iEnd, jEnd) and the parent node (parent)
    def __init__(self, iStart, jStart, iEnd, jEnd, parent=None):
        self.iStart = iStart
        self.jStart = jStart
        self.iEnd = iEnd
        self.jEnd = jEnd
        self.parent = parent

    # Setter for the coordinates of a room
    # It receives coordinates of a room (i1, j1, i2, j2)
    def room(self, i1, j1, i2, j2):
        self.roomiStart = i1
        self.roomjStart = j1
        self.roomiEnd = i2
        self.roomjEnd = j2

    # This method returns the space width
    def roomWidth(self):
        return self.jEnd - self.jStart + 1

    # This method returns the space height
    def roomHeight(self):
        return self.iEnd - self.iStart + 1
