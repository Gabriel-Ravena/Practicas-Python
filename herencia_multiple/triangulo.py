from herencia_multiple.figura_geometrica import FiguraGeometrica
from herencia_multiple.color import Color

class Triangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho