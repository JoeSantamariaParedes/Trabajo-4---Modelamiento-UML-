class Rey():
    def __init__(self, nombre, corona, edad, servicio, sueldo):
        self.nombre = nombre
        self.corona = corona
        self.edad = edad
        self.servicio = servicio
        self.sueldo = sueldo

    def gobernar(self):
        return "el rey " + self.nombre + " gobierna con una corona de " + self.corona.getMaterial()

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorona(self):
        return self.corona

    def setCorona(self, corona):
        self.corona = corona