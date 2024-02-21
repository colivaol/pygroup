# Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this 
# temperature in degrees Fahrenheit. Then write a function named convertToCelsius() with a degreesFahrenheit parameter 
# and returns a number of this temperature in degrees Celsius.
def convertToFahrenheit(degreesCelsius):
  return print(degreesCelsius * (9 / 5) + 32)


def convertToCelsius(degreesFahrenheit):
  return print((degreesFahrenheit - 32) * (5 / 9))


#convertToFahrenheit(100)
#convertToCelsius(0)

degreesCelsius = int(input("Introduce los grados: "))
convertToFahrenheit(degreesCelsius)

# Esto es para pedirlo por consola con 'python.exe .\exercise2.py'
if __name__ == '__main__':
  convertToFahrenheit(int(input("Introduce los grados: ")))
  convertToCelsius(int(input("Introduce los grados: "))) 


# Otra forma de hacerlo por consola, abrimos python > import exercise2 > exercise2.convertToFahrenheit(100)