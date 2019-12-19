class Plano():
    def __init__(self,modelo,leyenda,precio,papel,grafico):
        self.modelo=modelo
        self.leyenda=leyenda
        self.precio=precio
        self.papel=papel
        self.grafico=grafico
    def plasmar(self):
        pass
    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo