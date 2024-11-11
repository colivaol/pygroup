# You will write three functions for this exercise. First, write a writeToFile() function with two parameters for the 
# filename of the file and the text to write into the file. Second, write an appendToFile() function, which is identical 
# to writeToFile() except that the file opens in append mode instead of write mode. Finally, write a readFromFile()
# function with one parameter for the filename to open. This function returns the full text contents of the file as a string.

def writeToFile(file, text): 
  f = open(file, 'w')
  f.write(text)
  f.close()

def appendToFile(file, text): 
  f = open(file, 'a')
  f.write(text)
  f.close()


def readFromFile(file):
  f = open(file, 'r')
  print(f.read())
  f.close()
  
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt')