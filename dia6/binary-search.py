numbers = [2, 4, 7, 34, 76, 80, 91]
# numbers.sort(True)
# print(str(numbers))
number = int(input('Que numero desea buscar? '))

start = 0
end = len(numbers)

while start <= end:
    middle = (start + end) // 2
    if numbers[middle] == number:
        print('Encontrado en el indice: ', middle)
        break
    elif numbers[middle] > number:
        end = middle - 1
    else:
        start = middle + 1
else:
    print('No fue encontrado')
print('fin...')

# character = 'a'
# number = ord(character)
# print(number)

# number = 98
# character = chr(number)
# print(character)






