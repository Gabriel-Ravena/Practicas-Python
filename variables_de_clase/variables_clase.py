class MiClase:
    variable_clase = "Variables de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
objeto1 = MiClase("Variable instancia")
MiClase.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia) #Valores distintos
print(objeto1.variable_instancia) #Valores distintos

#Se puede acceder a las clases a traves de los objetos
print(objeto1.variable_clase)
#Se puede acceder a las viariables con el nombre de la clase
print(MiClase.variable_clase)
objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase)
print(MiClase.variable_clase)

objeto2 = MiClase("Nuevo valor")
#print(objeto2.variable_clase)

objeto3 = MiClase("tercer objeto")

MiClase.variable_clase = "Cambio desde la clase"
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)