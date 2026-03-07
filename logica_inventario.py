import sqlite3

def consultar_stock(codigo):
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    cur.execute("""
        SELECT stock FROM Productos WHERE codigo = ?
    """, (codigo,))
    
    resultado = cur.fetchone()
    
    # fetchone(): Úsalo cuando buscas algo único (ej. el stock de un talle específico o el
    # nombre de un cliente). Te devuelve (dato1, dato2)
    
    # fetchall() o iterar el cursor: Úsalo cuando buscas listas, reportes o inventarios
    # completos. Te devuelve [ (dato1, dato2), (dato3, dato4) ]
    
    
    con.close()
    
    if resultado is not None:
        return resultado[0]
    else:
        return "-1"

def obtener_producto_para_venta(codigo):
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    cur.execute("""
                SELECT nombre, precio_centavos, stock FROM Productos WHERE codigo = ?
                """, (codigo,))
    resultado = cur.fetchone()
    con.close()
    return resultado       # Devuelve (nombre, precio, stock) o None


# --- ZONA DE PRUEBAS ---
# Usamos el truco para probar la funcion aca.
if __name__ == "__main__":
    print("Probando RF-01: Consulta de Stock...")
    
    stock = consultar_stock(1001)
    if stock == "-1" :
        print("no hay unidades en stock del producto seleccionado")
    else :
        print(f"Hay {stock} unidades en stock del producto 1001")
    
    stock_falso = consultar_stock(1002)
    if stock_falso == "-1" :
        print("no hay unidades en stock del producto seleccionado")
    else:
        print(f"Hay {stock_falso} unidades en stock del producto 1002")
