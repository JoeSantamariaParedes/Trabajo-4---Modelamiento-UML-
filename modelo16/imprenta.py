class Imprenta():
    def __init__(self,nombre,impresora,material,capacidad,estilo):
        self.nombre=nombre
        self.impresora=impresora
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def atender(self):
        return ("la imprenta "+self.nombre+" compro una nueva impresora "+self.impresora.getMarca())
    def getImpresora(self):
        return self.impresora
    def setImpresora(self,impresora):
        self.impresora=impresora
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre