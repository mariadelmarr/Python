# Cree un programa en Python que tenga funciones para calcular el área de las siguientes figuras geométricas:
# Círculo, Cuadrado, Rectángulo, Triángulo.
# La función del área del cuadrado y el rectángulo debe ser la misma, con el segundo parámetro para calcular 
# el rectángulo opcional.Debe ser interactivo de manera que el usuario use un menú donde pueda escoger qué 
# quiere calcular.

import math

def menu():
    option = int(input('Digite la opcion que desea realizar: \n 1-> calcular el área de un Círculo [1] \n 2-> calcular el área de un Cuadrado [2] \n 3-> calcular el área de un Rectángulo [3] \n 4-> calcular el área de un Triángulo. [4] \n 5-> Salir. [5] \n'))

    if option == 1:
        radio = int(input('Digite el radio del circulo: ')) 
        print ('El área del circulo es: ', math.pi * radio * radio, '\n')
        menu()
        
    elif option == 2:
        num1 = int(input('Ingrese el lado del cuadrado: '))
        num2 = num1
        area(num1, num2, type = 'Square')
        menu()

    elif option == 3:  
        num1 = int(input('Ingrese el lado del rectangulo: '))
        num2 = int(input('Ingrese la base del rectangulo: '))
        area(num1, num2, type = 'rectangle')
        menu()

    elif option == 4: 
        b = int(input('Digite la base del Triángulo: ')) 
        a = int(input('Digite la altura del Triángulo: '))
        print('El área del triángulo es: ', b * a / 2 , '\n')
        menu()

    elif option == 5:
        print('Gracias...')

    else:
        print('Opcion Incorrecta')
        menu()

"""Defino la función que calcula el área del cuadrado y el rectángulo"""
def area(num1, num2, type = 'Square'):
    print(type + '...')

    if type == 'Square':
        result = num1 * num2

    else:
        result = num1 * num2
    print(result,  '\n')

menu()