class Bata():
    def __init__(self,talla,peso,precio,modelo,material):
        self.talla=talla
        self.peso=peso
        self.precio=precio
        self.modelo=modelo
        self.material=material
    def cubrir(self):
        pass
    def getTalla(self):
        return self.talla
    def setTalla(self,talla):
        self.talla=talla


