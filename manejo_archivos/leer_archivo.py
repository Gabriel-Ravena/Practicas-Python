archivo = open("prueba.txt", "r")
print(archivo.read())
#Se puede leer cierta cantidad de caracteres
print(archivo.read(5))
print(archivo.read(4))
archivo.close()

