class Enfermo():
    def __init__(self,nro_paciente,edad,nombre,sexo,grado_enfermedad):
        self.nro_paciente = nro_paciente
        self.edad=edad
        self.nombre = nombre
        self.sexo=sexo
        self.grado_enfermedad=grado_enfermedad
    def vomitar(self,grado_enfermedad):
        self.grado_enfermedad=grado_enfermedad
    def getNro_paciente(self):
        return self.nro_paciente
    def setNro_paciente(self,nro_paciente):
        self.nro_paciente=nro_paciente


