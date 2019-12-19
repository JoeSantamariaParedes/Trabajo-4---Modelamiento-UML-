import mercado
import puesto
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=puesto.Puesto(zapato_marca,42,"cuero","deportivo",1200)
z1=mercado.Mercado(marca_zapatera,zap1,"madera",20,"americano")
print("mercado:"+z1.getNombre())
print("puesto:"+zap1.getNombre())
z1.setPuesto(zap1)
print(z1.recibir())