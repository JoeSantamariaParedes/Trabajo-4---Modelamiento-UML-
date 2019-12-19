class Zapato():
    def __init__(self,marca,talla,material,tipo,precio):
        self.marca=marca
        self.talla=talla
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def proteger(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca