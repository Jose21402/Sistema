import sqlite3

"""
Ejemplo de CRUD
author = _Jose_
"""
# Se crea una variable que almacena la conexion a
# la base de datos
 conexion = sqlite3.connect('registro.db')

"""
Create table 
"""
try:
movimientos = conexion.cursor()
movimientos.excute('''
CREATE TABLE Alumnos(
    id_alumnos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT(20) NOT NULL,
    a_paterno TEXT(20) NOT NULL,
    a_materno TEXT(20) NOT NULL,
    edad INTEGER
);
''')
print("Creacion de tabla correcto")
except:
    print("Error en la operacion: No se pudo crear la tabla")
    conexion




