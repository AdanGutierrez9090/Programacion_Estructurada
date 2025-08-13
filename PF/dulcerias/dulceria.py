# dulceria/dulceria.py
from conexionBD import get_conexion
from funciones import validar_codigo_4_digitos

def agregar_producto():
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()
    precio = float(input("Precio: "))
    stock = int(input("Cantidad inicial: "))

    try:
        conexion = get_conexion()
        cur = conexion.cursor()
        sql = "INSERT INTO producto (codigo, nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (codigo, nombre, descripcion, precio, stock))
        conexion.commit()
        cur.close()
        conexion.close()
        print("✅ Producto agregado correctamente")
    except Exception as e:
        print("❌ Error al agregar producto:", e)

def ver_inventario(limit=100):
    try:
        conexion = get_conexion()
        cur = conexion.cursor(dictionary=True)
        cur.execute("SELECT * FROM producto LIMIT %s", (limit,))
        filas = cur.fetchall()
        cur.close()
        conexion.close()
        return filas
    except Exception as e:
        print("❌ Error al obtener inventario:", e)
        return []

def buscar_por_codigo(codigo=None):
    if codigo is None:
        codigo = input("Ingrese el código del producto (4 dígitos): ").strip()
    if not validar_codigo_4_digitos(codigo):
        print("Código inválido. Debe tener 4 dígitos numéricos.")
        return None
    try:
        conexion = get_conexion()
        cur = conexion.cursor(dictionary=True)
        cur.execute(
            "SELECT id_producto, codigo, nombre, descripcion, precio, stock FROM producto WHERE codigo = %s LIMIT 1",
            (codigo,)
        )
        producto = cur.fetchone()
        if producto:
            print(f"\nCódigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
        else:
            print("No se encontró el producto con ese código.")
        cur.close()
        conexion.close()
        return producto
    except Exception as e:
        print("❌ Error al buscar producto:", e)
        return None


    try:
        if codigo is None:
            codigo = input("Ingrese el CÓDIGO del producto: ").strip()
        if cantidad is None:
            cantidad = int(input("Ingrese la cantidad a quitar: "))
        if cantidad <= 0:
            print("⚠ La cantidad debe ser mayor que 0.")
            return False

        conexion = get_conexion()
        cur = conexion.cursor()
        cur.execute("SELECT id_producto, stock, precio FROM producto WHERE codigo = %s", (codigo,))
        row = cur.fetchone()
        if not row:
            print(f"⚠ Producto con código '{codigo}' no existe.")
            cur.close()
            conexion.close()
            return False

        id_producto, stock_actual, precio = row
        if stock_actual < cantidad:
            print("⚠ Stock insuficiente.")
            cur.close()
            conexion.close()
            return False

        total = float(precio) * cantidad
        cur.execute("UPDATE producto SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_producto))
        cur.execute("INSERT INTO venta (id_usuario, id_producto, cantidad, total) VALUES (%s, %s, %s, %s)",
                    (id_usuario, id_producto, cantidad, total))

        conexion.commit()
        cur.close()
        conexion.close()
        print("✅ Salida registrada correctamente.")
        return True

    except Exception as e:
        print("❌ Error en salida de producto:", e)
        return False