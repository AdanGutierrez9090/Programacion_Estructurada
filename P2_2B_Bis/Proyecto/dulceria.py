
def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    print("\n🕒 Oprima cualquier tecla para continuar ...")
    input()

def menu_principal():
    print("\n\t📋 === SISTEMA DE INVENTARIO === \n\t1. Agregar producto 💾\n\t2. Ver inventario 📂\n\t3. Entrada de producto ➕\n\t4. Salida de producto ➖\n\t5. Buscar por código 🔍\n\t6. Salir 🚪")
    opcion = input("\tSeleccione una opción: ")
    return opcion

def agregar_producto(lista):
    borrarPantalla()
    print("\n📥 Agregar producto")

    while True:
        nombre = input("📝 Nombre del producto: ").strip().upper()
        if nombre:
            break
        print("❌ Campo obligatorio.")

    tipo = input("🏷️  Tipo (Dulce en bolsa, Granel, Frituras, Plásticos): ").strip().capitalize()
    unidad = input("📦 Unidad (pieza, gramos, bolsa, paquete): ").strip().lower()

    while True:
        clave = input("🔢 Código numérico de 4 dígitos: ").strip()
        if clave.isdigit() and len(clave) == 4:
            break
        print("❌ Debe ingresar un código de exactamente 4 dígitos numéricos.")

    while True:
        try:
            precio = float(input("💰 Precio unitario: $"))
            if precio >= 0:
                break
            print("❌ El precio no puede ser negativo.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

    while True:
        try:
            stock = int(input("📊 Stock inicial: "))
            if stock >= 0:
                break
            print("❌ El stock no puede ser negativo.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

    producto = {
        "nombre": nombre,
        "clave": clave,
        "tipo": tipo,
        "unidad": unidad,
        "precio": precio,
        "stock": stock
    }

    lista.append(producto)
    print("\n✅ Producto agregado exitosamente.")

def ver_inventario(lista):
    borrarPantalla()
    print("\n📦 Inventario actual")
    if lista:
        print(f"{'Producto':<15}{'Clave':<10}{'Tipo':<18}{'Unidad':<10}{'Precio':<10}{'Stock':<10}")
        print("-" * 70)
        for p in lista:
            print(f"{p['nombre']:<15}{p['clave']:<10}{p['tipo']:<18}{p['unidad']:<10}${p['precio']:<9.2f}{p['stock']:<10}")
        print("-" * 70)
        print(f"\n📋 Total de productos: {len(lista)}")
    else:
        print("❌ No hay productos registrados.")

def entrada_producto(lista):
    borrarPantalla()
    print("\n➕ Entrada de producto")
    codigo = input("🔎 Ingrese el código del producto: ")
    for p in lista:
        if p["clave"] == codigo:
            try:
                cantidad = int(input("📥 Cantidad a agregar: "))
                if cantidad > 0:
                    p["stock"] += cantidad
                    print("✅ Entrada registrada exitosamente.")
                else:
                    print("❌ La cantidad debe ser mayor a 0.")
            except ValueError:
                print("❌ Debe ingresar un número entero.")
            return
    print("❌ Producto no encontrado.")

def salida_producto(lista):
    borrarPantalla()
    print("\n➖ Salida de producto")
    codigo = input("🔎 Ingrese el código del producto: ")
    for p in lista:
        if p["clave"] == codigo:
            try:
                cantidad = int(input("📤 Cantidad a vender: "))
                if cantidad <= 0:
                    print("❌ La cantidad debe ser mayor que cero.")
                elif cantidad > p["stock"]:
                    print("❌ Stock insuficiente.")
                else:
                    p["stock"] -= cantidad
                    print("✅ Venta registrada exitosamente.")
            except ValueError:
                print("❌ Debe ingresar un número entero.")
            return
    print("❌ Producto no encontrado.")

def buscar_codigo(lista):
    borrarPantalla()
    print("\n🔍 Buscar producto por código")
    if not lista:
        print("❌ No hay productos en el inventario.")
        return

    codigo = input("🔢 Ingrese el código a buscar: ")
    for p in lista:
        if p["clave"] == codigo:
            print("\n✅ Producto encontrado:")
            print("-" * 50)
            print(f"Nombre  : {p['nombre']}")
            print(f"Código  : {p['clave']}")
            print(f"Tipo    : {p['tipo']}")
            print(f"Unidad  : {p['unidad']}")
            print(f"Precio  : ${p['precio']:.2f}")
            print(f"Stock   : {p['stock']} {p['unidad']}")
            print("-" * 50)
            return
    print("❌ Producto no encontrado.")
