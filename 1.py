"""
Word counter
"""

fileName =  input("Enter a file name with extension : ")

with open(fileName, 'r') as file:
    data = file.read()

wordList = data.split()
print("Number of words in the file: ", len(wordList))