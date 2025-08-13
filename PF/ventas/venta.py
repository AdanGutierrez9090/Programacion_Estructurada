# ventas/ventas.py
from conexionBD import get_conexion
from datetime import datetime

def listar_ventas(limit=100):
    try:
        sql = """
        SELECT v.id_venta, v.fecha, v.cantidad, v.total,
               p.codigo, p.nombre AS producto,
               u.nombre AS usuario, u.apellidos
        FROM venta v
        LEFT JOIN producto p ON v.id_producto = p.id_producto
        LEFT JOIN usuario u ON v.id_usuario = u.id
        ORDER BY v.fecha DESC LIMIT %s
        """
        conexion = get_conexion()
        cur = conexion.cursor(dictionary=True)
        cur.execute(sql, (limit,))
        filas = cur.fetchall()
        cur.close()
        conexion.close()
        return filas
    except Exception as e:
        print("❌ Error al listar ventas:", e)
        return []

def mostrar_ventas(limit=100):
    ventas = listar_ventas(limit)
    if ventas:
        print("\n\t=== Listado de Ventas ===")
        for v in ventas:
            print(f"ID: {v['id_venta']} | Fecha: {v['fecha']} | Cantidad: {v['cantidad']} | Total: {v['total']:.2f} | "
                  f"Producto: {v['producto']} ({v['codigo']}) | Usuario: {v['usuario']} {v['apellidos']}")
    else:
        print("No hay ventas registradas.")

def realizar_venta(id_usuario):
    try:
        codigo = input("Ingrese el código del producto a vender: ").strip()
        cantidad = int(input("Ingrese la cantidad a vender: "))

        conexion = get_conexion()
        cur = conexion.cursor()

        # Obtener id_producto y stock del producto por código
        cur.execute("SELECT id_producto, stock, precio FROM producto WHERE codigo = %s LIMIT 1", (codigo,))
        producto = cur.fetchone()

        if not producto:
            print("⚠ Producto no encontrado.")
            cur.close()
            conexion.close()
            return False

        id_producto, stock_actual, precio_unitario = producto

        if stock_actual < cantidad:
            print("⚠ Stock insuficiente.")
            cur.close()
            conexion.close()
            return False

        total = cantidad * precio_unitario
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Actualizar stock
        cur.execute("UPDATE producto SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_producto))

        # Insertar venta
        sql = "INSERT INTO venta (id_usuario, id_producto, cantidad, total, fecha) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (id_usuario, id_producto, cantidad, total, fecha))

        conexion.commit()
        cur.close()
        conexion.close()

        print("✅ Venta realizada correctamente.")
        return True

    except Exception as e:
        print("❌ Error al realizar venta:", e)
        return False