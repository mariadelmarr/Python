# Debe tener además una tupla con los cursos ya existentes. (‘Inglés’, ‘Ciencias’...)
# El programa debe tener un menú interactivo que permita dar mantenimiento a las listas de profesores y estudiantes.
# Además debe de poder crear grupos en un diccionario donde el key es la letra A, B, C, … A estos grupos se les asigna un curso, un profesor y varios estudiantes. Almacene estos grupos en una lista de diccionarios.
# Debe poder imprimir el estado actual de los grupos.

class Teacher:
    species = "Profesor"

    def __init__(self, name, course):
        self.name = name
        self.age = age
        
    def __str__(self):
         return f"Este {Teacher.species} se llama {self.name} y imparte el curso {self.course} "
         
    def speak(self, sound):
         return f"{self.name} dice {sound