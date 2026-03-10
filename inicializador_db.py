import sqlite3
def inicializar_base_de_datos():
    
    con = sqlite3.connect("database/tienda.db")
    cur = con.cursor()
    
    cur.execute("PRAGMA foreign_keys = ON;")
    
    cur.execute(""" DROP TABLE IF EXISTS Ventas """)
    cur.execute(""" DROP TABLE IF EXISTS Productos """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Productos (
            codigo INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio_centavos INTEGER NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0)
        )STRICT
    """)
    
    productos_prueba = [
        (1001, "Martillo", "Ferreteria", 1000000, 10),
        (1002,"Cuaderno" , "Libreria", 580000, 5),
        (1003, "Heladera", "Electrodomesticos", 40000000, 8),
    ]
    cur.executemany("""
        INSERT OR IGNORE INTO Productos(codigo, nombre, categoria, precio_centavos, stock) 
        VALUES(?,?,?,?,?)
    """, productos_prueba)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS Ventas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha_venta TEXT DEFAULT CURRENT_TIMESTAMP,
                    cliente TEXT NOT NULL,
                    codigo_producto INTEGER NOT NULL,
                    nombre_producto TEXT NOT NULL,
                    cantidad INTEGER NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY(codigo_producto) REFERENCES Productos(codigo)
                )STRICT
            """)
    
    
    
    
    
    
    
    
    
    
    
    con.commit()
    con.close()
    
    print("¡Base de datos 'tienda.db' actualizada!")

if __name__ == "__main__":
    inicializar_base_de_datos()

# Hicimos este archivo hoy para matar dos pájaros de un tiro: crear la estructura
# obligatoria que necesitamos, y meternos un par de productos inventados para poder
# empezar a programar las ventas ya mismo, sin depender del Excel.