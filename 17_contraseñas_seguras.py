'''
Crea un programa que genere contraseñas seguras de acuerdo con las preferencias del usuario.

El programa debe permitir al usuario elegir:
La longitud de la contraseña (mínimo 8 caracteres, máximo 64).
Si incluirá letras mayúsculas.
Si incluirá números.
Si incluirá caracteres especiales.
El programa debe generar y mostrar una contraseña aleatoria que cumpla 
con los criterios seleccionados.
Si el usuario selecciona criterios insuficientes (por ejemplo, no incluir 
ningún tipo de carácter), debe mostrar un mensaje de error.
'''

import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_especiales):
    """
    Genera una contraseña aleatoria según los criterios especificados.

    Parámetros:
    longitud (int): Longitud de la contraseña.
    usar_mayusculas (bool): Si incluir letras mayúsculas.
    usar_numeros (bool): Si incluir números.
    usar_especiales (bool): Si incluir caracteres especiales.

    Retorna:
    str: La contraseña generada.
    """
    if not (usar_mayusculas or usar_numeros or usar_especiales):
        return "Error: Debes seleccionar al menos un tipo de carácter adicional."

    caracteres = string.ascii_lowercase  # Siempre incluir letras minúsculas
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("Generador de Contraseñas Seguras")
    
    try:
        longitud = int(input("Ingrese la longitud de la contraseña (8-64): "))
        if longitud < 8 or longitud > 64:
            print("Error: La longitud debe estar entre 8 y 64.")
            return
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'

    contraseña = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_especiales)
    
    if contraseña.startswith("Error"):
        print(contraseña)
    else:
        print(f"\nContraseña generada: {contraseña}")

if __name__ == "__main__":
    main()
