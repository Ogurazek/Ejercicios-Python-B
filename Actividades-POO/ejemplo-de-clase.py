class Coche:
    ruedas = 4

    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")


# Crear objetos
mi_coche = Coche("Toyota", "Corolla", "Rojo")
otro_coche = Coche("Ford", "Ranger", "Azul")
otro_coche2 = Coche("Chevrolet", "cruze", "gris")

# Acceder a atributos
print("Atributos del primer coche:")
print(mi_coche.marca)
print(mi_coche.modelo)
print(mi_coche.color)
print(mi_coche.ruedas)

print("\nAtributos del segundo coche:")
print(otro_coche.marca)
print(otro_coche.modelo)
print(otro_coche.color)
print(otro_coche.ruedas)

print("\nAtributos del Tercer coche:")
print(otro_coche2.marca)
print(otro_coche2.modelo)
print(otro_coche2.color)
print(otro_coche2.ruedas)

mi_coche.acelerar()
otro_coche.frenar()
