class Conductor():
    def __init__(self,nombre,microfono,edad,servicio,sueldo):
        self.nombre=nombre
        self.microfono=microfono
        self.edad=edad
        self.servicio=servicio
        self.sueldo=sueldo
    def animar(self):
        return "el conductor "+self.nombre+" pierde el microfono "+self.microfono.getMarca()
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getMicrofono(self):
        return self.microfono
    def setMicrofono(self,microfono):
        self.microfono=microfono