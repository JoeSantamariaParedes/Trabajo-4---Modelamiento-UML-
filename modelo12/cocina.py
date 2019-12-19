class Cocina():
    def __init__(self,marca,ornillas,material,capacidad,estilo):
        self.marca=marca
        self.ornillas=ornillas
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def cocinar(self):
        return ("la cocina "+self.marca+" se le compraron ornillas "+self.ornillas.getMarca())
    def getOrnillas(self):
        return self.ornillas
    def setOrnillas(self,ornillas):
        self.ornillas=ornillas
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca