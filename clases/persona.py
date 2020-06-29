class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Persona.nombre = "Gabriel"
Persona.edad = 34

print(Persona.nombre)
print(Persona.edad)

#crear nuevo objeto
persona = Persona("Carlos", 32)
print(persona.nombre)
print(persona.edad)

persona2 = Persona("Lola", 38)
print(persona2.nombre)
print(persona2.edad)

