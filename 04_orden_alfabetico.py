"""
Escribe un programa que reciba una lista de palabras 
y las ordene alfabéticamente. Después, imprimirá la lista 
de palabras ordenada y la longitud de cada palabra.
"""

from typing import List

def ordenar_palabras(palabras: List[str]) -> List[str]:
    """Ordena una lista de palabras alfabéticamente."""
    return sorted(palabras)

def imprimir_palabras_ordenadas(palabras: List[str]):
    """Imprime las palabras ordenadas y su longitud."""
    for palabra in palabras:
        print(f"{palabra}: {len(palabra)} caracteres")

def main():
    palabras = ["manzana", "plátano", "pera", "kiwi", "naranja", "uva", "fresa"]
    palabras_ordenadas = ordenar_palabras(palabras)
    print("Palabras ordenadas alfabéticamente:")
    imprimir_palabras_ordenadas(palabras_ordenadas)

if __name__ == "__main__":
    main()
