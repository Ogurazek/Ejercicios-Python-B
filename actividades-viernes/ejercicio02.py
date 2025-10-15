# 2- Sumar todos los números {
# Definí una función sumar_todos() utilizando args que reciba una cantidad indefinida de
# números y devuelva la suma total (Acá podemos usar la función integrada de python
#  sum )


def sumar_todos(*args):
    """
    Recibe cualquier cantidad de números y devuelve su suma total.
    """
    return sum(args)


print(sumar_todos(20, 30, 40, 50, 500))
