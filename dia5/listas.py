#  primos = [2, 3, 5, 7, 11, 13]
# print(primos)
# primos.append(17) #para agregar datos a la lista
# print(primos[2:5])#para solicitar a partir del segundo indice hasta, hasta el parametro 5

# #Indices

#  name = 'Maria'
# print(name[3])


# print(name[-1])#para buscar el ultimo digito del indice

# label = primos + name
# print(label)

#practica de listas, sumar
add = True
numbers = []
while add:
    number = int(input('Ingrese un numero: '))#pido los numeros
    numbers.append(number)
    add = True if input('Desea continuar? S/N ') == 'S' else False
i = 0
total = 0
while i < len(numbers): #los recorro y los sumo
    total += numbers[i]
    i += 1
print('El total es:  ', total)
print(numbers)