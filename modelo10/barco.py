class Barco():
    def __init__(self,marca,motor,material,capacidad,estilo):
        self.marca=marca
        self.motor=motor
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def navegar(self):
        return ("al barco "+self.marca+" se le quemo el motor "+self.motor.getMarca())
    def getMotor(self):
        return self.motor
    def setMotor(self,motor):
        self.motor=motor
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
