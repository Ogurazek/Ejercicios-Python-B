# Ejercicio 01 Programción Orientada a Objetos 😎

# Consigna 🐍

# Crea una clase llamada Persona que tenga los atributos nombre y edad.
# Luego, crea un método que muestre un saludo con el nombre y la edad de la persona.
# Finalmente, crea un objeto de esa clase y haz que se muestre su saludo.


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Elías", 20)
persona2 = Persona("Pablo", 28)


persona1.saludar()
persona2.saludar()


# ---------------------------------------------------------------------------------------------------


# Ejercicio 02 Programación Orientada a Objetos 🤩

# Consigna

# Crea una clase llamada Perro que tenga los atributos nombre y raza.
# Agrega un método llamado ladrar que muestre un mensaje con el nombre del perro diciendo "¡Guau!".
# Luego crea un objeto de esa clase y haz que ladre.


class Perro:
    pass
