class Pair:
    def __init__(self, a = 1, b = 1):
        self.__a = a #simulate that this is at index 0
        self.__b = b #simulate that this is at index 1
        
        # getters
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    #overloaded operartors
    
    #the print operator __str__
    
    def __str__(self):
        return '(' + str(self.__a) + ',' + str(self.__b) + ')'
    
    #the boolean operator
    def __eq__(self, other):
        first = self.__a == other.getA()
        second = self.__b == other.getB()
        return first and second
    
    def __ne__(self, other):
        first = self.__a != other.getA()
        second = self.__b != other.getB()
        return first and second
    
    # the subscript operator [  ]
    #using [] as a accessor/ inspector / getter
    def __getitem__(self, index):
        if index == 0:
            return self.__a
        elif index == 1:
            return self.__b
        else:
            raise Exception('Invalid Index')
        
        
# Arthemetic Operarators : + - * / // **
    # __add__ to be able to use  + (p3 = p1 + p2)
    def __add__(self, other):
        a = self.__a + other.getA()
        b = self.__a + other.getB()
        return Pair(a,b)
    
    # overload __sub__ to be able to use  - (p3 = p1 - p2)
    def __sub__(self, other):
        a = self.__a - other.getA()
        b = self.__a - other.getB()
        return Pair(a,b)
    
    #overload __mul__ ot be able to use * (p3 = p1* p2)
    def __mul__(self, factor):
        a = self.__a * factor
        b = self.__a * factor
        return Pair(a,b)
    
    #overload __floordic__to be able to use // (p3 = p1 // p2)
    def __floordiv__(self, other):
        a = self.__a // self.__b
        b = other.getA() // other.getB()
        return pair(a,b)
        
        
    