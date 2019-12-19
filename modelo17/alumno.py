class Alumno():
    def __init__(self,nombre,numero,edad,tipo,peso):
        self.nombre=nombre
        self.numero=numero
        self.edad=edad
        self.tipo=tipo
        self.peso=peso
    def aprender(self):
        pass
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre