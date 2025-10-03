# Ejercicio 3: Diccionario de estudiante

# Dado este diccionario:
# estudiante = {
#  "nombre": "Ana",
#  "edad": 20,
#  "materias": ["Matemática", "Historia"]
# }
# 1- Mostrá el nombre y la edad
# 2- Agregá una materia nueva a la lista materias
# 3- Mostrá cuántas materias cursa con len()
# 4- Usá .get() para obtener la clave “promedio” con valor por defecto 0


estudiante = {"nombre": "Ana", "edad": 20, "materias": ["Matemática", "Historia"]}


print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])

estudiante["materias"].append("Biología")
cantidad_materias = len(estudiante["materias"])

print("La cantidad de materias que hay son: ", cantidad_materias)

# estudiante["promedio"]

promedio = estudiante.get("promedio", 20)
print("El promedio que tenes es:", promedio)

print(estudiante["materias"])
