#se compone por los elementos llave y valor(Key and value)
diccionario = {
    "HTML":  "lenguaje de maquetacion web",
    "CSS":   "lenguaje para dar estilo a nuestro sitio web",
    "Python": "Lenguaje de programacion orientada a objetos",
    "C++":    "lenguaje de programacion orientada a objetos usado para el desarrollo de video juegos",
    "SQL":    "lenguaje para manejar base de datos"
}
print(diccionario)
#Largo del diccionario
print("Cantidad de elementos del diccionario", len(diccionario))
#Acceder a determinado elemento del diccionario
print(diccionario["HTML"])
#Acceder a determinado elemento del diccionario pero de otra maneta con el mismo resultado
print(diccionario.get("SQL"))
#Modificando valores
diccionario["HTML"] = "Maquetado web"
print(diccionario)
#Ciclo for para recorrer diccionario
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])

for valor in diccionario.values():
    print(valor)

#Comprobar existencia de llave en el diccionario
print("HTML" in diccionario)
print("Java" in diccionario)

#Agregar nuevos elementos al diccionario
diccionario["PHP"] = "Lenguaje de programación web"
print(diccionario)
#Eliminar elemento del diccionario
diccionario.pop("SQL")
print(diccionario)
#Vaciar el diccionario
diccionario.clear()
print(diccionario)
#Eliminar diccionario
del diccionario
print(diccionario)