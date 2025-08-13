from funciones import borrarPantalla, esperarTecla
from conexionBD import get_conexion
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def registrar(nombre, apellidos, email, password):
    try:
        hashed = hash_password(password)

        conexion = get_conexion()
        cur = conexion.cursor()
        cur.execute(
            "INSERT INTO usuario (nombre, apellidos, email, password) VALUES (%s,%s,%s,%s)",
            (nombre, apellidos, email, hashed)
        )
        conexion.commit()
        cur.close()
        conexion.close()

        print("✅ Usuario registrado correctamente.")
        return True
    except Exception as e:
        print("❌ Error al registrar usuario:", e)
        return False

def iniciar_sesion(email, password):
    try:
        hashed = hash_password(password)

        conexion = get_conexion()
        cur = conexion.cursor(dictionary=True)
        cur.execute(
            "SELECT id, nombre, apellidos FROM usuario WHERE email = %s AND password = %s",
            (email, hashed)
        )
        user = cur.fetchone()
        cur.close()
        conexion.close()

        if user:
            borrarPantalla()
            print(f"👋 Bienvenido {user['nombre']} {user['apellidos']}")
            esperarTecla()
            return user["id"]
        else:
            return None
    except Exception as e:
        print("❌ Error al iniciar sesión:", e)
        return None
