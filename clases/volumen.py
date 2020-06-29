class Volumen:

    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def calcularVolumen(self):
        return self.largo * self.ancho * self.alto

largo = int(input("Introducir largo "))
ancho = int(input("Introducir ancho "))
alto = int(input("Introducir alto "))

#calculando volumen

print("Volumen obtenido ingresando los datos por teclado")
volumen = Volumen(largo, ancho, alto)
print("El volumen de la caja es: ", volumen.calcularVolumen())

print("Volumen obtenido por valores predefinidos")
volumen1 = Volumen(4, 7, 2)
print("El volumen de la caja es: ", volumen1.calcularVolumen())