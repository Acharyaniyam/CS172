from student import Student
from random import randint

if __name__ =='main':
    
    s = Student('Sam')
    t = Student('Tom')
    
    for i in range(0,5):
        gradeCode = ord('A') + randint(0,3)
        grade = chr(gradeCode)
        s.earnCredits(3.0, grade)
        gradeCode = ord('A') + randint(0,3)
        grade = chr(gradeCode)
        t.earnCredits(3.0, grade)
        
    print("Joe's GPA: ", s.getGPA())
    print("Jane's GPA: ", t.getGPA())
    
    print()
    print(s)
    print()
    print(t)
        
    print('\n Comparing two student objects to see if they hold the same values')
    if s == t:
        print('Both the objects hold the same values')
        