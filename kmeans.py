import pygame
import numpy as np
import random
import time
from screen import *

# INIT
pygame.init() # Pygame init
screen = Screen("k-Means Visualizer") # Screen init
exit = False # Game loop exit condition

# Node class for graph
class Point:
    def __init__(self, point: pygame.Vector2, radius, color, neighborList = [], value = []):
        # Visual properties
        self.origin = point # Center as vector
        self.radius = radius
        self.diameter = self.radius*2
        self.c = color
        # Data properties
        self.neighbors = neighborList
        self.value = value

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

class DataController:
    def __init__(self):
        # GAME OBJECTS
        self.dataCount = 5000 # number of data points to generate (will make more than this if anomalies are enabled)
        self.dataList = [] # array to store all data points
        self.generateAnomalies = True # generate data outside normal area
        self.anomalyRatio = 0.3 # Default 10% of datacount will be anomalous
        self.anomalyCount = int(self.dataCount*self.anomalyRatio)
        self.clusterCount = 3 # number of clusters to generate, also used to determine number of clusters for a k-means alg.
        self.clusterList = [] # Stores the cluster 
        self.genRadius = 150 # Radius of the generation circle
        self.pointDrawRadius = 3 # Size of each data point (visual only)
        self.pointColor = "black" # Defaults color to black
        self.drawLayer = 1
        self.generateData()
        self.kMeansManager = self.kMeans(self.dataList, self.clusterCount, self.drawLayer) # initializes the k-means algorithm
    
    def __del__(self):
        self.clearDrawData()

    def generateData(self):
        self.clearDrawData()
        self.generateData()

    def clearDrawData(self):
        for d in range(len(self.dataList)):
            screen.removeDraw(self.dataList[d])

    # CLUSTER CREATION
        # This system will define a cluster's positioning by creating a circular area in which data can appear. The more clusters, the less data is in each.
    # Generates the clusters and adds them to the list
    def generateClusters(self):
        for i in range(self.clusterCount):
            self.clusterOrigin = pygame.Vector2(int(random.randint(self.genRadius, screen.screenWidth-self.genRadius)),int(random.randint(self.genRadius, screen.screenHeight-self.genRadius))) # Computes a random point to serve as the cluster's center. All points will be within a radius of this point
            self.clusterList.append(self.clusterOrigin)
            # print("Cluster origin is at ")
            # print(self.clusterOrigin)

    # Generates the data within the clusters, the clusters MUST be generated before this can work.
    def generateData(self):
        startTime = time.time()
        
        for n in range(self.dataCount):
            cluster = n%self.clusterCount
            # cluster = random.randint(0, self.clusterCount-1) # Between 1 and cluster count, but zero indexed
            origin = self.clusterList[cluster] # Gets current cluster
            angle = random.uniform(0,1) * 2 * np.pi # Gets a random angle direction in a circular area
            # angle = random.random()%1 * 2 * np.pi
            radius = self.genRadius * np.sqrt(random.uniform(0,1)) # Gets a random distance from the origin to generates
            # Generates cartesian coordinates from angle and radius
            randx = radius * np.cos(angle)+origin.x # origin offsets the generation origin
            randy = radius * np.sin(angle)+origin.y
            randCoordinate = pygame.Vector2(randx, randy)
            # This line appends the coordinate, radius, color, AND assigns each point to be neighbors with all others
            newPoint = Point(randCoordinate, self.pointDrawRadius, self.pointColor, self.dataList)
            screen.addDraw(newPoint, self.drawLayer) 
            self.dataList.append(newPoint)
            # print(n)
        if (self.generateAnomalies):
            for a in range(self.anomalyCount):
                cluster = a%self.clusterCount
                origin = self.clusterList[cluster]
                angle = random.uniform(0,1) * 2 * np.pi # Gets a random angle direction in a circular area

                # This radius will purposefully create data much further away from the center than normal to create some erroneous data
                radius = self.genRadius * np.sqrt(random.uniform(1,2))
                randx = radius * np.cos(angle)+origin.x # origin offsets the generation origin
                randy = radius * np.sin(angle)+origin.y
                randCoordinate = pygame.Vector2(randx, randy)
                newPoint = Point(randCoordinate, self.pointDrawRadius, self.pointColor, self.dataList)
                screen.addDraw(newPoint, self.drawLayer)
                self.dataList.append(newPoint)
                # DEBUG PERFORMANCE
        endTime = time.time()
        print("Data Generated")
        print("\tGeneration Time: ")
        print(endTime-startTime)
    class kMeans:
        """
        Initialization:
            1. Choose a random data point for each cluster starting position (Forgy method)
            2. Generate a new point to represent the cluster centroid
            3. Assign each cluster a unique color
            4. Move to assignment step
        """
        def __init__(self, generatedData: Point, clusterCount, drawLayer):
            # Use Forgy method- Choose a random point in the data
            self.dataList = generatedData
            self.kList :Point # list of points for each k-cluster centroid
            self.step = 0 # Shows how many steps have been called for the kmeans
            for c in range(clusterCount):
                kpos = random.randint(0,len(self.dataList)) # Assign a random data point as the centroid for current cluster
                randColor = random.randint(0,255)
                kcolor = (randColor,randColor,randColor) # Random color for each cluster. This will serve as the 
                k = Point(kpos, 5, kcolor) # Creates a point for the each k-cluster. The neighbors array built in will serve as the closests data to the cluster.
                k.value = []
                for x in range(clusterCount):
                    k.value.append(k.origin.distance_squared_to())
                self.kList.append(k) # Assigns the cluster to a list of clusters
                screen.addDraw(k, drawLayer+1)
        """
        Assignment:
            1. For each point in data points, find the squared distance to each cluster.
            2. Whichever cluster is closests, assign that data to that cluster
            3. Color the data based on the current cluster (to visualize the specific data point's current cluster)
            4. Move to update step
        """
        def assignStep(self):
            self.centerStep()
        
        """
        Center:
            1. Take the average of all vectors in a cluster, reassign the centroid to that point
            2. Move to assigment step
        """
        def centerStep(self):
            self.assignStep()

        def update(self):
            if (self.step % 2 == 0): 
                self.assignStep()
            else:
                self.centerStep()
            self.step = self.step+1

Controller = DataController()

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
            if event.key == pygame.K_1:
                if(Controller): # checks if Controller exists
                    del Controller # Clear previous dataset
                    Controller = DataController() # Regenerate data
            if event.key == pygame.K_2:
                if(Controller): # checks if Controller exists
                    Controller.kMeansManager.update()
    
    screen.draw()

# QUIT
pygame.quit()