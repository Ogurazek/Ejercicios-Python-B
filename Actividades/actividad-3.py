# Nivel 2 | Registro de Stock {
# Dado un diccionario llamado stock que contiene productos como claves y una tupla con su
# precio y cantidad disponible como valor, escribí un programa que:
# A- Le pida al usuario que ingrese el nombre de un producto
# B- Verifique si el producto existe en el diccionario
# C- Si existe, muestre por pantalla el precio y la cantidad disponible
# D- Si no existe, deja un mensaje de que no se encontró el producto
# }


stock = {
    "pan": (100, 20),
    "leche": (200, 10),
}

producto = input("Ingrese el producto que desea: ")


if producto in stock:
    precio, cantidad = stock[producto]
    print(
        f"El precio del {producto} es: {precio}, el stock del producto es: {cantidad}"
    )
else:
    print("No se encuentra el producto")
