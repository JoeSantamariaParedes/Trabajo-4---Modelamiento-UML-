import universidad
import aula
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=aula.Aula(zapato_marca,42,"cuero","deportivo",1200)
z1=universidad.Universidad(marca_zapatera,zap1,"madera",20,"americano")
print("universidad:"+z1.getNombre())
print("aula:"+zap1.getNombre())
z1.setAula(zap1)
print(z1.inculcar())