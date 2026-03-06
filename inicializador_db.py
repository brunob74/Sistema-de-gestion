import sqlite3
def inicializar_base_de_datos():
    
    con = sqlite3.connect("database/archie.db")
    cur = con.cursor()
    
    cur.execute("PRAGMA foreign_keys = ON;")
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Productos (
            codigo INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        ) STRICT        
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Inventario (
            id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_producto INTEGER NOT NULL,
            talle INTEGER NOT NULL,
            precio_centavos INTEGER NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >0),
            FOREIGN KEY (codigo_producto) REFERENCE Productos (codigo),
        ) STRICT
    """)
    
    productos_prueba = [
        (1001, "Remera Basica Algodon"),
        (1002, "Pantalon Denim Clasico")
    ]
    cur.executemany("INSERT OR IGNORE INTO Productos (codigo, nombre) VALUES(?,?)", productos_prueba)
    
    inventario_prueba = [
        (1001, 4, 550000, 10),
        (1001, 6, 580000, 5),
        (1002, 12, 1500000, 8),
        (1002, 14, 1500000, 2)
    ]
    cur.executemany("""
        "INSERT INTO Inventario (codigo_producto, talle, precio_centavos, stock) 
        VALUES(?,?,?,?)
    """, inventario_prueba)
    
    con.commit()
    con.close()
    
    print("¡Base de datos 'archie.db' actualizada!")

if __name__ == "__main__":
    inicializar_base_de_datos()


# Hicimos este archivo hoy para matar dos pájaros de un tiro: crear la estructura
# obligatoria que necesitamos, y meternos un par de productos inventados para poder
# empezar a programar las ventas ya mismo, sin depender del Excel.