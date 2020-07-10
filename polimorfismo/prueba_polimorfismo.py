from polimorfismo.empleado import Empleado
from polimorfismo.gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto), end="\n\n" )
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Juan", 1000.00)
imprimir_detalles(empleado)

empleado = Gerente("Gabriel", 30000, "Sistemas")
imprimir_detalles(empleado)