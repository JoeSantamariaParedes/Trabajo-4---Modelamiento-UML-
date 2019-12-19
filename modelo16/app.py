import impresora
import imprenta
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=impresora.Impresora(zapato_marca,42,"cuero","deportivo",1200)
z1=imprenta.Imprenta(marca_zapatera,zap1,"madera",20,"americano")
print("imprenta:"+z1.getNombre())
print("impresora:"+zap1.getMarca())
z1.setImpresora(zap1)
print(z1.atender())