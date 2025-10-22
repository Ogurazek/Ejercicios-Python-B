# La herencia permite que una clase derive o herede comportamientos y atributos de otra clase. Esto promueve la reutilización de código y la creación de jerarquías de clases. La clase hija puede sobrescribir o extender los métodos y atributos de la clase base.


# Clase base
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años")


# Clase hija que hereda de Mascota
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        # Usamos super() para llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.raza = raza

    def mostrar_info(self):
        # Sobrescribimos el método del padre, pero también usamos super()
        super().mostrar_info()
        print(f"Raza: {self.raza}")

    def ladrar(self):
        print("¡Guau! ¡Guau!")


# Crear un objeto de la clase Perro
mi_perro = Perro("Max", 3, "Labrador")

# Usar métodos
mi_perro.mostrar_info()  # Usa método heredado + extendido
mi_perro.ladrar()  # Método propio de Perro
