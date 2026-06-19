# --- BIBLIOTECA DE FUNCIONES DEL SISTEMA ---

def registrar_ingreso(inventario):
    print("\n--- REGISTRO DE NUEVO LOTE ---")
    
    nombre_prod = input("Ingrese nombre del producto: ")
    
    # Validación de cantidad de cajas (Mientras cantidad_cajas <= 0)
    while True:
        try:
            cantidad_cajas = int(input("Ingrese cantidad de cajas: "))
            if cantidad_cajas > 0:
                break
            else:
                print("ERROR: La cantidad debe ser mayor a 0. Reintente.")
        except ValueError:
            print("ERROR: Por favor ingrese un número entero válido.")
            
    # Validación del peso (Mientras peso_prod <= 0)
    while True:
        try:
            peso_prod = float(input("Ingrese el peso total en Kg: "))
            if peso_prod > 0:
                break
            else:
                print("ERROR: El peso no puede ser negativo o cero. Reintente.")
        except ValueError:
            print("ERROR: Por favor ingrese un número decimal válido.")
            
    # Guardamos los datos en el inventario que recibimos desde el main
    nuevo_lote = {
        "nombre_prod": nombre_prod,
        "cantidad_cajas": cantidad_cajas,
        "peso_prod": peso_prod,
        "tipo_empaque": "No asignado",
        "zona_asignada": "No asignada",
        "cajas_danadas": 0,
        "porcentaje_merma": 0.0,
        "estado_merma": "No evaluado"
    }
    
    inventario.append(nuevo_lote)
    print(f">> Lote de {cantidad_cajas} cajas de {nombre_prod} registrado exitosamente.")


def asignar_zona(inventario):
    print("\n--- ASIGNACIÓN DE ZONA SEGURA ---")
    # Pendiente desarrollar en el siguiente paso
    pass 

def calcular_merma(inventario):
    print("\n--- CÁLCULO DE MERMA ---")
    # Pendiente desarrollar
    pass 

def mostrar_inventario(inventario):
    print("\n--- REPORTE DE STOCK ACTUAL ---")
    # Pendiente desarrollar
    pass 

def guardar_datos(inventario):
    print("\n--- GUARDAR Y SALIR ---")
    # Pendiente desarrollar
    pass