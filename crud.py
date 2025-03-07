
from conexion2 import conectar_bd
import mysql.connector

def crear_registro(conexion, nombre, apellido):
    cursor = conexion.cursor()
    sql = "INSERT INTO clientes (nombre, apellido) VALUES (%s, %s)"
    valoress = (nombre, apellido)
    cursor.execute(sql, valoress)
    conexion.commit()
    print("Registro insertado con éxito")
    cursor.close()
    conexion.close()

def leer_registros(conexion):
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    for nombre in resultados:
        print(nombre)

conexion = conectar_bd()

if conexion: 
    crear_registro(conexion, "juan", "Perez")
    # leer_registros(conexion)
    # actualizar_registro(conexion, 5, "Juan", 30)

    conexion.close()

else:
    print("Error al conectar a la base de datos")

conexion.close()
