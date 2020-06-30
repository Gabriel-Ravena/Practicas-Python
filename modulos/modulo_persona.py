class Persona:

    def __init__(self, nombre, edad, residencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__residencia = residencia

    def __str__(self):
        return  "Nombre: " + self.__nombre + " Edad: " + str(self.__edad) + " Residencia: " + self.__residencia


