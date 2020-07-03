class MiClase:

    variable_clase = "variable clase"

    def __init__(self):
        self.variable_instancia = "variable_instancia"

    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        #Desde un metodo estatico no podemos acceder a una variable de instancia
        #print(MiClase.variable_instancia)

    @classmethod
    def metodo_clase(cls):
        print("metodo de clase:"+ str(cls))
        print(cls.variable_clase)
        #No podemos acceder a una variable de instancia desde contexto estatico
        #print(cls.variable_instancia)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase()
objeto1.metodo_instancia()
