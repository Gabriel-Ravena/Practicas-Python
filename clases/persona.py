class Persona:
    def __init__(self, nombre, apellido, edad, domicilio, puesto):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.domicilio = domicilio
        self.puesto = puesto

Persona.nombre = "Gabriel"
Persona.apellido = "Ravena"
Persona.edad = 34
Persona.domicilio = "Roma 3322"
Persona.puesto = "QA Automation"

print(Persona.nombre)
print(Persona.apellido)
print(Persona.edad)
print(Persona.domicilio)
print(Persona.puesto)

#crear nuevo objeto
persona = Persona("Carlos", "Sanchez", 32, "Madrid 3322", "Qa")
print(persona.nombre)
print(persona.apellido)
print(persona.edad)
print(persona.domicilio)
print(persona.puesto)

persona2 = Persona("Lola", "more", 38, "Malvinas 3245", "Scrum master")
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.domicilio)
print(persona2.puesto)
