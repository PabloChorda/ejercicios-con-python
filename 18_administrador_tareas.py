'''
Crea un programa que funcione como un administrador básico de tareas.

El programa debe permitir al usuario:
Agregar tareas, indicando el título, descripción y prioridad (alta, media, baja).
Listar todas las tareas con su información (incluyendo un estado: "Pendiente" o "Completada").
Marcar una tarea como completada seleccionándola por su índice en la lista.
Eliminar tareas completadas de la lista.
El programa debe manejar entradas inválidas y mostrar menús interactivos para cada opción.
'''

def mostrar_tareas(tareas):
    """
    Muestra la lista de tareas con sus detalles.

    Parámetros:
    tareas (list): Lista de tareas.
    """
    if not tareas:
        print("\nNo hay tareas registradas.")
        return
    
    print("\nTareas:")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i + 1}. [{estado}] {tarea['titulo']} (Prioridad: {tarea['prioridad']})")
        print(f"   Descripción: {tarea['descripcion']}")


def agregar_tarea(tareas):
    """
    Agrega una nueva tarea a la lista de tareas.

    Parámetros:
    tareas (list): Lista de tareas.
    """
    titulo = input("\nTítulo de la tarea: ").strip()
    descripcion = input("Descripción de la tarea: ").strip()
    prioridad = input("Prioridad (alta, media, baja): ").strip().lower()
    
    if prioridad not in ["alta", "media", "baja"]:
        print("Prioridad inválida. Intenta nuevamente.")
        return
    
    tareas.append({"titulo": titulo, "descripcion": descripcion, "prioridad": prioridad, "completada": False})
    print("Tarea agregada con éxito.")


def completar_tarea(tareas):
    """
    Marca una tarea como completada.

    Parámetros:
    tareas (list): Lista de tareas.
    """
    mostrar_tareas(tareas)
    if not tareas:
        return
    
    try:
        indice = int(input("\nNúmero de la tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida. Ingresa un número.")


def eliminar_tareas_completadas(tareas):
    """
    Elimina las tareas que están marcadas como completadas.

    Parámetros:
    tareas (list): Lista de tareas.
    """
    tareas[:] = [tarea for tarea in tareas if not tarea["completada"]]
    print("Tareas completadas eliminadas.")


def main():
    tareas = []
    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tareas completadas")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tareas_completadas(tareas)
        elif opcion == "5":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
