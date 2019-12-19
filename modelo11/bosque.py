class Bosque():
    def __init__(self,nombre,arbol,edad,servicio,personas):
        self.nombre=nombre
        self.arbol=arbol
        self.edad=edad
        self.servicio=servicio
        self.personas=personas
    def defender(self):
        return "el bosque "+self.nombre+" presenta un numero de ramas de "+self.arbol.getRamas()
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getArbol(self):
        return self.arbol
    def setArbol(self,arbol):
        self.arbol=arbol