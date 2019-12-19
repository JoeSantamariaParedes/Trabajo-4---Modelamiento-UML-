class Colegio():
    def __init__(self,nombre,alumno,material,capacidad,aulas):
        self.nombre=nombre
        self.alumno=alumno
        self.material=material
        self.capacidad=capacidad
        self.aulas=aulas
    def inculcar(self):
        return ("el colegio "+self.nombre+" tuvo 1 ingresante llamado "+self.alumno.getNombre())
    def getAlumno(self):
        return self.alumno
    def setAlumno(self,alumno):
        self.alumno=alumno
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre