# 4- Mostrar información de una persona con **Kwargs {
# Creá una función mostrar_info() que reciba datos como nombre, edad, ciudad, etc, y los
# muestre con un formato legible.


def mostrar_info(**kwargs):
    """
    Recibe cualquier cantidad de datos sobre una persona y los muestra de manera legible.
    """
    print("Información de la persona:")
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")


mostrar_info(nombre="Ana", edad=25, ciudad="Buenos Aires", profesion="Desarrolladora")
