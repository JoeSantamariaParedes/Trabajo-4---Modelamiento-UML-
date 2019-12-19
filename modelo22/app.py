import corbata
import terno
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=corbata.Corbata(zapato_marca,42,"cuero","deportivo",1200)
z1=terno.Terno(marca_zapatera,zap1,"madera",20,"americano")
print("terno:"+z1.getMarca())
print("corbata:"+zap1.getMarca())
z1.setCorbata(zap1)
print(z1.elegantizar())