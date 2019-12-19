class Policia():
    def __init__(self,nombre,arma,edad,servicio,sueldo):
        self.nombre=nombre
        self.arma=arma
        self.edad=edad
        self.servicio=servicio
        self.sueldo=sueldo
    def defender(self):
        return "en un tiroteo el policia "+self.nombre+" se queda con un numero de balas de "+self.arma.getNro_balas()
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getArma(self):
        return self.arma
    def setArma(self,arma):
        self.arma=arma