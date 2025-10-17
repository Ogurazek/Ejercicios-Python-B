# Sin constructor


class Coche:
    pass


mi_coche = Coche()


# ------------------------------------------------------------

# Con constructor


class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = (
            marca  # Mi marca (la del coche actual) será la marca que me pasaron
        )
        self.modelo = modelo
        self.color = color  # Mi color (la de este coche) será el color que me pasaron


mi_toyota = Coche("Toyota", "Corolla", "Rojo")

mi_chevrolet = Coche("chevrolet", "cruze", "gris")

# ------------------------------------------------------------

# Explicación del por qué el self
