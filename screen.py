import pygame
from math import floor

pygame.init()

# VIEW OBJECT

# This system is a layer based approach, with only one draw per layer. Perhaps in the future I can investigate parallel programming which seems like the best approach to drawing two things on the same layer
class Screen:
    # Input of to caption text, horizontal width, vertical height
    defaultCaption = "Default Program"
    defaultScreenWidth = floor(pygame.display.Info().current_w*0.75)
    defaultScreenHeight = floor(pygame.display.Info().current_h*0.75)
    defaultGridStatus = True
    defaultGridSize = 20 # px
    defaultFpsStatus = False
    defaultFpsSize = 12 # px

    def __init__(self, captionInput = defaultCaption, screenWidthInput = defaultScreenWidth, screenHeightInput = defaultScreenHeight):
        # Defines the pygame canvas
        self.screenWidth = screenWidthInput
        self.screenHeight = screenHeightInput
        self.canvas = pygame.display.set_mode((self.screenWidth, self.screenHeight)) 
        
        # Stores all of the programs visual functions in order of layers
        self.drawMethods = []
        
        # Initialize caption
        self.captionText = captionInput
        self.updateCaption(self.captionText)

        self.gridStatus = self.defaultGridStatus
        self.gridSize = self.defaultGridSize
        self.fpsStatus = self.defaultFpsStatus
        self.fpsSize = self.defaultFpsSize

    # Adds a draw function to the draw array, takes an input of an object
    def addDraw(self, objectToDraw, preferredLayer):
        self.newNode = self.Node(objectToDraw, preferredLayer)
        self.drawMethods.append(self.newNode)
        # TODO: Measure performance impact of sorting every time a new draw is added
        self.drawMethods = self.sort(self.drawMethods) 

    # Externally accessible caption update
    def updateCaption(self, newCaption):
        self.captionText = newCaption
        pygame.display.set_caption(self.captionText)

    # Sorts the draw array by layer
    def sort(self, unsortedArray):
        array = unsortedArray
        if(array[len(array)-1] > array[len(array)-2]):
            i = 1
            while (i < len(array)):
                j = i
                while (j > 0 and array[j-1] > array[j]):
                    dummy = array[j]
                    array[j] = array[j-1]
                    array[j-1] = dummy
                    j -= 1
                i += 1
        return array
    
    # Optional toggles
    def toggleGrid(self):
        self.gridStatus = True if not self.gridStatus else False

    def toggleFPS(self):
        self.fpsStatus = True if not self.fpsStatus else False

    # Draws the grid
    def drawGrid(self):
        if(self.gridStatus):
            for x in range(0, self.screenWidth, self.gridSize):
                pygame.draw.line(self.canvas, "light gray", (x, 0), (x, self.screenHeight))
            for y in range(0, self.screenHeight, self.gridSize):
                pygame.draw.line(self.canvas, "light gray", (0, y), (self.screenWidth, y))
    # Draws the fps counter
    def drawFps(self):
        if(self.fpsStatus):
            self.fps = pygame.font.SysFont("Arial", self.fpsSize).render(str(int(pygame.time.get_ticks()/1000)), True, "dark green")
            self.canvas.blit(self.fps, (self.screenWidth-self.fpsSize, 0))
    

    # Stores the object and their layer
    class Node:
        def __init__(self, objectToDraw, preferredLayer = 1, visible = True):
            self.obj = objectToDraw
            self.layer = preferredLayer
            self.visible = visible
        # overload < operator
        def __lt__(self, other):
            return self.layer < other.layer
        
    # Primary screen update
    def draw(self):
        self.canvas.fill("white") 
        self.drawGrid()
        self.drawFps()
        for x in range(0, len(self.drawMethods)):
            if(self.drawMethods[x].visible):
                self.drawMethods[x].obj.draw(self.canvas)
        pygame.display.update()