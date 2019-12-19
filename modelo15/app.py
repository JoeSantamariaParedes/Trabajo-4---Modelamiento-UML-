import bagon
import locomotora
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=bagon.Bagon(zapato_marca,42,"cuero","deportivo",1200)
z1=locomotora.Locomotora(marca_zapatera,zap1,"madera",20,"americano")
print("bagon:"+zap1.getNumero())
print("locomotora:"+z1.getMarca())
z1.setBagon(zap1)
print(z1.transportar())