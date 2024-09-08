class Student:
    
    #add static / class attribute keep track of the current ID number
    __currentID = 1000
    
    
    #constructor
    def __init__(self, name):
        self.__name  = name
        self.__totalCredits = 0.0
        self.__qualityPoints = 0.0
        self.__ID = Student.__currentID
        Student.__currentID += 1
        
    #getters
    def getName(self, name):
        return self.__name
    
    def getTotalCredits(self):
        return self.__totalCredits
    
    def getStudentID(self):
        return self.__ID
    
    def getGPA(self):
        if self.__totalCredits ==0.0:
            return 0.0
        else:
            return self.__qualityPoints / self.__totalCredits
    #setters
    def earnCredits(self, crd, grade): #crd is the number of credit for a course, grade is the letter grade earned
        grade = grade.upper()
        if grade == 'A':
            qPoints = 4.0
        if grade == 'B':
            qPoints = 3.0
        if grade == 'C':
            qPoints = 2.0
        if grade == 'D':
            qPoints = 1.0
        else:
            qPoints = 0.0
            
        self.__totalCredits = self.__totalCredits + crd
        self.__qualityPoints = self.__qualityPoints + (qPoints + crd)
        
    #helper method ti display students
    def printStudent(self):
            print("Student's name : ", self.__name)
            print('Student ID: ', self.__ID)
            print("Credits earner : ", self.__totalCredits)
            print("Quality points : ", self.__qualityPoints)
            print('GPA: ', round(self.getGPA(), 2))
            
            #any static method to know wht is the next available ID number
    @staticmethod #put this when you are getting a static member
    def getNextIDAvailable():
            return Student.__currentID
        
      #OPERATOR OVERLOADING AND SPECIAL METHODS
        # __str__ to use with print
    def __str__(self):
        myStr = "Student's name: " + self.__name + '\n'
        myStr += "Student's ID: " + str(self.__ID) + '\n'
        myStr += "Credits Earned: " + str(self.__totalCredits) + '\n'
        myStr += "Student's GPA:" + str(self.getGPA()) + '\n'
        return myStr
    
    #comparison operators == __eq__, != __ne__, > __gt__, < __lt__, >= __ge__, <= __le__
    def __eq__(self, other):
        name = self.__name == other.getName()
        idNumber = self.__ID == other.getStudentID()
        creditsEarned = self.__totalCredits == other.getTotalCredits()
        gpa = self.getGPA() == other.getGPA()
        return name and idNumber and creditsEarned and gpa
    
    def __ne__(self, other):
        name = self.__name != other.getName()
        idNumber = self.__ID != other.getStudentID()
        creditsEarned = self.__totalCredits != other.getTotalCredits()
        gpa = self.getGPA() != other.getGPA()
        return name and idNumber and creditsEarned and gpa
    
    def __gt__ (self, other): #for sorting them in alphabetical order, we can see if one student is greater than the other based on the criteria of name
        return self.__name >other.getName()
        
