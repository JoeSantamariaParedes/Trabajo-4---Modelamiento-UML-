class Soldado():
    def __init__(self,nombre,estatura,edad,tipo,peso):
        self.nombre=nombre
        self.estatura=estatura
        self.edad=edad
        self.tipo=tipo
        self.peso=peso
    def combatir(self):
        pass
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre