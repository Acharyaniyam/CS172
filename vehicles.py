#File Name: vehicles.py
#Purpose:   Demo for abstract classes
#           Vehicle represents a generic vehicle that runs on fuel
#           Boat and Airplane are derived from Vehicle
#
#Details:  Every Vehicle has a maximum speed that it can reach
#          and a tank capacity. A Vehicle also has a current level
#          of fuel in the tank.
#          Maximum speed and tank capacity must be provided at
#          instantion time. If no data is provided for current
#          tank level, assume it's 0.
#          A tank can be refilled when needed, and in that case,
#          it will be refilled at full capacity
#          There are 2 abstract methods for this class:
#          calcNumMilesOnFullTank() and move()
#
#          A Boat is a type of Vehicle that has a hull type.
#          The hull type must be provided at instantion time
#          and cannot be changed. Additionally the Boat class has
#          an static attribute __milesPerGallon that's used to
#          calculate the number of miles that can be traveled
#          on a full tank. Its value is 4 miles/gallon
#
#          An Airplane is a type of Vehicle that has an engine type.
#          The engine type must be provided at instantion time
#          and cannot be changed. Additionally the Airplane class has
#          an static attribute __milesPerGallon that's used to
#          calculate the number of miles that can be traveled
#          on a full tank. Its value is 0.20 miles/gallon
#
#Author:   Adelaida A. Medlock
#Date:     October 16, 2023

# Import the module needed to create abstract classes
from abc import ABC, abstractmethod  

# Parent Abstrac Class
class Vehicle(ABC):
    # constructor
    def __init__(self, maxSpeed, tankCapacity, currentLevel = 0):
        self.__maxSpeed = maxSpeed
        self.__tankCapacity = tankCapacity
        self.__tankLevel = currentLevel
    
    # getters
    def getMaxSpeed(self):
        return self.__maxSpeed
    
    def getTankCapacity(self):
        return self.__tankCapacity
    
    def getTankLevel(self):
        return self.__tankLevel
    
    # setters
    def refillTank(self):
        self.__tankLevel = self.__tankCapacity
    
    # abstract methods
    # to be implemented by the derived classes
    @abstractmethod
    def calcNumMilesOnFullTank(self): 
        pass
    
    @abstractmethod
    def move(self): 
        pass
    
    # overloaded operators
    def __str__(self):
        vStr =  'Max Speed:    ' + str(self.__maxSpeed) + ' mph.\n'
        vStr += 'Tank Capacity:  ' + str(self.__tankCapacity) + ' gallons.\n'
        vStr += 'Current Fuel: ' + str(self.__tankLevel) + ' gallons.\n'
        return vStr
        
        
# Derived classes    
class Boat(Vehicle):
    
    __milesPerGallon = 4
    
    # constructor
    def __init__(self, maxSpeed, tankCapacity, hullType, currentLevel = 0):
        super().__init__(maxSpeed, tankCapacity, currentLevel)
        self.__hullType = hullType
        
    # getters
    def getHullType(self):
        return self.__hullType

    # implement the abstract methods
    def calcNumMilesOnFullTank(self):   
        return (super().getTankCapacity() * Boat.__milesPerGallon)
    
    def move(self):   
        return "Sailing"
        
    # overloaded operators
    def __str__(self):
        vStr =  super().__str__()
        vStr += 'Hull type:    ' + self.__hullType + '\n'
        vStr += 'Miles on Full Tank: ' + str(self.calcNumMilesOnFullTank()) 
        vStr += ' miles.\n'
        return vStr
    
    
class Airplane(Vehicle):
    
    __milesPerGallon = 0.20
    
    # constructor
    def __init__(self, mXSpeed, tankCapacity, engineType, currentLevel = 0):
        super().__init__(mXSpeed, tankCapacity, currentLevel)
        self.__engineType = engineType
        
    # getters
    def getEngineType(self):
        return self.__engineType
        
    # implement the abstract methods
    def calcNumMilesOnFullTank(self):   
        return (super().getTankCapacity() * Airplane.__milesPerGallon)
    
    def move(self):   
        return "Flying"

    # overloaded operators
    def __str__(self):
        vStr =  super().__str__()
        vStr += 'Engine type:  ' + self.__engineType + '\n'
        vStr += 'Miles on Full Tank: ' + str(self.calcNumMilesOnFullTank()) 
        vStr += ' miles.\n'
        return vStr
    

if __name__ == "__main__":
    # create some concret objects
    cruiser = Boat(50, 30, 'V-Bottom')
    plane = Airplane(550, 3500, 'Turbojet', 1500)
    
    # print objects
    print('Boat:')
    print(cruiser)
    print('Plane:')
    print(plane)
    
    # refuel
    cruiser.refillTank()
    plane.refillTank()
    
    # check tank
    print('After refueling')
    print('Boat tank level: ', cruiser.getTankLevel(), 'gallons.')
    print('Plane tank level:', plane.getTankLevel(), 'gallons.')
    print()
    
    # travel somewhere
    print('We are traveling now')
    print('We are', cruiser.move(), 'in our cruiser boat.')
    print('We are', plane.move(), 'for a vacation on the other side of the pond!')
    