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

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, maxSpeed, tankCap, currentFuel = 0):
        self.__maxSpeed = maxSpeed
        self.__tankCap = tankCap
        self.__currentFuel = currentFuel
        
    def getMaxSpeed(self):
        return self.__maxSpeed
    def getTankCap(self):
        return self.__tankCap
    def getCurrentFuel(self):
        return self.__currentFuel
        
    def refillTank(self):
        self.__currentFuel = self.__tankCap
        
    @abstractmethod
    def calcNumMilesOnFullTank(self):
        pass
    @abstractmethod
    def move(self):
        pass
    
    def __str__(self):
        myStr = 'Max Speed: ' + str(self.__maxSpeed) + 'mph.\n'
        myStr += 'Tank Capacity: ' + str(self.__tankCap) + 'gallons.\n'
        myStr += 'Current Fuel: ' + str(self.__currentFuel) + 'gallons.\n'
        return myStr
    
class Boat(Vehicle):
    __milesPerGallon = 4
    def __init__(self, maxSpeed, tankCap, hull, currentFuel = 0):
        super().__init__(maxSpeed, tankCap, currentFuel)
        self.__hull = hull
        
    def getHull(self):
        return self.__hull
        
    def calcNumMilesOnFullTank(self):
        totalMiles = super().getTankCap() * Boat.__milesPerGallon
        return totalMiles
    
    def move(self):
        return('Sailing!!')
    
    def __str__(self):
        myStr = 'Boat:\n' + super().__str__() + '\n'
        myStr += 'Hull type: ' + self.__hull + '\n'
        myStr += 'Miles on Full Tank: ' + str(self.calcNumMilesOnFullTank()) + ' miles.'
        return myStr
    
if __name__ == '__main__':
    cruiser = Boat(50, 30, 'V-Bottom')
    print(cruiser)
    
    print('After refueling')
    print('Boat tank level: ', cruiser.getTankCap(), 'gallons.')
    
    print('We are traveling now')
    print('We are', cruiser.move(), 'in our cruiser boat.')