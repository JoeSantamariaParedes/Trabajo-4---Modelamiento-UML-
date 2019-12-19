class Arbol():
    def __init__(self,hojas,tipo,precio,peso,ramas):
        self.hojas=hojas
        self.tipo=tipo
        self.precio=precio
        self.peso=peso
        self.ramas=ramas
    def oxigenar(self):
        pass
    def getRamas(self):
        return self.ramas
    def setRamas(self,ramas):
        self.ramas=ramas