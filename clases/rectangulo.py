class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = int(input("introduzca base: "))
altura = int(input("introduzca altura: "))

#calculando la base

print("Area del rectangulo ingresando base y altura por teclado")
rectangulo = Rectangulo(base, altura)
print("El area del rectangulo es: ", rectangulo.calcularArea())


print("Area del rectangulo con valores de base y altura predefinidos")
rectangulo1 = Rectangulo(3, 6)
print("El area del rectangulo es: ", rectangulo1.calcularArea())