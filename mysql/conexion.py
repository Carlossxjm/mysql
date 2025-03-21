#$ pip install mysqlclient
import MySQLdb

def conectar_bd():
    try:
        conexion = MySQLdb.connect(
            host='localhost',
            user='root',
            password='', #Reemplazar por la contraseña de la base de datos
            database='restaurante' #Reemplazar por el nombre de la base de datos
        )
        print('Conexión exitosa') #Mensaje de éxito
        return conexion
    except MySQLdb.connect.Error as error: # si hay un error de mysql
        print(f"Error al conectar a MySQL {error}")
        return None
    
    finally:
    # Bloque finnaly, para futuras implementaciones. como cerrar la conexión.
    # if conexion.is_connected():
    #     conexion.close()
    # print('Conexión cerrada')
        pass

    c=conectar_bd.cursor()
    c.execute("SELECT * FROM menu")
    c.fetchall()

    for menu in c:
        print(menu)
        pass

conexion = conectar_bd() # Llamamos a la función conectar_bd
# conexion.close() # Cerramos la conexión s