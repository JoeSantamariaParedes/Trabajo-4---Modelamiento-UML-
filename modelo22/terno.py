class Terno():
    def __init__(self,marca,corbata,material,color,estilo):
        self.marca=marca
        self.corbata=corbata
        self.material=material
        self.color=color
        self.estilo=estilo
    def elegantizar(self):
        return ("el terno "+self.marca+" tiene una corbata marca "+self.corbata.getMarca())
    def getCorbata(self):
        return self.corbata
    def setCorbata(self,corbata):
        self.corbata=corbata
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca