class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

print("Primera persona")
p1 = Persona("Gabriel", "Ravena")
print(p1.get_nombre())
print(p1.get_apellido())
print("Segunda persona")
p1.set_nombre("Juan")
p1.set_apellido("Acosta")
print(p1.get_nombre())
print(p1.get_apellido())
print("Tercera persona")
p1.set_nombre("Carlos")
p1.set_apellido("Suarez")
print(p1.get_nombre())
print(p1.get_apellido())