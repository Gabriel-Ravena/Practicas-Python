from clases_abstractas.figuras_geometricas import FiguraGeometrica
from clases_abstractas.color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        # super().__init__(lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho