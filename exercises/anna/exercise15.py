# Write a median() function that has a numbers parameter. This function returns the statistical median of the numbers list. 
# The median of an odd-length list is the number in the middlemost number when the list is in sorted order. If the
# list has an even length, the median is the average of the two middlemost numbers when the list is in sorted order.
# Feel free to use Python’s built-in sort() method to sort the numbers list.
# Passing an empty list to mode() should cause it to return None.

def median(numbers):
  if (len(numbers) == 0):
    return print('None')
  
  # for number in range(len(numbers)):
  #  for item in range(len(numbers)-1-number):
  #    if numbers[item] > numbers[item + 1]:
  #      numbers[item], numbers[item + 1] = numbers[item + 1], numbers[item]
  numbers.sort()

  if (len(numbers) % 2 == 0):
    middle = len(numbers) // 2
    return print((numbers[middle-1] + numbers[middle]) // 2)
    
  else:
    middle = len(numbers) // 2
    return print(numbers[middle])

median([1, 2, 3])