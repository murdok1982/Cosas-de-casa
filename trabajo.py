def sumar(num1, num2, num3):
    return num1 + num2 + num3

print(sumar(1, 2, 3))

resultado = sumar(1, 2, 3)
print(resultado)

# aqui la segunda parte
class Coche:
    def __init__(self):
        self.puertas = 0 # se inicializa la variable puertas en 0

    def añadir_puerta(self):
        self.puertas += 1 # se incrementa el numero de puertas en 1

miCoche = Coche() # se crea un objeto miCoche de la clase Coche
miCoche.añadir_puerta() # se llama a la funcion añadir_puerta del objeto miCoche
print(miCoche.puertas) # se imprime el numero de puertas del objeto miCoche
