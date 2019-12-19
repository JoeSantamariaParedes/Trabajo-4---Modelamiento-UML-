class Locomotora():
    def __init__(self,marca,bagon,material,capacidad,estilo):
        self.marca=marca
        self.bagon=bagon
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def transportar(self):
        return ("la locomotora "+self.marca+" transporta ovejas en en vagon numero "+self.bagon.getNumero())
    def getBagon(self):
        return self.bagon
    def setBagon(self,bagon):
        self.bagon=bagon
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca