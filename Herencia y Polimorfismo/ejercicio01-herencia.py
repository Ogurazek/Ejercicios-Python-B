# Definimos la clase Persona
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


# Definimos la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)  # Llamamos al constructor de Persona
        self.carrera = carrera  # Nuevo atributo propio de Estudiante

    def obtener_carrera(self):
        return f"Está estudiando la carrera de {self.carrera}"


persona1 = Persona("Juan", "Pérez")
print(persona1.nombre_completo())

estudiante1 = Estudiante("Ana", "García", "Ingeniería en Sistemas")
print(estudiante1.nombre_completo())
print(estudiante1.obtener_carrera())
