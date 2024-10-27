"""
CAJERO AUTOMÁTICO SIMPLIFICADO
Este programa permite al usuario realizar operaciones básicas de un cajero automático:
consultar saldo, depositar dinero y retirar-lo.
"""

def mostrar_menu():
    """
    Imprime el menú de opciones para el cajero automático.
    """
    print("\n=== Cajero Automático ===")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def consultar_saldo(saldo):
    """
    Muestra el saldo actual.
    
    Parámetros:
    saldo (float): Saldo de la cuenta.
    """
    print(f"Saldo actual: ${saldo:.2f}")

def depositar(saldo):
    """
    Permite al usuario depositar dinero en su cuenta.
    
    Parámetros:
    saldo (float): Saldo de la cuenta.
    
    Devuelve:
    float: Nuevo saldo tras el depósito.
    """
    try:
        cantidad = float(input("Ingrese la cantidad a depositar: $"))
        if cantidad > 0:
            saldo += cantidad
            print(f"Has depositado ${cantidad:.2f}. Saldo actualizado: ${saldo:.2f}")
        else:
            print("La cantidad debe ser mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")
    return saldo

def retirar(saldo):
    """
    Permite al usuario retirar dinero de su cuenta.
    
    Parámetros:
    saldo (float): Saldo de la cuenta.
    
    Devuelve:
    float: Nuevo saldo tras el retiro.
    """
    try:
        cantidad = float(input("Ingrese la cantidad a retirar: $"))
        if 0 < cantidad <= saldo:
            saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Saldo actualizado: ${saldo:.2f}")
        elif cantidad > saldo:
            print("Fondos insuficientes.")
        else:
            print("La cantidad debe ser mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")
    return saldo

def main():
    """
    Función principal que permite al usuario interactuar con el cajero automático.
    """
    saldo = 1000.0  # Saldo inicial
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
