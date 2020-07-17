from dog import Dog
from races import JackRussellTerrier
from races import Dachsund
from races import Bulldog
from myList import MyList

dogs = MyList()
# dogs.append(1)
# dogs.append('a')
# dogs.append(False)

# print(dogs)

def menu():
    print('Menu:\n')
    print('''
    a.Crear
    b.Leer
    c.Editar
    d.Eliminar
    e.Salir
    ''')
    selection = input()

    if selection.lower() == 'a':
        addDog()
        menu()
    elif selection.lower() == 'b':
        printDogs()
        menu()
    elif selection.lower() == 'c':
        editDog()
        menu()
    elif selection.lower() == 'd':
        deletDog()
        menu()
    elif selection.lower() == 'e':
        print ('Saliendo...')
    else:
        print('Opcion incorrecta')

def addDog():
    dog = None
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
