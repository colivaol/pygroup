# Write a printASCIITable() function that displays the ASCII number and its corresponding text character, from 32 to 126.

def printASCIITable():
  for number in range(32, 127):
    print(number,(chr(number)))


printASCIITable()