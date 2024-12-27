'''

Simulador de Hackeo

Te convertirás en un hacker que intenta infiltrarse en un sistema de seguridad de alto nivel. 
Tu objetivo es descifrar una contraseña cifrada y acceder a la base de datos central antes de que se agote el tiempo o los intentos permitidos. 
Para lograrlo, deberás superar diferentes niveles de dificultad enfrentándote a:

Rompecódigos: Resolverás contraseñas generadas mediante patrones numéricos o alfanuméricos.
Desafíos de Lógica: Resolver acertijos lógicos para desbloquear pistas.
Cifrado Básico: Decodificar cadenas cifradas en métodos simples como el Cifrado César o Base64.
El sistema te ofrecerá pistas en cada nivel, pero si fallas demasiado, podrías activar sistemas de defensa (bloquear tu sesión o perder intentos).

'''

import random
import base64
import time

# Configuración inicial
TIEMPO_LIMITE = 300  # 5 minutos para completar el hackeo
INTENTOS_MAXIMOS = 10

# Generar contraseñas y desafíos
def generar_contraseña_patron():
    """Genera una contraseña basada en un patrón lógico."""
    secuencia = [random.randint(1, 9) for _ in range(4)]
    secuencia.append(secuencia[-1] + secuencia[-2])  # Suma lógica
    return secuencia[:-1], secuencia[-1]

def cifrar_cesar(texto, desplazamiento):
    """Aplica un cifrado César a un texto."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def generar_cadena_cifrada():
    """Genera una cadena cifrada en Base64."""
    texto = random.choice(["hack", "system", "access", "secure", "admin"])
    return base64.b64encode(texto.encode()).decode()

# Funciones de niveles
def nivel_1():
    print("\n--- Nivel 1: Rompecódigos ---")
    secuencia, respuesta = generar_contraseña_patron()
    print(f"La secuencia lógica es: {secuencia} _")
    intentos = 3
    while intentos > 0:
        try:
            entrada = int(input("Ingresa el siguiente número en la secuencia: "))
            if entrada == respuesta:
                print("¡Correcto! Acceso al siguiente nivel.")
                return True
            else:
                print("Incorrecto. Intenta de nuevo.")
                intentos -= 1
        except ValueError:
            print("Entrada no válida.")
    print("Has fallado en este nivel.")
    return False

def nivel_2():
    print("\n--- Nivel 2: Decodificación Básica ---")
    cadena_cifrada = generar_cadena_cifrada()
    print(f"Tu cadena cifrada en Base64 es: {cadena_cifrada}")
    intentos = 3
    while intentos > 0:
        entrada = input("Decodifica la cadena: ").strip()
        if entrada == base64.b64decode(cadena_cifrada).decode():
            print("¡Correcto! Acceso al siguiente nivel.")
            return True
        else:
            print("Incorrecto. Intenta de nuevo.")
            intentos -= 1
    print("Has fallado en este nivel.")
    return False

def nivel_3():
    print("\n--- Nivel 3: Cifrado César ---")
    texto = "hackthecode"
    desplazamiento = random.randint(1, 5)
    cifrado = cifrar_cesar(texto, desplazamiento)
    print(f"Texto cifrado: {cifrado}")
    print(f"Pista: el desplazamiento es {desplazamiento}.")
    intentos = 3
    while intentos > 0:
        entrada = input("Descifra el texto: ").strip()
        if entrada == texto:
            print("¡Correcto! Has completado el hackeo.")
            return True
        else:
            print("Incorrecto. Intenta de nuevo.")
            intentos -= 1
    print("Has fallado en este nivel.")
    return False

# Función principal
def simulador_hackeo():
    print("=== SIMULADOR DE HACKEO ===")
    print("¡Bienvenido, hacker! Tu objetivo es descifrar el sistema antes de que se agote el tiempo.")
    print(f"Tienes un límite de {TIEMPO_LIMITE // 60} minutos y {INTENTOS_MAXIMOS} intentos totales.\n")

    inicio = time.time()
    intentos_totales = INTENTOS_MAXIMOS
    
    niveles = [nivel_1, nivel_2, nivel_3]
    for nivel in niveles:
        if time.time() - inicio > TIEMPO_LIMITE:
            print("¡Se agotó el tiempo! Hackeo fallido.")
            return
        if intentos_totales <= 0:
            print("¡Te quedaste sin intentos! Hackeo fallido.")
            return
        exito = nivel()
        if not exito:
            intentos_totales -= 1
            print(f"Intentos restantes: {intentos_totales}")
            if intentos_totales <= 0:
                print("¡Te quedaste sin intentos! Hackeo fallido.")
                return
    
    print("\n=== ¡Felicidades! Has completado el hackeo y accedido al sistema. ===")

# Ejecutar el simulador
if __name__ == "__main__":
    simulador_hackeo()
