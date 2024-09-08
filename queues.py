#File:     queues.py
#Purpose:  implement our  version of a queue (FIFO)
#Author:   Adelaida A. Medlock
#Date:     11/04/2023

# len(), str(), isEmpty(), peek(), enqueue()/put(), 
# dequeue()/get(), clear()

class MyQueue():
    # constructor
    def __init__(self):
        self.__theList = []
    
    # overloaded operators
    def __str__(self):
        if len(self.__theList) == 0:
            return "Empty Queue"
        s = ''
        for i in range(0, len(self.__theList)) :
            s = s + str(self.__theList[i]) + '\t'
        return s
    
    def __len__(self):
        return( len(self.__theList) )
    
    # setters
    # add elements to the end of the queue
    def put(self, item):
        self.__theList.append(item)
    
    # remove elements from the front of the queue
    def get(self):
        a = self.__theList.pop(0)
        return a
    
    # remove all elements from queue
    def clear(self):
        self.__theList = []
    
    # getters 
    # check (but not remove) the element at the front
    def peek(self):
        return self.__theList[0]
    
    # check if queue is empty    
    def isEmpty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False

# Testing our queue implementation
if __name__ == '__main__' :
    
    print('Testing our queue implementation')
    print('--------------------------------')
    
    # create a display a new queue
    line = MyQueue()
    print('Here is our empty queue:')
    print(line)
    
    # enqueue a few items
    line.put('Mary')
    line.put('John')
    line.put('Rose')
    line.put('Bob')
    
    # process the queue
    if not line.isEmpty() :
        print('\nHere is our queue after adding a few people:')
        print(line)
        
        print('There are', len(line), 'people in the queue.\n')
    
        # dequeue an item from the queue
        first = line.get()  # get first item from the queue
        print('First in line:', end = ' ')
        print(first)
        
        second = line.get()
        print('Second in line:', second)
        
        # peek to see which is the item at the front of queue
        print('After dequeueing 1st person, next in line is:', end = ' ')
        print(line.peek())
    
        print('\nHere is our queue after dequeing first and second person:')
        print(line)
        print()
        
    # using a while loop
    print("Using a loop")
    while not line.isEmpty():
        print(line.get(), end = ' ')
        
    
