condicion = False
if condicion:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")

cond = False
if cond == True :
    print("Condicion verdadera")
elif cond == False:
    print("Condicion falsa")
else:
    print("Condicion no reconocida")

numero = int(input("proporciona un numero entre 1 y 3:"))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "valor fuera de rango"

print("numero proporcionado:", numeroTexto)


