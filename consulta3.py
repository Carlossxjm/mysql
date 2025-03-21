from conexion2 import conectar_bd
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def leer_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    resultados = cursor.fetchall()
    return resultados

@app.route('/')
def mostrar_pacientes():
    conexion = conectar_bd()
    resultados = leer_registros(conexion)
    return render_template('index2.html', estudiantes=resultados)

if __name__ == '__main__':
    app.run(debug=True)