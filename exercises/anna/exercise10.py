# Write a findAndReplace() function that has three parameters: text is the string with text to be replaced, oldText 
# is the text to be replaced, and newText is the replacement text. Keep in mind that this function must be case-sensitive:
# if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG JONESY' won’t be replaced.

def findAndReplace(text, oldText, newText): 
  replacedText = ''
  i = 0
  while i < len(text):
    if (text[i:i + len(oldText)] == oldText):
      print('1: ',replacedText)
      replacedText += newText
      print('2: ',replacedText)
      i+=len(oldText)
    else: 
      replacedText += text[i]
      i+= 1
  return replacedText

print(findAndReplace('the fox and su puta madre y the fox again', 'fox', 'dog')) # 'dogdog'
##findAndReplace('The fox and the cat and the fox', 'fox', 'dog') # 'The dog
##findAndReplace('fox', 'fox', 'dog') # 'dog'
##findAndReplace('Firefox', 'fox', 'dog') # 'Firedog'
##findAndReplace('The Fox and fox.', 'fox', 'dog') # 'The Fox and dog.'