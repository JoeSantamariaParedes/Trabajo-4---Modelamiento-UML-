class Ejercito():
    def __init__(self,nombre,soldado,material,capacidad,estilo):
        self.nombre=nombre
        self.soldado=soldado
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def planificar(self):
        return ("el ejercito "+self.nombre+" expulso al soldado "+self.soldado.getNombre())
    def getSoldado(self):
        return self.soldado
    def setSoldado(self,soldado):
        self.soldado=soldado
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre