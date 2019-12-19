import balon
import coliseo
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=balon.Balon(zapato_marca,42,"cuero","deportivo",1200)
z1=coliseo.Coliseo(marca_zapatera,zap1,"madera",20,"americano")
print("coliseo:"+z1.getNombre())
print("balon:"+zap1.getMarca())
z1.setBalon(zap1)
print(z1.atender())