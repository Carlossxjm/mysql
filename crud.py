
from conexion2 import conectar_bd
import mysql.connector

def crear_registro(conexion,curso,duracion,descripcion):

    cursor = conexion.cursor()
    sql = "INSERT INTO curso (curso,duracion,descripcion) VALUES (%s, %s, %s)" #` INSERT INTO `#` (`id_#`, `nombre`, `edad`) VALUES (NULL, 'Juan', '25') *Insertar un registro
    valoress = (curso,duracion,descripcion)
    cursor.execute(sql, valoress)
    conexion.commit()
    print("Registro insertado con éxito")
    cursor.close()
    conexion.close()    

def leer_registros(conexion):
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM curso") #` SELECT * FROM `#` *Seleccionar todos los registros de una tabla
    resultados = cursor.fetchall()
    for nombre in resultados:
        print(nombre)

def eliminar_registro(conexion, id):

    cursor = conexion.cursor()
    sql = "DELETE FROM curso WHERE id_curso = (%s)" #` DELETE FROM `#` WHERE `id_#` = 1 *Eliminar una tabla
    cursor.execute(sql, (id,))
    conexion.commit()
    print("Registro eliminado con éxito")
    cursor.close()
    conexion.close()

def actualizar_registro(conexion, curso, duracion, descripcion, id):
    cursor = conexion.cursor()
    sql = "UPDATE curso SET curso = %s, duracion = %s, descripcion = %s WHERE id_curso = %s #" #` UPDATE `#` SET `nombre` = 'Juan', `edad` = 30 WHERE `id_#` = 5 *Actualizar un registro
    cursor.execute(sql, (curso, duracion, descripcion, id))
    conexion.commit()
    print("Registro actualizado con éxito")
    cursor.close()
    conexion.close()

conexion = conectar_bd()

if conexion: 
    #crear_registro(conexion,"Edición", "5 meses", "Curso de edición de videos")
    #eliminar_registro(conexion,13)
    #leer_registros(conexion)
    actualizar_registro(conexion, "Edición", "8 meses", "Curso de edición de videos", 12)

    # leer_registros(conexion)
    # actualizar_registro(conexion, 5, "Juan", 30)
    conexion.close()

else:
    print("Error al conectar a la base de datos")

conexion.close()
