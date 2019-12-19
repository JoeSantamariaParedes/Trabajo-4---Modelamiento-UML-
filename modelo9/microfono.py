class Microfono():
    def __init__(self,modelo,tipo,precio,peso,marca):
        self.modelo=modelo
        self.tipo=tipo
        self.precio=precio
        self.peso=peso
        self.marca=marca
    def disparar(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca