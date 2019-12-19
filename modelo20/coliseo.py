class Coliseo():
    def __init__(self,nombre,impresora,material,capacidad,estilo):
        self.nombre=nombre
        self.impresora=impresora
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def atender(self):
        return ("el coliseo "+self.nombre+" presenta un balon marca "+self.impresora.getMarca())
    def getBalon(self):
        return self.balon
    def setBalon(self,balon):
        self.balon=balon
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre