# 5- Registro flexible de usuarios {
# Creá una función registrar_usuario() que reciba_
# *args con los intereses del usuario, por ejemplo (Música, Programación, Videojuegos, etc)
# **kwargs con su información básica (nombre, edad, etc.)
# Y que devuelva un resumen legible.


def registrar_usuario(*args, **kwargs):
    """
    Registra un usuario con información básica (**kwargs)
    y una lista de intereses (*args), y devuelve un resumen legible.
    """
    # Información básica
    print("=== Información del usuario ===")
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

    # Intereses
    if args:
        print("\nIntereses:")
        for interes in args:
            print(f"- {interes}")
    else:
        print("\nNo se especificaron intereses.")

    print("\nUsuario registrado con éxito.")


registrar_usuario(
    "Música",
    "Programación",
    "Videojuegos",
    nombre="Ana",
    edad=25,
    ciudad="Buenos Aires",
)
