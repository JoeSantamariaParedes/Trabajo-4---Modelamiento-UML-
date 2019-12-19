class Sshh():
    def __init__(self,ubicacion,inodoro,material,capacidad,estilo):
        self.ubicacion=ubicacion
        self.inodoro=inodoro
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def atender(self):
        return ("los ss.hh de "+self.ubicacion+" tienen inodoros "+self.inodoro.getMarca())
    def getInodoro(self):
        return self.inodoro
    def setInodoro(self,inodoro):
        self.inodoro=inodoro
    def getUbicacion(self):
        return self.ubicacion
    def setUbicacion(self,ubicacion):
        self.ubicacion=ubicacion