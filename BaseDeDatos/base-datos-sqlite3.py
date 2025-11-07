import sqlite3
import uuid
import datetime

conn = sqlite3.connect("alquiler.db")

cursor = conn.cursor()


def crear_tabla():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuario (
        uuid_usuario VARCHAR PRIMARY KEY,
        email VARCHAR UNIQUE NOT NULL,
        nombre VARCHAR, 
        fecha_nacimiento TIMESTAMP NOT NULL,
        pais VARCHAR
        )
"""
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pelicula (
        uuid_pelicula VARCHAR PRIMARY KEY,
        titulo VARCHAR NOT NULL,
        genero VARCHAR, 
        duracion INT,
        año TIMESTAMP NOT NULL
        )
"""
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alquiler (
        uuid_alquiler VARCHAR PRIMARY KEY,
        uuid_usuario VARCHAR,
        uuid_pelicula VARCHAR, 
        fecha TIMESTAMP,
        precio REAL, 
        tipo_vista VARCHAR,
        FOREIGN KEY(uuid_usuario) REFERENCES usuario(uuid_usuario),
        FOREIGN KEY(uuid_pelicula) REFERENCES pelicula(uuid_pelicula)
        )
"""
    )

    conn.commit()


def insertar_usuario():
    email = input("Email: ")
    nombre = input("Nombre: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    pais = input("País: ")
    uuid_usuario = str(uuid.uuid4())

    query = """INSERT INTO usuario (uuid_usuario, email, nombre, fecha_nacimiento, pais)
                VALUES (?, ?, ?, ?, ?)"""

    cursor.execute(query, (uuid_usuario, email, nombre, fecha_nacimiento, pais))
    conn.commit()
    print("El usuario se registro correctamente!!")


def insertar_pelicula():
    titulo = input("Título: ")
    genero = input("Género: ")
    duracion = int(input("Duración (minutos)"))
    año = input("Fecha")
    uuid_pelicula = str(uuid.uuid4())

    query = """INSERT INTO pelicula (uuid_pelicula, titulo, genero, duracion, año)
                VALUES (?, ?, ?, ?, ?)"""

    cursor.execute(query, (uuid_pelicula, titulo, genero, duracion, año))
    conn.commit()
    print("La pelicula se registro correctamente!!")


def AlquilarUsuario():
    listar_usuarios()
    uuid_usuario = input("UUID del usuario que alquila: ")
    listar_peliculas()
    uuid_pelicula = input("UUID de la película: ")

    precio = float(input("Precio del alquiler: "))
    tipo_vista = input("Descarga u Online? ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uuid_alquiler = str(uuid.uuid4())

    query = """INSERT INTO alquiler (uuid_alquiler, uuid_usuario, uuid_pelicula, precio, fecha, tipo_vista)
                VALUES (?, ?, ?, ?, ?, ?)"""
    #
    cursor.execute(
        query, (uuid_alquiler, uuid_usuario, uuid_pelicula, precio, fecha, tipo_vista)
    )
    conn.commit()
    print("La pelicula se alquilo correctamente!!")


def listar_usuarios():
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()

    for u in usuarios:
        print(u)


def listar_peliculas():
    cursor.execute("SELECT * FROM pelicula")
    peliculas = cursor.fetchall()

    for p in peliculas:
        print(p)


# Menú de opciones
def menu():
    crear_tabla()
    while True:
        print("Menu")
        print("1. Insertar un usuario")
        print("2. Insertar una película")
        print("3. Alquilar una película")
        print("4. Listar usuarios")
        print("5. Listar películas")
        print("6. Listar alquileres")
        print("0. Salir")

        opcion = input("seleccione una opción: ")

        if opcion == "1":
            insertar_usuario()
        elif opcion == "2":
            insertar_pelicula()
        elif opcion == "3":
            AlquilarUsuario()
        elif opcion == "4":
            listar_usuarios()
        elif opcion == "5":
            listar_peliculas()
        # elif opcion == "6":
        # Listar alquileres
        elif opcion == "0":
            print("Cerrar conexión")
            break


menu()
