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
    def __init__(self, point, radius, color, neighborList = []):
        # Visual properties
        self.origin = point # Center as vector
        self.radius = radius
        self.diameter = self.radius*2
        self.c = color
        # Data properties
        self.neighbors = neighborList
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
        pygame.draw.circle(canvas, self.c, self.origin, self.radius)


# GAME OBJECTS
dataCount = 20
dataList = []
clusterCount = 3
clusterList = []

# QUADRANT CREATION
# This system will define a cluster's positioning by creating a circular area in which data can appear. The more clusters, the less there are. Also ensures two clusters do not overlap.
for i in range(clusterCount):
    clusterOrigin = (random.randint(0, screen.screenWidth),random.randint(0, screen.screenHeight)) # Computes a random point to serve as the cluster's center. All points will be within a radius of this point
    radius = 20
    clusterList.append(clusterOrigin)

    


# clusterList.append((0, int(screen.screenHeight/clusterCount)))
# clusterList.append((int(screen.screenHeight/clusterCount), screen.screenHeight))

for n in range(dataCount):
    # Choose a random cluster to plot points
    cluster = random.randint(0, clusterCount-1)
    randx = random.randint()
    randy = int(random.randint(clusterList[cluster][0], clusterList[cluster][1]))
    randCoordinate = pygame.Vector2(randx, randy)
    # Color black
    color = "black"

    # Color by cluster at creation
    # if(cluster == 0):
    #     color = "dark blue"
    # else:
    #     color = "dark red"
    rad = 4
    # This line appends the coordinate, radius, color, AND assigns each point to be neighbors with all others
    dataList.append(Point(randCoordinate, rad, color, dataList))

for point in dataList:
    screen.addDraw(point, 1)

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
    screen.draw()

# QUIT
pygame.quit()