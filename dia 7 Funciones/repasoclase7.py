print('Binevenido al super software de menus.')

def main():
    print('Ingrese dos números.')
    num1 = int(input('Agregue el primer número: '))
    num2 = int(input('Agregue el segundo número: '))
    menu(num1, num2)

def menu(num1, num2):
    print('''Opciones:
    a. Sumar.
    b. Restar.
    c. Multiplicar.
    d. Salir.
    ''')
    selection = input('Selección: ')

    if selection == 'A' or selection == 'a':
        proccess(num1, num2, type='Adding')
        main()
    elif selection.lower() == 'b':
        proccess(num1, num2, type='Substracting')
        main()
    elif selection.lower() == 'c':
        proccess(num1, num2, type='Multiplying')
        main()
    elif selection.lower() == 'd':
        print('Gracias...')
    else:
        print('Opción incorrecta.')
        menu()

def proccess(num1, num2, type = 'Adding'):
    print(type + '...')
    
    if type == 'Adding':
        result = num1 + num2
    elif type == 'Substracting':
        result = num1 - num2
    else:
        result = num1 * num2
    print(result)

main()

# print('Bienvenido al super software de menus')

# def main():
#     print('Ingrese dos numeros')
#     num1 = int(input('Primer numero: '))
#     num2 = int(input('Segundo numero: '))
#     menu(num1, num2)

# def menu(num1, num2):
#     print('''Digite la accion que desea realizar: 
#     a.Sumar.
#     b.Restar.
#     c.Multiplicar
#     d.Salir.
#     ''')
#     seleccion = input('Opcion: ')

#     if seleccion == 'A' or seleccion == 'a':
#         proccess(num1, num2, type = 'Adding')
#         main()
    
#     elif seleccion.lower() == 'b':
#         proccess(num1, num2, type = 'Substracting')
#         main()
    
#     elif seleccion.lower() == 'c':
#         proccess(num1, num2, type = 'Multiplying')
#         main()
    
#     elif seleccion.lower() == 'd':
#         print('Gracias...')
#     else:
#         print('Opcion incorrecta.')
#         main()

# def proccess(num1, num2, type = 'Adding'):
#     print(type + '...')

#     if type == 'Adding':
#         result = num1 + num2
#     elif type == 'Substracting':
#         result = num1 - num2
#     else:
#         result = num1 * num2
#     print(result)
# main()
