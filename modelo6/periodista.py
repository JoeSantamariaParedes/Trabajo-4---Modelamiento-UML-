class Periodista():
    def __init__(self,nombre,edad,servicio,camara,sexo):
        self.nombre=nombre
        self.edad=edad
        self.servicio=servicio
        self.camara=camara
        self.sexo=sexo
    def entrevistar(self):
        return "el periodista "+self.nombre+" tiene una camara de marca "+self.camara.getMarca()
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getCamara(self):
        return self.camara
    def setCamara(self,camara):
        self.camara=camara
