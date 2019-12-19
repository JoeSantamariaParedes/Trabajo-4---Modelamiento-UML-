class Restaurant():
    def __init__(self,nombre,mesero,mesas,capacidad,sshh):
        self.nombre=nombre
        self.mesero=mesero
        self.mesas=mesas
        self.capacidad=capacidad
        self.sshh=sshh
    def cocinar(self):
        return ("el restaurant "+self.nombre+" contrato al mesero "+self.mesero.getNombre())
    def getMesero(self):
        return self.mesero
    def setMesero(self,mesero):
        self.mesero=mesero
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre