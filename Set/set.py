#No tiene orden ni indices, no se pueden repetir elementos, no se pueden modificar, pero si agregar o eliminar
planetas = {"Mercurio", "Venus", "Tierra", "Marte"}
print(planetas)
#largo del set
print("Cantidad de elementos del set:", len(planetas))
#Verificar si un elemento se encuentra en el set o no
print("Se encuentra este elemento en la lista?", "Marte" in planetas)
print("Se encuentra este elemento en la lista?", "Neptuno" in planetas)
#Agregar nuevo elemento
planetas.add("Jupiter")
print(planetas)
#Agregar elemento repetido(No lo reconoce)
planetas.add("Mercurio")
print(planetas)
#Eliminar elementos
planetas.remove("Venus")
print(planetas)
#Elimimar mal un elemento sin que arroje ninguna excepcion
planetas.discard("Tierras")
print(planetas)
#Eliminar todos los valores del set
planetas.clear()
print(planetas)
#Eliminar set(Arroja error al no encontrar la variable definida)
print("Tira error al no encontrar la variable definida")
del planetas
print(planetas)