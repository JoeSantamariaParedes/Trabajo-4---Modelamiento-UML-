class Enfermera():
    def __init__(self,nombre,edad,servicio,enfermo,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.servicio=servicio
        self.enfermo=enfermo
        self.sueldo=sueldo
    def cuidar(self):
        return "la enfermera " +self.nombre + " está cuidando al paciente " + self.enfermo.getNro_paciente()
    def getEnfermo(self):
        return self.enfermo
    def setEnfermo(self,enfermo):
        self.enfermo=enfermo
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre


