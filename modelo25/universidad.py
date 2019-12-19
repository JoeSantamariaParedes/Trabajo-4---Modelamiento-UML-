class Universidad():
    def __init__(self,nombre,aula,escuelas,capacidad,facultades):
        self.nombre=nombre
        self.aula=aula
        self.escuelas=escuelas
        self.capacidad=capacidad
        self.facultades=facultades
    def inculcar(self):
        return ("la universidad "+self.nombre+" esta construyendo el aula "+self.aula.getNombre())
    def getAula(self):
        return self.aula
    def setAula(self,aula):
        self.aula=aula
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre