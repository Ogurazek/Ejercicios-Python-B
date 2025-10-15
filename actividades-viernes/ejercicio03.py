# 3- Mutiplicar todos los números {
# Escribí una función multiplicar() utilizando args, que reciba varios números y devuelva el
# resultado de multiplicarlos todos.


def multiplicar(*args):
    """
    Recibe cualquier cantidad de números y devuelve el resultado de multiplicarlos todos.
    """
    if not args:  # Si no se pasan números, devolvemos 1
        return 1

    resultado = 1
    for numero in args:
        resultado *= numero  # Multiplicamos cada número al resultado

    return resultado
