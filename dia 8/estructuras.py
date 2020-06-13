# practica estructuras de datos
# Tuplas y diccionarios

# Tuplas
colors = ('rojo', 'azul', 'verde', 'anaranjado')
fruits = ('banano', 'naranja', 'pera')

# set
days = {'lunes', 'martes', 'miercoles', 'jueves', 'viernes'}

# list
students = []

def menu():
    print('Seleccione una opcion: ')
    print('''
    a. Imprimir colores
    b. Imprimir frutas
    c. Imprimir los dias
    d. Imprimir estudiantes
    e. Agregar estudiante
    f. Salir
    ''')
    selection = input()

    if selection.lower() == 'a':
        printColors()
        menu()

    elif selection.lower() == 'b':
        printFruits()
        menu()

    elif selection.lower() == 'c':
        printDays()
        menu()

    elif selection.lower() == 'd':
        printStudents()
        menu()

    elif selection.lower() == 'e':
        addStudent()
        menu()

    elif selection.lower() == 'f':
        quitProgram()

    else:
        print('Opcion incorrecta')
        menu()
            
            
def printColors():
    print(colors)

def printFruits():
    print(fruits)

def printDays():
    print(days)

def printStudents():
    print(students)

def addStudent():
    student = {}
    student['name'] = input('Ingrese un nombre: ')
    print('Seleccione un color (0, 1, 2, 3): ', colors)
    i = int(input())
    student['colors'] = colors[i]
    print('Seleccione una fruta (0, 1, 2): ', fruits)
    i = int(input())
    student['frutas'] = fruits[i]
    print('Asignando un dia: ', days)
    day = days.pop()
    print('dia asignado', day)
    student['day'] = days.pop()
    students.append(student)
    
    print(student)

def quitProgram():
    print('Gracias.\nCiao.')

menu()