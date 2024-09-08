#Simple Maze Class
#Programmer = Niyam Acharya (nka42)
#Program date = 16th November, 2023
#Drexel University
#CS 172
#Description = The Room module provides the Room class, representing individual rooms within a maze. Each Room object contains a
#              description and connections to other rooms in different directions (north, south, east, west). It allows setting and
#              getting descriptions, as well as linking rooms in various directions to create the maze structure.

class Room:
    #Constructor sets the description
    #And all four doors should be initially set to None
    def __init__(self, descr):
        self.description = descr
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        
        
    #Accessors
    #Return the correct values
    def __str__(self):
        return self.description
    
    def getNorth(self):
        return self.north
    
    def getSouth(self):
        return self.south
    
    def getEast(self):
        return self.east
    
    def getWest(self):
        return self.west
    
    def setDescription(self, d):
        self.description = d
    
    def setNorth(self, n):
        self.north = n
    
    def setSouth(self, s):
        self.south = s
    
    def setEast(self, e):
        self.east = e
        
    def setWest(self, w):
        self.west = w
    