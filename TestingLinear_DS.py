#File:     TestingLinearDS.py
#Purpose:  demo on how to use Python's queue, LifoQueue, 
#          and PriorityQueue classes
#Author:   Adelaida Medlock
#Date:     5/13/2023

# imports to use the data structures as defined in Python
from queue import Queue, LifoQueue, PriorityQueue

# a Customer class
class Customer:
    def __init__(self, name, ticket):
        self.__name = name
        self.__ticket = ticket

    def getName(self):
        return self.__name
    
    def getTicket(self):
        return self.__ticket
    
    def setTicket(self, ticket):
        self.__ticket = ticket
    
    def __str__(self):
        return self.__name + ' has ticket# ' + str(self.__ticket)
    
    def __gt__(self, other):
        return self.__ticket > other.__ticket   

# our main script
if __name__ == "__main__":
    
    # create objects to place in a queue, stack, and priority queue
    julie = Customer('Julie', 18)
    harry = Customer('Harry', 20)
    marie = Customer('Marie', 15)
    
    # using the Python Queue class 
    q = Queue()
    q.put(julie)
    q.put(harry)
    q.put(marie)
    
    print('Servicing customers in the order they arrived (FIFO):')
    while not q.empty():
        print(q.get())
    print()
        
    # using the Python Stack class --> LifoQueue
    s = LifoQueue()
    s.put(julie)
    s.put(harry)
    s.put(marie)
    
    print('Servicing customers starting with last one to arrive')
    while not s.empty():
        print(s.get())
    print()
    
    # using the Python priority queue class --> PriorityQueue
    p = PriorityQueue()
    p.put(julie)
    p.put(harry)
    p.put(marie)
    
    # ticket number is used as the priority: higher ticket 
    # number means lower priority
    print('Servicing customers by priority:')
    while not p.empty():
        print(p.get())
    print()  
    
    # another example of priority queue with simple 
    # built-in data type objects added to the queue
    tasks = PriorityQueue()
    tasks.put((2, 'code'))
    tasks.put((1, 'eat'))
    tasks.put((3, 'sleep'))
    
    print('Here are tasks in the to-do list, in order of priority:')
    while not tasks.empty():
        next_item = tasks.get()
        print(next_item[1])
 