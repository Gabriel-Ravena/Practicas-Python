from mundo_pc.monitor import Monitor
from mundo_pc.dispositivo_entrada import DispositivoEntrada
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadoras = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self):
        return (
            f"""
            {self.__nombre} : {self.__id_computadoras}
            Monitor : {self.__monitor},
            Teclado: {self.__teclado},
            Raton: {self.__raton}

            """
                )


"""
monitor1 = Monitor("Coradir", "14 Pulgadas")
teclado1 = Teclado("Acer", "usb")
raton1 = Raton("Genius", "bluetooh")
computadora1 = Computadora("Acer", monitor1, teclado1, raton1)
print(computadora1)

monitor2 = Monitor("hp", "19 Pulgadas")
teclado2 = Teclado("Genius", "usb")
raton2 = Raton("Genius", "usb")
computadora2 = Computadora("HP", monitor2, teclado2, raton2)
print(computadora2)
"""