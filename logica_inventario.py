import sqlite3
import datetime

def consultar_stock(codigo):
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    cur.execute("""
        SELECT stock FROM Productos WHERE codigo = ?
    """, (codigo,))
    
    resultado = cur.fetchone()
    
    
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
    return resultado      

def obtener_ventas_diarias():
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    try:
        fecha_hoy = datetime.date.today().strftime("%d-%m-%Y")
        busqueda_fecha = f"{fecha_hoy}%"
        cur.execute("""
                        SELECT id, fecha_venta, cliente, codigo_producto, nombre_producto, cantidad, total 
                        FROM Ventas
                        WHERE fecha_venta LIKE ?
                        ORDER BY fecha_venta DESC
        """, (busqueda_fecha,))
        ventas = cur.fetchall() 
        return ventas
    except Exception as e:
        print(f"Error al obtener las ventas diarias: {e}")
        return []
    finally:
        con.close()

def obtener_ventas_historico():
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    try:
        cur.execute("""
                        SELECT id, fecha_venta, cliente, codigo_producto, nombre_producto, cantidad, total 
                        FROM Ventas
                        ORDER BY fecha_venta DESC
        """)
        ventas = cur.fetchall() 
        return ventas
    except Exception as e:
        print(f"Error al obtener las ventas diarias: {e}")
        return []
    finally:
        con.close()



def registrar_venta(codigo, cantidad, cliente, nombre_producto, total):
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    try:
        cur.execute("""
            SELECT stock FROM Productos WHERE codigo = ?
        """, (codigo,))
        
        resultado = cur.fetchone()
        
        if resultado is not None:
            stock_actual = resultado[0]
            if stock_actual >= cantidad:
                nuevo_stock = stock_actual - cantidad
                cur.execute("""
                    UPDATE Productos SET stock = ? WHERE codigo = ?
                """, (nuevo_stock, codigo))
                
                hora_exacta = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                cur.execute("""
                    INSERT INTO Ventas(fecha_venta, cliente, codigo_producto, nombre_producto, cantidad, total)
                    VALUES(?, ?, ?, ?, ?, ?)
                """, (hora_exacta, cliente, codigo, nombre_producto, cantidad, total))
                
                
                con.commit()
                con.close()
                return True 
            else:
                con.close()
                return False 
        else:
            con.close()
            return False
    except Exception as e:
        print(f"Error al registrar la venta: {e}")
        con.rollback()
        return False
    finally:
        con.close()

def anular_venta(id_venta):
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    try:
        cur.execute("SELECT codigo_producto, cantidad FROM Ventas WHERE id = ?", (id_venta,))
        venta = cur.fetchone()
        
        if venta:
            codigo_prod, cantidad_vendida = venta
            cur.execute("UPDATE Productos SET stock = stock + ? WHERE codigo = ?", (cantidad_vendida, codigo_prod))
            
            cur.execute("DELETE FROM Ventas WHERE id = ?", (id_venta,))
            
            con.commit()
            return True
        return False
        
    except Exception as e:
        print(f"ERROR CRÍTICO AL ANULAR: {e}")
        con.rollback()
        return False
    finally:
        con.close()

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
