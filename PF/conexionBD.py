import mysql.connector
from mysql.connector import Error

def get_conexion():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='bd_dulceria',
            autocommit=True
        )
        return conexion
    except Error as e:
        print("Error de conexión:", e)
        raise