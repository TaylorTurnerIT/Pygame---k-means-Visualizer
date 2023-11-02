import pygame
import numpy as np
import random
from screen import *

# INIT
pygame.init() # Pygame init
screen = Screen("k-Means Visualizer") # Screen init
exit = False # Game loop exit condition

# Node class for graph
class Point:
    def __init__(self, point, radius, color):
        # Visual properties
        self.origin = point # Center as vector
        self.radius = radius
        self.diameter = self.radius*2
        self.c = color
        # Data properties
        self.neighbors = []
        self.value = None

    def addNeighbor(self, neighborInput):
        # Check if it exists already, else append
        if (self.neighbors.count(neighborInput) == 0):
            self.neighbors.append(neighborInput)

    def removeNeighbor(self, neighborInput):
        # Chef if it exists, then delete
        if (self.neighbors.count(neighborInput) != 0):
            self.neighbors.remove(neighborInput)

    def draw(self, canvas):
        pygame.draw.circle(screen, "black", self.origin, self.radius)


# GAME OBJECTS
dataCount = 20
dataList = []
clusterCount = 2

for n in dataCount:
    # Choose a random cluster to plot points
    cluster = random.randint%clusterCount
    randCoordinate = pygame.Vector2(random.randint%cluster, random.randint%cluster)
    dataList.append(Point())

for point in dataList:
    screen.addDraw(point)

# GAME LOOP
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit = True
            if event.key == pygame.K_g:
                screen.toggleGrid()
            if event.key == pygame.K_f:
                screen.toggleFPS()

    
    screen.draw()

# QUIT
pygame.quit()