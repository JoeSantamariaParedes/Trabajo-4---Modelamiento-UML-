class Bagon():
    def __init__(self,numero,marca,material,tipo,precio):
        self.numero = numero
        self.marca=marca
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def almacenar(self):
        pass
    def getNumero(self):
        return self.numero
    def setNumero(self,numero):
        self.numero=numero