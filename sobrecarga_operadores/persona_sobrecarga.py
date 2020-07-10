class Persona:

    def __init__(self, nombre):
        self.__nombre = nombre

    def __add__(self, otro):
        return self.__nombre + " ",   otro.__nombre

persona = Persona("Juan")
persona2 = Persona("Carla")

print(persona + persona2)