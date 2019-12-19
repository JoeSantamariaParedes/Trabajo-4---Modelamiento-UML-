class Arma():
    def __init__(self,modelo,tipo,precio,peso,nro_balas):
        self.modelo=modelo
        self.tipo=tipo
        self.precio=precio
        self.peso=peso
        self.nro_balas=nro_balas
    def disparar(self):
        pass
    def getNro_balas(self):
        return self.nro_balas
    def setNro_balas(self,nro_balas):
        self.nro_balas=nro_balas