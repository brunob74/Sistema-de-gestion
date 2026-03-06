import customtkinter as ctk

ctk.set_appearance_mode("dark")

def regla_codigo(texto):
    if texto == "" or (texto.isdigit() and len(texto) <=4):
        return True
    return False
def regla_talle(texto):
    if texto == "" or (texto.isdigit() and len(texto) <=2):
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
    
    frame_menu = ctk.CTkFrame(ventana, fg_color="#313131", width=350, corner_radius=0)
    frame_menu.pack(side = "left", fill="y")
    global frame_contenido
    frame_contenido = ctk.CTkFrame(ventana)
    frame_contenido.pack(side="right", fill="both", expand = True )
    
    
    titulo = ctk.CTkLabel(frame_menu, text="Tienda Menu", text_color="white", font=("Arial", 28, "bold"))
    titulo.pack(pady=30)
    
    btn_venta = ctk.CTkButton(frame_menu, text="Registrar venta", fg_color="#313131", text_color="#DCE4EE", font=("Arial", 16, "bold"), width=300, height=40, hover_color="#0B7B56")
    
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
    entrada_codigo = ctk.CTkEntry(frame_formulario, fg_color = "white", text_color = "#242424", font=("Arial", 16),
                                validate="key", validatecommand=(validar_cod, "%P"))
    entrada_codigo.grid(row=0, column=1, pady=10, padx=10, sticky="w")
    
    
    btn_buscar = ctk.CTkButton(frame_formulario, text="Buscar", font=("Arial", 16))
    btn_buscar.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
    #====================================================================================
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()