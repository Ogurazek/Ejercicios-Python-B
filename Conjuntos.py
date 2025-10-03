# Conjuntos

frutas = {"manzana", "pera", "manzana", "naranja", "manzana", "manzana"}

# frutas = set() Para hacer un conjunto vacío, se hace con el set()

# print(frutas)

frutas.add("frutilla")
# frutas.remove("sandía")
frutas.discard("Sandía")
frutas.pop()

# print("Agregando fruta", frutas)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Unión
print(A & B)  # Intersección
print(B - A)  # Diferencia
