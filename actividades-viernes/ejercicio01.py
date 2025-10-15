# 1 – Sistema de calificaciones de estudiantes {
# Creá un programa que guarde las notas de varios estudiantes en un diccionario,
# Luego, crea funciones para:
# A- Agregar estudiante con sus notas
# B- Calcular el promedio de un estudiante
# C- Mostrar los estudiantes aprobados (promedio >=6)


# Diccionario para guardar estudiantes y sus notas
estudiantes = {}


# Función para agregar un estudiante con sus notas
def agregar_estudiante(nombre, notas):
    """
    nombre: str -> nombre del estudiante
    notas: list -> lista de números (notas)
    """
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado con notas {notas}.")


# Función para calcular el promedio de un estudiante
def promedio_estudiante(nombre):
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = sum(notas) / len(notas)
        return promedio
    else:
        print("Estudiante no encontrado.")
        return None


# Función para mostrar estudiantes aprobados (promedio >= 6)
def estudiantes_aprobados():
    aprobados = []
    for nombre in estudiantes:
        promedio = promedio_estudiante(nombre)
        if promedio >= 6:
            aprobados.append((nombre, promedio))
    return aprobados


agregar_estudiante("Ana", [7, 8, 6])
agregar_estudiante("Juan", [5, 6, 4])
agregar_estudiante("Luis", [9, 7, 8])

print("\nPromedio de Ana:", promedio_estudiante("Ana"))
print("\nEstudiantes aprobados:")
for estudiante, promedio in estudiantes_aprobados():
    print(f"{estudiante}: {promedio}")
