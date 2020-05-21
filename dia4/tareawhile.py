number = int(input('Ingrese un numero: '))

while number > 0:
    row = ''
    temp = number
    while temp > 0:
        row = row + str(temp) + ''
        temp = temp - 1
    print(row)
    number = number - 1
print('Ciao')
