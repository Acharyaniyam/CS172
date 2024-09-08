#File Name: main.py
#Purpose:   Test the pets, dog and cat classes
#Author:    Adelaida A. Medlock
#Date:      October 16, 2023

# Import needed classes
from pets import *

# The showPetInfo function accepts an object
# as an argument, and calls its makeSound method
def showPetInfo(creature):
    if isinstance(creature, Pet):
        print(creature)
        creature.makeSound() #polymorphism in action
    else:
        print('That is not a pet!')

# the main script
if __name__ == "__main__":
    # Create a few Pets
    myPet = Pet('generic pet', 2)
    snoopy = Dog('beagle', 3)
    fluffy = Cat(3,7)
    
    pets = [myPet, snoopy, fluffy]
    
    # call the function for all pets in the list
    for pet in pets:
        showPetInfo(pet)  # polymorphism
        print()
    
    # What if we pass a non-pet to the function?
    showPetInfo('a string')

