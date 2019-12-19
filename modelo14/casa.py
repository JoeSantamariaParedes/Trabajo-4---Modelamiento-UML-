class Casa():
    def __init__(self,propietario,piso,material,capacidad,estilo):
        self.propietario=propietario
        self.piso=piso
        self.material=material
        self.capacidad=capacidad
        self.estilo=estilo
    def abrigar(self):
        return ("el dueño de la casa "+self.propietario+" habita en el piso numero "+self.piso.getNro_piso())
    def getPiso(self):
        return self.piso
    def setPiso(self,piso):
        self.piso=piso
    def getPropietario(self):
        return self.propietario
    def setPropietario(self,propietario):
        self.propietario=propietario