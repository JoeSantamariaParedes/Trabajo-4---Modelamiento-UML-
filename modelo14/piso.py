class Piso():
    def __init__(self,nro_piso,mz,material,tipo,precio):
        self.nro_piso=nro_piso
        self.mz=mz
        self.material=material
        self.tipo=tipo
        self.precio=precio
    def alojar(self):
        pass
    def getNro_piso(self):
        return self.nro_piso
    def setNro_piso(self,nro_piso):
        self.nro_piso=nro_piso