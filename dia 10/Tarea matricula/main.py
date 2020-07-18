# El programa debe tener un menú interactivo que permita dar mantenimiento a las listas de profesores y estudiantes.
# Además debe de poder crear grupos en un diccionario donde el key es la letra A, B, C, … A estos grupos se les asigna un curso, un profesor y varios estudiantes. Almacene estos grupos en una lista de diccionarios.
# Debe poder imprimir el estado actual de los grupos.


from teacher import Teacher
from student import Student
from list import Courses
from list import Group
from list import List


Courses = ('English', 'Maths', 'Science', 'Geography')


def menuPrincipal():
    print('Menu:\n')
    print('''
    a.Teachers
    b.Students
    c.Print Courses
    d.Add Groups
    e.Print Groups
    f.Exit
    ''')
    selection = input()

    if selection.lower() == 'a':
        def menuTeacher():
        print('Menu:\n')
        print('''
        a.Ingresar profesor
        b.Mostrar profesores
        c.Editar profesores
        d.Eliminar profesores
        e.Ir al menu principal
        ''')
        selection = input()

        if selection.lower() == 'a':
            addTeacher()
            menuTeacher()
        elif selection.lower() == 'b':
            printTeacher()
            menuTeacher()
        elif selection.lower() == 'c':
            editTeacher()
            menuTeacher()
        elif selection.lower() == 'd':
            deletTeacher()
            menuTeacher()
        elif selection.lower() == 'e':
            menuPrincipal()
        else:
            print('Opcion incorrecta')
            menuPrincipal()

    if selection.lower() == 'b':
        def menuStudents():
        print('Menu:\n')
        print('''
        a.Ingresar estudiante
        b.Mostrar estudiante
        c.Editar estudiante
        d.Eliminar estudiante
        e.Ir al menu principal
        ''')
        selection = input()

        if selection.lower() == 'a':
            addStudent()
            menuStudents()
        elif selection.lower() == 'b':
            displayStudent()
            menuStudents()
        elif selection.lower() == 'c':
            updateStudent()
            menuStudents()
        elif selection.lower() == 'd':
            deleteStudent()
            menuStudents()
        elif selection.lower() == 'e':
            menuPrincipal()
        else:
            print('Opcion incorrecta')
            menuPrincipal()

    if selection.lower() == 'c':
        printCourses()
        menuPrincipal()

    if selection.lower() == 'd':
        addGroup()
        menuPrincipal()
    
    if selection.lower() == 'e'
        printGroup()
        menuPrincipal()

    if selection.lower() == 'f'
        print('Ciao')

#o bien para hacer los 3 imports anteriores d ela siguiente manera
#import races import *

# lea = Dog('Lea', 2)
# Jack = JackRussellTerrier('Jack', 3)
# buddy = Dachsund('Buddy', 9)
# billy = Bulldog('Billy', 2)

# print(lea)
# print(lea.speak('Guof'))
# print(Jack.species)
# print(buddy.name)
# print(buddy)
# print(billy.speak('Woof'))

# print(Jack.speak())
# print(buddy.speak('Woooonf'))
