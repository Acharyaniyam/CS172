#CS 172 - Lab 3 Start Code
# Name = Niyam Acharya User Name = nka42(14510667)

class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self, a, b):
        self.__num = a
        self.__den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.__den == 1 :
            return str(self.__num)
        else:
            return str(self.__num) + "/" + str(self.__den)
            
    #Get the Numerator
    def getNum(self):
        return self.__num
        
    #Get the Denominator
    def getDen(self):
        return self.__den
        
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.__num / self.__den
        
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.__num, self.__den)
        self.__num = self.__num // x
        self.__den = self.__den // x
        
    #Find the GCD of a and b
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    #Compare two fraction objects
    def __eq__(self,other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()
    
    
    
    #Complete these methods in lab
    def __add__(self, other):
        newNum = ((self.__num * other.__den) + (other.__num * self.__den)) 
        newDen = (self.__den * other.__den)
        return Fraction(newNum , newDen)
        
    def __sub__(self, other):
        newNum = ((self.__num * other.__den) - (other.__num * self.__den)) 
        newDen = (self.__den * other.__den)
        return Fraction(newNum , newDen)
        
    def __mul__(self, other):
        newNum = (self.__num * other.__num)
        newDen = (self.__den * other.__den)
        return Fraction(newNum, newDen)
        
    def __truediv__(self, other):
        newNum = (self.__num * other.__den)
        newDen = (self.__den * other.__num)
        return Fraction(newNum, newDen)
        
    def __pow__(self, k):
        if k == 0:
            return Fraction(1,1)
        elif k > 0:
            newNum = self.__num ** k
            newDen = self.__den ** k
            return Fraction(newNum, newDen)
        elif k < 0:
            newNum = self.__den ** abs(k)
            newDen = self.__num ** abs(k)
            return Fraction(newNum, newDen)
        
        
            
    
    