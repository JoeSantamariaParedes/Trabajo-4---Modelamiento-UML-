class Doctor():
    def __init__(self,nombre,bata,sexo,servicio,sueldo):
        self.nombre=nombre
        self.bata=bata
        self.sexo=sexo
        self.servicio=servicio
        self.sueldo=sueldo
    def curar(self):
        return "el doctor "+self.nombre+" lleva una bata de talla "+self.bata.getTalla()
    def getBata(self):
        return self.bata
    def setBata(self,bata):
        self.bata=bata
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre

