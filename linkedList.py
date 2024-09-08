#File Name:  linkedList.py
#Purpose:    Node and LinkedList implementations
#Author:     Niyam Acharya
#Date:       November 29, 2023

# The Node class - same as lecture notes
class Node():
    # constructor
    def __init__(self, item, next = None):
        self.__data = item
        self.__next = next
    
    # getters
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    #setters
    def setData(self, d):
        self.__data = d

    def setNext(self, n):
        self.__next = n

    #overloaded operator __str__ to support print()
    def __str__(self):
        return str(self.__data) + " --> " + str(self.__next)
    

# Linked List Class
class LinkedList():
    # constructor
    def __init__(self):
        self.__head = None
        
    # NEW getter: get the head of the list, or first node
    def getHead(self):
        return self.__head
        
    # setter: add a node at the end of the linked list
    def append(self, data):
        newNode = Node(data)
        
        if self.__head == None:       
            self.__head = newNode
        else: 
            current = self.__head
            while current.getNext() != None: 
                current = current.getNext()
            current.setNext(newNode)
                       
    #overloaded operators
    # __str__ used to support print() 
    def __str__(self):    
        myStr = ''
        current = self.__head
        
        if current == None:
            myStr += 'Empty linked list'
        else :
            while current != None:
                myStr += str(current.getData()) + ' --> '
                current = current.getNext()
            myStr += 'None'
        return myStr
    
    # __len__ used to support len()
    def __len__(self):    
        if self.__head == None: 
            return 0
        
        current = self.__head 
        counter = 1
        
        while current.getNext() != None: 
            counter += 1
            current = current.getNext()
        return counter
