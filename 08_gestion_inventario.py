"""
SISTEMA DE GESTIÓN DE INVENTARIO
Este programa permite al usuario agregar, eliminar y consultar productos en el inventario de una tienda.
"""

def mostrar_menu():
    """
    Imprime el menú de opciones para el sistema de gestión de inventario.
    """
    print("\n=== Sistema de Gestión de Inventario ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Consultar inventario")
    print("4. Salir")

def agregar_producto(inventario):
    """
    Permite al usuario agregar un producto al inventario.

    Parámetros:
    inventario (dict): Diccionario del inventario actual.

    Devuelve:
    dict: Inventario actualizado.
    """
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad > 0:
            inventario[nombre] = inventario.get(nombre, 0) + cantidad
            print(f"{cantidad} unidades de '{nombre}' han sido añadidas al inventario.")
        else:
            print("La cantidad debe ser mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    return inventario

def eliminar_producto(inventario):
    """
    Permite al usuario eliminar un producto del inventario.

    Parámetros:
    inventario (dict): Diccionario del inventario actual.

    Devuelve:
    dict: Inventario actualizado.
    """
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        try:
            cantidad = int(input(f"Ingrese la cantidad a eliminar de '{nombre}': "))
            if 0 < cantidad <= inventario[nombre]:
                inventario[nombre] -= cantidad
                print(f"{cantidad} unidades de '{nombre}' han sido eliminadas del inventario.")
                if inventario[nombre] == 0:
                    del inventario[nombre]  # Elimina el producto si la cantidad llega a cero
            elif cantidad > inventario[nombre]:
                print("No hay suficientes unidades para eliminar esa cantidad.")
            else:
                print("La cantidad debe ser mayor a cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
    return inventario

def consultar_inventario(inventario):
    """
    Muestra el inventario actual.

    Parámetros:
    inventario (dict): Diccionario del inventario actual.
    """
    if inventario:
        print("\nInventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad} unidades")
    else:
        print("El inventario está vacío.")

def main():
    """
    Función principal que permite al usuario interactuar con el sistema de gestión de inventario.
    """
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            inventario = agregar_producto(inventario)
        elif opcion == "2":
            inventario = eliminar_producto(inventario)
        elif opcion == "3":
            consultar_inventario(inventario)
        elif opcion == "4":
            print("Gracias por utilizar el sistema de gestión de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
