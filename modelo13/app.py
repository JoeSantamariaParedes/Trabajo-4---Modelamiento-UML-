import pantalla
import televisor
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=pantalla.Pantalla(zapato_marca,42,"cuero","deportivo",1200)
z1=televisor.Televisor(marca_zapatera,zap1,"madera",20,"americano")
print("pantalla:"+zap1.getMarca())
print("televisor:"+z1.getMarca())
z1.setPantalla(zap1)
print(z1.distraer())