import sqlite3

def consultar_stock(codigo_producto, talle):
    con = sqlite3.connect("database/archie.db")
    cur = con.cursor()
    
    cur.execute("""
        SELECT stock FROM Inventario WHERE codigo_producto = ? AND talle = ?
    """, (codigo_producto, talle))
    
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




# --- ZONA DE PRUEBAS ---
# Usamos el truco para probar la funcion aca.
if __name__ == "__main__":
    print("Probando RF-01: Consulta de Stock...")
    
    stock_remera = consultar_stock(1001, 4)
    if stock_remera == "-1" :
        print("no hay unidades en stock del producto con el talle seleccionado")
    else :
        print(f"Hay {stock_remera} unidades en stock de la prenda 1001, talle 4")
    
    stock_falso = consultar_stock(1002, 22)
    if stock_falso == "-1" :
        print("no hay unidades en stock del producto con el talle seleccionado")
    else:
        print(f"Hay {stock_falso} unidades en stock de la prenda 1002, talle 22")
