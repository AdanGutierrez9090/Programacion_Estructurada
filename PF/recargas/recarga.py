# recarga/recargas.py
from conexionBD import get_conexion
from datetime import datetime

def listar_recargas(limit=100):
    try:
        sql = """
        SELECT r.id_recarga, r.fecha, r.cantidad, r.comentario,
               p.codigo, p.nombre AS producto,
               u.nombre AS usuario, u.apellidos
        FROM recarga r
        LEFT JOIN producto p ON r.id_producto = p.id_producto
        LEFT JOIN usuario u ON r.id_usuario = u.id
        ORDER BY r.fecha DESC LIMIT %s
        """
        conexion = get_conexion()
        cur = conexion.cursor(dictionary=True)
        cur.execute(sql, (limit,))
        filas = cur.fetchall()
        cur.close()
        conexion.close()
        return filas
    except Exception as e:
        print("❌ Error al listar recargas:", e)
        return []

def mostrar_recargas(limit=100):
    recargas = listar_recargas(limit)
    if recargas:
        print("\n\t=== Listado de Recargas ===")
        for r in recargas:
            print(f"ID: {r['id_recarga']} | Fecha: {r['fecha']} | Cantidad: {r['cantidad']} | "
                  f"Producto: {r['producto']} ({r['codigo']}) | Usuario: {r['usuario']} {r['apellidos']}")
    else:
        print("No hay recargas registradas.")

def recargar_stock(id_usuario=None):
    try:
        if id_usuario is None:
            id_usuario = input("Ingrese su ID de usuario: ").strip()

        codigo = input("Ingrese el código del producto a recargar (4 dígitos): ").strip()
        if len(codigo) != 4 or not codigo.isdigit():
            print("⚠ Código inválido. Debe ser de 4 dígitos numéricos.")
            return False

        cantidad = input("Ingrese la cantidad a recargar: ").strip()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("⚠ La cantidad debe ser un número entero mayor que 0.")
            return False
        cantidad = int(cantidad)

        comentario = None  # Comentario no solicitado

        conexion = get_conexion()
        cur = conexion.cursor()

        # Obtener id_producto según código
        cur.execute("SELECT id_producto FROM producto WHERE codigo = %s LIMIT 1", (codigo,))
        producto = cur.fetchone()
        if not producto:
            print("⚠ Producto no encontrado.")
            cur.close()
            conexion.close()
            return False

        id_producto = producto[0]

        # Insertar recarga
        sql_recarga = """
            INSERT INTO recarga (id_producto, fecha, cantidad, comentario, id_usuario)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(sql_recarga, (id_producto, datetime.now(), cantidad, comentario, id_usuario))

        # Actualizar stock
        sql_update = "UPDATE producto SET stock = stock + %s WHERE id_producto = %s"
        cur.execute(sql_update, (cantidad, id_producto))

        conexion.commit()
        cur.close()
        conexion.close()

        print("✅ Recarga registrada y stock actualizado correctamente.")
        return True

    except Exception as e:
        print("❌ Error al recargar stock:", e)
        return False