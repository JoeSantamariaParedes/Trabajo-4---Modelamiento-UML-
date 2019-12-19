import inodoro
import sshh
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=inodoro.Inodoro(zapato_marca,42,"cuero","deportivo",1200)
z1=sshh.Sshh(marca_zapatera,zap1,"madera",20,"americano")
print("sshh:"+z1.getUbicacion())
print("inodoro:"+zap1.getMarca())
z1.setInodoro(zap1)
print(z1.atender())