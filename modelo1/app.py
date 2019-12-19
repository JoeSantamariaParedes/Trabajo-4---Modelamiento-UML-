import enfermo
import enfermera
import os
nro_paciente1= os.sys.argv[1]
nombre_enfermera= os.sys.argv[2]
p1=enfermo.Enfermo(nro_paciente1,18,"juan","m","83grados")
e1=enfermera.Enfermera(nombre_enfermera,18,12,p1,1200)
print("enfermo:" + p1.getNro_paciente())
print("enfermera:" + e1.getNombre())
e1.setEnfermo(p1)
print(e1.cuidar())