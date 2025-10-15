# 1- Generador de hechizos aleatorios {
# Escribe una función que combine aleatoriamente un prefijo y sufijo de listas dadas y cree un
# hechizo mágico (Usar módulo random)

import random


def generar_hechizo():
    prefijos = ["Abra", "Alakaza", "Zendo", "Foco", "Magi"]
    sufijos = ["cadabra", "lumos", "mora", "nox", "flama"]

    prefijo_aleatorio = random.choice(prefijos)
    sufijo_aleatorio = random.choice(sufijos)

    print(f"{prefijo_aleatorio}-{sufijo_aleatorio}")


generar_hechizo()
