#Programmer = Niyam Acharya nka42
#Program date = 16th November, 2023
#CS 172 - Maze Game
#Drexel University 2018
#Description= This module contains the Maze class, which represents a maze structure. The Maze class handles the navigation within
#             the maze, keeping track of rooms, connections, and the player's current position. It allows movement through the maze
#             using directional methods and checks whether the player has reached the exit.

class Maze:
    #Inputs: Pointers to start room and exit room
    #Sets current to be start room
    def __init__(self, st = None, ex = None):
        # TODO 
        #Room the player starts in
        
        #If the player finds this room they win
        # TODO
        
        #What room is the player currently in
        # TODO
        self.start = st
        self.exit = ex
        self.current = st
    #Return the room the player is in (current)
    def getCurrent(self):
        return self.current

    #The next four methods all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new room (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
         if self.current.getNorth():
            self.current = self.current.getNorth()
            print(self.current)
            return True
         else:
            print("Direction invalid, try again.")
            return False
    
    def moveSouth(self):
        if self.current.getSouth():
            self.current = self.current.getSouth()
            print(self.current)
            return True
        else:
            print("Direction invalid, try again.")
            return False
        
    def moveEast(self):
        if self.current.getEast():
            self.current = self.current.getEast()
            print(self.current)
            return True
        else:
            print("Direction invalid, try again.")
            return False
    
    def moveWest(self):
        if self.current.getWest():
            self.current = self.current.getWest()
            print(self.current)
            return True
        else:
            print("Direction invalid, try again.")
            return False
    
    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        return self.current == self.exit

    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start room
    def reset(self):
        self.current = self.start