 #declaro la clase
class Rectangle:
    #constructor
    def __init__(self, width, heigth, color):
        self.width = width
        self.heigth = heigth
        self.color = color

    #defino funciones
    def getArea(self):
        area = self.width * self.heigth
        return area

    def getPerimeter(self):
        perimeter = (self.width + self.heigth) * 2
        #o bien, reutilizando el codigo 
        return perimeter

#...uso la clase Rectangulo para crear los siguientes objetos

curtain = Rectangle(2, 3, 'cafe')
monitor = Rectangle(1, 1, 'Negro')
pool = Rectangle(15, 25, 'Azul')
print('\n')
print('La cortina es de color {}'.format( curtain.color))
print('\n')
print('El area del monitor es {} metros cuadrados. '.format(monitor.getArea()))
print('\n')
x = pool.getPerimeter()
print(x)