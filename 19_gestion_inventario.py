"""
Crea un programa para gestionar el inventario de un pequeño negocio. 
El sistema debe permitir agregar, eliminar, actualizar y buscar productos 
en el inventario. También incluirá la funcionalidad de registrar ventas y calcular el stock disponible en tiempo real.

Funcionalidades principales:
Gestión de productos:
Agregar nuevos productos con nombre, precio y cantidad inicial.
Modificar información de productos existentes.
Eliminar productos del inventario.
Búsqueda de productos:
Buscar productos por nombre o ID.
Registro de ventas:
Registrar una venta y disminuir automáticamente el stock del producto.
Reportes:
Mostrar el inventario actual.
Generar un informe de ventas con totales acumulados.
Persistencia de datos:
Guardar y cargar los datos del inventario en un archivo JSON.
"""

import json

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
                self.productos = datos.get("productos", {})
                self.ventas = datos.get("ventas", [])
        except FileNotFoundError:
            self.productos = {}
            self.ventas = []

    def guardar_datos(self):
        with open(self.archivo, "w") as file:
            json.dump({"productos": self.productos, "ventas": self.ventas}, file, indent=4)

    def agregar_producto(self, id_producto, nombre, precio, cantidad):
        if id_producto in self.productos:
            print("Error: Ya existe un producto con este ID.")
            return
        self.productos[id_producto] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"Producto '{nombre}' agregado correctamente.")

    def modificar_producto(self, id_producto, nombre=None, precio=None, cantidad=None):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return
        if nombre:
            self.productos[id_producto]["nombre"] = nombre
        if precio:
            self.productos[id_producto]["precio"] = precio
        if cantidad is not None:
            self.productos[id_producto]["cantidad"] = cantidad
        print(f"Producto '{id_producto}' actualizado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto '{id_producto}' eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto, None)

    def registrar_venta(self, id_producto, cantidad_vendida):
        if id_producto not in self.productos:
            print("Error: Producto no encontrado.")
            return
        producto = self.productos[id_producto]
        if producto["cantidad"] < cantidad_vendida:
            print("Error: Stock insuficiente.")
            return
        producto["cantidad"] -= cantidad_vendida
        total_venta = cantidad_vendida * producto["precio"]
        self.ventas.append({"id_producto": id_producto, "cantidad": cantidad_vendida, "total": total_venta})
        print(f"Venta registrada: {cantidad_vendida} unidades de '{producto['nombre']}' por un total de ${total_venta:.2f}.")

    def mostrar_inventario(self):
        print("\n--- Inventario Actual ---")
        for id_producto, datos in self.productos.items():
            print(f"ID: {id_producto} | Nombre: {datos['nombre']} | Precio: ${datos['precio']:.2f} | Stock: {datos['cantidad']}")
        print("-------------------------\n")

    def mostrar_reporte_ventas(self):
        print("\n--- Reporte de Ventas ---")
        if not self.ventas:
            print("No se han registrado ventas.")
            return
        total_acumulado = 0
        for venta in self.ventas:
            producto = self.productos.get(venta["id_producto"], {"nombre": "Desconocido"})
            print(f"Producto: {producto['nombre']} | Cantidad: {venta['cantidad']} | Total: ${venta['total']:.2f}")
            total_acumulado += venta["total"]
        print(f"Total acumulado: ${total_acumulado:.2f}")
        print("-------------------------\n")

# Programa principal
def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Registrar venta")
        print("6. Mostrar inventario")
        print("7. Mostrar reporte de ventas")
        print("8. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad inicial del producto: "))
            inventario.agregar_producto(id_producto, nombre, precio, cantidad)
        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a modificar: ")
            nombre = input("Nuevo nombre (deje vacío para no cambiar): ") or None
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            precio = float(precio) if precio else None
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            inventario.modificar_producto(id_producto, nombre, precio, cantidad)
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "4":
            id_producto = input("Ingrese el ID del producto a buscar: ")
            producto = inventario.buscar_producto(id_producto)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            id_producto = input("Ingrese el ID del producto vendido: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            inventario.registrar_venta(id_producto, cantidad)
        elif opcion == "6":
            inventario.mostrar_inventario()
        elif opcion == "7":
            inventario.mostrar_reporte_ventas()
        elif opcion == "8":
            inventario.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
