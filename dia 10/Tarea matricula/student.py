class Student:
    # species = "Canis familiaritis"

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
        
    # def __str__(self):
    #     return f"Este {Dog.species} se llama {self.name} y es de {self.age} años"
         
    # def speak(self, sound):
    #     return f"{self.name} dice {sound

    from dog import Dog
class JackRussellTerrier(Dog):
    race = 'JackRussellTerrier'
    def speak(self, sound='Argg'):
        return f'{sound} es lo que dice {self.name}'

class Dachsund(Dog):
    race = 'Dachshund'

class Bulldog(Dog):
    race = 'Bulldog'