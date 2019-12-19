class Corbata():
    def __init__(self,marca,numero,material,tipo,precio):
        self.marca=marca
        self.numero=numero
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def adornar(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca