#Programmer = Niyam Acharya (nka42)
#Program date = 16th November, 2023
#Description = This program simulates a maze navigation system using linked lists. It consists of Room and Maze classes to represent
#              rooms and the maze structure, along with a play function for user interaction. Users can navigate through the maze by
#              choosing directions (north, south, east, west) and attempt to reach the exit.

from maze import Maze
from room import Room

def play(my_maze):
#Play a game
    while not my_maze.atExit():
## TODO: Get direction from user
        print(my_maze.getCurrent())
        direction = input("Enter direction to move (north, south, east, west, restart): ").lower()
        if direction == 'north':
            my_maze.moveNorth()
        elif direction == 'south':
            my_maze.moveSouth()
        elif direction == 'east':
            my_maze.moveEast()
        elif direction == 'west':
            my_maze.moveWest()
        elif direction == 'restart':
            my_maze.reset()
            print("You went back to the start!")
        else:
            print("Invalid direction, try again.")
## TODO: Based on choice do what was asked.
    print("You found the exit!")


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE
room1 = Room("Room1")
room2 = Room("Room2")
room3 = Room("Room3")

room1.setEast(room2)
room2.setWest(room1)
room2.setNorth(room3)
room3.setSouth(room2)

SIMPLE_MAZE = Maze(room1, room3)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE

roomA = Room("Room with a Painting")
roomB = Room("Library Room")
roomC = Room("Kitchen Area")
roomD = Room("Secret Chamber")
roomE = Room("Art Gallery")
roomF = Room("Exit Room")

roomA.setWest(roomB)
roomB.setEast(roomA)
roomB.setWest(roomC)
roomC.setEast(roomB)
roomC.setWest(roomD)
roomD.setEast(roomC)
roomD.setNorth(roomE)
roomE.setSouth(roomD)
roomE.setEast(roomF)
roomF.setWest(roomE)

INTERMEDIATE_MAZE = Maze(roomA, roomF)


if __name__=="__main__":
## TODO: Define this play function above and run on your INTERMEDIATE_MAZE
    play(INTERMEDIATE_MAZE)