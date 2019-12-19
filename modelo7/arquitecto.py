class Arquitecto():
    def __init__(self,nombre,edad,servicio,plano,sexo):
        self.nombre=nombre
        self.edad=edad
        self.servicio=servicio
        self.plano=plano
        self.sexo=sexo
    def proyectar(self):
        return "el arquitecto "+self.nombre+" se encarga del plano sobre el "+self.plano.getModelo()
    def getPlano(self):
        return self.plano
    def setPlano(self,plano):
        self.plano=plano
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
