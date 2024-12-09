"""
Crea un simulador de ecosistema donde el jugador debe ayudar a un animal a sobrevivir:
- El animal tiene tres atributos principales: energía, hambre e hidratación, que comienzan en 50.
- Cada día ocurre un evento aleatorio que afecta estos atributos, como encontrar agua, comida o enfrentarse a depredadores.
- El jugador debe elegir una acción cada día entre las siguientes:
  1. Buscar comida (-10 energía, +30 hambre).
  2. Buscar agua (-10 energía, +30 hidratación).
  3. Descansar (+20 energía, -10 hambre, -10 hidratación).
- Los atributos no pueden exceder un valor de 100, pero si cualquiera de ellos llega a 0, el jugador pierde.
- El objetivo es sobrevivir el mayor número de días posible mientras se gestionan los recursos.
- La partida termina si el jugador se queda sin energía, hambre o hidratación.
"""

import random

# Estados iniciales del animal
energy = 50
hunger = 50
hydration = 50
day = 1

# Opciones de eventos aleatorios
events = [
    "Una tormenta arrasa el área, consume energía mientras encuentras refugio.",
    "Encuentras un lago cristalino, puedes beber agua.",
    "Una manada de depredadores te persigue, debes correr y gastar energía.",
    "Encuentras un arbusto lleno de frutas, puedes alimentarte.",
    "Un día soleado y tranquilo, puedes descansar para recuperar energía.",
    "No encuentras comida ni agua, el hambre y la sed aumentan."
]

print("¡Bienvenido al simulador de ecosistema!")
print("Eres un animal que debe sobrevivir día tras día. Gestiona tu energía, hambre y sed para sobrevivir.")
print("Si cualquiera de estos llega a 0, pierdes el juego.\n")

while energy > 0 and hunger > 0 and hydration > 0:
    print(f"\nDía {day}:")
    print(f"Energía: {energy} | Hambre: {hunger} | Hidratación: {hydration}\n")

    # Presentar evento aleatorio
    event = random.choice(events)
    print(f"Evento del día: {event}")

    # Opciones de acción del usuario
    print("\n¿Qué quieres hacer?")
    print("1. Buscar comida (-10 energía, +30 hambre)")
    print("2. Buscar agua (-10 energía, +30 hidratación)")
    print("3. Descansar (+20 energía, -10 hambre, -10 hidratación)")
    action = input("Elige una opción (1, 2 o 3): ")

    if action == "1":
        energy -= 10
        hunger += 30
    elif action == "2":
        energy -= 10
        hydration += 30
    elif action == "3":
        energy += 20
        hunger -= 10
        hydration -= 10
    else:
        print("Opción inválida, pierdes un turno.")
    
    # Impacto del evento del día
    if "tormenta" in event:
        energy -= 20
    elif "lago" in event:
        hydration += 20
    elif "depredadores" in event:
        energy -= 30
    elif "frutas" in event:
        hunger += 20
    elif "día soleado" in event:
        energy += 10
    elif "no encuentras comida" in event:
        hunger -= 20
        hydration -= 20

    # Limitar valores al máximo de 100
    energy = min(100, energy)
    hunger = min(100, hunger)
    hydration = min(100, hydration)

    # Avanzar al siguiente día
    day += 1

# Fin del juego
if energy <= 0:
    print("\nTe quedaste sin energía. No pudiste continuar. Fin del juego.")
elif hunger <= 0:
    print("\nTe moriste de hambre. Fin del juego.")
elif hydration <= 0:
    print("\nTe deshidrataste. Fin del juego.")
else:
    print("\n¡Sobreviviste al ecosistema! ¡Eres un campeón de la naturaleza!")
