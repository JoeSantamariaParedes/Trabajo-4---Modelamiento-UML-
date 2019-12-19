import ornillas
import cocina
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=ornillas.Ornillas(zapato_marca,42,"cuero","deportivo",1200)
z1=cocina.Cocina(marca_zapatera,zap1,"madera",20,"americano")
print("cocina:"+zap1.getMarca())
print("ornillas:"+z1.getMarca())
z1.setOrnillas(zap1)
print(z1.cocinar())