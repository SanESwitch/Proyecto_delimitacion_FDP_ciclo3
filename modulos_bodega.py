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
    
    # 1. Validación de seguridad: Verificar si hay lotes en el inventario
    if not inventario:
        print("ERROR: No hay lotes registrados en el inventario. Use la opción 1 primero.")
        return

    # 2. Mostrar los lotes registrados para que el usuario elija cuál evaluar
    print("Seleccione el lote para registrar mermas:")
    for i, lote in enumerate(inventario):
        print(f"  {i + 1}. Producto: {lote['nombre_prod']} | Total Cajas: {lote['cantidad_cajas']} | Merma actual: {lote['porcentaje_merma']:.2f}%")
        
    # 3. Validar la selección del lote
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

    # Tomamos de forma automática las cajas totales guardadas en el lote
    cajas_totales = lote_seleccionado["cantidad_cajas"]
    print(f"\nProducto seleccionado: {lote_seleccionado['nombre_prod']} (Total de cajas en stock: {cajas_totales})")

    # 4. Leer y validar las cajas dañadas (Equivalente al condicional Si cajas_danadas > cajas_totales)
    while True:
        try:
            cajas_danadas = int(input("Ingrese cantidad de cajas dañadas/aplastadas: "))
            if cajas_danadas < 0:
                print("ERROR: Las cajas dañadas no pueden ser un número negativo.")
            elif cajas_danadas > cajas_totales:
                print(f"ERROR: Las cajas dañadas ({cajas_danadas}) no pueden superar el total de cajas ({cajas_totales}). Reintente.")
            else:
                break # Entrada válida, salimos del bucle
        except ValueError:
            print("ERROR: Por favor ingrese un número entero válido.")

    # 5. Cálculo del porcentaje de merma (Fórmula exacta de tu pseudocódigo)
    porcentaje_merma = (cajas_danadas / cajas_totales) * 100
    
    # Guardamos los resultados dentro de nuestro lote seleccionado
    lote_seleccionado["cajas_danadas"] = cajas_danadas
    lote_seleccionado["porcentaje_merma"] = porcentaje_merma
    
    print(f">> Porcentaje de merma: {porcentaje_merma:.2f}%")
    
    # 6. Evaluación de Umbrales (Estructura Si-Entonces-Sino de tu pseudocódigo)
    if porcentaje_merma > 15:
        lote_seleccionado["estado_merma"] = "ALERTA ROJA"
        print("ALERTA ROJA: Merma excesiva, revisar estiba urgente.")
    else:
        lote_seleccionado["estado_merma"] = "Aceptable"
        print("Estado Aceptable.")

def mostrar_inventario(inventario):
    print("\n--- REPORTE DE STOCK ACTUAL ---")
    
    # 1. Validación de seguridad: Si no hay datos registrados
    if not inventario:
        print("El inventario está vacío. No hay lotes registrados para mostrar.")
        print(">> Fin del reporte.")
        return

    print("Generando listado de zonas y productos en tiempo real...\n")
    
    # Cabecera de nuestra tabla informativa
    # Los símbolos <15, <8, etc., sirven para alinear el texto en columnas perfectas
    print(f"{'N°':<3} | {'Producto':<15} | {'Cajas':<6} | {'Peso (Kg)':<9} | {'Zona Asignada':<25} | {'Merma':<7} | {'Estado Stock'}")
    print("-" * 95)
    
    # 2. Recorrer los "arreglos reales" (lista de diccionarios) para imprimir cada lote
    for i, lote in enumerate(inventario):
        nombre = lote["nombre_prod"]
        cajas = lote["cantidad_cajas"]
        peso = lote["peso_prod"]
        zona = lote["zona_asignada"]
        merma = lote["porcentaje_merma"]
        estado = lote["estado_merma"]
        
        # Determinar el color/estado de disponibilidad según las reglas del proyecto
        if estado == "ALERTA ROJA":
            estado_visual = "ROJO (Merma Excesiva)"
        elif estado == "Aceptable":
            estado_visual = "VERDE (Disponible)"
        else:
            estado_visual = "VERDE (Sin evaluar merma)"
            
        # Imprimir la fila formateada
        print(f"{i + 1:<3} | {nombre:<15} | {cajas:<6} | {peso:<9.1f} | {zona:<25} | {merma:<5.1f}% | {estado_visual}")
        
    print("\n>> Fin del reporte.")

def guardar_datos(inventario):
    print("\n--- GUARDAR Y SALIR ---")
    # Pendiente desarrollar
    pass