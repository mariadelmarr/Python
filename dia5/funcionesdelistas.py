# # Ordenar elementos de una lista
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
list2 = [3, 5, 2, 4, 1]

mylist.sort()#ordena mylist conforme al orden del abecedario
list2.sort()#ordena list2 con respecto al orden de los numeros

print(mylist)
print(list2)

# Eliminar un elemento de la lista
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)
removed = mylist.pop(1) #elimina el elemento que se encuentra en el indice 1, puesto que si no se indica el indice que se 
#desea eliminar, se eliminara el ultimo

print('Se elimino el indice: ',removed)

# Insertar elementos a una lista

mylist = [1, 2, 3, 4, 5]
mylist.insert(3, 'Hello') #Primero se inserta el indice referente a la posicion donde deseo insertar el nuevo elemento

print(mylist)