'''

Crea un programa que verifique si una contraseña cumple con los 
siguientes requisitos:

La contraseña debe tener al menos 8 caracteres.
Debe contener al menos una letra minúscula, una letra mayúscula, 
un número y un carácter especial (como @, #, $, etc.).
No debe contener espacios.
El programa debe permitir al usuario ingresar una contraseña y verificar 
si es válida o no. Si no es válida, deberá indicar qué requisitos no cumple.
'''
import re

def validar_contraseña(contraseña):
    """
    Verifica si una contraseña cumple con los requisitos mínimos.

    Parámetros:
    contraseña (str): La contraseña a verificar.

    Retorna:
    list: Una lista con los errores encontrados o una lista vacía si es válida.
    """
    errores = []

    # Verificar la longitud
    if len(contraseña) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")

    # Verificar si contiene una letra mayúscula
    if not any(char.isupper() for char in contraseña):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    # Verificar si contiene una letra minúscula
    if not any(char.islower() for char in contraseña):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    # Verificar si contiene un número
    if not any(char.isdigit() for char in contraseña):
        errores.append("La contraseña debe contener al menos un número.")

    # Verificar si contiene un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        errores.append("La contraseña debe contener al menos un carácter especial.")

    # Verificar si contiene espacios
    if ' ' in contraseña:
        errores.append("La contraseña no debe contener espacios.")

    return errores

def main():
    contraseña = input("Ingrese una contraseña para validar: ")
    errores = validar_contraseña(contraseña)

    if not errores:
        print("La contraseña es válida.")
    else:
        print("La contraseña no es válida. Errores:")
        for error in errores:
            print(f"- {error}")

if __name__ == "__main__":
    main()
