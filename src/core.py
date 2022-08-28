# put all the computational logic stuff here
class GameBoard:
    # visual representation of the game board

    def __init__(self, size=(100, 100)):
        self.size = size

    def render(self):
        # render the actual board
        # call this method every frame to draw the updated board
        pass

class GameOfLife:
    # making our game of life object

    def __init__(self, size=(100, 100), units=100):
        # initialize our game of life object
        self.gameboard = GameBoard(size)
    