#Mantiene el orden pero no se puede modificar(inmutable)
frutas = ("Manzana", "Naranja", "Banana", "Uva", "Mandarina")
print(frutas)
print("Cantidad de frutas:", len(frutas))
#Ingresar a un elemento determinado
print(frutas[3])
#Navegación inversa
print(frutas[-4])
#Rangos
print(frutas[0:2])
print(frutas[4:])
#Convertir tupla en lista para poder modificar valores y volver a convertir en tupla
listaFrutas = list(frutas)
listaFrutas[1] = "Melón"
frutas = tuple(listaFrutas)
print(frutas)
#Recorrer tupla con ciclo FOR
for fruta in frutas:
    print(fruta, end=" ")
#No se puede eliminar ni agregar elementos a una tupla
#Eliminamos la variable y nos tira error al no encontrar definida la variable
del frutas
print(frutas)