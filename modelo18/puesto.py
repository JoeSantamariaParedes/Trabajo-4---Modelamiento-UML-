class Puesto():
    def __init__(self,nombre,numero,material,tipo,precio):
        self.nombre=nombre
        self.numero=numero
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def atender(self):
        pass
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre