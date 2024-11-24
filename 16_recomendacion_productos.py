'''
Crea un programa que funcione como un sistema básico de recomendación de productos.

El programa debe tener una lista de productos con descripciones.
El usuario debe ingresar una palabra clave.
El programa buscará la palabra clave en las descripciones de los productos
y mostrará las recomendaciones.
Si no encuentra coincidencias, mostrará un mensaje indicando que no hay recomendaciones 
disponibles.
'''
def buscar_productos(palabra_clave, productos):
    """
    Busca productos cuya descripción contiene la palabra clave.

    Parámetros:
    palabra_clave (str): La palabra clave ingresada por el usuario.
    productos (list): Lista de productos con nombre y descripción.

    Retorna:
    list: Lista de productos coincidentes.
    """
    resultados = []
    palabra_clave = palabra_clave.lower()  # Convertir a minúsculas para búsqueda insensible a mayúsculas
    for producto in productos:
        if palabra_clave in producto['descripcion'].lower():
            resultados.append(producto)
    return resultados

def main():
    # Lista de productos con nombre y descripción
    productos = [
        {"nombre": "Laptop Pro", "descripcion": "Laptop de alto rendimiento ideal para programadores."},
        {"nombre": "Smartphone X", "descripcion": "Teléfono inteligente con cámara profesional y gran batería."},
        {"nombre": "Auriculares SoundMax", "descripcion": "Auriculares con cancelación de ruido y sonido premium."},
        {"nombre": "Reloj SmartFit", "descripcion": "Reloj inteligente con monitoreo de salud y GPS."},
        {"nombre": "Teclado Mecánico RGB", "descripcion": "Teclado mecánico con retroiluminación personalizable."}
    ]

    print("Sistema de Recomendación de Productos")
    palabra_clave = input("Ingrese una palabra clave para buscar productos: ")

    resultados = buscar_productos(palabra_clave, productos)

    if resultados:
        print("\nProductos recomendados:")
        for producto in resultados:
            print(f"- {producto['nombre']}: {producto['descripcion']}")
    else:
        print("\nNo se encontraron productos relacionados con la palabra clave.")

if __name__ == "__main__":
    main()
