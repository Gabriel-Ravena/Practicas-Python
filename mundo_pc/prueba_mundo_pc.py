from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado
from mundo_pc.monitor import Monitor
from mundo_pc.computadoras import Computadora

teclado_hp = Teclado("HP", "usb")
raton_hp = Raton("HP", "bluetooh")
monitor_hp = Monitor("HP", "17 Pulgadas")
computadora_hp = Computadora("HP", monitor_hp, teclado_hp, raton_hp)

teclado_acer = Teclado("Acer", "usb")
raton_acer = Raton("Acer", "usb")
monitor_acer = Monitor("Acer", "19 Pulgadas")
computadora_acer = Computadora("Acer", monitor_acer, teclado_acer, raton_acer)

teclado_gamer = Teclado("Gamer", "usb")
raton_gamer = Raton("Gamer", "usb")
monitor_gamer = Monitor("Gamer", "19 Pulgadas")
computadora_gamer = Computadora("Gamer", monitor_gamer, teclado_gamer, raton_gamer)

computadora_armada = Computadora("Armada", monitor_gamer, teclado_acer, raton_hp)

computadoras1 = [computadora_acer, computadora_hp]
orden1 = Orden(computadoras1)
orden1.agregar_computadoras(computadora_gamer)
print(orden1)

computadoras2 = [computadora_acer, computadora_hp, computadora_armada]
orden2 = Orden(computadoras2)
orden2.agregar_computadoras(computadora_armada)
print(orden2)