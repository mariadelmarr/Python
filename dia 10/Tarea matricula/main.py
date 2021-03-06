# El programa debe tener un menú interactivo que permita dar mantenimiento a las listas de profesores y estudiantes.
# Además debe de poder crear grupos en un diccionario donde el key es la letra A, B, C, … A estos grupos se les asigna un curso, un profesor y varios estudiantes. Almacene estos grupos en una lista de diccionarios.
# Debe poder imprimir el estado actual de los grupos.

from teacher import Teacher
from student import Student
from list import *

courses = ('English', 'Maths', 'Science', 'Geography')
groups = {'key' : ['A1'],'course' : None , 'Teacher' : None , 'Student' : None}


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
                Teacher.addT()
                menuTeacher()
            elif selection.lower() == 'b':
                displayT()
                menuTeacher()
            elif selection.lower() == 'c':
                updateT()
                menuTeacher()
            elif selection.lower() == 'd':
                deleteT()
                menuTeacher()
            elif selection.lower() == 'e':
                menuPrincipal()
            else:
                print('Opcion incorrecta')
                menuPrincipal()

        menuTeacher()

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

        menuStudents()

    
    if selection.lower() == 'c':
        printCourses('', courses)
        menuPrincipal()

    if selection.lower() == 'd':
        addGroup()
        menuPrincipal()
    
    if selection.lower() == 'e':
        printGroup()
        menuPrincipal()

    if selection.lower() == 'f':
        print('Ciao')

menuPrincipal()

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
