import random

def adivina_el_numero():
    """
    Juego de adivinanza en el que el usuario intenta adivinar un número entre 1 y 100.
    El programa le da pistas si el número es mayor o menor hasta que acierte.

    Retorna:
    None
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("El programa ha elegido un número entre 1 y 100. ¡Adivínalo!")

    while True:
        try:
            adivinanza = int(input("Ingresa tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Muy bajo, intenta otra vez.")
            elif adivinanza > numero_secreto:
                print("Muy alto, intenta otra vez.")
            else:
                print(f"¡Correcto! Lo lograste en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()
