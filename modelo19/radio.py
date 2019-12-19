class Radio():
    def __init__(self,marca,parlante,material,capacidad,estilo):
        self.marca=marca
        self.parlante=parlante
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def reproducir(self):
        return ("a la radio "+self.marca+" se le averio un parlante "+self.parlante.getMarca())
    def getParlante(self):
        return self.parlante
    def setParlante(self,parlante):
        self.parlante=parlante
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca