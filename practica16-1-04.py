class Persona:
    def __init__(self):
        self.__edad = 0
        self.__nombre = ""
        self.__telefono = ""
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_telefono(self):
        return self.__telefono

if __name__ == "__main__":
    persona = Persona()
    persona.set_edad(30)
    persona.set_nombre("Juan")
    persona.set_telefono("555-555-555")

    print("Edad: ", persona.get_edad())
    print("Nombre: ", persona.get_nombre())
    print("Telefono: ", persona.get_telefono())
