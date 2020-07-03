from clases_abstractas.cuadrado import Cuadrado
from clases_abstractas.figuras_geometricas import FiguraGeometrica

#No se puede instanciar una clase abstracta
#figuraGeometrica = FiguraGeometrica(3,4)

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

#Method Resolution Order
print(Cuadrado.mro())