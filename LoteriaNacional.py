class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche = Coche("rojo", 4, 4, 120, 1500)
print(coche.color)
print(coche.ruedas)
print(coche.puertas)
print(coche.velocidad)
print(coche.cilindrada)
