class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def resultado(self):
        if self.nota >= 5:
            print("El alumno " + self.nombre + " ha aprobado con un " + str(self.nota))
        else:
            print("El alumno " + self.nombre + " ha suspendido con un " + str(self.nota))

estudiante = Alumno("Juan", 7)
estudiante.imprimir()
estudiante.resultado()
