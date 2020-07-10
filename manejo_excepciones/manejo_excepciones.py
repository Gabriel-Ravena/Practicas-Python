from manejo_excepciones.numeros_identicos_exception import NumerosIdenticosException

resultado = None

try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    if a == b:
        raise NumerosIdenticosException("Ocurrio un error, numeros identicos")
    resultado = a/b
except ZeroDivisionError as e:
    print("Ha ocurrido un error con ZeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ha ocurrido un error con TypeError", e)
    print(type(e))
except ValueError as e:
    print("Ha ocurrido un error con ValueError", e)
    print(type(e))
except Exception as e:
    print("Ha ocurrido un error con Exception", e)
    print(type(e))
else:
    print("No hubo ninguna excepcion")
finally:
    print("Fin del manejo de excepciones")
print("Resultado", resultado)
print("Continuamos......")