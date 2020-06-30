class Persona:

    def __init__(this, n, a, e, d, p, *v, **di):
        this.nombre = n
        this.apellido = a
        this.edad = e
        this.domicilio = d
        this.puesto = p
        this.valores = v
        this.diccionario = di

    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Apellido: ", this.apellido)
        print("Edad: ", this.edad)
        print("Domicilio: ", this.domicilio)
        print("Puesto: ", this.puesto)
        print("Valores: ", this.valores)
        print("Diccionario: ", this.diccionario)

p1 = Persona("Gabriel", "Ravena", 34, "roma 3322", "QA Automation")
p1.desplegar()

p2 = Persona("Juan", "Acosta", 33, "Madrid 4433", "Operario", 4, 5, 21, 33)
p2.desplegar()

p3 = Persona("Laura", "Martinez", 31, "Mexico 2111", "Scrum Master", L="lau", M="Martinez")
p3.desplegar()