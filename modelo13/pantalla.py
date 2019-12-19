class Pantalla():
    def __init__(self,marca,version,material,tipo,precio):
        self.marca=marca
        self.version=version
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def proyectar(self):
        pass
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca