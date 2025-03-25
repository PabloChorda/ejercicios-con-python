'''
Aventura en el Laberinto
Eres un explorador atrapado en un laberinto misterioso de 5x5 casillas. 
Para escapar, debes encontrar la salida (S) sin caer en trampas ocultas (T).
Puedes moverte en cuatro direcciones:

Norte (↑)

Sur (↓)

Este (→)

Oeste (←)

El laberinto no es visible en su totalidad, solo conocerás la casilla 
en la que estás. A medida que avanzas, descubrirás si tu camino es 
seguro o si has caído en una trampa.

Reglas del juego:
Si pisas una trampa (T), pierdes inmediatamente.

Si llegas a la salida (S), ganas el juego.

Si intentas moverte fuera de los límites del laberinto, no podrás avanzar.

El juego finaliza cuando encuentras la salida o caes en una trampa.

¿Podrás encontrar la salida antes de caer en una trampa? 
'''

import random

# Definir el laberinto como una cuadrícula de 5x5 con 'S' (salida), 'T' (trampa) y espacios vacíos '.'
laberinto = [
    ['.', '.', '.', 'T', '.'],
    ['.', 'T', '.', '.', '.'],
    ['.', '.', 'T', '.', '.'],
    ['.', '.', '.', '.', 'T'],
    ['.', '.', '.', '.', 'S']
]

# Posición inicial del jugador
pos_x, pos_y = 0, 0

def mostrar_laberinto():
    """Muestra el laberinto parcialmente, revelando solo las posiciones visitadas."""
    for i in range(5):
        fila = []
        for j in range(5):
            if (i, j) == (pos_x, pos_y):
                fila.append("P")  # Posición del jugador
            else:
                fila.append("?")  # Espacios no revelados
        print(" ".join(fila))
    print()

def mover_jugador(direccion):
    """Mueve al jugador en la dirección indicada si es válida."""
    global pos_x, pos_y
    movimientos = {"norte": (-1, 0), "sur": (1, 0), "este": (0, 1), "oeste": (0, -1)}
    
    if direccion in movimientos:
        dx, dy = movimientos[direccion]
        nuevo_x, nuevo_y = pos_x + dx, pos_y + dy
        
        if 0 <= nuevo_x < 5 and 0 <= nuevo_y < 5:
            pos_x, pos_y = nuevo_x, nuevo_y
            return True
        else:
            print("No puedes salir del laberinto en esa dirección.")
    else:
        print("Dirección no válida. Usa norte, sur, este u oeste.")
    
    return False

def jugar():
    """Bucle principal del juego."""
    print("¡Bienvenido a la Aventura en el Laberinto!")
    print("Encuentra la salida sin caer en trampas.\n")

    while True:
        mostrar_laberinto()
        movimiento = input("¿A dónde quieres ir? (norte/sur/este/oeste): ").strip().lower()
        
        if mover_jugador(movimiento):
            casilla = laberinto[pos_x][pos_y]
            if casilla == "T":
                print("¡Caíste en una trampa! Fin del juego.")
                break
            elif casilla == "S":
                print("¡Felicidades! Encontraste la salida. ¡Ganaste!")
                break

if __name__ == "__main__":
    jugar()
