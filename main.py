import customtkinter as ctk
import logica_inventario
from tkinter import ttk

ctk.set_appearance_mode("dark")

def regla_codigo(texto):
    if texto == "" or (texto.isdigit() and len(texto) <=4):
        return True
    return False
def regla_cantidad(texto):
    if texto == "" or (texto.isdigit() and len(texto) <= 4):
        return True
    return False
def regla_nombre(texto):
    if texto == "" or ( all(c.isalpha() or c.isspace() for c in texto)):
        return True
    return False

def mostrar_en_contenido(frame_a_mostrar):
    for hijo in frame_contenido.winfo_children():
        hijo.pack_forget()
    frame_a_mostrar.pack(expand=True, fill="both")

def iniciar_aplicacion():
    ventana = ctk.CTk()
    ventana.title("SISTEMA TIENDA - Gestión de Ventas")
    ventana.geometry('1280x720')
    ventana.configure()
    
    validar_cod = ventana.register(regla_codigo)
    validar_cant = ventana.register(regla_cantidad)
    validar_nombre = ventana.register(regla_nombre)
    
    
    frame_menu = ctk.CTkFrame(ventana, fg_color="#313131", width=350, corner_radius=0)
    frame_menu.pack(side = "left", fill="y")
    global frame_contenido
    frame_contenido = ctk.CTkFrame(ventana)
    frame_contenido.pack(side="right", fill="both", expand = True )
    
    
    titulo = ctk.CTkLabel(frame_menu, text="Tienda Menu", text_color="white", font=("Arial", 28, "bold"))
    titulo.pack(pady=30)
    
    btn_venta = ctk.CTkButton(frame_menu, text="Registrar venta", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#0B7B56",
                                command=lambda: mostrar_en_contenido(frame_ventas))
    
    btn_consulta = ctk.CTkButton(frame_menu, text="Consultar stock", fg_color="#313131", text_color="white", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#3E3E42",
                                command=lambda: mostrar_en_contenido(frame_consulta))
    
    btn_listado = ctk.CTkButton(frame_menu, text="Listado ventas diarias", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#3E3E42")
    btn_modificar = ctk.CTkButton(frame_menu, text="Modificar venta", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#3E3E42")
    btn_eliminar = ctk.CTkButton(frame_menu, text="Eliminar venta", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#711111")
    btn_excel = ctk.CTkButton(frame_menu, text="Cargar/Actualizar Productos", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#3E3E42")
    
    
    btn_venta.pack(pady=10, fill="x")
    btn_consulta.pack(pady=10, fill="x")
    btn_listado.pack(pady=10, fill="x")
    btn_modificar.pack(pady=(50,10), fill="x")
    btn_eliminar.pack(pady=10, fill="x")
    btn_excel.pack(pady=10, fill="x")
    
    
    
#===================================================================================
    
    
    frame_consulta = ctk.CTkFrame(frame_contenido, fg_color="transparent")
    
    titulo_consulta = ctk.CTkLabel(frame_consulta, text="Consulta de stock", text_color="#FFFFFF", font=("Arial", 28, "bold"))
    titulo_consulta.pack(pady=(30, 20))
    
    # --- Creo un "Frame Formulario" para agrupar las cosas ---
    frame_formulario = ctk.CTkFrame(frame_consulta, fg_color="transparent")
    frame_formulario.pack(pady =10)
    
    lbl_codigo = ctk.CTkLabel(frame_formulario, text="Codigo del producto", font=("Arial", 16))
    lbl_codigo.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
    
    
    
    def buscar_stock(_event=None):
        cod_ingresado = entrada_codigo.get()
        if cod_ingresado == "":
            lbl_resultado.configure(text="Por favor, ingrese un codigo", text_color="#FFCC00")
            return
        stock = logica_inventario.consultar_stock(int(cod_ingresado))
        if stock == "-1":
            lbl_resultado.configure(text= "Producto no encontrado", text_color="#FF4C4C")
        else:
            lbl_resultado.configure(text= f"Se encontraron {stock} unidades del producto {cod_ingresado}", text_color="#38FC6C")
        
        entrada_codigo.delete(0,"end")
    
    
    entrada_codigo = ctk.CTkEntry(frame_formulario, fg_color = "white", text_color = "#242424", font=("Arial", 16),
                                validate="key", validatecommand=(validar_cod, "%P"))
    entrada_codigo.grid(row=0, column=1, pady=10, padx=10, sticky="w")
    
    entrada_codigo.bind("<Return>", buscar_stock)
    btn_buscar = ctk.CTkButton(frame_formulario, text="Buscar", font=("Arial", 16),
                                command=buscar_stock)
    btn_buscar.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
    
    lbl_resultado = ctk.CTkLabel(frame_formulario, text=" ", font=("Arial", 18, "bold"), width=500, height=30)
    lbl_resultado.grid(row=3, column=0, columnspan=2, pady=10)
#====================================================================================   
    
    frame_ventas = ctk.CTkFrame(frame_contenido, fg_color="transparent")
    
    titulo_ventas = ctk.CTkLabel(frame_ventas, text="Registro de ventas", text_color="#FFFFFF", font=("Arial", 28, "bold"))
    titulo_ventas.pack(pady=(30, 20))
    
    frame_contventas = ctk.CTkFrame(frame_ventas, fg_color="transparent")
    frame_contventas.pack(expand=True, fill="both", padx=20)
    
    col_izq = ctk.CTkFrame(frame_contventas, width=400, fg_color="transparent")
    col_izq.pack(side="left", fill="both", padx=10, pady=10)
    col_izq.pack_propagate(False)
    
    lbl_encabezado = ctk.CTkLabel(col_izq, text="Datos de la venta", font=("Arial", 18, "bold"))
    lbl_encabezado.grid(row = 0, column=0, columnspan=2, pady=10)
    
    lbl_nombre = ctk.CTkLabel(col_izq, text="Nombre del cliente:", font=("Arial", 16))
    lbl_nombre.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
    lbl_codigo = ctk.CTkLabel(col_izq, text="Codigo:", font=("Arial", 16))
    lbl_codigo.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
    lbl_cant = ctk.CTkLabel(col_izq, text="Cantidad:", font=("Arial", 16))
    lbl_cant.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
    
    def agregar_producto():
        cod = entrada_cod2.get()
        cant = entrada_cantidad.get()
        cliente = entrada_nombre.get().title()
        if not cod or not cant:
            return
        ## nombre_formateado
        
        datos = logica_inventario.obtener_producto_para_venta(int(cod))
        if datos:
            nombre_prod = datos[0]
            precio_centavos = datos[1]
            stock_actual = int(datos[2])
            
            if int(cant) > stock_actual:
                print("No hay stock suficiente") # Aquí podrías usar un Label de error
                return
            precio_pesos = precio_centavos / 100
            subtotal = precio_pesos * int(cant)
            
            tabla_ventas.insert("", "end", values=(cod, cliente, nombre_prod, cant, f"$ {subtotal:.2f}"))
            entrada_cod2.delete(0, "end")
            entrada_cantidad.delete(0, "end")
            entrada_cod2.focus()
        else:
            print("Producto no encontrado")
    
    entrada_nombre = ctk.CTkEntry(col_izq, fg_color="#5A5A5A", font=("Arial", 16), width=270, validate="key", validatecommand=(validar_nombre, "%P"))
    entrada_nombre.grid(row=1, column=1, pady=10)
    nombre_formateado = entrada_nombre.get().title()
    entrada_cod2 = ctk.CTkEntry(col_izq, fg_color="#5A5A5A", font=("Arial", 16), width=270, validate="key", validatecommand=(validar_cod, "%P"))
    entrada_cod2.grid(row=2, column=1, pady=10)
    entrada_cantidad= ctk.CTkEntry(col_izq, fg_color="#5A5A5A",font=("Arial", 16), width=270, validate="key", validatecommand=(validar_cant, "%P"))
    entrada_cantidad.grid(row=3, column=1, pady=10)
    
    btn_carrito = ctk.CTkButton(col_izq, text="AGREGAR", fg_color="#078E00", text_color="white", font=("Arial", 16, "bold"), hover_color="#013B09", height=40,
                                command=agregar_producto)
    btn_carrito.grid(row=4, column=0, columnspan=2, pady=30)
    
    
    col_der = ctk.CTkFrame(frame_contventas, fg_color="transparent", height= 500, width=1100)
    col_der.pack(side="right", fill="y", expand=True, padx=10, pady=10)
    col_der.pack_propagate(False)
    
    frame_sup = ctk.CTkFrame(col_der, fg_color="transparent", height=500)
    frame_sup.pack(side="top", fill="both", expand=True)
    frame_sup.pack_propagate(False)
    columnas=("codigo","cliente", "producto", "cantidad", "subtotal")
    tabla_ventas= ttk.Treeview(frame_sup, columns=columnas,displaycolumns=("cliente", "producto", "cantidad", "subtotal"), show="headings")
    
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                background="#2b2b2b",      # Fondo de las filas
                foreground="white",        # Color de la letra
                fieldbackground="#4E4E4E", # Fondo del área vacía
                bordercolor="#333333",
                borderwidth=0,
                font=("Arial", 12))
    
    style.configure("Treeview.Heading",
                background="#333333",      # Fondo del encabezado
                foreground="white",        # Letra del encabezado
                relief="flat",
                font=("Arial", 12, "bold"))
    
    style.map("Treeview", background=[('selected', "#254f7e")]) # Azul oscuro al seleccionar
    style.map("Treeview.Heading", background=[('active', "#3E3E42")])
    
    tabla_ventas.heading("cliente", text="CLIENTE")
    tabla_ventas.heading("producto", text="PRODUCTO")
    tabla_ventas.heading("cantidad", text="CANTIDAD")
    tabla_ventas.heading("subtotal", text="SUBTOTAL")
    tabla_ventas.column("codigo", width=0, stretch=False)
    tabla_ventas.column("cliente",width=150, anchor="w")
    tabla_ventas.column("producto",width=250, anchor="w")
    tabla_ventas.column("cantidad",width=100, anchor="center")
    tabla_ventas.column("subtotal",width=120, anchor= "e")
    
    scroll_tabla = ctk.CTkScrollbar(frame_sup, orientation="vertical", command=tabla_ventas.yview)
    tabla_ventas.configure(yscrollcommand=scroll_tabla.set)
    scroll_tabla.pack(side="right", fill="y")
    tabla_ventas.pack(side="left", fill="both", expand=True)
    
    frame_bot= ctk.CTkFrame(col_der, fg_color="transparent")
    frame_bot.pack(side="bottom", fill="both", expand=True)
    frame_bot.pack_propagate(False)
    
    frame_cobrar= ctk.CTkFrame(frame_bot, fg_color="transparent")
    frame_cobrar.pack(side="left", fill="both", expand=True)
    btn_cobrar = ctk.CTkButton(frame_cobrar, text="COBRAR", fg_color="#078E00", text_color="white", font=("Arial", 16, "bold"), hover_color="#013B09", height=40)
    btn_cobrar.pack(pady=30)
    
    
    def eliminar_item_seleccionado():
        seleccion = tabla_ventas.selection()
        for item in seleccion: 
            tabla_ventas.delete(item)
        btn_eliminar.configure(state="disabled")
        #actualizar_total_venta()
    
    def limpiar_tabla_completa():
        for item in tabla_ventas.get_children():
            tabla_ventas.delete(item)
        #actualizar_total_venta()
    
    def subir_datos_a_campos():
        seleccion = tabla_ventas.selection()
        if not seleccion:
            return
        item_ID = seleccion[0]
        # Si la fila decía "xxxx |Bruno | Alfajor | 2 | $3000", 
        # la variable valores ahora guarda exactamente esa lista de palabras.
        valores = tabla_ventas.item(item_ID, "values") 
        
        entrada_nombre.delete(0, "end")
        entrada_cod2.delete(0, "end")
        entrada_cantidad.delete(0,"end")
        
        entrada_nombre.insert(0,valores[1])
        entrada_cod2.insert(0, valores[0])
        entrada_cantidad.insert(0,valores[3])
        
        tabla_ventas.delete(item_ID)
    
    frame_botones_tabla = ctk.CTkFrame(frame_bot, fg_color="transparent")
    frame_botones_tabla.pack(side="right", fill="both", expand=True, pady=30)
    
    btn_modificar = ctk.CTkButton(frame_botones_tabla, text="Modificar", state="disabled",  text_color="white", font=("Arial", 16, "bold"), height=40,
                                    command=subir_datos_a_campos )
    btn_modificar.grid(row=0, column=0, padx=20)
    
    btn_eliminar = ctk.CTkButton(frame_botones_tabla, text="Eliminar Item", state="disabled", fg_color="#812A2A", text_color="white", font=("Arial", 16, "bold"), height=40,
                                    command=eliminar_item_seleccionado)
    btn_eliminar.grid(row=0,column=1, padx=20)
    
    
    btn_limpiar = ctk.CTkButton(frame_botones_tabla, text="Vaciar Carrito", text_color="white", font=("Arial", 16, "bold"), height=40,
                            command=limpiar_tabla_completa)
    btn_limpiar.grid(row=0,column=2, padx=20)
    
    
    
    def manejar_seleccion_tabla(event):
        seleccion = tabla_ventas.selection()
        if seleccion:
            # Si hay algo marcado, habilitamos los botones
            btn_eliminar.configure(state="normal")
            btn_modificar.configure(state="normal")
        else:
            # Si no hay nada, los volvemos a dormir
            btn_eliminar.configure(state="disabled")
            btn_modificar.configure(state="disabled")
    tabla_ventas.bind("<<TreeviewSelect>>", manejar_seleccion_tabla)
    
    
    
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()