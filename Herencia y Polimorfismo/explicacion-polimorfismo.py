# El polimorfismo permite que diferentes clases implementen métodos con el mismo nombre, pero con comportamientos distintos. Esto se logra mediante la sobrescritura de métodos o el uso de interfaces comunes, y permite que el mismo código opere sobre objetos de diferentes clases de manera coherente.


class Animal:
    def hacer_sonido(self):
        pass  # Método vacío, las clases hijas lo sobrescribirán


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"


# Función que usa polimorfismo
def hacer_hablar(animal):
    print(animal.hacer_sonido())


# Crear instancias de diferentes animales
perro = Perro()
gato = Gato()
vaca = Vaca()

# Llamar a la misma función, pero cada animal hace un sonido diferente
hacer_hablar(perro)  # Guau
hacer_hablar(gato)  # Miau
hacer_hablar(vaca)  # Muu


# vehiculos = [Coche(), Bicicleta(), Avion()]
