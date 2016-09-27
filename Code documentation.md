<b>Code documentation</b>

1. Comparison of maze generation algorithms

A. Binary Space Partitioning
The code of this algorithm consists of the following files:
  <ul>
  <li>Constants.py – this file contains necessary constants that is used in the algorithm</li>
  <li>NodeClass.py – this file contains description of the class “Node” that is used in the algorithm</li>
  <li>BSP.py – this file contains description of the class “BSP” that is used in the algorithm</li>
  </ul>
  
  
B. Methods of BSP class
# Constructor of the class
    __init__(self)
# This function splits the space into two parts
    __split_part(self, node, horizontal=True)
# This function recursively splits the space and forms the tree of spaces
    __generate_partitions(self, node)
# This function places rooms with random size into a space
    __generate_rooms(self)
# This is auxiliary function. It connects "holes" and uncompleted corridors
    __go(self, i, j, height, width)
# This function connects two rooms via corridor
    __connect(self, leftNode, rightNode)
# This function connects all the rooms via corridors
    __generate_corridors(self, node)
# This is auxiliary function
    # It prints the matrix for checking if it is needed
    __print_matrix(self)
# This function generates a picture (map) that based on the output matrix
    __show_matrix(self)
    
    

C. Methods of Node class:
# Constructor of the class. It receives coordinates of a space (iStart, jStart, iEnd, jEnd) and the parent node (parent)
    __init__(self, iStart, jStart, iEnd, jEnd, parent=None)
# Setter for the coordinates of a room. It receives coordinates of a room (i1, j1, i2, j2)
    room(self, i1, j1, i2, j2)
# This method returns the space width
    roomWidth(self)
# This method returns the space height
    roomHeight(self)


D. Look Ahead Digger
The code of this algorithm consists of the following files:
<ul>
  <li>Constants.py – this file contains necessary constants that is used in the algorithm</li>
  <li>Digger.py – this file contains description of the class “Digger” that is used in the algorithm</li>
</ul>


E. Methods of class Digger
# Constructor of the class. It initializes the variables
    __init__(self)
# This function checks whether it possible to place a room with given height and width at coordinate (i,j)
    __can_place_room(self, i, j, height, width)
# This function checks whether it possible to place a corridor with given length and direction at coordinate (i,j)
    __can_place_corridor(self, i, j, length, direction)
# This function places (or deletes) a corridor with given length and direction at coordinate (i,j)
    __place_corridor(self, i, j, length, direction, delete=False)
# This function changes the matrix by replacing '0' to '#'
    __correct_matrix(self)
 # This function starts to generate the maze from the given position (i,j)
    dig(self, i, j)
# This function places a room with given height and width at coordinate (i,j)
    __placeRoom(self, i, j, height, width)
# This is auxiliary function. It prints the matrix to the screen
    print_matrix(self)
# This function generates a picture (map) that based on the output matrix
    __show_maze(self)
    
    
 
F. Cellular Automata Generator
The code of this algorithm consists of the following files:
<ul>
  <li>Constants.py – this file contains necessary constants that is used in the algorithm</li>
  <li>CellularAutomata.py – this file contains description of the class “Digger” that is used in the algorithm</li>
</ul>

G. Methods of class CellularAutomata
# Constructor for the class. It receives number of generation than it needs to generate
    __init__(self, generations)
# This function initializes new matrix
    __init_new_matrix(self)
# This function fills the matrix with random noise
    __fill_random(self)
# This function generates new generation for the matrix
    __make(self)
# This function return the number of walls around the cell at position (i,j)
    __count_walls(self, i, j)
# This function places a wall at position (i,j)
    __place_wall(self, i, j)
# This is auxiliary function. It prints the matrix to the screen
    print_matrix(self)
# This function generates cave
    generate_cave(self)
# This function generates a picture (map) that based on the output matrix
    __show_matrix(self)


2. Poems generation

The code of this algorithm consists of the following files:
<ul>
<li>Poetry.py – the file describes the class Generator</li>
<li>Word.py – the files describes the class Word_List</li>
<li>add_words.py – the script parses the Data File and generates the quatrain with given verse size and string length (count of syllables)</li>
<li>base1.txt – the Data file. It has the following structure:
  <ul>
  <li>list of rhyme words with the same representation</li>
  <li>representation of these words</li>
  </ul>
</ul>

A. Methods of Class Generator
# Constructor for the class. It receives list of WordList objects
    __init__(self, groups)
# This function returns a rhyme to the given word
    __get_rhyme(self, word)
# This function deletes the word from the length group. It receives a word, length of the word and type of the word
    __delete_word(self, word, length, type)
# This function constructs a string. It receives type of the string (iamb or trochee), length of the string and the last word of the previous string
    __construct_string(self, type, length, last_word='')
# This function generates a poem. It receives length of the string (count of syllables) and type of the poem (iamb or trochee)
    generate(self, count_of_syllables, type)


A. Methods of Class Word List
# Constructor for the class. It receives the list of Word objects and representation of the words in this list
    __init__(self, words, representation)
# This function sets the type (iamb or trochee) for the WordList object
    __get_type(self)
