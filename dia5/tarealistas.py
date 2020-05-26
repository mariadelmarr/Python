# Cree un programa en Python que llene una lista con números indicados por el usuario.
# Cuando la lista ya está llena, debe buscar el número mayor de la lista.
# Debe imprimir el resultado y la lista.
lista = []
cantidad = int(input('Indique la cantidad de numeros que desea ingresar: '))

while cantidad > 0:
    numero = float(input('Ingrese el numero: '))
    lista.append(numero)
    cantidad = cantidad - 1
    mayor = max(lista)

print('El resultado es: '+str(lista)+'y el numero mayor es: '+str(mayor))