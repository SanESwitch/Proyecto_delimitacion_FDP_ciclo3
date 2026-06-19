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
    
    # 1. Validación de seguridad: Verificar si hay lotes en el inventario
    if not inventario:
        print("ERROR: No hay lotes registrados en el inventario. Use la opción 1 primero.")
        return # Sale de la función y regresa al menú

    # 2. Mostrar los lotes registrados para que el usuario elija cuál configurar
    print("Seleccione el lote al que desea asignar la zona:")
    for i, lote in enumerate(inventario):
        print(f"  {i + 1}. Producto: {lote['nombre_prod']} | Cajas: {lote['cantidad_cajas']} | Zona actual: {lote['zona_asignada']}")
        
    # 3. Validar que la opción elegida por el usuario sea correcta
    while True:
        try:
            seleccion = int(input("Ingrese el número del lote (ej. 1): "))
            if 1 <= seleccion <= len(inventario):
                lote_seleccionado = inventario[seleccion - 1]
                break
            else:
                print(f"ERROR: Selección inválida. Elija un número entre 1 y {len(inventario)}.")
        except ValueError:
            print("ERROR: Por favor ingrese un número entero válido.")

    # 4. Solicitar el tipo de empaque (Equivalente al Leer tipo_empaque del pseudocódigo)
    print("\nTipos de empaque sugeridos: Carton, Plastico, Saco")
    tipo_empaque = input("Ingrese tipo de empaque: ").strip().capitalize()
    
    # 5. Estructura Condicional idéntica a tu pseudocódigo (Si-Entonces-Sino)
    if tipo_empaque == "Carton":
        lote_seleccionado["tipo_empaque"] = "Carton"
        lote_seleccionado["zona_asignada"] = "BAJA (Máximo 2 niveles)"
        print(">> Etiqueta A Frágil. Zona asignada: BAJA (Máximo 2 niveles).")
        
    elif tipo_empaque == "Saco":
        lote_seleccionado["tipo_empaque"] = "Saco"
        lote_seleccionado["zona_asignada"] = "SUELO"
        print(">> Etiqueta B Pesado. Zona asignada: SUELO.")
        
    else:
        # Si el usuario ingresa Plastico o cualquier otro valor estándar
        lote_seleccionado["tipo_empaque"] = tipo_empaque if tipo_empaque else "Plastico"
        lote_seleccionado["zona_asignada"] = "MEDIA"
        print(">> Etiqueta C Estándar. Zona asignada: MEDIA.")
        
    print(f">> Configuración guardada para el lote de {lote_seleccionado['nombre_prod']}.")

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