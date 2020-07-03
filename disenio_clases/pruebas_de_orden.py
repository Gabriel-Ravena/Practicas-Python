from disenio_clases.producto import Producto
from disenio_clases.orden import Orden

producto1 = Producto("camisa", 300)
producto2 = Producto("pantalon", 500)
producto3 = Producto("Medias", 50)
producto4 = Producto("Zapatillas", 2400)


lista_de_productos = [producto1, producto2]
print("Lista de productos de orden1 y su total")
print()
orden1 = Orden(lista_de_productos)
print(orden1)
print("Precio total de la orden:", orden1.calcular_total())

print()
print("Lista de productos de orden2 y su total")
print()
#lista_de_productos.append(producto3)
orden2 = Orden(lista_de_productos)
orden2.agregar_producto(producto3)
print(orden2)
print("Precio total de la orden:", orden2.calcular_total())

print()
print("Lista de productos de orden3 y su total")
print()
orden3 = Orden(lista_de_productos)
lista_de_productos.remove(producto3)
orden3.agregar_producto(producto4)
print(orden3)
print("Precio total de la orden:", orden3.calcular_total())

orden4 = Orden(lista_de_productos)
orden4.agregar_producto(producto3)
print(orden4)
print(orden4.calcular_total())

