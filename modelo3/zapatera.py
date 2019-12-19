class Zapatera():
    def __init__(self,marca,zapato,material,capacidad,estilo):
        self.marca=marca
        self.zapato=zapato
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def almacenar(self):
        return ("la zapatera "+self.marca+" presenta zapatos de marca "+self.zapato.getMarca())
    def getZapato(self):
        return self.zapato
    def setZapato(self,zapato):
        self.zapato=zapato
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca

