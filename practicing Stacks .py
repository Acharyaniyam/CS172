from queue import LifoQueue

class Stack:
    def __init__(self):
        self.__list = []
        
    def __len__(self):
        return len(self.__list)
    
    def __str__(self):
        if len(self.__list) == 0:
            print('Empty List')
        else:
            s = ''
            for i in range(0, len(self.__list)):
                s = s + str(self.__list[i]) + '\n'
            return s
        
    def put(self, item):
        self.__list.insert(0, item)
        
    def get(self):
        a = self.__list.pop(0)
        return a
    
    def clear(self):
        self.__list = []
        
    def isEmpty(self):
        if self.__list == []:
            return True
        else:
            return False
        
    def peek(self):
        return self.__list[0]
    
    
myStack = Stack()
myStack.put('Jose')
myStack.put('Jeremy')
myStack.put('Luis')

if not myStack.isEmpty():
    print("My list is as follows:")
    print(myStack)

    myStack.get()
    print('List after dequeue:')
    print(myStack)

    print('Next in list after dequeue:')
    print(myStack.peek())

    
        
        
            