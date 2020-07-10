class Monitor():

    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitores = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return (
            f"ID: {self.__id_monitores},"
            f"Marca: {self._marca},"
            f"Tamaño: {self._tamanio}"
        )

#monitor = Monitor("HP", "15 Pulgadas")
#print(monitor)