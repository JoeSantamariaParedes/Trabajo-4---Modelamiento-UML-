import piso
import casa
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=piso.Piso(zapato_marca,42,"cuero","deportivo",1200)
z1=casa.Casa(marca_zapatera,zap1,"madera",20,"americano")
print("piso:"+zap1.getNro_piso())
print("propietario:"+z1.getPropietario())
z1.setPiso(zap1)
print(z1.abrigar())