# put all the computational logic stuff here

class GameBoard:
    # visual representation of the game board
    # don't do the logic here, this is mainly where the graphics are handled

    def __init__(self, size=(100, 100)):
        self.size = size

    def render(self):
        # render the actual board
        # call this method every frame to draw the updated board
        pass

class Cell:
    # a cell on the game board
    
    def __init__(self, position, color, size):
        self.position = position
        self.color = color
        self.size = size
    
    


class GameOfLife:
    # making our game of life object
    # this is the parent object that controls everything else
    # it has a game board and a list of cells
    def __init__(self, size=(100, 100), units=100):
        # initialize our game of life object
        self.gameboard = GameBoard(size)
    