# Write a mode() function that has a numbers parameter. This function returns the mode, or most frequently appearing number, of the list of 
# integer and floating-point numbers passed to the function.
import random


def mode(numbers): 
  if len(numbers) == 0:
    return print('None')
  numberCount = {}
  patata = random.seed(8)
  print('patata', patata)
  mostFreqNumber = None
  mostFreqNumberCount = 0

  for number in numbers:
    if number not in numberCount:
      numberCount[number] = 1
    else: 
      numberCount[number] += 1
  
    if numberCount[number] >= mostFreqNumberCount:
      mostFreqNumber = number
      mostFreqNumberCount = numberCount[number]
    
  return print(mostFreqNumber)


mode([1, 2, 2, 3, 3, 4]) # == 4