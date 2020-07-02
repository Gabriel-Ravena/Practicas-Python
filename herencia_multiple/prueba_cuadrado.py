from herencia_multiple.cuadrado import Cuadrado
from herencia_multiple.triangulo import Triangulo

cuadrado = Cuadrado(3, "rojo")
print("###CUADRADO###")
print("Area del cuadrado: ", cuadrado.area())
print("Color del cuadrado: ", cuadrado.color)
print("###TRIANGULO###")
triangulo = Triangulo(4, 5, "Amarillo")
print("Area del triangulo: ", triangulo.area())
print("Color del triangulo:", triangulo.color)