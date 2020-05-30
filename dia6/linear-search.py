chars = ['d', 't', 'a', 'r', 'z', 'y', 'x', 'b']
char = input('Que quiere buscar? ')

# Recorro la lista para buscar un indice
for i in range(len(chars)):
    if chars[i] == char:
        print('Encontrado en el indice: ', i)
        break #frena el for
else:
    print('No fue encontrado')
print('fin...')

