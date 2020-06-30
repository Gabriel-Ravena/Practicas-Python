class Persona:
    def __init__(self, nombre, ape_materno, ape_paterno):
        self.nombre = nombre                     #PUBLICO
        self._apellido_materno = ape_materno     #PROTEGIDO
        self.__apellido_paterno = ape_paterno    #PRIVADO

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_materno)
        print(self.__apellido_paterno)

    def get_ape_paterno(self):
        return self.__apellido_paterno

    def set_ape_paterno(self, paterno):
        self.__apellido_paterno = paterno

p1 = Persona("Carlos", "Iriarte", "Mora")
p1.metodo_publico()
print(p1.nombre)
print(p1._apellido_materno)
print(p1.get_ape_paterno())
#print(p1.__apellido_paterno)  #No lo encuentra porque es privado