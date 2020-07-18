from teacher import Teacher
from student import Student
from list import Courses
from list import Group
from list import List

Teacher = List()
# dogs.append(1)
# dogs.append('a')
# dogs.append(False)

# print(dogs)

def menuPrincipal():
    print('Menu:\n')
    print('''
    a.Teachers
    b.Students
    c.Courses
    d.Groups
    e.Salir
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
        e.Salir
        ''')
        selection = input()

        if selection.lower() == 'a':
            addTeacher()
            menu()
        elif selection.lower() == 'b':
            printTeacher()
            menu()
        elif selection.lower() == 'c':
            editTeacher()
            menu()
        elif selection.lower() == 'd':
            deletTeacher()
            menu()
        elif selection.lower() == 'e':
            print ('Saliendo...')
        else:
            print('Opcion incorrecta')
        
        def addTeacher():
            teacher = None
            print(f'1-{JackRussellTerrier.race} 2-{Dachsund.race} 3-{Bulldog.race}')
            race = input('Raza? ')
            name = input('Nombre? ')
            age = input('Edad? ')

            if int(race) == 1:
                dog = JackRussellTerrier(name, age)
            elif int(race) == 2:
                dog = Dachsund(name, age)
            elif int(race) == 3:
                dog = Bulldog(name, age)

            dogs.append(dog)

        def printDogs():
            print(dogs)

        def editDog():
            pass

        def deletDog():
            pass

        menu()
    if selection.lower() == 'b':
        def menuStudents():
        print('Menu:\n')
        print('''
        a.Ingresar estudiante
        b.Mostrar estudiante
        c.Editar estudiante
        d.Eliminar estudiante
        e.Salir
        ''')
        selection = input()

        if selection.lower() == 'a':
            addStudent()
            menu()
        elif selection.lower() == 'b':
            printStudent()
            menu()
        elif selection.lower() == 'c':
            editStudent()
            menu()
        elif selection.lower() == 'd':
            deletStudentr()
            menu()
        elif selection.lower() == 'e':
            print ('Saliendo...')
        else:
            print('Opcion incorrecta')

    if selection.lower() == 'c':
        def menuCourses():
        print('Menu:\n')
        print('''
        a.Ingresar curso
        b.Mostrar curso
        c.Editar curso
        d.Eliminar curso
        e.Salir
        ''')
        selection = input()

        if selection.lower() == 'a':
            addCoursest()
            menu()
        elif selection.lower() == 'b':
            printCourses()
            menu()
        elif selection.lower() == 'c':
            editCourses()
            menu()
        elif selection.lower() == 'd':
            deletCourses()
            menu()
        elif selection.lower() == 'e':
            print ('Saliendo...')
        else:
            print('Opcion incorrecta')

    if selection.lower() == 'b':
        def menuGroup():
        print('Menu:\n')
        print('''
        a.Ingresar estudiante
        b.Mostrar estudiante
        c.Editar estudiante
        d.Eliminar estudiante
        e.Salir
        ''')
        selection = input()

        if selection.lower() == 'a':
            addGroup()
            menu()
        elif selection.lower() == 'b':
            printGroup()
            menu()
        elif selection.lower() == 'c':
            editGroup()
            menu()
        elif selection.lower() == 'd':
            deletGroup()
            menu()
        elif selection.lower() == 'e':
            print ('Saliendo...')
        else:
            print('Opcion incorrecta')

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
