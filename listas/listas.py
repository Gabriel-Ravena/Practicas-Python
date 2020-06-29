nombres = ["Gabriel", "Lorena", "Juan", "Beto"]
print(nombres)
#largo de la lista
print("elementos de la lista: ", len(nombres))
#Elementos por numero
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
#Elementos en una sola linea
print(nombres[0], nombres[1], nombres[2], nombres[3])
#Elementos por indice negativo
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])
#Elementos en una sola linea llamados por indice negativo
print(nombres[-1], nombres[-2], nombres[-3], nombres[-4])
#Imprimir por rango
print(nombres[0:2])
print(nombres[:3])
print(nombres[1:])
#Cambiar elementos de una lista
nombres[3] = "Ifran"
print(nombres)
#Recorrer elementos con ciclo for
for nombre in nombres:
    print(nombre)
#Revisar si elemento existe en la lista
if "Gabriel" in nombres:
    print("Gabriel si existe en la lista")
else:
    print("Gabriel no existe en la lista")
#Agregar nuevo elemento en la lista
nombres.append("Silvina")
print(nombres)
#Agregar elemento nuevo a la lista en un indice especifico
nombres.insert(2, "Alvaro")
print(nombres)
#Eliminar elemento de la lista
nombres.remove("Alvaro")
nombres.remove("Juan")
print(nombres)
#Eliminar ultimo elemento de la lista
nombres.pop()
print(nombres)
#Remover indice indicado de la lista
del nombres[0]
print(nombres)
#Limpiar todos los elementos de la lista
nombres.insert(1, "Gabriel")
nombres.append("Mariana")
nombres.append("Christian")
nombres.append("Facundo")
nombres.append("Rocio")
print(nombres)
nombres.clear()
print(nombres)
#Eliminar variable(Tira error al no encontrar la variable definida)
del nombres
print(nombres)




