class Impresora():
    def __init__(self,marca,modelo,material,tipo,precio):
        self.marca=marca
        self.modelo=modelo
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def imprimir(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca