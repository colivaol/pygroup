# Write a getChessSquareColor() function that has parameters column and row. The function either returns 'black' 
# or 'white' depending on the color at the specified column and row. Chess boards are 8 x 8 spaces in size, 
# and the columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. If the arguments
# for column or row are outside the 0 to 7 range, the function returns a blank string.

def getChessSquareColor(column, row):
  if (column >= 0 and column <= 7) and (row >=0 and row <=7):
    if (column % 2 == 0 and row % 2 == 0) or (column % 2 != 0 and row % 2 != 0):
      print('white')
    else:
      print('black')
  else: 
    print('')
   


getChessSquareColor(0, 0)
getChessSquareColor(1, 0)
getChessSquareColor(0, 1)
getChessSquareColor(7, 7)
getChessSquareColor(0, 8)
getChessSquareColor(2, 9)