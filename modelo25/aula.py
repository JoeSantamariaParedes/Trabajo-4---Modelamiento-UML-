class Aula():
    def __init__(self,nombre,carpeta,computadoras,tipo,sillas):
        self.nombre=nombre
        self.carpeta=carpeta
        self.computadoras=computadoras
        self.tipo=tipo
        self.sillas=sillas
    def aprender(self):
        pass
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre