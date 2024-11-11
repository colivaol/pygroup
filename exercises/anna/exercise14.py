# Write an average() function that has a numbers parameter. This function returns the statistical average of the list of 
# integer and floating-point numbers passed to the function. While Python’s built-in sum() function can help you solve
# this exercise, try writing the solution without using it.
# Passing an empty list to average() should cause it to return None.

def average(numbers):
  if (len(numbers) == 0):
    return print('None')

  result = numbers[0]
  for number in numbers[1:]:
    result += number 

  total = result / len(numbers)
  return print(total)

average([12, 20, 37])