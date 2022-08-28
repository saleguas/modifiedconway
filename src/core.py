import pygame
import random
# put all the computational logic stuff here

class GameBoard:
    # visual representation of the game board
    # don't do the logic here, this is mainly where the graphics are handled

    def __init__(self, size=(800, 800)):
        self.size = size


    def startWindow(self):
        pygame.init()
        pygame.display.set_caption('Quick Start')
        window_surface = pygame.display.set_mode(self.size)

        self.background = pygame.Surface(self.size)
        self.background.fill(pygame.Color('#000000'))
        self.window_surface = window_surface
        


    def render(self, cells):
        # render the actual board
        # call this method every frame to draw the updated board

        is_running = True
        
        while is_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            self.window_surface.blit(self.background, (0, 0))
            for cell in cells:
                pygame.draw.rect(self.window_surface, cell.color, (cell.position[0], cell.position[1], cell.size[0], cell.size[1]))
            pygame.display.update()
        
class Cell:
    # a cell on the game board
    
    def __init__(self, position, color, size=(5, 5)):
        self.position = position
        self.color = color
        self.size = size
    
    


class GameOfLife:
    # making our game of life object
    # this is the parent object that controls everything else
    # it has a game board and a list of cells
    def __init__(self, size=(800, 800), units=100):
        # initialize our game of life object
        self.gameboard = GameBoard(size)
        self.units = units
        self.cells = []

    def generate_cells(self):
        # generate the cells for the game board
        # make possible_colors red, green or blue in hex
        possible_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        cell_size = (5, 5)
        for x in range(self.units):
            # random position on the game board
            position = (random.randint(0, self.gameboard.size[0]), random.randint(0, self.gameboard.size[1]))
            # random color from the possible_colors list
            color = random.choice(possible_colors)
            # create a cell object
            cell = Cell(position, color, cell_size)
            # add the cell to the list of cells
            self.cells.append(cell)

    def update(self):
        # apply the rules of the game of life to the cells
        # this is where the logic is
        pass
        
    
    def start(self):
        # start the game
        self.gameboard.startWindow()
        self.generate_cells()
        self.gameboard.render(self.cells)

    

g = GameOfLife()
g.start()