class Aritmetica:

    def __init__(self, operando1, operando2):
        """Clase"""
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

# Creando nuevo objeto

aritmetica = Aritmetica(4, 2)
print("El resultado de la suma es:", aritmetica.sumar())
print("El resultado de la resta es:", aritmetica.restar())
print("El resultado de la multiplicacion es:", aritmetica.multiplicar())
print("El resultado de la division es:", aritmetica.dividir())




