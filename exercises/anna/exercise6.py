# In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinalSuffix()
# function with an integer parameter named number and returns a string of the number with its ordinal suffix. 
# For example, ordinalSuffix(42) should return the string '42nd

def ordinalSuffix(number): 
  strnumber = str(number)
  lastNumber = strnumber[len(strnumber)-1:]
  lastTwoNumbers = strnumber[len(strnumber)-2:]
  if len(strnumber) > 2 and lastTwoNumbers in ('11', '12', '13'):
    return strnumber + 'th'
  elif lastNumber in '1':
    return strnumber + 'st'
  elif lastNumber in '2':
    return strnumber + 'nd'
  elif lastNumber in '3':
    return strnumber + 'rd'
  else: 
    return strnumber + 'th'

print(ordinalSuffix(3))