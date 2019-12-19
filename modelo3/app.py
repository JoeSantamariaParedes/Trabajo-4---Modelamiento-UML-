import zapato
import zapatera
import os
marca_zapatera=os.sys.argv[1]
zapato_marca=os.sys.argv[2]
zap1=zapato.Zapato(zapato_marca,42,"cuero","deportivo",1200)
z1=zapatera.Zapatera(marca_zapatera,zap1,"madera",20,"americano")
print("la marca de zapato es:"+zap1.getMarca())
print("la marca de la zapatera es:"+z1.getMarca())
z1.setZapato(zap1)
print(z1.almacenar())
