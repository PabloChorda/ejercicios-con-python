"""
Crea un programa que reciba una cadena de texto y devuelva la misma cadena 
invertida, sin utilizar funciones propias del lenguaje 
que hagan esto directamente.
"""

def invertir_cadena(cadena):
    """ 
    Invierte una cadena de texto.

    Parámetros:
    cadena (str): La cadena de texto a invertir.

    Retorna:
    str: La cadena de texto invertida.
    """
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

def main():
    cadena = input("Ingrese una cadena de texto: ")
    invertida = invertir_cadena(cadena)
    print(f"La cadena invertida es: {invertida}")

if __name__ == "__main__":
    main()
