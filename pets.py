#File Name: pets.py
#Purpose:   The Pet class represents a generic pet
#           A pet belongs to a species and it has an age in years
#           A pet makes a sound. A pet gets older every year
#Author:    Adelaida A. Medlock
#Date:      October 16, 2023

# Parent Class
class Pet:
    # constructor 
    def __init__(self, species, age = 0):
        self.__species = species
        self.__age = age

    # getters
    def getSpecies(self):
        return self.__species
    
    def getAge(self):
        return self.__age
    
    # setters
    def haveBirthday(self):
        self.__age = self.__age + 1   

    # The make_sound method is the pet's way of making a generic sound
    def makeSound(self):
        print('Grrrrr')
       
    # overloading the print operator
    def __str__(self):
        myStr = 'A ' + str(self.__age) + '-year old ' + self.__species
        return myStr
    
    # overloading the __eq__ operator
    def __eq__(self, other) :
        species = self.__species == other.getSpecies() 
        age = self.__age == other.getAge()
        return species and age

# Derived classes

# The Dog class represents a dog, which is a type of pet
# Every dog has a breed and likes to play catch
class Dog(Pet):
    # constructor
    def __init__(self, breed, age = 0):
        super().__init__('dog', age) #calling constructor from parent class
        self.__breed = breed   #additional attribute
    
    # getters and setters
    def getBreed(self):
        return self.__breed
 
    # additional behavior
    def playCatch(self) :
        print('Running and catching the stick. Good doggie!')
    
    # override makeSound
    def makeSound(self):
        print('Woof! Woof!')
        
    # override __str__
    def __str__(self):
        myStr = super().__str__() +  ', ' + self.__breed
        return myStr

    # override the __eq__ operator
    def __eq__(self, other) :
        return (self.__breed == other.getBreed() and super().__eq__(other))


# The Cat class represents a cat, which is a type of pet
# Every cat has a number of lives left and likes to catch mice
class Cat(Pet):
    # constructor
    def __init__(self, age = 0, lives = 9):
        super().__init__('cat', age) #calling constructor from parent class
        self.__lives = lives  #additional attribute 
    
    # getters and setters
    def getLives(self):
        return self.__lives
    
    def updateLives(self):
        if self.__lives > 0:
            self.__lives -= 1
        else :
            self.__lives = 0
     
    # additional behavior
    def catchMouse(self) :
        print('Here goes the hunter! Good kitty!')
    
    # override makeSound
    def makeSound(self):
        print('Meow')
        
    # override __str__
    def __str__(self):
        myStr = super().__str__() +  ', with '
        myStr +=  str(self.__lives) + ' lives left.'
        return myStr
    
    # override the __eq__ operator
    def __eq__(self, other) :
        return (self.__lives == other.getLives() and super().__eq__(other))
    