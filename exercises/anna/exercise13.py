# Write two functions named calculateSum() and calculateProduct(). They both have a parameter named numbers, which will be
# a list of integer or floating-point values. The calculateSum() function adds these numbers and returns the sum while
# the calculateProduct() function multiplies these numbers and returns the product. If the list passed to calculateSum()
# is empty, the function returns 0. If the list passed to calculateProduct() is empty, the function returns 1. Since this function
# replicates Python’s sum() function, your solution shouldn’t call.

def calculateSum(numbers):
  if (len(numbers) == 0):
    return print(0)

  result = numbers[0]
  for number in numbers[1:]:
    result += number

  return print(result)

def calculateProduct(numbers):
  if (len(numbers) == 0):
    return print(1)
  
  result = numbers[0]
  for number in numbers[1:]:
    result *= number

  return print(result)

calculateSum([2, 4, 6, 8, 10])
calculateProduct([2, 4, 6, 8, 10])