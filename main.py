import os
# Importamos nuestra biblioteca personalizada con un alias corto (mb)
import modulos_bodega as mb

def menu_principal():
    # Aquí creamos la lista del inventario. Al estar aquí, los datos vivirán 
    # de forma segura durante toda la ejecución del programa.
    inventario_bodega = []
    opcion = 0
    
    while opcion != 5:
        print("\n========================================")
        print("   SISTEMA DE GESTIÓN DE BODEGA V1.0    ")
        print("========================================")
        print("1. Registrar ingreso de cajas")
        print("2. Asignar zona de estiba")
        print("3. Registrar e identificar merma")
        print("4. Consultar inventario")
        print("5. Guardar datos y Salir")
        print("========================================")
        
        try:
            opcion = int(input("Ingrese una opción (1-5): "))
            
            if opcion == 1:
                # Llamamos a la biblioteca pasándole el inventario como argumento
                mb.registrar_ingreso(inventario_bodega)
            elif opcion == 2:
                mb.asignar_zona(inventario_bodega)
            elif opcion == 3:
                mb.calcular_merma(inventario_bodega)
            elif opcion == 4:
                mb.mostrar_inventario(inventario_bodega)
            elif opcion == 5:
                mb.guardar_datos(inventario_bodega)
            else:
                print("ERROR: Opción inválida. Ingrese un número del 1 al 5.")
            
            if opcion != 5:
                input("\nPresione ENTER para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear') 
                
        except ValueError:
            print("ERROR: Por favor ingrese un número válido, no letras.")
            input("\nPresione ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    menu_principal()