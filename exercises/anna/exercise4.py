# You will write four functions for this exercise. The functions area() and perimeter() have length and width 
# parameters and the functions volume() and surfaceArea() have length, width, and height parameters. These functions 
# return the area, perimeter, volume, and surface area, respectively.

def area(length, width): 
  return print(length * width)

def perimeter(length, width): 
  return print(length + width + length + width)

def volume (height):
  return print(length * width * height)

def surfaceArea (length, width, height):
  return print((length * width * 2)+(length * height * 2)+(width * height * 2))

area(10,10)
perimeter(10,10)
volume(10,10,10)
surfaceArea(10,10,10)