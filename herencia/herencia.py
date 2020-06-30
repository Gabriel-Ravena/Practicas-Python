class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre " + self.nombre + " Edad " + str(self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + " Sueldo " + str(self.sueldo)

persona = Persona("Gabriel", 34)
print(persona)

empleado1 = Empleado("Lorena", 37, 50000)
print(empleado1)

empleado1.nombre = "Silvina"
empleado1.edad = 28
empleado1.sueldo = "40000"
print(empleado1)
