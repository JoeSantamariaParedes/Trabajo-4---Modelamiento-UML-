class Camara():
    def __init__(self,marca,modelo,pixeles,precio,peso):
        self.marca=marca
        self.modelo=modelo
        self.pixeles=pixeles
        self.precio=precio
        self.peso=peso
    def grabar(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
