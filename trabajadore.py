# Clase Persona
class Persona:
    def __init__(self):
        # Variables privadas
        self.edad = 0
        self.nombre = ""
        self.telefono = ""
# Clase Cliente, hereda de Persona
class Cliente(Persona):
    def __init__(self):
        super().__init__()
        self.credito = 0.0
        # Clase Trabajador, hereda de Persona
class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        self.salario = 0.0
        
if __name__ == "__main__":
    # Crear objeto cliente
    cliente = Cliente()
    cliente.edad = 30
    cliente.nombre = "Juan"
    cliente.telefono = "555-555-555"
    cliente.credito = 1000.50

    print("Edad: ", cliente.edad)
    print("Nombre: ", cliente.nombre)
    print("Telefono: ", cliente.telefono)
    print("Credito: ", cliente.credito)
    # Crear objeto trabajador
    trabajador = Trabajador()
    trabajador.edad = 25
    trabajador.nombre = "Maria"
    trabajador.telefono = "555-555-555"
    trabajador.salario = 2000.50

    print("Edad: ", trabajador.edad)
    print("Nombre: ", trabajador.nombre)
    print("Telefono: ", trabajador.telefono)
    print("Salario: ", trabajador.salario)
