class Biblioteca():
    def __init__(self,nombre,libro,mesas,sillas,computadoras):
        self.nombre=nombre
        self.libro=libro
        self.mesas=mesas
        self.sillas=sillas
        self.computadoras=computadoras
    def investigar(self):
        return "pablo pregunto por un libro de autor "+self.libro.getAutor()+" en la biblioteca "+self.nombre
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getLibro(self):
        return self.libro
    def setLibro(self,libro):
        self.libro=libro
