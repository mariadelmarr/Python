
import datetime
x = datetime.datetime.now()

def menu():
    print('Seleccione una opcion: ')
    print('''
    a. Imprimir hora
    b. Imprimir día del mes
    c. Imprimir día de la semana
    d. Imprimir mes
    e. Imprimir año
    f. Salir
    ''')
    selection = input()

    if selection.lower() == 'a':
        print ('Its: ',x.hour, ':', x.minute,':',x.second) 
        menu()

    elif selection.lower() == 'b':
        print('Today is ',x.strftime("%A"), x.day, 'of the month ',x.month)
        menu()

    elif selection.lower() == 'c':
        print(x.strftime('day: '"%A"))
        menu()

    elif selection.lower() == 'd':
        print('Month: ',x.month)
        menu()

    elif selection.lower() == 'e':
        print('Year: ',x.year)
        menu()

    elif selection.lower() == 'f':
        print('Ciao!')

menu()