'''

Juego de Bolsa de Valores
Eres un inversor que tiene un capital inicial de $10,000 y decides entrar al mercado de valores. En cada turno, verás una lista de acciones con precios que fluctúan de forma aleatoria.

Tu objetivo es comprar y vender acciones estratégicamente para obtener la mayor cantidad de dinero posible en 10 turnos.
Al final del juego, verás tu capital final y si has generado ganancias o pérdidas.

Reglas y características:
Puedes comprar o vender acciones en cada turno.
Cada acción tiene un precio aleatorio que cambia en cada turno.
Si vendes acciones, obtendrás dinero basado en el precio actual.
Ganas si tu capital supera los $10,000 al final de los 10 turnos.

'''

import random

def mostrar_acciones(acciones):
    print("\n=== PRECIOS DE LAS ACCIONES ===")
    for i, (nombre, precio) in enumerate(acciones.items(), 1):
        print(f"{i}. {nombre}: ${precio}")
    print("===============================\n")

def jugar_bolsa():
    # Configuración inicial
    capital = 10000
    acciones_disponibles = {
        "Tesla": random.randint(50, 500),
        "Apple": random.randint(50, 500),
        "Amazon": random.randint(50, 500),
        "Google": random.randint(50, 500),
        "Meta": random.randint(50, 500)
    }
    portafolio = {accion: 0 for accion in acciones_disponibles.keys()}
    turnos = 10

    print("\n¡Bienvenido al Juego de Bolsa de Valores!")
    print(f"Tienes un capital inicial de ${capital}.\n")

    for turno in range(1, turnos + 1):
        print(f"\n=== TURNO {turno} ===")
        mostrar_acciones(acciones_disponibles)
        print(f"Tu capital actual: ${capital}")
        print("Tu portafolio:")
        for accion, cantidad in portafolio.items():
            if cantidad > 0:
                print(f"- {accion}: {cantidad} acciones")
        print("\n¿Qué quieres hacer?")
        print("1. Comprar acciones")
        print("2. Vender acciones")
        print("3. Pasar turno")
        eleccion = input("Elige una opción (1/2/3): ").strip()

        if eleccion == "1":  # Comprar acciones
            accion_a_comprar = input("¿Qué acción quieres comprar? (Escribe el nombre): ").strip()
            if accion_a_comprar in acciones_disponibles:
                precio = acciones_disponibles[accion_a_comprar]
                try:
                    cantidad_a_comprar = int(input(f"El precio actual de {accion_a_comprar} es ${precio}. ¿Cuántas quieres comprar?: "))
                    if cantidad_a_comprar < 0:
                        print("No puedes comprar una cantidad negativa.")
                        continue
                    costo_total = precio * cantidad_a_comprar
                    if costo_total <= capital:
                        capital -= costo_total
                        portafolio[accion_a_comprar] += cantidad_a_comprar
                        print(f"Has comprado {cantidad_a_comprar} acciones de {accion_a_comprar}.")
                    else:
                        print("No tienes suficiente capital para esta compra.")
                except ValueError:
                    print("Debes ingresar un número válido.")
            else:
                print("Esa acción no está disponible.")
        
        elif eleccion == "2":  # Vender acciones
            accion_a_vender = input("¿Qué acción quieres vender? (Escribe el nombre): ").strip()
            if accion_a_vender in portafolio and portafolio[accion_a_vender] > 0:
                precio = acciones_disponibles[accion_a_vender]
                try:
                    cantidad_a_vender = int(input(f"Tienes {portafolio[accion_a_vender]} acciones de {accion_a_vender}. ¿Cuántas quieres vender?: "))
                    if cantidad_a_vender < 0:
                        print("No puedes vender una cantidad negativa.")
                        continue
                    if cantidad_a_vender <= portafolio[accion_a_vender]:
                        ingresos = precio * cantidad_a_vender
                        capital += ingresos
                        portafolio[accion_a_vender] -= cantidad_a_vender
                        print(f"Has vendido {cantidad_a_vender} acciones de {accion_a_vender} por ${ingresos}.")
                    else:
                        print("No tienes suficientes acciones para vender esa cantidad.")
                except ValueError:
                    print("Debes ingresar un número válido.")
            else:
                print("No tienes acciones de esa compañía para vender.")
        
        elif eleccion == "3":  # Pasar turno
            print("Has decidido no hacer nada este turno.")

        else:
            print("Opción no válida. Perdiste tu turno.")

        # Actualizar precios de las acciones
        for accion in acciones_disponibles:
            acciones_disponibles[accion] = random.randint(50, 500)

    # Fin del juego
    print("\n=== FIN DEL JUEGO ===")
    print(f"Tu capital final es: ${capital}")
    print("Tu portafolio final:")
    for accion, cantidad in portafolio.items():
        if cantidad > 0:
            print(f"- {accion}: {cantidad} acciones")
    if capital > 10000:
        print("\n¡Felicidades! Has generado ganancias.")
    else:
        print("\nLo siento, has tenido pérdidas.")

# Iniciar el juego
jugar_bolsa()
