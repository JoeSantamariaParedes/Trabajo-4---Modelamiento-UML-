class Corona():
    def __init__(self, modelo, tipo, precio, peso, material):
        self.modelo = modelo
        self.tipo = tipo
        self.precio = precio
        self.peso = peso
        self.material = material

    def adornar(self):
        pass

    def getMaterial(self):
        return self.material

    def setMaterial(self, material):
        self.material = material