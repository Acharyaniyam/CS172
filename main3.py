#Programmer = Niyam Acharya
#Program date = October 10, 2023
#User Name = nka42 (1410667)
#Purpose: Create a file main.py that reads in a text file and prints out any word that is not found in the spelling dictionary.

from spellchecker import Spellchecker

correctWords = 0
incorrectWords = 0

def get_file():
    while True:
        try:
            fileName = input('Enter the name of the file to read: ')
            with open(fileName, 'r') as file:
                return fileName
            break    
        except FileNotFoundError:
            print('Could not open file. ')
            
SP = Spellchecker('/Users/niyamacharya/Documents/DREXEL Fall 2023/english_words.txt')

callFile = get_file()

try:
    with open(callFile, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Could not open the file.")
    exit()
    
lines = text.split('\n')

print('Welcome to Text File Spellchecker.')

line_num = 1

for line in lines:
    words = line.split()
    
    
    for word in words:   
        cleanWord = word.strip(".,!?\"'()[]{}")
        lowerWord = cleanWord.lower()
        
        if not SP.check(lowerWord):
            print(f"Possible Spelling Error on line {line_num}: {cleanWord}")
            incorrectWords += 1
        else:
            correctWords += 1
        
    line_num += 1
    
    
total_words = correctWords + incorrectWords
correct_percentage = (correctWords / total_words) * 100

print('{} words passed spell checker.'.format(total_words))
print('{} words failed spell checker.'.format(incorrectWords))
print('{:.2f}% of the words passed.'.format(correct_percentage))