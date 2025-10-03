# El usuario tiene que tener la posibilidad de ingresar un nombre del algún producto, y preguntarles si les gustó
# o no el producto


encuesta = {}


for i in range(4):
    nombre = input("Ingresa el nombre del producto: ")
    respuesta = input(f"Te gustó el {nombre}: ")
    encuesta[nombre] = [respuesta]

print(encuesta)
