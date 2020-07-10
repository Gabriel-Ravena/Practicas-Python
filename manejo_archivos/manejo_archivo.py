try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()

#Después de close ya no se puede seguir trabajando porque el archivo se corta ahi
