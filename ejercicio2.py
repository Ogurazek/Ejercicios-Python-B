colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

cantidad_rojo = colores.count("rojo")
indice_verde = colores.index("verde")
colores[indice_verde] = "amarillo"
print("Cantidad de rojos", cantidad_rojo)
print("Lista final", colores)
