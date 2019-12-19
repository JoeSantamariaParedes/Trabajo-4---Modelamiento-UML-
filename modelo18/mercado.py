class Mercado():
    def __init__(self,nombre,puesto,material,capacidad,estilo):
        self.nombre=nombre
        self.puesto=puesto
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def recibir(self):
        return ("el mercado "+self.nombre+" cerraron el puesto "+self.puesto.getNombre())
    def getPuesto(self):
        return self.puesto
    def setPuesto(self,puesto):
        self.puesto=puesto
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre