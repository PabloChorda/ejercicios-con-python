'''
Eres un inversor en un mercado de criptomonedas donde los precios cambian constantemente. 
Puedes comprar y vender criptos con el objetivo de maximizar tus ganancias antes de que el tiempo se acabe.

Características:
Inicio: Comienzas con una cantidad fija de dinero y un mercado con criptos aleatorias.

Fluctuaciones: Cada cripto cambia de precio cada ronda con eventos aleatorios.

Eventos Aleatorios: Noticias, hacks, regulación o "hype" afectan los precios.

Acciones: Puedes comprar, vender o esperar la siguiente ronda.

Final: Tras X rondas, el juego muestra tu balance final y si obtuviste ganancias o pérdidas.
'''

import random

class Cripto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def actualizar_precio(self):
        cambio = random.uniform(-0.3, 0.3)  # Variación del precio entre -30% y +30%
        self.precio = max(1, round(self.precio * (1 + cambio), 2))  # Evitar precios negativos

class Mercado:
    def __init__(self):
        self.criptos = [Cripto("Bitcoin", 50000), Cripto("Ethereum", 3000), Cripto("DogeCoin", 0.1)]
    
    def actualizar_precios(self):
        for cripto in self.criptos:
            cripto.actualizar_precio()
    
    def mostrar_precios(self):
        print("\nMercado Actual:")
        for cripto in self.criptos:
            print(f"{cripto.nombre}: ${cripto.precio}")

class Jugador:
    def __init__(self, capital):
        self.capital = capital
        self.portafolio = {}
    
    def comprar(self, cripto, cantidad):
        costo = cripto.precio * cantidad
        if self.capital >= costo:
            self.capital -= costo
            self.portafolio[cripto.nombre] = self.portafolio.get(cripto.nombre, 0) + cantidad
            print(f"Compraste {cantidad} de {cripto.nombre} por ${costo}")
        else:
            print("Fondos insuficientes.")
    
    def vender(self, cripto, cantidad):
        if self.portafolio.get(cripto.nombre, 0) >= cantidad:
            self.capital += cripto.precio * cantidad
            self.portafolio[cripto.nombre] -= cantidad
            print(f"Vendiste {cantidad} de {cripto.nombre} por ${cripto.precio * cantidad}")
        else:
            print("No tienes suficientes criptos.")
    
    def mostrar_estado(self):
        print(f"\nCapital disponible: ${self.capital}")
        print("Portafolio:")
        for cripto, cantidad in self.portafolio.items():
            print(f"{cripto}: {cantidad}")

def juego(acciones):
    mercado = Mercado()
    jugador = Jugador(capital=100000)
    rondas = 5
    
    for ronda in range(1, rondas+1):
        print(f"\n--- RONDA {ronda} ---")
        mercado.actualizar_precios()
        mercado.mostrar_precios()
        jugador.mostrar_estado()
        
        if not acciones:
            break
        
        accion = acciones.pop(0).lower()
        if accion in ['c', 'v']:
            nombre_cripto = acciones.pop(0) if acciones else ""
            cripto = next((c for c in mercado.criptos if c.nombre.lower() == nombre_cripto.lower()), None)
            if not cripto:
                print("Cripto no encontrada. Asegúrate de escribir bien el nombre.")
                continue
            
            try:
                cantidad = float(acciones.pop(0)) if acciones else 0
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")
                continue
            
            if accion == 'c':
                jugador.comprar(cripto, cantidad)
            elif accion == 'v':
                jugador.vender(cripto, cantidad)
    
    print("\n--- FIN DEL JUEGO ---")
    jugador.mostrar_estado()

if __name__ == "__main__":
    acciones_simuladas = ["c", "Bitcoin", "0.5", "v", "Ethereum", "1", "s"]  # Simulación de acciones
    juego(acciones_simuladas)
