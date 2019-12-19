class Motor():
    def __init__(self,marca,precio,material,tipo,peso):
        self.marca=marca
        self.precio=precio
        self.material=material
        self.tipo=tipo
        self.peso=peso
    def avanzar(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca