# # Ordenar elementos de una lista

mylist = ['tuv', 'fgh', 'abc', 'klm', 'opq']
list2 = [3, 5, 2, 4, 1]

print('Se ordenaran las listas: ', mylist, ',', list2, 'usando la funcion: ".sort"')

mylist.sort()#ordena mylist conforme al orden del abecedario
list2.sort()#ordena list2 con respecto al orden de los numeros

print(mylist)
print(list2)
print('')

# Eliminar un elemento de la lista
print('De la siguiente lista: ', mylist, 'eliminaremos el indice: ')
removed = mylist.pop(1) #elimina el elemento que se encuentra en el indice 1, puesto que si no se indica el indice que se 
#desea eliminar, se eliminara el ultimo
print('->', removed)
print('El resultado es:', mylist)
print('')

# Insertar elementos a una lista
print('Insertaremos "Hello" en el tercer indice de la lista: ', mylist)
mylist.insert(3, 'Hello') #Primero se inserta el indice referente a la posicion donde deseo insertar el nuevo elemento

print(mylist)