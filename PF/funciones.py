# funciones.py
def borrarPantalla():
  import os
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def validar_codigo_4_digitos(codigo: str):
    return codigo.isdigit() and len(codigo) == 4

def formato_moneda(valor):
    return f"${valor:,.2f}"