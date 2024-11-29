'''
Crea un programa para gestionar las reservas de un gimnasio. 
El sistema debe permitir registrar clases (como yoga, spinning, pilates, etc.), gestionar clientes, y realizar reservas para las clases. Además, debe generar reportes de asistencia y guardar los datos en un archivo JSON.
Funcionalidades principales:

Agregar nuevas clases con nombre, descripción, capacidad máxima y horario.
Modificar información de clases existentes.
Eliminar clases.
Gestión de clientes:

Registrar nuevos clientes con nombre, correo electrónico y teléfono.
Modificar datos de clientes.
Eliminar clientes.
Reservas:

Permitir a los clientes reservar un lugar en una clase.
Controlar la capacidad máxima de la clase (no se puede exceder).
Cancelar reservas.
Reportes:

Mostrar las clases disponibles y sus horarios.
Generar un informe de reservas realizadas por cliente o por clase.
Persistencia de datos:

Guardar y cargar datos en un archivo JSON para clases, clientes y reservas.

'''

import json

class Gimnasio:
    def __init__(self, archivo="gimnasio.json"):
        self.archivo = archivo
        self.clases = {}
        self.clientes = {}
        self.reservas = {}
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
                self.clases = datos.get("clases", {})
                self.clientes = datos.get("clientes", {})
                self.reservas = datos.get("reservas", {})
        except FileNotFoundError:
            self.clases = {}
            self.clientes = {}
            self.reservas = {}

    def guardar_datos(self):
        with open(self.archivo, "w") as file:
            json.dump({
                "clases": self.clases,
                "clientes": self.clientes,
                "reservas": self.reservas
            }, file, indent=4)

    def agregar_clase(self, id_clase, nombre, descripcion, capacidad, horario):
        if id_clase in self.clases:
            print("Error: Ya existe una clase con este ID.")
            return
        self.clases[id_clase] = {
            "nombre": nombre,
            "descripcion": descripcion,
            "capacidad": capacidad,
            "horario": horario,
            "reservas": 0
        }
        print(f"Clase '{nombre}' agregada correctamente.")

    def registrar_cliente(self, id_cliente, nombre, correo, telefono):
        if id_cliente in self.clientes:
            print("Error: Ya existe un cliente con este ID.")
            return
        self.clientes[id_cliente] = {"nombre": nombre, "correo": correo, "telefono": telefono}
        print(f"Cliente '{nombre}' registrado correctamente.")

    def reservar_clase(self, id_cliente, id_clase):
        if id_cliente not in self.clientes:
            print("Error: Cliente no registrado.")
            return
        if id_clase not in self.clases:
            print("Error: Clase no encontrada.")
            return
        clase = self.clases[id_clase]
        if clase["reservas"] >= clase["capacidad"]:
            print("Error: Clase llena.")
            return
        self.reservas.setdefault(id_clase, []).append(id_cliente)
        clase["reservas"] += 1
        print(f"Reserva confirmada para el cliente '{self.clientes[id_cliente]['nombre']}' en la clase '{clase['nombre']}'.")

    def mostrar_clases(self):
        print("\n--- Clases Disponibles ---")
        for id_clase, datos in self.clases.items():
            print(f"ID: {id_clase} | Nombre: {datos['nombre']} | Capacidad: {datos['capacidad']} | Horario: {datos['horario']} | Reservas: {datos['reservas']}")
        print("-------------------------\n")

    def mostrar_reporte_reservas(self):
        print("\n--- Reporte de Reservas ---")
        for id_clase, lista_reservas in self.reservas.items():
            clase = self.clases[id_clase]
            print(f"Clase: {clase['nombre']} | Reservas: {len(lista_reservas)}")
            for id_cliente in lista_reservas:
                cliente = self.clientes[id_cliente]
                print(f"- Cliente: {cliente['nombre']} ({cliente['correo']})")
        print("-------------------------\n")


# Programa principal
def main():
    gimnasio = Gimnasio()

    while True:
        print("\n--- Menú de Gestión de Gimnasio ---")
        print("1. Agregar clase")
        print("2. Registrar cliente")
        print("3. Reservar clase")
        print("4. Mostrar clases disponibles")
        print("5. Mostrar reporte de reservas")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_clase = input("Ingrese el ID de la clase: ")
            nombre = input("Ingrese el nombre de la clase: ")
            descripcion = input("Ingrese una breve descripción de la clase: ")
            capacidad = int(input("Ingrese la capacidad máxima de la clase: "))
            horario = input("Ingrese el horario de la clase: ")
            gimnasio.agregar_clase(id_clase, nombre, descripcion, capacidad, horario)
        elif opcion == "2":
            id_cliente = input("Ingrese el ID del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            correo = input("Ingrese el correo electrónico del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            gimnasio.registrar_cliente(id_cliente, nombre, correo, telefono)
        elif opcion == "3":
            id_cliente = input("Ingrese el ID del cliente: ")
            id_clase = input("Ingrese el ID de la clase a reservar: ")
            gimnasio.reservar_clase(id_cliente, id_clase)
        elif opcion == "4":
            gimnasio.mostrar_clases()
        elif opcion == "5":
            gimnasio.mostrar_reporte_reservas()
        elif opcion == "6":
            gimnasio.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
