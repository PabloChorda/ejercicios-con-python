'''

Cazador de Reliquias

Eres un cazador de reliquias que explora un antiguo templo lleno de misterios y peligros. 
El templo está representado como una cuadrícula (por ejemplo, de 5x5). Tu objetivo es recolectar una reliquia escondida en el mapa y salir del templo antes de ser atrapado por trampas o enemigos.

Reglas del Juego:
El jugador comienza en una posición inicial (0, 0) en la cuadrícula.
La reliquia está en una ubicación aleatoria desconocida para el jugador.
El jugador puede moverse hacia arriba, abajo, izquierda o derecha escribiendo comandos (w, s, a, d).
El mapa contiene:
Trampas: Casillas que terminan el juego si el jugador cae en ellas.
Enemigos: Casillas que persiguen al jugador (se mueven después de cada turno).
Tesoro: El objetivo del juego.
Si el jugador encuentra la reliquia, deberá regresar a la salida (0, 0) para ganar.
El mapa y los elementos deben generarse aleatoriamente, y el jugador no verá las posiciones de trampas, enemigos o la reliquia, solo recibirá pistas como:
"Sientes una presencia cercana" (enemigo próximo).
"El aire aquí huele extraño" (trampa próxima).
"Algo brilla en la distancia" (tesoro próximo).
El jugador tiene un número limitado de movimientos (por ejemplo, 30).
Objetivo:
Encuentra la reliquia, evita las trampas y enemigos, y regresa a la salida antes de quedarte sin movimientos.

Desafíos Técnicos:
Generar el mapa con elementos aleatorios.
Implementar movimiento de los enemigos que persiguen al jugador.
Mostrar pistas basadas en las posiciones relativas de los elementos.
Manejar las condiciones de ganar o perder el juego.

'''

import random

# Configuración inicial
TAMAÑO_MAPA = 5
MOVIMIENTOS_MAXIMOS = 30

# Generar el mapa vacío
def generar_mapa():
    return [["." for _ in range(TAMAÑO_MAPA)] for _ in range(TAMAÑO_MAPA)]

# Colocar un elemento en el mapa
def colocar_elemento(mapa, simbolo):
    while True:
        x = random.randint(0, TAMAÑO_MAPA - 1)
        y = random.randint(0, TAMAÑO_MAPA - 1)
        if mapa[x][y] == ".":  # Solo colocar en casillas vacías
            mapa[x][y] = simbolo
            return (x, y)

# Mostrar el mapa (para depuración, ocultar trampas/reliquias al jugador)
def mostrar_mapa(mapa, jugador):
    for i in range(TAMAÑO_MAPA):
        fila = ""
        for j in range(TAMAÑO_MAPA):
            if (i, j) == jugador:
                fila += "P "  # Posición del jugador
            else:
                fila += ". "  # Ocultar el contenido real
        print(fila)
    print()

# Movimiento del jugador
def mover_jugador(posicion, direccion):
    x, y = posicion
    if direccion == "w" and x > 0:       # Arriba
        x -= 1
    elif direccion == "s" and x < TAMAÑO_MAPA - 1:  # Abajo
        x += 1
    elif direccion == "a" and y > 0:    # Izquierda
        y -= 1
    elif direccion == "d" and y < TAMAÑO_MAPA - 1:  # Derecha
        y += 1
    return (x, y)

# Inicialización del juego
def iniciar_juego():
    mapa = generar_mapa()
    
    # Colocar elementos
    posicion_jugador = (0, 0)
    posicion_reliquia = colocar_elemento(mapa, "R")
    trampas = [colocar_elemento(mapa, "T") for _ in range(3)]
    enemigos = [colocar_elemento(mapa, "E") for _ in range(2)]
    
    movimientos_restantes = MOVIMIENTOS_MAXIMOS
    
    print("¡Bienvenido al Cazador de Reliquias!")
    print("Encuentra la reliquia y vuelve a la salida antes de que se acaben los movimientos.")
    print("Controles: w (arriba), s (abajo), a (izquierda), d (derecha).")
    
    # Bucle del juego
    while movimientos_restantes > 0:
        mostrar_mapa(mapa, posicion_jugador)
        print(f"Movimientos restantes: {movimientos_restantes}")
        
        # Pedir movimiento
        direccion = input("Ingresa tu movimiento (w/a/s/d): ").strip().lower()
        if direccion not in ["w", "a", "s", "d"]:
            print("Movimiento no válido. Intenta de nuevo.")
            continue
        
        # Actualizar posición del jugador
        nueva_posicion = mover_jugador(posicion_jugador, direccion)
        if nueva_posicion == posicion_reliquia:
            print("¡Has encontrado la reliquia! Ahora regresa a la salida.")
            posicion_reliquia = None  # Marcar que se ha recogido
        elif nueva_posicion in trampas:
            print("¡Caíste en una trampa! Fin del juego.")
            return
        elif nueva_posicion in enemigos:
            print("Un enemigo te atrapó. Fin del juego.")
            return
        
        # Actualizar posición
        posicion_jugador = nueva_posicion
        movimientos_restantes -= 1
        
        # Condición de victoria
        if posicion_jugador == (0, 0) and posicion_reliquia is None:
            print("¡Has regresado a la salida con la reliquia! ¡Victoria!")
            return
    
    print("Se te acabaron los movimientos. Fin del juego.")

# Ejecutar el juego
if __name__ == "__main__":
    iniciar_juego()
