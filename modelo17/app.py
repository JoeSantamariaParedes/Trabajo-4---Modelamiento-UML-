import colegio
import alumno
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=alumno.Alumno(zapato_marca,42,"cuero","deportivo",1200)
z1=colegio.Colegio(marca_zapatera,zap1,"madera",20,"americano")
print("colegio:"+z1.getNombre())
print("alumno:"+zap1.getNombre())
z1.setAlumno(zap1)
print(z1.inculcar())