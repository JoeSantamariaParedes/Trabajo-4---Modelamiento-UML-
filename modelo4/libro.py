class Libro():
    def __init__(self,autor,editorial,precio,peso,indice):
        self.autor=autor
        self.editorial=editorial
        self.precio=precio
        self.peso=peso
        self.indice=indice
    def aprender(self):
        pass
    def getAutor(self):
        return self.autor
    def setAutor(self,autor):
        self.autor=autor