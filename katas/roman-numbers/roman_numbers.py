def roman_numbers_conversion(number):
    diccionario = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    if number in diccionario:
        return(diccionario.get(number))
    else:
        temp_array_number = []
        temp_array_symbol = []
        result = ''

        for i in list(diccionario.keys()):
            while number >= i or sum(temp_array_number) < number:
                print(f'i: {i}')
                result += diccionario.get(i)
                temp_array_number.append(i)
                print(f'Array: {temp_array_number}')
                print(f'Suma array: {sum(temp_array_number)}')
                temp_array_symbol.append(diccionario.get(i))
                break

        # if number//max(temp_array_number) == 0:

        print(f'Result: {result}')


if __name__ == '__main__':
    roman_numbers_conversion(14)